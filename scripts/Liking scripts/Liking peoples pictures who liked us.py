from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import timeit
from twilio.rest import Client
from random import *
import pickle
import datetime
import pandas as pd
import sys, logging

#Home computer
sys.path.insert(0, 'C:/Users/jamie/PycharmProjects/Instagram/Insta files/scripts/Functions')
#Work computer
sys.path.insert(0, 'C:/Users/jamie.kapilivsky/PycharmProjects/Instagram/Insta files/scripts/Functions')

from Insta_functions import sleep, twilio, text_me, error_handling, open_chrome, search, like_unlike_check, \
stats_range, right_arrow, remove_k_m_periods_commas, click_first_post, error_log, go_to_profile, search, \
click_posts_followers_followings

def likes_persons_posts(num_images_to_like):
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

def check_if_account_is_private():
    try:
        if driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/article/div/h2'''):
            print('Account is Private')
            return True
    except NoSuchElementException:
        return False

def check_if_account_exists():
    try:
        availability = driver.find_elements_by_xpath('''/html/body/div/div[1]/div/div/h2''')
        if availability.text == 'Sorry, this page isn\'t available.':
            return True
    except NoSuchElementException:
        driver.back()
        sleep()
        driver.refresh()
        sleep()
        return False

def check_if_image_is_not_a_video():
    try:
        if driver.find_element_by_class_name('QvAa1'):
            driver.find_element_by_class_name('''coreSpriteRightPaginationArrow''').click()
            sleep()
    except:
        pass


def like_peoples_stuffs(number_of_valeria_pictures, people_to_follow, number_of_pics_to_like):
    pic_counter = 1

    for y in range(number_of_valeria_pictures):
        pic_count = 0
        print('picture number:', y)

        check_if_image_is_not_a_video()

        # Click liking button
        driver.find_element_by_class_name('zV_Nj').click()
        # ########################################begin space bar!#################################################
        tab = 0
        while tab <= 2:
            variable = driver.find_element_by_class_name('_914pk')
            actions = webdriver.ActionChains(driver)
            actions.move_to_element(variable)
            # actions.click()
            actions.send_keys(Keys.TAB)
            actions.perform()
            time.sleep(.5)
            tab += 1

        count = 0
        while count < int(people_to_follow/3):  # Spacebar X number of times
            variable = driver.find_element_by_class_name('_914pk')
            actions = webdriver.ActionChains(driver)
            actions.move_to_element(variable)
            # actions.click()
            actions.send_keys(Keys.SPACE)
            actions.perform()

            time.sleep(.75)
            count += 1
        # #################################End repeat space bar###############################################

        people_list = []
        for people in range(people_to_follow):
            selenium_list = driver.find_elements_by_class_name('FPmhX')
            people_list.append(selenium_list[people].text)

        print(people_list)
        driver.back()

        # Likes the first x people!
        for x in people_list:  # Still need to click out of image to get to the search bar!!
            sleep()
            print(people_list.index(x), x)
            search(x)


            # Check if they found a Sorry, this page isn't available.
            try:
                driver.find_element_by_class_name('error-container')
                driver.find_element_by_xpath('''/html/body/div/div[1]/header/div/div[1]/a''').click()
                time.sleep(3)
                continue
            except NoSuchElementException:
                if people_list.index(x) == len(people_list)-1:
                    continue
                pass

            if check_if_account_is_private() is True:
                if people_list.index(x) == len(people_list)-1:
                    break
                continue

            # Makes sure that the user has enough images to like!
            total_images  = driver.find_elements_by_class_name('g47SY')[0].text
            total_images = remove_k_m_periods_commas(total_images)

            # Clicks the person's first image
            pics = driver.find_elements_by_class_name('_9AhH0')
            pics[0].click()

            if total_images >= number_of_pics_to_like:
                total_images = number_of_pics_to_like
                sleep()

            likes_persons_posts(total_images)
            sleep()

            # Below goes back twice to profile to start for loop over again
            driver.back()
            sleep()
            # driver.back()
            # sleep()

        driver.back()
        sleep()

        # go to profile
        go_to_profile()
        sleep()

        # Clicks image we started with and then loops through where to go... (not the best)
        pics = driver.find_elements_by_class_name('_9AhH0')
        pics[(row-1)*3 + (column-1)].click()

        sleep()
        while pic_count < pic_counter:
            driver.find_element_by_class_name('''coreSpriteRightPaginationArrow''').click()
            pic_count += 1
            sleep()

        pic_counter += 1

def repeat_space_bar(number_of_times):
    count = 0
    while count < number_of_times:
        driver.find_element_by_class_name('coreSpriteGlyphBlack').send_keys(Keys.SPACE)
        time.sleep(1)
        count += 1

# choose the picture!
row = 2
column = 2


error = 1
while error >= 0:
    try:
        global driver
        driver = open_chrome('Liking_pics_Profile')
        twilio()
        start = timeit.default_timer()
        sleep()

        go_to_profile()
        sleep()

        # Click 'load more'
        try:
            driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/article/div/a''').click()
            sleep()
        except NoSuchElementException:
            pass

        if row < 10:
            spacebars = row/2
        else:
            spacebars = row/2 - 3

        repeat_space_bar(spacebars)  # Scrolls down to the bottom of the profile page
        sleep()
        # select image
        pics = driver.find_elements_by_class_name('_9AhH0')
        print((row-1)*3 + (column-1))
        pics[(row-1)*3 + (column-1)].click()
        # try:
        #     driver.find_element_by_xpath(
        #         '''//*[@id="react-root"]/section/main/div/article/div[1]/div/div[''' + str(row) + ''']/div[''' + str(column) + ''']/a/div[1]''').click()  # They changed the xpath -.- its fixed now
        #
        # except:
        #     driver.find_element_by_xpath(
        #         '''//*[@id="react-root"]/section/main/div/article/div[1]/div/div[''' + str(row) + ''']/div[''' + str(column) + ''']/a/div[2]''').click()

        sleep()
        like_peoples_stuffs(2, 2, 2)  # Number of Valeria's pics, number of people, Number of pics to like (line 264)

        stop = timeit.default_timer()
        print('Liking people\'s stuffs')
        print('Minutes: ', (stop - start)/60)
        print('Total Seconds: ', (stop - start))
        driver.close()  #

    except Exception as err:
        print(err)
        issue = error_handling()
        script = 'Liking peoples pictures who liked us'
        error_log(issue, script)
        driver.close()
        error -= 1

        if error == 0:
            #text_me('Liking stuff QUIT!!!' + repr(err))
            quit()

        text = 'caught this error: ' + repr(err)
        #text_me(text)
#