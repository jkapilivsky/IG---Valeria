import time
from twilio.rest import Client
import sys, logging
import pandas as pd
from selenium import webdriver
import pickle

from random import randint

def open_chrome(profile):
    global driver
    global client
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-data-dir=C:/Users/jamie/PycharmProjects/Instagram/Profiles/" + profile)  # Path to your chrome profile
    driver = webdriver.Chrome(executable_path='../../assets/chromedriver', chrome_options=options)

    cookies = pickle.load(open("../../assets/cookies.p", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.get("https://www.instagram.com/")

    return driver

def text_me(message):
    twilio_number = '+19562653630'
    jamie_number = '+19568214550'
    valeria_number = '+19564370322'
    #phone_number = '+1%s' % input('What is your phone number?')

    client.messages.create(to=jamie_number,
                           from_=twilio_number,
                           body=message)

def twilio():
    global client
    twilio_dict = pd.read_pickle('../../../API Keys/Twilio_API.p')
    twilio_acc = list(twilio_dict.values())[0]
    twilio_cred = list(twilio_dict.values())[1]
    client = Client(twilio_acc, twilio_cred)  # For Twilio

def sleep():
    time.sleep(randint(6, 9))

def error_handling():
    return '{}, {}, line: {}'.format(sys.exc_info()[0],
                                     sys.exc_info()[1],
                                     sys.exc_info()[2].tb_lineno)
