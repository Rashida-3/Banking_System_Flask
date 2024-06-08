import hashlib
import time
import random


def generate_transaction_id():
    # Get the current time in milliseconds
    current_time = int(time.time() * 1000)
    # Create a unique identifier by combining the current time with a random number
    unique_string = f"{current_time}{random.randint(100000, 999999)}"
    # Hash the unique string using SHA256 and take the first 10 digits of the hexadecimal representation
    transaction_id = hashlib.sha256(unique_string.encode()).hexdigest()[:10]
    return transaction_id