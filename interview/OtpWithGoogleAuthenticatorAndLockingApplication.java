import org.springframework.boot.*;
import org.springframework.boot.autoconfigure.*;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.data.redis.core.ValueOperations;
import org.springframework.web.bind.annotation.*;
import com.warrenstrange.googleauth.*;
import org.springframework.beans.factory.annotation.Autowired;

import javax.annotation.PostConstruct;
import java.util.concurrent.TimeUnit;

@SpringBootApplication
public class OtpWithGoogleAuthenticatorApplication {

    private static final GoogleAuthenticator gAuth = new GoogleAuthenticator();
    private static final String user = "user@example.com";

    public static void main(String[] args) {
        SpringApplication.run(OtpWithGoogleAuthenticatorApplication.class, args);
    }

    @RestController
    @RequestMapping("/otp")
    public static class OtpController {
        
        private static final int MAX_ATTEMPTS = 3;
        private static final int LOCK_DURATION = 10;  // minutes

        @Autowired
        private StringRedisTemplate stringRedisTemplate;

        @GetMapping("/generate")
        public String generateSecretKey() {
            String secretKey = GoogleAuthenticatorKeyGenerator.createCredentials().getKey();
            String otpUrl = GoogleAuthenticatorQRGenerator.getOtpAuthURL("App", user, new GoogleAuthenticatorKey(secretKey));
            return String.format("Please register this URL in your Authenticator app: %s", otpUrl);
        }

        @PostMapping("/validate")
        public String validateOtp(@RequestParam int otpCode) {
            String lockKey = "lock:" + user;
            ValueOperations<String, String> valueOps = stringRedisTemplate.opsForValue();
            String attemptsStr = valueOps.get(lockKey);
            int attempts = (attemptsStr != null) ? Integer.parseInt(attemptsStr) : 0;

            if (attempts >= MAX_ATTEMPTS) {
                return "Account is locked. Try after " + LOCK_DURATION + " minutes.";
            }

            GoogleAuthenticatorKey key = GoogleAuthenticatorKeyGenerator.createCredentials();
            boolean isCodeValid = gAuth.authorize(key.getKey(), otpCode);
            if (!isCodeValid) {
                attempts++;
                valueOps.set(lockKey, String.valueOf(attempts), LOCK_DURATION, TimeUnit.MINUTES);
                return "Invalid OTP. " + (MAX_ATTEMPTS - attempts) + " attempts left.";
            }

            // success, reset attempts
            stringRedisTemplate.delete(lockKey);
            return "OTP is valid.";
        }
    }
}
