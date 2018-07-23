from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import datetime
import pickle
import pandas as pd
import sys

sys.path.insert(0, 'C:/Users/jamie/PycharmProjects/Instagram/Insta files/scripts/Functions')
from Insta_functions import sleep, twilio, text_me, error_handling, open_chrome, search, like_unlike_check, \
stats_range, right_arrow, remove_k_m_periods_commas, click_first_post, error_log, click_posts_followers_followings, \
isEnglish


def tab_and_space(num_spacebars):
    tab = 0
    while tab <= 2:
        actions_tab = ActionChains(driver)
        actions_tab.send_keys(Keys.TAB)
        actions_tab.perform()
        time.sleep(.5)
        tab += 1
    sleep()

    count = 0
    while count < int(num_spacebars / 3):  # Spacebar X number of times
        actions_space = ActionChains(driver)
        actions_space.send_keys(Keys.SPACE)
        actions_space.perform()
        time.sleep(.75)
        count += 1


def likes_persons_posts(num_images_to_like):
    count_posts = 0

    while count_posts < num_images_to_like:
        # if statement looks for a video
        try:
            like_unlike_check()
            sleep()
            # right click on images to scroll
            right_arrow()
            sleep()
            count_posts += 1

        except NoSuchElementException:
            print('Image is not a picture!')
            count_posts += 1


def like_and_follow_people(people_list, number_of_pics_to_like=3):
    # Search for users
    global followed
    followed = 0
    global people_followed_list
    people_followed_list = []
    for person in people_list:
        print('---searching:', person)
        driver.get('https://www.instagram.com/'+person)
        sleep()

        # Make sure they are not private
        try:
            if driver.find_element_by_class_name('rkEop'):
                continue
        except NoSuchElementException:
            pass

        # Check stats to make sure they are "acceptable"
        if stats_range(follower_min = 150, follower_max = 25000,
                following_min= 150, following_max = 5000,
                posts_min = 150, posts_max = 99999999) == False:
            print('out of stat range')
            continue

        # Like their first 3 things
        click_first_post()

        likes_persons_posts(number_of_pics_to_like)
        sleep()

        # Gets out of pic window to go to their account
        driver.back()
        sleep()

        # TODO - turn off/on following them
        #driver.find_element_by_class_name('_5f5mN').click()
        people_followed_list.append(driver.current_url)
        followed += 1

        # BREAK - make sure we get to 150 follow
        if followed == max_to_follow:
            print('followed 150, time to unfollow')
            break
            # TODO - DO SOMETHING


        print('#'*20)
        # need to save the users in a database!

        sleep()


def get_accounts_that_liked_influncer(num_people=350):
    # Need to scroll down
    tab_and_space(num_people)

    # Get list of usernames
    people_list = []
    for people in range(num_people):
        selenium_list = driver.find_elements_by_class_name('FPmhX')
        people_list.append(selenium_list[people].text)
    print(people_list)
    driver.back()
    return people_list

errors = 1
max_to_follow = 150
while errors > 0:
    try:
        global driver
        driver = open_chrome('Follow_Like_150')
        twilio()

        influencers_list = ['vdethe', 'ashleesummer', 'snitchery', 'mamapeach_',
                            'sichenmakeupholic', 'nyane', 'michellephan', 'hudabeauty','wengie',
                            'sophxsmithh','hailiebarber', 'laur_elyse','ponysmakeup']

        influencers_list2 = ['sophxsmithh', 'nyane']

        # If we want to randomize list
        # randomized_list = sorted(influencers_list, key=lambda x:random())
        for influencer in influencers_list2:
            print('following:', influencer)
            driver.get("https://www.instagram.com/" + influencer)
            sleep()

            click_first_post()
            time.sleep(2)
            # Click likes amount to get to people who've liked their picture
            driver.find_element_by_class_name('zV_Nj').click()

            sleep()
            people_list = get_accounts_that_liked_influncer(2)  # Number of people to follow
            sleep()

            like_and_follow_people(people_list, number_of_pics_to_like=2)  # Sends list of people and number of likes per person

            if followed == 150:
                break


        # TODO - UNFOLLOW SECTION!!!
        for people_url in reversed(people_followed_list):
            driver.get(people_url)
            driver.find_element_by_class_name('_5f5mN').click()
            sleep()

        # Completed
        driver.close()
        print('########time to start over#######waiting 2 hours########')
        time.sleep(120*60)  # Wait 2 hours to start over

    except Exception as err:
        errors -= 1
        print(err)
        issue = error_handling()
        script_name = 'Follow Influencers engagement'
        error_log(issue, script_name)
        driver.close()

        if errors == 0:
            text_me('Follow 150 quit...')
            quit()
        message = 'Influencer+engagement follow error...' + str((errors)) + ' errors remaining'
        #text_me(message)
        time.sleep(60 * 10)