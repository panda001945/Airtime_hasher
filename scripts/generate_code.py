# generate_code.py
import random

def generate_code():
    """Generate a 16-digit random number."""
    return ''.join([str(random.randint(0, 9)) for _ in range(16)])