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
        "user-data-dir=C:/Users/jamie.kapilivsky/PycharmProjects/Instagram/Profiles/Follow_Nyane_Profile")  # Path to your chrome profile
    driver = webdriver.Chrome(executable_path='../../assets/chromedriver', chrome_options=options)
    driver.get("https://www.instagram.com/")
    sleep()

def sleep():
    time.sleep(randint(6, 9))

def text_me(message):
    twilio_number = '+19562653630'
    jamie_number = '+19568214550'
    valeria_number = '+19564370322'
    #phone_number = '+1%s' % input('What is your phone number?')

    client.messages.create(to=jamie_number,
                           from_=twilio_number,
                           body=message)

def who_to_follow(person):
    global famous_person
    hour = int(datetime.datetime.now().strftime('%H'))
    if hour <= 12:
        famous_person = person
    else:
        famous_person = person

def search_famous_person():
    # Search bar
    search = driver.find_element_by_xpath('''//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input''')
    search.clear()
    search.send_keys(famous_person)
    search.send_keys(Keys.ENTER)
    sleep()
    # Goes to first person in search
    search_results = driver.find_elements_by_class_name('_gimca')
    search_results[0].click()
    sleep()

def write_to_database(name, future_followers):
    # Begin pickle
    data = pickle.load(open("../../data/Instagram_data.p", "rb"))
    df = pd.DataFrame(
        [[name[future_followers].text, 'Following', str(datetime.datetime.now()),
          'Follow_by_tag_' + str(famous_person)]],
        columns=['username', 'status', 'time_stamp', 'acquisition'])
    data = data.append(df)
    pickle.dump(data, open("../../data/Instagram_data.p", "wb"))
    # End pickle
    sleep()

def follow_people(amount):
    # Click followers on image
    driver.find_element_by_xpath('''/html/body/div[4]/div/div[2]/div/article/div[2]/section[2]/div/a''').click()
    sleep()

    for future_followers in range(amount):
        data_names = pickle.load(open("../../data/Instagram_data.p", "rb"))
        username_list = data_names['username'].tolist()

        name = driver.find_elements_by_class_name('_2g7d5')
        buttons = "../../../../div[2]/span"

        if name[future_followers].text == 'linethmm':
            continue

        if name[future_followers].text in username_list:
            continue

        if name[future_followers].find_element_by_xpath(buttons).text == 'Follow':
            name[future_followers].find_element_by_xpath(buttons).click()
            sleep()
        else:
            continue
        print("Now following: ", name[future_followers].text)

        write_to_database(name, future_followers)

def check_for_new_post(amount):
    driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/article/div/div[1]/div[1]/div[1]/a/div''').click()
    post_time = driver.find_element_by_class_name('_p29ma').text
    if "HOURS AGO" in post_time:
        print('new pic!')
        follow_people(amount)
        sleep()
    else:
        pass

def error_handling():
    return '{}, {}, line: {}'.format(sys.exc_info()[0],
                                     sys.exc_info()[1],
                                     sys.exc_info()[2].tb_lineno)

def error_log(err):
    error_log = pickle.load(open("../../data/Instagram_error_log.p", "rb"))
    df = pd.DataFrame([[err, 'Follow new Nyane post', str(datetime.datetime.now())]],
                      columns=['error message', 'script', 'time_stamp'])
    error_log = error_log.append(df)
    pickle.dump(error_log, open("../data/Instagram_error_log.p", "wb"))

errors = 1
while errors > 0:
    try:
        open_chrome()
        who_to_follow('nyane')  # day and night
        search_famous_person()
        check_for_new_post(8)  # amount = number of people to follow

        driver.close()
        print('Waiting 20 minutes!')
        time.sleep(20*60)

    except Exception as err:
        issue = error_handling()
        error_log(issue)
        driver.close()

        errors -= 1
        if errors == 0:
            text_me('follow famous person QUIT!')
            quit()
        message = 'Nyane Famous person error...' + str((errors)) + ' errors remaining'
        text_me(message)
