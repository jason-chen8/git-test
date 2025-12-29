import requests
import json
from datetime import datetime
from pytz import timezone
import pytz
from datetime import timedelta





def addition(a,b):
    '''Sum two numbers a and b togerther'''
    try:
        return int(a)+int(b)
    except Exception as e:
        raise ValueError("Not a string")

import random

print(addition(random.randint(0,100), random.randint(0, 100)))