from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import json
import timeit
from twilio.rest import Client
import datetime
import pickle
import pandas as pd
from random import *

errors = pd.read_pickle('../../data/Instagram_error_log_backup.p')

errors.to_csv('error_log_12_26_2017.csv')