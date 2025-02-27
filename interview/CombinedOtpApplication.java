import org.springframework.boot.*;
import org.springframework.boot.autoconfigure.*;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.data.redis.core.ValueOperations;
import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import com.twilio.Twilio;
import com.twilio.rest.api.v2010.account.Message;
import com.twilio.type.PhoneNumber;
import com.warrenstrange.googleauth.*;

import java.util.concurrent.TimeUnit;

@SpringBootApplication
public class CombinedOtpApplication {

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

    public static void main(String[] args) {
        SpringApplication.run(CombinedOtpApplication.class, args);
    }

    private static final GoogleAuthenticator gAuth = new GoogleAuthenticator();
    private static final String userKeyRedis = "user:otp:key:";

    @RestController
    @RequestMapping("/otp")
    public static class OtpController {

        @Autowired
        private StringRedisTemplate redisTemplate;

        @Autowired
        private CombinedOtpApplication config;

        @GetMapping("/generate")
        public String generateOtp(@RequestParam String phoneNumber) {
            GoogleAuthenticatorKey credentials = gAuth.createCredentials();
            String otpKey = credentials.getKey();
            redisTemplate.opsForValue().set(userKeyRedis + phoneNumber, otpKey, 5, TimeUnit.MINUTES);

            String message = "Your OTP is: " + gAuth.getTotpPassword(otpKey);
            Message.creator(new PhoneNumber(phoneNumber), new PhoneNumber(config.twilioPhoneNumber), message).create();

            return "OTP sent via SMS.";
        }

        @PostMapping("/validate")
        public String validateOtp(@RequestParam String phoneNumber, @RequestParam int otp) {
            String otpKey = redisTemplate.opsForValue().get(userKeyRedis + phoneNumber);
            if (otpKey == null) {
                return "OTP expired or user not found.";
            }

            boolean isValid = gAuth.authorize(otpKey, otp);
            if (isValid) {
                redisTemplate.delete(userKeyRedis + phoneNumber);
                return "OTP is valid.";
            } else {
                return "Invalid OTP.";
            }
        }
    }
}
