# -*- coding: utf-8 -*-

import time, datetime
from twilio.rest import Client
import sys
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle
from selenium.webdriver.common.action_chains import ActionChains
import platform

from random import randint

def open_chrome(profile):
    global driver
    global client
    options = webdriver.ChromeOptions()

    # default directory. Personal desktop at home
    dir = "user-data-dir=C:/Users/jamie/PycharmProjects/Instagram/Profiles/"

    # Identify Solarwinds computer to change directory
    if platform.processor() == 'Intel64 Family 6 Model 78 Stepping 3, GenuineIntel':
        dir = "user-data-dir=C:/Users/jamie.kapilivsky/PycharmProjects/Instagram/Profiles/"

    options.add_argument(dir + profile)  # Path to your chrome profile
    driver = webdriver.Chrome(executable_path='../../assets/chromedriver', chrome_options=options)
    cookies = pickle.load(open("../../assets/cookies.p", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.get("https://www.instagram.com/")
    time.sleep(randint(6, 9))

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

def search(name):
    driver.get("https://www.instagram.com/" + name)
    sleep()

def remove_k_m_periods_commas(value):
    if 'k' in value:
        if '.' in value:
            value = value + '00'
        else:
            value = value + '000'

    if 'm' in value:
        if '.' in value:
            value = value + '00000'
        else:
            value = value + '000000'

    value = value.replace('k', '')
    value = value.replace('m', '')
    value = value.replace('.', '')
    value = value.replace(',', '')
    return int(value)

def like_unlike_check():
    # like_elem = driver.find_elements_by_xpath("//a[@role = 'button']/span[text()='Like']")
    # liked_elem = driver.find_elements_by_xpath("//a[@role = 'button']/span[text()='Unlike']")
    #
    # if len(like_elem) == 1:
    #     driver.execute_script(
    #         "document.getElementsByClassName('" + like_elem[0].get_attribute("class") + "')[0].click()")
    #     print('--> Image Liked!')
    #     time.sleep(2)
    # elif len(liked_elem) == 1:
    #     print('--> Already Liked!')
    # else:
    #     print('--> Invalid Like Element!')

    try:
        like_button = driver.find_element_by_class_name('glyphsSpriteHeart__outline__24__grey_9')
        like_button.click()
        print('--> Image Liked!')
    except:
        try:
            driver.find_element_by_class_name('glyphsSpriteHeart__filled__24__red_5')
            print('--> Already Liked!')
        except:
            print('--> Invalid Like Element!')

def isEnglish(characters):
    try:
        characters.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    return True

def stats_range(follower_min = 150, follower_max = 25000,
                following_min= 150, following_max = 5000,
                posts_min = 25, posts_max = 99999999):

    posts = driver.find_elements_by_class_name('g47SY')[0].text
    followers = driver.find_elements_by_class_name('g47SY')[1].text
    followings = driver.find_elements_by_class_name('g47SY')[2].text

    posts = remove_k_m_periods_commas(posts)
    followers = remove_k_m_periods_commas(followers)
    followings = remove_k_m_periods_commas(followings)

    if (followers < follower_min or followers > follower_max or
                following_max < following_min or followings > following_max
                or posts < posts_min or posts > posts_max):
        print('Out of follower/following range!')
        return False
    else:
        return True

def right_arrow():
    driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()

def click_first_post():
    stats = driver.find_elements_by_class_name('eLAPa')
    stats[0].click()

def go_to_profile():
    driver.find_element_by_class_name('coreSpriteDesktopNavProfile').click()

def click_posts_followers_followings(which_one):
    options = driver.find_elements_by_class_name('Y8-fY')
    if which_one == 'posts':
        options[0].click()
    elif which_one == 'followers':
        options[1].click()
    elif which_one == 'followings':
        options[2].click()

def repeat_down_arrow(number_of_times):
    actions_down = ActionChains(driver)
    actions_down.send_keys(Keys.ARROW_DOWN)
    count = 0
    while count < number_of_times:
        actions_down.perform()
        time.sleep(1.5)
        count += 1

def follow_button():
    btn_list = driver.find_elements_by_class_name('_5f5mN')
    main_btn = btn_list[0]
    return main_btn

def error_log(err, script):
    error_log = pickle.load(open("../../data/Instagram_error_log.p", "rb"))
    df = pd.DataFrame([[err, script, str(datetime.datetime.now())]],
                      columns=['error message', 'script', 'time_stamp'])
    error_log = error_log.append(df)
    pickle.dump(error_log, open("../../data/Instagram_error_log.p", "wb"))

def click_specific_post(post_num):
    all_posts = driver.find_elements_by_class_name('eLAPa')
    all_posts[post_num].click()