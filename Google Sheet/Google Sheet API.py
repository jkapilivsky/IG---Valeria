import math
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import timeit
from selenium.webdriver.common.action_chains import ActionChains
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from twilio.rest import Client
import sys, logging
import pandas as pd
import pickle

def sleep():
    time.sleep(3.5)

def log_into_instagram(username, password):
    driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a''').click()
    time.sleep(5)

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

def repeat_space_bar(number_of_times):
    count = 0
    while count < number_of_times:
        driver.find_element_by_class_name('coreSpriteGlyphBlack').send_keys(Keys.SPACE)
        time.sleep(1)
        count += 1

def overall_stats():
    # grab followers number
    global follower, following, posts

    follower = driver.find_element_by_xpath(
        '''//*[@id="react-root"]/section/main/article/header/section/ul/li[2]/a/span''')
    follower = follower.get_attribute('title')
    follower = follower.replace(',', '')  # Deletes the comma when over 1,000
    follower = int(follower)  # Turns the text into an integer
    # grab following number
    following = driver.find_element_by_xpath(
        '''//*[@id="react-root"]/section/main/article/header/section/ul/li[3]/a/span''').text
    following = following.replace(',', '')
    following = int(following)

    # Grab number of posts
    posts = driver.find_element_by_xpath(
        '''//*[@id="react-root"]/section/main/article/header/section/ul/li[1]/span/span''').text
    posts = posts.replace(',', '')
    posts = int(posts)

    sleep()

def text_me(message):
    twilio_number = '+19562720613'
    jamie_number = '+19568214550'
    valeria_number = '+19564370322'
    #phone_number = '+1%s' % input('What is your phone number?')

    client.messages.create(to=jamie_number,
                           from_=twilio_number,
                           body=message)

def twilio():
    global client
    twilio_dict = pd.read_pickle('../../API Keys/Twilio_API.p')
    twilio_acc = list(twilio_dict.values())[0]
    twilio_cred = list(twilio_dict.values())[1]
    client = Client(twilio_acc, twilio_cred)  # For Twilio

def open_chrome():
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-data-dir=C:/Users/jamie.kapilivsky/PycharmProjects/Instagram/Profiles/GSheet_Profile")  # Path to your chrome profile
    driver = webdriver.Chrome(executable_path='../assets/chromedriver', chrome_options=options)
    driver.get("https://www.instagram.com/")
    sleep()

def error_handling():
    return '{}, {}, line: {}'.format(sys.exc_info()[0],
                                     sys.exc_info()[1],
                                     sys.exc_info()[2].tb_lineno)

def error_log(err):
    error_log = pickle.load(open("../../data/Instagram_error_log.p", "rb"))
    df = pd.DataFrame([[err, 'new FOLLOW script', str(datetime.datetime.now())]],
                      columns=['error message', 'script', 'time_stamp'])
    error_log = error_log.append(df)
    pickle.dump(error_log, open("../../data/Instagram_error_log.p", "wb"))

errors = 3
while errors > 0:
    try:
        start = timeit.default_timer()
        open_chrome()
        twilio()
        posts = follower = following = None
        sleep()
        #log_into_instagram('linethmm', 'I1232123you')

        # go to profile
        driver.find_element_by_xpath('''//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a''').click()
        sleep()

        overall_stats()

        # Click 'load more'
        try:
            driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/article/div/a''').click()
            sleep()
        except NoSuchElementException:
            pass

        repeat_space_bar(round(int(posts)/3))  # Scrolls down to the bottom of the profile page

        likes = 0
        video_views = 0
        comments = 0

        # [0] is the first return in that function. aka posts
        for pictures in range(int(posts)):
            x = math.floor(pictures/3) + 1
            y = (pictures % 3) + 1

            images = driver.find_elements_by_class_name('_e3il2')
            hover = ActionChains(driver).move_to_element(images[pictures])
            hover.perform()
            information = driver.find_element_by_class_name('_lpowm').find_elements_by_tag_name("span")

            try:
                driver.find_element_by_class_name('_puatn')
                likes += int(information[0].text)

            except NoSuchElementException:
                # driver.find_element_by_class_name('_d9a84')
                video_views += int(information[0].text)

            comments += int(information[2].text)

            time.sleep(.3)

        print(likes)
        print(video_views)
        print(comments)

        #  ################################-----BELOW----SEND DATA TO GOOGLE SHEETS-----#####################################   #

        # use creds to create a client to interact with the Google Drive API
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('../../API Keys/GSheet_client_secret', scope)
        client = gspread.authorize(creds)

        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        follower_data_sheet = client.open("API Version - Valeria's Insta Analytics").worksheet('Follower Data')
        like_data_sheet = client.open("API Version - Valeria's Insta Analytics").worksheet('Like Data')
        follow_data_per_hour = client.open("API Version - Valeria's Insta Analytics").worksheet('Follower Data per hour')
        like_data_per_hour = client.open("API Version - Valeria's Insta Analytics").worksheet('Like Data per hour')

        # update the 'today' cell
        follower_data_sheet.update_cell(2, 14, str(datetime.date.today()))
        like_data_sheet.update_cell(2, 13, str(datetime.date.today()))
        follow_data_per_hour.update_cell(2, 12, str(datetime.date.today()))
        like_data_per_hour.update_cell(2, 14, str(datetime.date.today()))

        # Checks if the cell is Today and sends value to Google Sheets#
        sheet1_counter = 0
        sheet2_counter = 0
        follow_per_hour_counter = 0
        like_data_per_hour_counter = 0

        for x in range(1, follower_data_sheet.row_count):
            if follower_data_sheet.cell(x, 2).value == str(datetime.date.today()):
                follower_data_sheet.update_cell(x, 5, follower)
                follower_data_sheet.update_cell(x, 12, following)
                sheet1_counter += 1
                break

        # checks for today's date and sends number of posts/likes/video views to Google sheets
        for x in range(1, like_data_sheet.row_count):
            if like_data_sheet.cell(x, 2).value == str(datetime.date.today()):
                like_data_sheet.update_cell(x, 3, posts)
                like_data_sheet.update_cell(x, 5, likes)
                like_data_sheet.update_cell(x, 7, video_views)
                like_data_sheet.update_cell(x, 10, comments)
                sheet2_counter += 1
                break

        for x in range(1, follow_data_per_hour.row_count):
            if follow_data_per_hour.cell(x, 2).value != '':
                continue
            else:
                follow_data_per_hour.update_cell(x, 1, str(datetime.datetime.now()))
                follow_data_per_hour.update_cell(x, 2, str(datetime.date.today()))

                hour = int(datetime.datetime.now().strftime('%H'))
                if hour > 12:
                    hour = str(hour - 12) + 'pm'
                else:
                    hour = str(hour) + 'am'
                follow_data_per_hour.update_cell(x, 3, hour)
                follow_data_per_hour.update_cell(x, 6, follower)
                follow_data_per_hour.update_cell(x, 10, following)
                follow_per_hour_counter += 1
                break

        for x in range(1, like_data_per_hour.row_count):
            if like_data_per_hour.cell(x, 2).value != '':
                continue
            else:
                like_data_per_hour.update_cell(x, 1, str(datetime.datetime.now()))
                like_data_per_hour.update_cell(x, 2, str(datetime.date.today()))

                hour = int(datetime.datetime.now().strftime('%H'))
                if hour > 12:
                    hour = str(hour - 12) + 'pm'
                else:
                    hour = str(hour) + 'am'
                like_data_per_hour.update_cell(x, 3, hour)
                like_data_per_hour.update_cell(x, 5, posts)
                like_data_per_hour.update_cell(x, 7, likes)
                like_data_per_hour.update_cell(x, 9, video_views)
                like_data_per_hour.update_cell(x, 11, comments)
                like_data_per_hour_counter += 1
                break

        # calculates runtime
        stop = timeit.default_timer()
        print('Minutes: ', (stop - start) / 60)
        print('Total Seconds: ', (stop - start))
        print(datetime.datetime.now())
        wait_time=3600 - int(math.floor(stop-start))

        driver.close()
        time.sleep(wait_time)

    except Exception as err:
        issue = logging.error(error_handling())
        error_log(issue)
        driver.close()
        msg = "Google API down" + repr(err)
        text_me(message=msg)
        errors -= 1
