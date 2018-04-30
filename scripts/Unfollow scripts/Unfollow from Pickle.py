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


sys.path.insert(0, 'C:/Users/jamie/PycharmProjects/Instagram/Insta files/scripts/Functions')
from Insta_functions import sleep, twilio, text_me, error_handling, open_chrome


def log_into_instagram(username, password):
    driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a''').click()
    time.sleep(1.5)

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

def read_pickle():
    # Begin pickle
    global follow_unfollow_df
    data = pickle.load(open("../../data/Instagram_data.p", "rb"))

    bad_status = ['Not_searchable', 'Wrong_search', 'hashtag', 'location', 'deleted_account']
    today = str(datetime.date.today())  # Gets today's date
    follow_unfollow_df = data[data['status'].isin(['Following'])]
    follow_unfollow_df = follow_unfollow_df[~follow_unfollow_df['status'].isin(bad_status)]
    follow_unfollow_df = follow_unfollow_df[~follow_unfollow_df['time_stamp'].isin([today])]
    print('unfollowing:', follow_unfollow_df['username'].tolist())

def no_unfollow():
    if len(follow_unfollow_df) == 0:
        text_me('nothing to follow?')
        driver.close()
        quit()

def error_log(err):
    error_log = pickle.load(open("../../data/Instagram_error_log.p", "rb"))
    df = pd.DataFrame([[err, 'Unfollow from Pickle', str(datetime.datetime.now())]],
                      columns=['error message', 'script', 'time_stamp'])
    error_log = error_log.append(df)
    pickle.dump(error_log, open("../../data/Instagram_error_log.p", "wb"))

count = 0
error = 1
while error > 0:
    try:
        global driver
        driver = open_chrome('Unfollow_Profile')
        twilio()
        read_pickle()
        no_unfollow()

        for people in follow_unfollow_df['username']:
            search = driver.find_element_by_xpath('''//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input''')
            search.clear()
            search.send_keys(people)
            search.send_keys(Keys.ENTER)
            sleep()
            # Goes to first person in search
            search_results = driver.find_elements_by_class_name('_ndl3t')

            # checks if results are found
            try:
                search_results[0].click()
                sleep()
            except:
                try:
                    driver.find_element_by_class_name('_oznku')
                    data = pickle.load(open("../../data/Instagram_data.p", "rb"))
                    df = pd.DataFrame([[people, 'Not_searchable', str(datetime.datetime.now())]],
                                      columns=['username', 'status', 'time_stamp'])
                    data = data.append(df)
                    pickle.dump(data, open("../../data/Instagram_data.p", "wb"))
                    search.clear()
                    continue
                except NoSuchElementException:
                    continue

            # Check if they found hashtag
            try:
                driver.find_element_by_class_name('_kwqc3')

                data = pickle.load(open("../../data/Instagram_data.p", "rb"))
                df = pd.DataFrame([[people, 'hashtag', str(datetime.datetime.now())]],
                                  columns=['username', 'status', 'time_stamp'])
                data = data.append(df)
                pickle.dump(data, open("../../data/Instagram_data.p", "wb"))
                continue
            except NoSuchElementException:
                pass

            # Check if they found a location
            try:
                driver.find_element_by_class_name('_thew0')

                data = pickle.load(open("../../data/Instagram_data.p", "rb"))
                df = pd.DataFrame([[people, 'location', str(datetime.datetime.now())]],
                                  columns=['username', 'status', 'time_stamp'])
                data = data.append(df)
                pickle.dump(data, open("../../data/Instagram_data.p", "wb"))
                continue
            except NoSuchElementException:
                pass

            # Check if they found a Sorry, this page isn't available.
            try:
                driver.find_element_by_class_name('error-container')

                data = pickle.load(open("../../data/Instagram_data.p", "rb"))
                df = pd.DataFrame([[people, 'deleted_account', str(datetime.datetime.now())]],
                                  columns=['username', 'status', 'time_stamp'])
                data = data.append(df)
                pickle.dump(data, open("../../data/Instagram_data.p", "wb"))
                driver.find_element_by_xpath('''/html/body/div/div[1]/header/div/div[1]/a''').click()
                time.sleep(3)
                continue
            except NoSuchElementException:
                pass

            # Found the wrong person!
            try:
                if driver.find_element_by_class_name('_rf3jb').text != people:
                    data = pickle.load(open("../../data/Instagram_data.p", "rb"))
                    df = pd.DataFrame([[people, 'Wrong_search', str(datetime.datetime.now())]],
                                      columns=['username', 'status', 'time_stamp'])
                    data = data.append(df)
                    pickle.dump(data, open("../../data/Instagram_data.p", "wb"))
                    continue
            except NoSuchElementException:
                continue

            button = driver.find_element_by_class_name('_r9b8f')

            if button.text == 'Following':
                button.click()
                print('unfollowed', people)
                sleep()
                # Begin pickle
                data = pickle.load(open("../../data/Instagram_data.p", "rb"))
                df = pd.DataFrame([[people, 'Unfollowed', str(datetime.datetime.now())]],
                                  columns=['username', 'status', 'time_stamp'])
                data = data.append(df)
                pickle.dump(data, open("../../data/Instagram_data.p", "wb"))
                count += 1
                # End pickle

            elif button.text == 'Requested':
                # button.click()
                # print('unfollow requested! Need to track this by time', people)
                # Begin pickle
                data = pickle.load(open("../../data/Instagram_data.p", "rb"))
                df = pd.DataFrame([[people, 'Requested', str(datetime.datetime.now())]],
                                  columns=['username', 'status', 'time_stamp'])
                data = data.append(df)
                pickle.dump(data, open("../../data/Instagram_data.p", "wb"))
                # End pickle

            elif button.text == 'Follow':
                # Begin pickle
                data = pickle.load(open("../../data/Instagram_data.p", "rb"))
                df = pd.DataFrame([[people, 'Unfollowed', str(datetime.datetime.now())]],
                                  columns=['username', 'status', 'time_stamp'])
                data = data.append(df)
                pickle.dump(data, open("../../data/Instagram_data.p", "wb"))
                # End pickle

            # Updates data frame files
            data = pickle.load(open("../../data/Instagram_data.p", "rb"))
            data.drop_duplicates(subset='username', keep='last', inplace=True)
            pickle.dump(data, open("../../data/Instagram_data.p", "wb"))
            # End pickle

            if (count + 1) % 16 == 0:  # Sleeps for 15 minutes every 16 unfollow
                print(count, 'Unfollowed: Waiting 11 minutes')
                time.sleep(11 * 60)

        driver.close()
    except Exception as err:
        issue = error_handling()
        print(issue)
        error_log(issue)
        driver.close()
        print(err)
        error -= 1
        msg = 'Unfollow issue!'
        if error == 0:
            text_me('unfollow ended!')
            quit()
        text_me(msg)
