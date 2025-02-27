# Secure OTP Application with Twilio and JWT

This secure Spring Boot application integrates Google Authenticator for generating the One-Time-Passwords (OTPs), Twilio for sending OTPs via SMS, Redis for caching credentials, and JWT for managing secure sessions after user authentication.

## Prerequisites:
- Java 11+
- Maven
- Twilio Account
- Redis installation or managed service

## Setup Instructions:
1. **Clone the Repository**
   - `git clone https://github.com/yourusername/secure-otp-application.git`
   - `cd secure-otp-application`

2. **Update Application Properties**
   - Fill in your Twilio account details and Redis configuration in `src/main/resources/application.properties`.

3. **Build the Application**
  -  `mvn clean install`

4. **Run the Application**
   - `mvn spring-boot:run`

5. **Access the Application**
   - Generate OTP: `http://localhost:8080/otp/generate?username=user`
   - Validate OTP: `http://localhost:8080/otp/validate?username=user&otp=123456`

## Documentation Links:
- [Spring Boot Documentation](https://spring.io/projects/spring-boot)
- [Twilio API Documentation](https://www.twilio.com/docs)
- [Google Authenticator GitHub](https://github.com/wstrange/GoogleAuth)
- [Redis Documentation](https://redis.io/documentation)
- [JWT Introduction](https://jwt.io/introduction)

