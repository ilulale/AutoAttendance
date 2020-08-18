from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from datetime import datetime,timedelta

def startweek():
    abhi = datetime.now()
    req = abhi
    while (req.weekday() != 0):
        req = req + timedelta(days=1)
    return req

