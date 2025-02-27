import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import io.github.resilience4j.ratelimiter.annotation.RateLimiter;
import io.github.resilience4j.circuitbreaker.annotation.CircuitBreaker;
import java.time.LocalDateTime;

@SpringBootApplication
@RestController
public class RateLimiterCircuitBreakerApp {

    public static void main(String[] args) {
        SpringApplication.run(RateLimiterCircuitBreakerApp.class, args);
    }

    @GetMapping("/rateLimitedEndpoint")
    @RateLimiter(name = "backendA")
    public String rateLimited() {
        return "Request passed through rate limiter at " + LocalDateTime.now();
    }

    @GetMapping("/circuitBreakerEndpoint")
    @CircuitBreaker(name = "backendA")
    public String circuitBreaker() {
        if (Math.random() > 0.5) {
            throw new RuntimeException("Random failure occurred!");
        }
        return "Request passed through circuit breaker at " + LocalDateTime.now();
    }
}
