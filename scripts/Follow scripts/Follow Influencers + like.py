from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time, datetime, pickle, sys
import pandas as pd
from random import *


sys.path.insert(0, 'C:/Users/jamie/PycharmProjects/Instagram/Insta files/scripts/Functions')
from Insta_functions import sleep, twilio, text_me, error_handling, open_chrome

def search_famous_person():
    # Search bar
    search = driver.find_element_by_xpath('''//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input''')
    search.clear()
    search.send_keys(famous_person)
    search.send_keys(Keys.ENTER)
    sleep()
    # Goes to first person in search
    search_results = driver.find_elements_by_class_name('_ndl3t')
    search_results[0].click()
    sleep()

def write_to_database(name, future_followers):
    # Begin pickle
    data = pickle.load(open("../../data/Instagram_data.p", "rb"))
    df = pd.DataFrame(
        [[name[future_followers].text, 'Following', str(datetime.datetime.now()),
          'Follow_influencer_person_' + str(famous_person)]],
        columns=['username', 'status', 'time_stamp', 'acquisition'])
    data = data.append(df)
    pickle.dump(data, open("../../data/Instagram_data.p", "wb"))
    # End pickle
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

def likes_persons_posts(num_images_to_like):
    count_posts = 0
    not_pic_count = 0

    while count_posts < num_images_to_like:
        # if statement looks for a video
        try:
            like_unlike_check()
            time.sleep(2)
            # right click on images to scroll
            driver.find_element_by_class_name('''coreSpriteRightPaginationArrow''').click()
            sleep()
            count_posts += 1

        except NoSuchElementException:
            print('Image is not a picture!')
            not_pic_count += 1

            if not_pic_count == 3:
                break

    if not_pic_count == 3:
        driver.back()
    else:
        driver.back()
        sleep()
        driver.back()

def follow_people(amount):
    # Click followers
    driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/article/header/section/ul/li[2]/a''').click()
    sleep()

    for future_followers in range(amount):
        data_names = pickle.load(open("../../data/Instagram_data.p", "rb"))
        username_list = data_names['username'].tolist()

        name = driver.find_elements_by_class_name('_2g7d5')
        buttons = "../../../../div[2]/span"

        if name[future_followers].text == 'linethmm' or name[future_followers].text in username_list:
            continue

        if name[future_followers].find_element_by_xpath(buttons).text == 'Follow':
            name[future_followers].find_element_by_xpath(buttons).click()
            print("Now following: ", name[future_followers].text)
            write_to_database(name, future_followers)
            sleep()
        else:
            continue

        # Click person in list order (goes to their profile)
        name[future_followers].click()
        sleep()

        # Clicks the person's first image
        try:
            driver.find_element_by_class_name('''_e3il2''').click()
            sleep()
        except NoSuchElementException:
            driver.back()
            continue

        likes_persons_posts(3)
        sleep()

def error_log(err):
    error_log = pickle.load(open("../../data/Instagram_error_log.p", "rb"))
    df = pd.DataFrame([[err, 'Follow Famous people followers', str(datetime.datetime.now())]],
                      columns=['error message', 'script', 'time_stamp'])
    error_log = error_log.append(df)
    pickle.dump(error_log, open("../../data/Instagram_error_log.p", "wb"))

errors = 6
while errors > 0:
    try:
        global driver
        driver = open_chrome('Follow_Like_Influencers')
        twilio()
        influencers_list = ['michellephan', 'wengie', 'sichenmakeupholic', 'hudabeauty', 'nyane']
        randomized_list = sorted(influencers_list, key=lambda x:random())

        for influencer in randomized_list:
            famous_person = influencer
            search_famous_person()
            follow_people(16)  # amount = number of people to follow
            print('Waiting 5 minutes!')
            time.sleep(5*60)
            driver.back()

    except Exception as err:
        print(err)
        issue = error_handling()
        error_log(issue)
        driver.close()

        errors -= 1
        if errors == 0:
            #text_me('follow famous person QUIT!')
            quit()
        message = 'Influencer error...' + str((errors)) + ' errors remaining'
        #text_me(message)

