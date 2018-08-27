from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import datetime
import pickle
import pandas as pd
import sys, os
from random import randint

sys.path.insert(0, 'C:/Users/jamie/PycharmProjects/IG---Valeria/scripts/Functions')
from Insta_functions import sleep, twilio, text_me, error_handling, open_chrome, search, like_unlike_check, \
stats_range, right_arrow, remove_k_m_periods_commas, click_first_post, error_log, click_posts_followers_followings, \
isEnglish


def repeat_space_bar(number_of_times):
    count = 0
    while count < number_of_times:
        driver.find_element_by_class_name('FPmhX').send_keys(Keys.SPACE)
        time.sleep(1)
        count += 1

def check_if_account_is_private():
    try:
        if driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/div/article/div/div/h2'''):
            print('Account is Private')
            sleep()
            return True
    except NoSuchElementException:
        return False

def check_if_image_is_not_a_video():
    try:
        driver.find_element_by_class_name('''_gu6vm''').click()
        return True
    except NoSuchElementException:
        # Skips the video and goes to the next image to check if it's not a video
        driver.find_element_by_class_name('''coreSpriteRightPaginationArrow''').click()
        sleep()
        return False

def follow_people(num_of_people, num_of_their_followers, sleep_time_minutes):
    for people in range(num_of_people):
        name = driver.find_elements_by_class_name('FPmhX')
        user_followers_list.append(name[people].text)

    driver.back()
    sleep()
    ################################Get's list of people to follow COMPLETE############################################
    ppl_followed = 0
    for person in user_followers_list[7:]:
        # Goes directly to person's profile
        driver.get("https://www.instagram.com/" + person)
        sleep()

        if check_if_account_is_private():
            continue

        # clicks followers
        try:
            click_posts_followers_followings('followers')
            sleep()
        except: 
            continue

        repeat_space_bar(num_of_their_followers/3)

        people_to_follow_from_friend = []
        for future_followers in range(num_of_their_followers):
            name = driver.find_elements_by_class_name('FPmhX')
            people_to_follow_from_friend.append('https://www.instagram.com/'+name[future_followers].text)

        data_names = pickle.load(open("../../data/Instagram_data.p", "rb"))
        username_list = data_names['user_url'].tolist()  # TODO - filter by number of interactions!

        for person_url in people_to_follow_from_friend:
            if person_url in username_list:
                continue

            if isEnglish(person_url[26:]) == False:
                continue

            driver.get(person_url)

            if check_if_account_is_private():
                continue

            # Make sure page is available
            try:
                if driver.find_element_by_class_name('error-container'):
                    continue
            except NoSuchElementException:
                pass

            # Check stats to make sure they are "acceptable"
            if stats_range(follower_min=150, follower_max=25000,
                           following_min=150, following_max=6000,
                           posts_min=35, posts_max=99999999) == False:
                sleep()
                continue

            flw_btn = driver.find_element_by_class_name('_5f5mN')
            if flw_btn.text == 'Follow':
                flw_btn.click()
                ppl_followed += 1
                sleep()
            else:
                continue

            print("Now following: ", person_url)

            posts = driver.find_elements_by_class_name('g47SY')[0].text
            followers = driver.find_elements_by_class_name('g47SY')[1].text
            followings = driver.find_elements_by_class_name('g47SY')[2].text
            # Begin pickle
            data = pickle.load(open("../../data/Instagram_data.p", "rb"))
            df = pd.DataFrame([['No', os.path.basename(__file__)[:-3], 'Following', driver.current_url,
                                str(datetime.datetime.now()), str(datetime.datetime.now()),
                                1, posts, followers, followings]],
                              columns=['Official_Friend', 'acquisition', 'status', 'user_url',
                                       'first_interacted_time', 'last_interacted_time',
                                       'number_of_interactions', 'posts', 'followers', 'following'])
            data = data.append(df)
            pickle.dump(data, open("../../data/Instagram_data.p", "wb"))
            # End pickle

            if (ppl_followed + 1) % 11 == 0:  # Sleeps for 6 minutes every 10 unfollow
                print(ppl_followed, 'Followed: Waiting', sleep_time_minutes, 'minutes')
                time.sleep(sleep_time_minutes * 60)
            else:
                continue

        driver.back()
        time.sleep(3)
        driver.back()
        sleep()

errors = 3

while errors > 0:
    try:
        global driver
        driver = open_chrome('Follow_Profile')
        twilio()
        # go to profile
        driver.get('https://www.instagram.com/linethmm')
        sleep()
        # Get's people to follow!
        click_posts_followers_followings('followers')
        sleep()

        number_of_people = 12

        repeat_space_bar(number_of_people/2)

        # Create new list of people to follow!
        user_followers_list = []
        follow_people(number_of_people, 25, 20)  # Number of people, number of followings, time to wait
        print(user_followers_list)

        # ###################################Check # of followings##########################################################
        # go to profile
        driver.get('https://www.instagram.com/linethmm')
        sleep()

        followings_text = driver.find_elements_by_class_name('g47SY')[2].text
        followings_int = remove_k_m_periods_commas(followings_text)
        print(followings_int)

    except Exception as err:
        print(err)
        issue = error_handling()
        script_name = 'FOLLOW friends of friends script'
        error_log(issue, script_name)
        driver.close()

        errors -= 1
        if errors == 0:
            text_me('new follow script quit!')
            quit()
        message = 'Follow error = #' + str(errors)
        text_me(message)
