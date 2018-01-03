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

def remove_k_m_periods_commas(value):
    value = value.replace('k', '')
    value = value.replace('m', '')
    value = value.replace('.', '')
    value = value.replace(',', '')
    return value

like_with_k = '195'

likes = int(remove_k_m_periods_commas(like_with_k))
if '.' in like_with_k:
    likes = likes * 100
elif 'k' in like_with_k:
    likes = likes * 1000

print(type(like_with_k))
print(type(likes))
print(likes)