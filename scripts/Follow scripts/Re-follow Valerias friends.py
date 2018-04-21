from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from twilio.rest import Client
import datetime
import pickle
import pandas as pd
from random import *
import sys, logging
#
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
        "user-data-dir=C:/Users/jamie.kapilivsky/PycharmProjects/Instagram/Profiles/Follow_Profile")  # Path to your chrome profile
    driver = webdriver.Chrome(executable_path='../../assets/chromedriver', chrome_options=options)
    driver.get("https://www.instagram.com/")
    sleep()

def sleep():
    time.sleep(randint(4, 6))

def text_me(message):
    twilio_number = '+19562653630'
    jamie_number = '+19568214550'
    valeria_number = '+19564370322'
    #phone_number = '+1%s' % input('What is your phone number?')

    client.messages.create(to=jamie_number,
                           from_=twilio_number,
                           body=message)

def error_handling():
    return '{} {} line: {}'.format(sys.exc_info()[0],
                                     sys.exc_info()[1],
                                     sys.exc_info()[2].tb_lineno)

def error_log(err):
    error_log = pickle.load(open("../../data/Instagram_error_log.p", "rb"))
    df = pd.DataFrame([[err, 'new FOLLOW script', str(datetime.datetime.now())]],
                      columns=['error message', 'script', 'time_stamp'])
    error_log = error_log.append(df)
    pickle.dump(error_log, open("../../data/Instagram_error_log.p", "wb"))
#

df = pickle.load(open('../../data/Instagram_data.p', 'rb'))
#print(df)
of_df = df[df['status'].isin(['official_friend'])]
of_df = of_df['username']
friend_list = of_df.tolist()

errors = 1
count = 0
list_that_didnt_follow = []
while errors > 0:
    try:
        open_chrome()
        twilio()

        data_names = pickle.load(open("../../data/Instagram_data.p", "rb"))
        people_list = df['username'].tolist()

        for x in people_list:
            sleep()
            search = driver.find_element_by_xpath('''//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input''')
            search.clear()
            search.send_keys(x)
            search.send_keys(Keys.ENTER)
            sleep()
            # Goes to first person in search
            search_results = driver.find_elements_by_class_name('_gimca')

            # checks if results are found
            try:
                search_results[0].click()
                sleep()
            except:
                list_that_didnt_follow.append(x)
                driver.find_element_by_class_name('_oznku')
                search.clear()
                # if statement that breaks for loop if were at the end...
                if people_list.index(x) == len(people_list) - 1:
                    break
                continue

            # Check if they found hashtag
            try:
                driver.find_element_by_class_name('_kwqc3')
                list_that_didnt_follow.append(x)
                continue
            except NoSuchElementException:
                if people_list.index(x) == len(people_list) - 1:
                    break
                pass

            # Check if they found a location
            try:
                driver.find_element_by_class_name('_thew0')
                list_that_didnt_follow.append(x)
                continue
            except NoSuchElementException:
                if people_list.index(x) == len(people_list) - 1:
                    break
                pass

            # Check if they found a Sorry, this page isn't available.
            try:
                driver.find_element_by_class_name('error-container')
                driver.find_element_by_xpath('''/html/body/div/div[1]/header/div/div[1]/a''').click()
                time.sleep(3)
                list_that_didnt_follow.append(x)
                continue
            except NoSuchElementException:
                if people_list.index(x) == len(people_list) - 1:
                    continue
                pass

            # Makes sure we are liking the right person!
            try:
                username_found = driver.find_element_by_xpath(
                    '''//*[@id="react-root"]/section/main/article/header/section/div[1]/h1''').text
                if x != username_found:
                    if people_list.index(x) == len(people_list) - 1:
                        print("didn't follow:", x)
                        list_that_didnt_follow.append(x)
                        break
                    continue
            except:
                continue

            follow_button = driver.find_element_by_class_name('_qv64e')
            sleep()

            if follow_button.text == 'Follow':
                follow_button.click()
                print(x, 'FOLLOWED!')
                count += 1
                sleep()
            else:
                print(x, 'is already followed!')
                list_that_didnt_follow.append(x)

            sleep()

            if (count + 1) % 11 == 0:  # Sleeps for 6 minutes every 10 unfollow
                print('SLEEP TIME! for 10 minutes')
                time.sleep(10 * 60)
            else:
                continue

    except Exception as err:
        print('CHECK ERROR LIST')
        print(list_that_didnt_follow)
        text_me('check your laptop!')
        errors -= 1
        if errors == 0:
            quit()

