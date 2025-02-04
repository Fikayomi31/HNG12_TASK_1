from flask import Flask, jsonify, request
from flask_cors import CORS
from os import environ
import requests

app = Flask(__name__)
CORS(app) 

# Sorting key for Flask's JSON encoder 
app.json.sort_keys = False


def is_prime(n):
    """
    Helper function to check if a number is prime.
    """
    if n <= 1 or n % 2 == 0:
        return False
    """
    int(n ** 0) + 1 mean square of n and only the int whole number
    will be used  and add will 1
    example int(10 ** 0.5) + 1 = 4
    the loop with be for i in range(2, 4), start from 2 to 4
    if 10 %  2 == 0 so it return False 
    """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_perfect(n):
    """
    Helper function to check if a number is perfect.
    """
    if n < 2:
        return False
    # it collect i when i is == 0
    divisors = [i for i in range(1, n) if n % i == 0]
    # sum all the divisors collected in the [] and return True if it == n
    return sum(divisors) == n


def is_armstrong(n):
    """
    Helper function to check if a number is an Armstrong number.
    
    """
    if n < 0:
        return False
    # convert the number to a str 
    digits = str(n)
    power = len(digits)
    """loop through each digit convert it to int square it by the power
    and check if it == to the number itself
    """
    return sum(int(digit) ** power for digit in digits) == n



def digit_sum(n):
    """
    Helper function to calculate the sum of the digits of a number.
    Convert the number to absolute and str we loop  it and sum
    """
    
    return sum(int(digit) for digit in str(abs(n)))


@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    """
    Checks the mathematical properties of a number,
    and returns a JSON response containing the number,
    its properties, and a fun fact about the number
    from the Numbers API.
    """
    # Get the number parameter from the query string
    number = request.args.get('number')

    try:
        number = int(number)
    except ValueError:
        return jsonify({
            "number": "alphabet",
            "error": True}
        ), 400

    armstrong = is_armstrong(number)
    # checking for odd and even
    parity = "odd" if number % 2 != 0 else "even"
    
    # Checking for Armstrong properties and parity
    properties = []
    if armstrong:
        properties.append("armstrong")
    properties.append(parity)

    # Fetch the fun fact from the Numbers API using the math endpoint
    api_url = f"http://numbersapi.com/{number}/math?json"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        # print(data)
        fun_fact = data.get("text", "")
    except Exception as e:
        fun_fact = f"Could not retrieve fun fact: {str(e)}"

    # the JSON response
    data = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": fun_fact
    }
    return jsonify(data), 200  


# Handling error pages and wrong redirections
@app.errorhandler(404)
def page_not_found(e):
    """
    Returns an error message in JSON
    """
    
    data = {
        "number": "alphabet",
        "error": True  # myStr
    }
    return jsonify(data), 404


if __name__ == "__main__":
    port = int(environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port, debug=True) 