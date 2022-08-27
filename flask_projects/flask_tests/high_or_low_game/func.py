import random


def get_secret_number():
    secret_number = random.randint(0, 9)
    return secret_number


def is_number(num, secret_number):
    if num == secret_number:
        return True
    else:
        return False
