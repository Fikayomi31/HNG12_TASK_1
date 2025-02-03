# Number Classifier API

This API classifies a number and provides interesting mathematical properties along with a fun fact. It is built using **Python** and **Flask**, and it is designed to be deployed in a production environment using **Gunicorn**.

---

## Features
- **Prime Number Check**: Determines if a number is prime.
- **Perfect Number Check**: Determines if a number is perfect.
- **Armstrong Number Check**: Determines if a number is an Armstrong number.
- **Digit Sum**: Calculates the sum of the digits of the number.
- **Fun Fact**: Fetches an interesting mathematical fact about the number from the [Numbers API](http://numbersapi.com/).

---

## API Endpoint

### Classify a Number

#### Parameters
- `number` (required): The number to classify.

#### Example Request

#### Example Response
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

### Setup and Installation

    ```bash
    pip (Python package manager)


### Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name

### Create a virtual environment:

    ```bash
    python -m venv venv

### Activate the virtual environment:
### On Windows:

    ```bash
    venv\Scripts\activate
    
### On macOS/Linux:

    ```bash
    source venv/bin/activate

### Install dependencies:

    ```bash
    pip install -r requirements.txt

### Run the development server:

    ```bash
    python app.py

### Access the API at:

    ```bash
    http://127.0.0.1:5000/api/classify-number?number=<your-number>