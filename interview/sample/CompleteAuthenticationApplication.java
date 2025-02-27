import org.springframework.boot.*;
import org.springframework.boot.autoconfigure.*;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.crypto.password.NoOpPasswordEncoder;
import org.springframework.data.redis.core.StringRedisTemplate;
import com.warrenstrange.googleauth.GoogleAuthenticator;
import com.warrenstrange.googleauth.GoogleAuthenticatorKey;
import com.twilio.Twilio;
import com.twilio.rest.api.v2010.account.Message;
import com.twilio.type.PhoneNumber;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;

import java.util.Collections;
import java.util.concurrent.TimeUnit;
import java.util.Date;

@SpringBootApplication
public class CompleteAuthenticationApplication {

    @Value("${twilio.account.sid}")
    private String twilioAccountSid;

    @Value("${twilio.auth.token}")
    private String twilioAuthToken;

    @Value("${twilio.phone.number}")
    private String twilioPhoneNumber;

    @Bean
    public void initializeTwilio() {
        Twilio.init(twilioAccountSid, twilioAuthToken);
    }

    @Bean
    public GoogleAuthenticator googleAuthenticator() {
        return new GoogleAuthenticator();
    }

    @Autowired
    private StringRedisTemplate redisTemplate;

    public static void main(String[] args) {
        SpringApplication.run(CompleteAuthenticationApplication.class, args);
    }

    @EnableWebSecurity
    static class WebSecurityConfig extends WebSecurityConfigurerAdapter {
        @Override
        protected void configure(HttpSecurity http) throws Exception {
            http
                .csrf().disable()
                .authorizeRequests()
                .antMatchers("/otp/**").permitAll()
                .anyRequest().authenticated()
                .and()
                .httpBasic();
        }

        @Override
        protected void configure(AuthenticationManagerBuilder auth) throws Exception {
            auth.inMemoryAuthentication()
                .passwordEncoder(NoOpPasswordEncoder.getInstance())
                .withUser("user").password("password").roles("USER");
        }

        @Override
        @Bean
        public AuthenticationManager authenticationManagerBean() throws Exception {
            return super.authenticationManagerBean();
        }
    }

    @RestController
    @RequestMapping("/otp")
    public class OtpController {

        private final GoogleAuthenticator gAuth;
        private final String userKeyPrefix = "user:otp:";
        private final String userOtpKeyPrefix = "user:otpKey:";

        OtpController(GoogleAuthenticator gAuth) {
            this.gAuth = gAuth;
        }

        @GetMapping("/generate")
        public String generateOtp(@RequestParam String username) {
            GoogleAuthenticatorKey credentials = gAuth.createCredentials();
            String otpKey = credentials.getKey();
            redisTemplate.opsForValue().set(userOtpKeyPrefix + username, otpKey, 5, TimeUnit.MINUTES);

            String otp = String.valueOf(gAuth.getTotpPassword(otpKey));
            sendSms(username, "Your OTP: " + otp);
            return "OTP sent to your phone.";
        }

        @PostMapping("/validate")
        public String validateOtp(@RequestParam String username, @RequestParam int otp) {
            String otpKey = redisTemplate.opsForValue().get(userOtpKeyPrefix + username);
            if (otpKey == null) {
                return "OTP expired or user not found.";
            }

            boolean isValid = gAuth.authorize(otpKey, otp);
            if (isValid) {
                redisTemplate.delete(userOtpKeyPrefix + username);
                return "OTP is valid. " + generateToken(username);
            } else {
                return "Invalid OTP.";
            }
        }

        private void sendSms(String to, String message) {
            Message.creator(new PhoneNumber(to), new PhoneNumber(twilioPhoneNumber), message).create();
        }

        private String generateToken(String username) {
            long expirationTime = 1000 * 60 * 60;  // 1 hour
            return Jwts.builder()
                    .setSubject(username)
                    .setIssuedAt(new Date())
                    .setExpiration(new Date(System.currentTimeMillis() + expirationTime))
                    .signWith(SignatureAlgorithm.HS256, "SecretKey")
                    .compact();
        }
    }
}
