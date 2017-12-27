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

def error_handling():
    return '{} {} line: {}'.format(sys.exc_info()[0],
                                     sys.exc_info()[1],
                                     sys.exc_info()[2].tb_lineno)

def error_log(err):
    # error_log = pickle.load(open("../../data/Instagram_error_log.p", "rb"))
    # df = pd.DataFrame([[err, 'new FOLLOW script', str(datetime.datetime.now())]],
    #                   columns=['error message', 'script', 'time_stamp'])
    # error_log = error_log.append(df)
    # pickle.dump(error_log, open("../../data/Instagram_error_log.p", "wb"))
    print('WORKING')
#
#
# error = 1
# while error > 0:
#     try:
#         aa + b
#     except Exception as err:
#         issue = error_handling()
#         print(issue)
#         error_log(issue)
#         error -= 1
#

