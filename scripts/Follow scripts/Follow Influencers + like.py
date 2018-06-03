from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time, datetime, pickle, sys
import pandas as pd
from random import *


sys.path.insert(0, 'C:/Users/jamie/PycharmProjects/Instagram/Insta files/scripts/Functions')
from Insta_functions import sleep, twilio, text_me, error_handling, open_chrome, search, remove_k_m_periods_commas
from Insta_functions import isEnglish

def write_to_database(name, future_followers):
    # Begin pickle
    data = pickle.load(open("../../data/Instagram_data.p", "rb"))
    df = pd.DataFrame(
        [[name[future_followers].text, 'Following', str(datetime.datetime.now()),
          'Follow_influencer_person_' + str(influencer)]],
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

    while count_posts <= num_images_to_like:
        count_posts += 1
        sleep()
        # if statement looks for a video
        if count_posts >= num_images_to_like:
            break

        try:
            like_unlike_check()
            sleep()
            # right click on images to scroll
            driver.find_element_by_class_name('''HBoOv''').click()
            sleep()

        except NoSuchElementException:
            print('Image is not a picture!')
            not_pic_count += 1
            count_posts =- 1

            if not_pic_count == 3:
                break

    if not_pic_count == 3:
        driver.back()
    else:
        driver.back()
        sleep()
        driver.back()

def follow_people(amount, num_pics_to_like):
    # Click followers
    driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a''').click()
    sleep()

    for future_followers in range(amount):
        data_names = pickle.load(open("../../data/Instagram_data.p", "rb"))
        username_list = data_names['username'].tolist()

        # TODO - update 1
        name = driver.find_elements_by_class_name('FPmhX')
        buttons = "../../../../div[2]/span"

        # Makes sure there are only english characters
        if isEnglish(name[future_followers].text) == False:
            continue

        # Making sure we haven't already iteracted with them or is our own account
        if name[future_followers].text == 'linethmm' or name[future_followers].text in username_list:
            # TODO - update 2 to check
            print(name[future_followers].text)
            continue

        if name[future_followers].find_element_by_xpath(buttons).text == 'Follow':
            name[future_followers].find_element_by_xpath(buttons).click()
            print("Now following: ", name[future_followers].text)
            write_to_database(name, future_followers)
            sleep()  #Deletethis
            # TODO - THIS IS WHERE TO TURN ON AND OFF THE LIKING STUFFFFFF
            # continue
        else:
            continue

        # Click person in list order (goes to their profile)
        name[future_followers].click()
        sleep()

        # Check number of posts they have!
        # Makes sure that the user has enough images to like!
        try:
            total_images = driver.find_element_by_xpath(
            '''//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span/span''').text
            total_images = remove_k_m_periods_commas(total_images)

            if total_images >= num_pics_to_like:
                total_images = num_pics_to_like

        except NoSuchElementException:
            print('unavailable page?')
            driver.back()
            continue

        # Clicks the person's first image
        try:
            # TODO - update 3... change class name from _e3il2 to eLAPa
            driver.find_element_by_class_name('''eLAPa''').click()
            sleep()
        except NoSuchElementException:
            print('Private account')
            driver.back()
            continue

        likes_persons_posts(total_images)
        sleep()

def error_log(err):
    error_log = pickle.load(open("../../data/Instagram_error_log.p", "rb"))
    df = pd.DataFrame([[err, 'Follow Famous people followers', str(datetime.datetime.now())]],
                      columns=['error message', 'script', 'time_stamp'])
    error_log = error_log.append(df)
    pickle.dump(error_log, open("../../data/Instagram_error_log.p", "wb"))

errors = 1
while errors > 0:
    try:
        global driver
        driver = open_chrome('Follow_Like_Influencers')
        twilio()
        influencers_list = ['sichenmakeupholic', 'nyane']
        #finding_hash_first = ['michellephan', 'hudabeauty','wengie', ]
        new_influencers_list = ['vdethe', 'ashleesummer', 'snitchery', 'mamapeach_'] + influencers_list
        randomized_list = sorted(influencers_list, key=lambda x:random())
        randomized_list2 = sorted(new_influencers_list, key=lambda x:random())

        for influencer in randomized_list2:
            print('following:', influencer)
            search(influencer)
            follow_people(8, 3)  # amount = number of people to follow, number of pictures to like
            print('======Waiting 8 minutes!======')
            time.sleep(8*60)
            driver.back()

        driver.close()

    except Exception as err:
        print(err)
        issue = error_handling()
        error_log(issue)
        driver.close()

        errors -= 1
        if errors == 0:
            text_me('Influencer+like QUIT!')
            quit()
        message = 'Influencer+like error...' + str((errors)) + ' errors remaining'
        text_me(message)

# Traceback (most recent call last):
#   File "C:/Users/jamie/PycharmProjects/Instagram/Insta files/scripts/Follow scripts/Follow Influencers + like.py", line 152, in <module>
#     search(influencer)
#   File "C:/Users/jamie/PycharmProjects/Instagram/Insta files/scripts/Functions\Insta_functions.py", line 62, in search
#     # Goes to first person in search
# IndexError: list index out of range