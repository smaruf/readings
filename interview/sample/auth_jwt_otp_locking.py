import os
from flask import Flask, request, jsonify
from flask_redis import FlaskRedis
from twilio.rest import Client
from datetime import timedelta, datetime
import pyotp
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_default_secret_key')
app.config['REDIS_URL'] = os.getenv('REDIS_URL', "redis://localhost:6379/0")
redis_client = FlaskRedis(app)

# Twilio setup using environment variables or default values
twilio_account_sid = os.getenv('TWILIO_ACCOUNT_SID', 'your_twilio_account_sid')
twilio_auth_token = os.getenv('TWILIO_AUTH_TOKEN', 'your_twilio_auth_token')
twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER', 'your_twilio_phone_number')
twilio_client = Client(twilio_account_sid, twilio_auth_token)


@app.route('/otp/generate', methods=['GET'])
def generate_otp():
    """
    Generate an OTP and send it to the specified phone number using Twilio SMS service.
    
    Query Parameters:
        username (str): The username of the user requesting the OTP.
        phone (str): The phone number to which the OTP is to be sent.
        
    Returns:
        str: Confirmation message indicating the OTP has been sent.
    """
    username = request.args.get('username')
    totp = pyotp.TOTP(pyotp.random_base32())
    redis_client.set(f"user_otp_{username}", totp.now(), ex=300)  # OTP expires after 5 minutes

    # Send SMS via Twilio
    message = twilio_client.messages.create(
        body=f"Your OTP: {totp.now()}",
        to=request.args.get('phone'),
        from_=twilio_phone_number
    )
    return f"OTP sent to {request.args.get('phone')}."


@app.route('/otp/validate', methods=['POST'])
def validate_otp():
    """
    Validate the provided OTP and issue a JWT if the validation is successful.
    
    JSON Body:
        username (str): The username of the user validating the OTP.
        otp (str): The OTP provided by the user.
        
    Returns:
        json: Access token if validation is successful or error message if it's not.
    """
    username = request.json.get('username')
    otp_provided = request.json.get('otp')
    otp_server = redis_client.get(f"user_otp_{username}")

    if otp_server and otp_provided == otp_server.decode():
        token = jwt.encode({
            'user_id': username,
            'exp': datetime.utcnow() + timedelta(hours=1)
        }, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'access_token': token})
    else:
        return jsonify({'message': 'Invalid or expired OTP'}), 400


if __name__ == "__main__":
    app.run(debug=True)
