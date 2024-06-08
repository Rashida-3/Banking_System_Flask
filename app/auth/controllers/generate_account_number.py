import time
import random



def generate_account_number():
    timestamp = int(time.time())   
    random_number = random.randint(1000, 9999)  
    account_number = int(f"{timestamp}{random_number}")  
    return account_number
