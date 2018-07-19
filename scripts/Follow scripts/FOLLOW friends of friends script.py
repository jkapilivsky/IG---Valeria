from selenium.common.exceptions import NoSuchElementException
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

def repeat_space_bar(number_of_times):
    count = 0
    while count < number_of_times:
        driver.find_element_by_class_name('FPmhX').send_keys(Keys.SPACE)
        time.sleep(1)
        count += 1

def check_if_account_is_private():
    try:
        if driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/article/div/h2'''):
            print('Account is Private')
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

    for person in user_followers_list:
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

        repeat_space_bar(30)

        for future_followers in range(num_of_their_followers):
            sleep()
            data_names = pickle.load(open("../../data/Instagram_data.p", "rb"))
            username_list = data_names['username'].tolist()

            name = driver.find_elements_by_class_name('FPmhX')
            buttons = "../../../../div[2]"

            if name[future_followers].text == 'linethmm':
                continue

            if name[future_followers].text in username_list:
                continue

            if isEnglish(name[future_followers].text) == False:
                continue

            if name[future_followers].find_element_by_xpath(buttons).text == 'Follow':
                name[future_followers].find_element_by_xpath(buttons).click()
                sleep()
            else:
                continue

            print("Now following: ", name[future_followers].text)

            # Begin pickle
            data = pickle.load(open("../../data/Instagram_data.p", "rb"))
            df = pd.DataFrame(
                [[name[future_followers].text, 'Following', str(datetime.datetime.now()), 'Friends_of_friends']],
                columns=['username', 'status', 'time_stamp', 'acquisition'])
            data = data.append(df)
            pickle.dump(data, open("../../data/Instagram_data.p", "wb"))
            # End pickle

            sleep()

            if (future_followers + 1) % 11 == 0:  # Sleeps for 6 minutes every 10 unfollow
                print(future_followers, 'Followed: Waiting', sleep_time_minutes, 'minutes')
                time.sleep(sleep_time_minutes * 60)
            else:
                continue

        driver.back()
        time.sleep(3)
        driver.back()
        sleep()

errors = 3
followings = 0
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

        repeat_space_bar(15)

        # Create new list of people to follow!
        user_followers_list = []
        follow_people(40, 12, 20)  # Number of people, number of followings, time to wait
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



