from flask import Flask, request, jsonify
import requests
from collections import OrderedDict

app = Flask(__name__)

# Enable CORS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET')
    return response

# Helper function to check whether the digit is prime number or not
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Helper function to check whether the digit is perfect number
def is_perfect(n):
    if n <= 1:
        return False
    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum == n


# Helper function to check whether the digit is armstrong 
def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    length = len(digits)
    return sum(d**length for d in digits) == n

# Helper function to get the digit sum
def get_digit_sum(n):
    return sum(int(d) for d in str(n))

# Helper to check whether the digit is odd or even 
def get_parity(n):
    return "odd" if n % 2 else "even"

# function for the fun fact 
def get_fun_fact(n):
    if is_armstrong(n):
        digits = [int(d) for d in str(n)]
        length = len(digits)
        explanation = " + ".join(f"{d}^{length}" for d in digits)
        return f"{n} is an Armstrong number because {explanation} = {n}"
    else:
        url = f"http://numbersapi.com/{n}/math"
        response = requests.get(url)
        return response.text if response.status_code == 200 else "No fun fact available."


# API endpoint
@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')
    if not number or not number.isdigit():
        return jsonify({
            "number": "alpahbet",
            "error": True
        }), 400

    number = int(number)
    properties = []

    # Check if the number is an Armstrong number
    if is_armstrong(number):
        properties.append("armstrong")

    # Add parity (odd/even)
    parity = get_parity(number)
    properties.append(parity)

    # Ensure properties adhere to the specified combinations
    if "armstrong" not in properties:
        properties = [parity]
        

    # Create an ordered dictionary for the response
    response_data = OrderedDict([
        ("number", number),
        ("is_prime", is_prime(number)),
        ("is_perfect", is_perfect(number)),
        ("properties", properties),
        ("digit_sum", get_digit_sum(number)),
        ("fun_fact", get_fun_fact(number)),
    ])

    return jsonify(response_data), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)