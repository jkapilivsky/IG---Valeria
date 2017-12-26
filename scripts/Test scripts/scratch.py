from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import timeit
from selenium.webdriver.common.action_chains import ActionChains
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from twilio.rest import Client
import pandas as pd

#errors = pd.read_pickle('../../data/Instagram_error_log_backup.p')

#errors.to_csv('error_log_12_26_2017.csv')

twilio_dict = pd.read_pickle('../../../API Keys/Twilio_API.p')
print(twilio_dict)
print(list(twilio_dict.values())[0])
#print(twilio_dict.keys()[0])

posts = 100

print(round(int(posts)/3))