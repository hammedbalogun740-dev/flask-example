import secrets
import string

def generate_random_otp(length: int): 
    """Generate random otp"""
    random_digits = [secrets.choice(string.digits) for _ in range(length)]
    return "".join(random_digits)   