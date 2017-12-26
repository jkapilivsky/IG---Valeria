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
        "user-data-dir=C:/Users/jamie.kapilivsky/PycharmProjects/Instagram/Profiles/Follow_Like_Profile")  # Path to your chrome profile
    driver = webdriver.Chrome(executable_path='../../assets/chromedriver', chrome_options=options)
    driver.get("https://www.instagram.com/")
    sleep()
def sleep():
    time.sleep(randint(6, 9))

def text_me(message):
    twilio_number = '+19562720613'
    jamie_number = '+19568214550'
    valeria_number = '+19564370322'
    #phone_number = '+1%s' % input('What is your phone number?')

    client.messages.create(to=jamie_number,
                           from_=twilio_number,
                           body=message)

def search_famous_person(hashtag):
    # Search bar
    search = driver.find_element_by_xpath('''//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input''')
    search.clear()
    search.send_keys(hashtag)
    search.send_keys(Keys.ENTER)
    sleep()
    # Goes to first person in search
    search_results = driver.find_elements_by_class_name('_gimca')
    search_results[0].click()
    sleep()

def like_unlike_check():

    like_elem = driver.find_elements_by_xpath("//a[@role = 'button']/span[text()='Like']")
    liked_elem = driver.find_elements_by_xpath("//a[@role = 'button']/span[text()='Unlike']")

    if len(like_elem) == 1:
        driver.execute_script(
            "document.getElementsByClassName('" + like_elem[0].get_attribute("class") + "')[0].click()")
        print('--> Image Liked!')
        time.sleep(2)
    elif len(liked_elem) == 1:
        print('--> Already Liked!')
    else:
        print('--> Invalid Like Element!')

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

def follow_like_people(number_of_people, minutes):
    count = 0
    followed = 0
    while count < number_of_people:
        try:
            follow_button = driver.find_element_by_class_name('_4tgw8')
            if follow_button.text == 'Follow':
                follow_button.click()
                write_pickle()
                followed += 1
        except NoSuchElementException:
            continue

        time.sleep(.3)
        like_unlike_check()
        # right click on images to scroll
        driver.find_element_by_class_name('''coreSpriteRightPaginationArrow''').click()
        count += 1
        sleep()
        wait_time(followed, minutes)

def wait_time(followed, minutes):
    if (followed + 1) % 11 == 0:  # Sleeps for x minutes every 10 unfollow
        print(followed, 'Followed: Waiting', minutes, 'minutes')
        time.sleep(minutes * 60)  # multiply by 60 seconds

def error_handling():
    return '{}, {}, line: {}'.format(sys.exc_info()[0],
                                     sys.exc_info()[1],
                                     sys.exc_info()[2].tb_lineno)

def error_log(err):
    error_log = pickle.load(open("../../data/Instagram_error_log.p", "rb"))
    df = pd.DataFrame([[err, 'Follow and like by tag', str(datetime.datetime.now())]],
                      columns=['error message', 'script', 'time_stamp'])
    error_log = error_log.append(df)
    pickle.dump(error_log, open("../../data/Instagram_error_log.p", "wb"))

errors = 1
while errors > 0:
    try:
        open_chrome()
        hastag_list = ['#hudabeauty', '#beautiful', '#iggers', '#followforfollow', '#likeforlike',
                       '#Beautiful', '#me', '#instagood', '#Austin']

        for hash in hastag_list:
            search_famous_person(hash)
           # click first image of 'recent posts' *skipping to posts
            driver.find_element_by_xpath(
                '''//*[@id="react-root"]/section/main/article/div[2]/div[1]/div[1]/div[1]/a/div''').click()
            sleep()

            follow_like_people(22, 20)  # number of people to follow, time to wait every 10 people followed
            driver.get("https://www.instagram.com/")

        driver.close()

    except Exception as err:
        issue = logging.error(error_handling())
        error_log(issue)
        driver.close()
        errors -= 1
        if errors == 0:
            text_me('follow #tags quit!')
            quit()
        message = 'Follow #tag error...'  + str(errors) + ' errors remaining'
        text_me(message)
