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

df = pd.read_pickle('../../data/Instagram_data.p')

df = df[df['status'].isin(['official_friend'])]
df = df[df['username'].isin(['nyane'])]
print(df)