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
from Insta_functions import sleep, twilio, text_me, error_handling, open_chrome, search, like_unlike_check
from Insta_functions import stats_range, right_arrow, remove_k_m_periods_commas, click_first_post

def num_posts_to_like(num_images_to_like):
    count_posts = 0

    while count_posts < num_images_to_like:
        # if statement looks for a video
        try:
            like_unlike_check()
            sleep()
            # right click on images to scroll
            driver.find_element_by_class_name('''coreSpriteRightPaginationArrow''').click()
            sleep()
            count_posts += 1

        except NoSuchElementException:
            print('Image is not a picture!')
            count_posts += 1

def write_pickle():
    name = driver.find_element_by_class_name('_2g7d5').text
    print(name, 'has been followed')
    # Begin pickle
    data = pickle.load(open("../../data/Instagram_data.p", "rb"))
    df = pd.DataFrame(
        [[name, 'Following', str(datetime.datetime.now()),
          'Follow_by_tag']],
        columns=['username', 'status', 'time_stamp', 'acquisition'])
    data = data.append(df)
    pickle.dump(data, open("../../data/Instagram_data.p", "wb"))
    # End pickle

def likes_persons_posts(num_images_to_like):
    count_posts = 0

    while count_posts < num_images_to_like:
        # if statement looks for a video
        try:
            like_unlike_check()
            time.sleep(1)
            # right click on images to scroll
            right_arrow()
            sleep()
            count_posts += 1

        except NoSuchElementException:
            print('Image is not a picture!')
            right_arrow()
            count_posts += 1

def like_people(number_of_people, number_pics_to_like):
    count = 0
    followed = 0
    while count < number_of_people:

        #clicks person's name to go their profile
        try:
            driver.find_element_by_class_name('FPmhX').click()
            sleep()
        except:
            right_arrow()
            count += 1
            continue
        # TODO - ends here!

        print('liking: ', driver.find_element_by_class_name('AC5d8').text)

        # TODO - questionable if nessesary..
        # Move to top of page
        # variable = driver.find_element_by_class_name('AC5d8')
        # actions = webdriver.ActionChains(driver)
        # actions.move_to_element(variable)

        try:
        # If out of range. Go back and select next picture
            if stats_range() is False:
                driver.back()
                sleep()
                right_arrow()
                sleep()
                continue
        except:  # if you can't find the stats still go back...
            driver.back()
            sleep()
            right_arrow()
            sleep()
            continue

        # Makes sure that the user has enough images to like!
        total_images = driver.find_elements_by_class_name('g47SY')[0].text
        total_images = remove_k_m_periods_commas(total_images)


        # Clicks the person's first image
        click_first_post()

        # TODO - is this correct?! shouldn't it be <= num_pics_to_like?
        if total_images >= number_pics_to_like:
            total_images = number_pics_to_like
            sleep()

        likes_persons_posts(total_images)

        #Goes back twice to get back to hashtag
        driver.back()
        driver.back()
        sleep()
        # right click on images to scroll
        right_arrow()
        count += 1
        sleep()

def error_log(err):
    error_log = pickle.load(open("../../data/Instagram_error_log.p", "rb"))
    df = pd.DataFrame([[err, 'Follow and like by tag', str(datetime.datetime.now())]],
                      columns=['error message', 'script', 'time_stamp'])
    error_log = error_log.append(df)
    pickle.dump(error_log, open("../../data/Instagram_error_log.p", "wb"))

errors = 1
while errors > 0:
    try:
        global driver
        driver = open_chrome('Like_by_tag_Profile')
        twilio()

        hashtag_list = ['#hudabeauty', '#beautiful', '#iggers', '#followforfollow', '#likeforlike',
                       '#Beautiful', '#me', '#instagood', '#Austin', '#makeupbyme']
        makeup_list = ['#makeupbyme', '#makeupdolls', '#makeupaddict', '#instamakeup', '#makeupblogger',
                       '#beautyaddict', '#styleblogger', '#fashionblogger', '#maccosmetics',
                       '#lashlover', '#naturallashes', '#hudabeauty', '#lipstick', '#eyeshadow']
        influnecer_list = ['#styleblogger', '#instamakeup'] + makeup_list

        #Randomizes list!
        hashtag_list = sorted(hashtag_list, key=lambda x: random())
        makeup_list = sorted(makeup_list, key=lambda x: random())
        influnecer_list = sorted(influnecer_list, key=lambda x:random())

        for hash in influnecer_list:
            print('----liking:', hash, '----')
            search(hash)

            # click first image of 'recent posts' *skipping top posts
            driver.find_element_by_xpath(
                '''//*[@id="react-root"]/section/main/article/div[2]/div[1]/div[1]/div[1]/a/div''').click()
            sleep()

            like_people(6, 3)  # number of people, number of pics to like
            driver.back()

            print('======Waiting 15 minutes!======')
            time.sleep(15*60)

        driver.close()

    except Exception as err:
        issue = error_handling()
        error_log(issue)
        driver.close()
        print(err)
        errors -= 1
        if errors == 0:
            text_me('follow #tags quit!.. reason = ' + str(err))
            quit()
        message = 'Follow #tag error...'  + str(errors) + ' errors remaining'
        text_me(message)
