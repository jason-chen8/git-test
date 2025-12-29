import requests
import json
from datetime import datetime, timedelta
from pytz import timezone
import pytz






def addition(a,b):
    '''Sum two numbers a and b togerther'''
    try:
        return int(a)+int(b)
    except Exception as e:
        raise ValueError("Not a string")

import random

print(addition(random.randint(0,110), random.randint(0, 100)))