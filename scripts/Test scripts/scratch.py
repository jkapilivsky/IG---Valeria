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
import pickle
from random import random
import sys, logging

df = pickle.load(open('../../data/Instagram_data.p', 'rb'))

not_official_friends = df[~df['status'].isin(['official_friend'])]
print(not_official_friends)