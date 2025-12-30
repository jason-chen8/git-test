import requests
import json
from datetime import datetime, timedelta
from pytz import timezone
import pytz
import random
#This is the new feature subtraction

def subtraction(a,b):
    '''Subtract two numbers a and b together'''
    try:
        return int(a)-int(b)
    except Exception as e:
        raise ValueError("Not a string")    


def addition(a,b):
    '''Sum two numbers a and b together'''
    try:
        return int(a)+int(b)
    except Exception as e:
        raise ValueError("Not a string")

def multiplication(a,b):
    '''Multiply two numbers a and b together'''
    try:
        return int(a)*int(b)
    except Exception as e:
        raise ValueError("Not a string")

def division(a,b):
    '''Divide two numbers a and b together'''
    try:
        return int(a)/int(b)
    except Exception as e:
        raise ValueError("Not a string")


print(addition(random.randint(0,100), random.randint(0, 100)))
print(subtraction(1,2))
if __name__ == 'Main':
    print('Hello World')