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
        "user-data-dir=C:/Users/jamie.kapilivsky/PycharmProjects/Instagram/Profiles/Liking_people_following_Profile")  # Path to your chrome profile
    driver = webdriver.Chrome(executable_path='../../assets/chromedriver', chrome_options=options)
    driver.get("https://www.instagram.com/")
    sleep()

def sleep():
    time.sleep(randint(4,7))

def text_me(message):
    twilio_number = '+19562720613'
    jamie_number = '+19568214550'
    valeria_number = '+19564370322'
    #phone_number = '+1%s' % input('What is your phone number?')

    client.messages.create(to=jamie_number,
                           from_=twilio_number,
                           body=message)

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
        driver.find_element_by_class_name('''_gu6vm''').click()
        return True
    except NoSuchElementException:
        # Skips the video and goes to the next image to check if it's not a video
        driver.find_element_by_class_name('''coreSpriteRightPaginationArrow''').click()
        sleep()
        return False

def log_into_instagram(username, password):
    driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a''').click()
    time.sleep(4)

    # Input username
    user = driver.find_element_by_xpath(
        '''//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[1]/div/input''')
    user.clear()
    user.send_keys(username)

    # Input password
    pw = driver.find_element_by_xpath(
        '''//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/input''')
    pw.clear()
    pw.send_keys(password)

    pw.send_keys(Keys.ENTER)
    time.sleep(3)

def remove_k_m_periods_commas(value):
    value = value.replace('k', '')
    value = value.replace('m', '')
    value = value.replace('.', '')
    value = value.replace(',', '')
    return value

def like_peoples_stuffs(people_to_follow, number_of_pics_to_like):
    # go to profile
    driver.find_element_by_xpath('''//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a''').click()
    sleep()

    # Select following people
    driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/article/header/section/ul/li[2]/a''').click()
    sleep()
    # ########################7################begin space bar!#################################################
    tab = 0
    while tab <= 2:
        variable = driver.find_element_by_class_name('_si7dy')
        actions = webdriver.ActionChains(driver)
        actions.move_to_element(variable)
        # actions.click()
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(.5)
        tab += 1

    count = 0
    while count < int(people_to_follow/3):  # Spacebar X number of times
        variable = driver.find_element_by_class_name('_4rbun')
        actions = webdriver.ActionChains(driver)
        actions.move_to_element(variable)
        # actions.click()
        actions.send_keys(Keys.SPACE)
        actions.perform()

        time.sleep(.25)
        count += 1
    # #################################End repeat space bar###############################################

    people_list = []
    for people in range(people_to_follow):
        selenium_list = driver.find_elements_by_class_name('''_2g7d5''')
        people_list.append(selenium_list[people].text)

    print(people_list)

    driver.back()
    sleep()

    # Likes the first x people!
    for x in people_list:  # Still need to click out of image to get to the search bar!!
        print(people_list.index(x), x)
        search = driver.find_element_by_xpath('''//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input''')
        search.clear()
        search.send_keys(x)
        search.send_keys(Keys.ENTER)
        sleep()
        # Goes to first person in search
        search_results = driver.find_elements_by_class_name('_gimca')

        # checks if results are found
        try:
            search_results[0].click()
            sleep()
        except:
            driver.find_element_by_class_name('_oznku')
            search.clear()
            # if statement that breaks for loop if were at the end...
            if people_list.index(x) == len(people_list)-1:
                break
            continue


        # Check if they found hashtag
        try:
            driver.find_element_by_class_name('_kwqc3')
            continue
        except NoSuchElementException:
            if people_list.index(x) == len(people_list)-1:
                break
            pass

        # Check if they found a location
        try:
            driver.find_element_by_class_name('_thew0')
            continue
        except NoSuchElementException:
            if people_list.index(x) == len(people_list)-1:
                break
            pass

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

        # Makes sure we are liking the right person!
        username_found = driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/article/header/section/div[1]/h1''').text
        if x != username_found:
            if people_list.index(x) == len(people_list)-1:
                break
            continue


        if check_if_account_is_private() is True:
            if people_list.index(x) == len(people_list)-1:
                break
            continue

        # Makes sure that the user has enough images to like!
        total_images = driver.find_element_by_xpath(
            '''//*[@id="react-root"]/section/main/article/header/section/ul/li[1]/span/span''').text
        total_images = remove_k_m_periods_commas(total_images)
        total_images = int(total_images)

        # Clicks the person's first image
        try:
            driver.find_element_by_class_name('''_e3il2''').click()
            sleep()
        except NoSuchElementException:
            driver.back()
            continue

        if total_images >= number_of_pics_to_like:
            total_images = number_of_pics_to_like
            sleep()

        likes_persons_posts(total_images)
        sleep()

        # Below goes back twice to profile to start for loop over again
        driver.back()
        sleep()
        driver.back()
        sleep()

    driver.back()
    sleep()

    # go to profile
    driver.find_element_by_xpath('''//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a''').click()
    sleep()

def error_handling():
    return '{}, {}, line: {}'.format(sys.exc_info()[0],
                                     sys.exc_info()[1],
                                     sys.exc_info()[2].tb_lineno)

def error_log(err):
    error_log = pickle.load(open("../../data/Instagram_error_log.p", "rb"))
    df = pd.DataFrame([[err, 'Liking people following', str(datetime.datetime.now())]],
                      columns=['error message', 'script', 'time_stamp'])
    error_log = error_log.append(df)
    pickle.dump(error_log, open("../data/Instagram_error_log.p", "wb"))

error = 1
while error >= 0:
    try:
        open_chrome()
        twilio()
        start = timeit.default_timer()
        sleep()

        like_peoples_stuffs(250, 4)  #number of people, Number of pics to like (line 264)

        stop = timeit.default_timer()
        print('Liking people\'s stuffs')
        print('Minutes: ', (stop - start)/60)
        print('Total Seconds: ', (stop - start))
        driver.close()

    except Exception as err:
        issue = logging.error(error_handling())
        error_log(issue)
        driver.close()
        error -= 1
        if error == 0:
            text_me('Liking follower QUIT!!!' + repr(err))
            quit()
        text = 'caught this error for liking followers: ' + repr(err)
        text_me(text)

#