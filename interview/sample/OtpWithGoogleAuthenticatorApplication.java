import org.springframework.boot.*;
import org.springframework.boot.autoconfigure.*;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.data.redis.core.ValueOperations;
import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import com.twilio.Twilio;
import com.twilio.rest.api.v2010.account.Message;
import com.twilio.type.PhoneNumber;
import com.warrenstrange.googleauth.*;

import java.util.concurrent.TimeUnit;

@SpringBootApplication
public class OtpWithGoogleAuthenticatorApplication {

    // Initialize Twilio
    @Bean
    public void initializeTwilio(@Value("${twilio.account.sid}") String accountSid,
                                 @Value("${twilio.auth.token}") String authToken) {
        Twilio.init(accountSid, authToken);
    }

    @Value("${twilio.phone.number}")
    private String fromNumber;

    private static final GoogleAuthenticator gAuth = new GoogleAuthenticator();
    private static final String user = "user@example.com; // User’s phone number should actually be here

    public static void main(String[] args) {
        SpringApplication.run(OtpWithGoogleAuthenticatorApplication.class, args);
    }

    @RestController
    @RequestMapping("/otp")
    public static class OtpController {

        @Autowired
        private StringRedisTemplate stringRedisTemplate;
        @Autowired
        private OtpWithGoogleAuthenticatorApplication app;

        @GetMapping("/generate")
        public String generateSecretKey(@RequestParam String phoneNumber) {
            String secretKey = GoogleAuthenticatorKeyGenerator.createCredentials().getKey();
            String otp = String.format("%04d", gAuth.getTotpPassword(secretKey));
            sendSms(phoneNumber, "Your OTP is: " + otp);
            return "OTP sent via SMS to " + phoneNumber;
        }

        private void sendSms(String to, String message) {
            Message.creator(new PhoneNumber(to), new PhoneNumber(app.fromNumber), message).create();
        }

        @PostMapping("/validate")
        public String validateOtp(@RequestParam String otp) {
            // OTP validation logic
            return "Valid or invalid response";
        }
    }
}
