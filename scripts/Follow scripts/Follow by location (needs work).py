from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import json
import timeit
from twilio.rest import Client
import json
import datetime
import pickle
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from random import *

def twilio():
    global client
    twilio_dict = pd.read_pickle('../../../API Keys/Twilio_API.p')
    twilio_acc = list(twilio_dict.values())[0]
    twilio_cred = list(twilio_dict.values())[1]
    client = Client(twilio_acc, twilio_cred)  # For Twilio

def open_chrome():
    global driver
    global client
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-data-dir=C:/Users/jamie.kapilivsky/PycharmProjects/Instagram/Profiles/Extra_Profile")  # Path to your chrome profile
    driver = webdriver.Chrome(executable_path='../../assets/chromedriver', chrome_options=options)
    driver.get("https://www.instagram.com/")
    sleep()

def sleep():
    time.sleep(randint(1, 6))

def text_me(message):
    twilio_number = '+19563912057'
    jamie_number = '+19568214550'
    valeria_number = '+19564370322'
    #phone_number = '+1%s' % input('What is your phone number?')

    client.messages.create(to=jamie_number,
                           from_=twilio_number,
                           body=message)

def remove_k_m_periods_commas(value):
    value = value.replace('k', '')
    value = value.replace('m', '')
    value = value.replace('.', '')
    value = value.replace(',', '')
    return value

def follower_following_range(follower_min, follower_max, following_min, following_max):
    num_follower = driver.find_element_by_xpath(
        '''//*[@id="react-root"]/section/main/article/header/div[2]/ul/li[2]/a/span''').text

    num_following = driver.find_element_by_xpath(
        '''//*[@id="react-root"]/section/main/article/header/div[2]/ul/li[3]/a/span''').text

    num_follower = int(remove_k_m_periods_commas(num_follower))
    num_following = int(remove_k_m_periods_commas(num_following))

    print('follower:', num_follower, '| following: ', num_following)

    if (num_follower < follower_min or num_follower > follower_max or
                num_following < following_min or num_following > following_max):
        print('Out of follower/following range!')
        return False
    else:
        print('good to go')
        return True


open_chrome()
twilio()

sleep()

locations = ['Austin, TX']

for city in locations:
    search = driver.find_element_by_xpath('''//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input''')
    search.clear()
    search.send_keys(city)
    search.send_keys(Keys.ENTER)
    sleep()
    # Goes to first option in search
    search_results = driver.find_elements_by_class_name('_gimca')

    # checks if results are found
    try:
        search_results[0].click()
        sleep()
    except:
        search.clear()
        continue

    # Click first image
    image = driver.find_element_by_xpath(
        '''//*[@id="react-root"]/section/main/article/div[2]/div[1]/div[1]/div[1]/a/div/div[2]''')
    hover = ActionChains(driver).move_to_element(image)
    hover.perform()
    image.click()
    sleep()

    for x in range(3):
        # Click person's name
        driver.find_element_by_class_name('_eeohz').click()
        sleep()

        if follower_following_range(10, 5000, 10, 5000) is False:
            driver.back()
            sleep()
            driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            continue

        # Get button information
        button = driver.find_element_by_class_name('_qv64e')

        if button.text == 'Follow':
            button.click()
        else:
            driver.back()
            sleep()
            driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            continue

        driver.back()
        sleep()
        driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()