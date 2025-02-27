from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import pybreaker
import random
import datetime

app = Flask(__name__)

# Setup rate limiter
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["10 per minute"]
)

# Setup circuit breaker
circuit_breaker = pybreaker.CircuitBreaker(
    fail_max=5,  # number of failures before the circuit is opened
    reset_timeout=10  # number of seconds before the circuit is reset
)

@app.route("/rateLimitedEndpoint")
@limiter.limit("2 per second")
def rate_limited():
    return f"Request passed through rate limiter at {datetime.datetime.now()}"

@app.route("/circuitBreakerEndpoint")
def circuit_breaker_endpoint():
    try:
        response = circuit_breaker.call(simulated_function)
        return f"Response: {response} at {datetime.datetime.now()}"
    except pybreaker.CircuitBreakerError:
        return "Circuit Breaker is open!", 503

def simulated_function():
    if random.random() > 0.5:
        raise Exception("Random failure occurred!")
    return "Success"

if __name__ == "__main__":
    app.run(debug=True)
