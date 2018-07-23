from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import timeit
import datetime
from twilio.rest import Client
import pickle
import pandas as pd
from random import *
import sys, logging

sys.path.insert(0, 'C:/Users/jamie/PycharmProjects/Instagram/Insta files/scripts/Functions')
from Insta_functions import sleep, twilio, text_me, error_handling, open_chrome, remove_k_m_periods_commas, go_to_profile

def log_into_instagram(username, password):
    driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a''').click()
    time.sleep(3)

    # Input username
    user = driver.find_element_by_xpath(
        '''//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[1]/div/input''')
    user.clear()
    user.send_keys(username)

    # Input password
    pw = driver.find_element_by_xpath(
        '''//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/input''')
    pw.clear()
    pw.send_keys(password)

    pw.send_keys(Keys.ENTER)
    time.sleep(3)

def repeat_down_arrow(number_of_times):
    actions_down = ActionChains(driver)
    actions_down.send_keys(Keys.ARROW_DOWN)

    count = 0
    while count < number_of_times:
        actions_down.perform()
        time.sleep(1.5)
        count += 1

def repeat_space_bar(number_of_times):
    actions_space = ActionChains(driver)
    actions_space.send_keys(Keys.SPACE)
    count = 0
    while count < number_of_times:
        actions_space.perform()
        time.sleep(1)
        count += 1

def error_log(err):
    error_log = pickle.load(open("../../data/Instagram_error_log.p", "rb"))
    df = pd.DataFrame([[err, 'Valeria new unfollowing script', str(datetime.datetime.now())]],
                      columns=['error message', 'script', 'time_stamp'])
    error_log = error_log.append(df)
    pickle.dump(error_log, open("../../data/Instagram_error_log.p", "wb"))

data = pickle.load(open("../../data/Instagram_data.p", "rb"))
official_friends = data['username'][data['status'] == 'official_friend'].tolist()

error = 2
while error > 0:
    try:
        global driver
        driver = open_chrome('Unfollow_Profile')
        twilio()

        start = timeit.default_timer()

        # go to profile
        go_to_profile()
        sleep()

        # Click unfollowing list
        driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a''').click()
        sleep()

        # Tab into the list
        actions_tab = ActionChains(driver)
        actions_tab.send_keys(Keys.TAB)
        actions_tab.perform()

        people_to_unfollow = 350
        repeat_space_bar(people_to_unfollow/5)

        count = 0
        for people in reversed(range(0, people_to_unfollow)):
            unfollow_button = driver.find_elements_by_class_name('sqdOP')
            name = driver.find_elements_by_class_name('FPmhX')

            # Todo - check if name is equal to button... or it will unfollow wrong peoples
            # Checks if the person's name is in Valeria's official following_list
            if name[people] in official_friends:
                print('Valeria\'s friend!!!')
                continue

            unfollow_button[people+1].click()
            time.sleep(randint(3,5))
            count += 1
            print('unfollowed:', name[people].text)


            if (people+1) % 16 == 0:  # Sleeps for 15 minutes every 16 unfollow
                print(people, 'Unfollowed: Waiting 5 minutes')
                time.sleep(5*60)

            if (people+1) % 25 == 0:  # Catches up for scrolling
                repeat_space_bar(1)

            # Begin pickle
            data = pickle.load(open("../../data/Instagram_data.p", "rb"))
            df = pd.DataFrame([[name[people].text, 'Unfollowed', str(datetime.datetime.now())]],
                              columns=['username', 'status', 'time_stamp'])
            data = data.append(df)
            pickle.dump(data, open("../../data/Instagram_data.p", "wb"))
            # End pickle

        stop = timeit.default_timer()
        print('Unfollowed: ', count, ' people!')
        print('Minutes: ', (stop - start)/60)
        driver.close()


    except Exception as err:
        print(err)
        issue = error_handling()
        error_log(issue)
        driver.close()

        error -= 1
        if error == 0:
            text_me('Oldschool unfollow QUIT')
            quit()
        message = 'Oldschool unfollow error...' + str((error)) + ' errors remaining'
        text_me(message)
        time.sleep(60*10)


