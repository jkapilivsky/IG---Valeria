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

errors = pd.read_pickle('../../data/Instagram_error_log_backup.p')

#errors.to_csv('error_log_12_26_2017.csv')

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('../../../API Keys/GSheet_client_secret', scope)
client = gspread.authorize(creds)