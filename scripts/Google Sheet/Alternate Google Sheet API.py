import math
import time
import timeit
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import sys
import pandas as pd
import pickle
from random import randint

sys.path.insert(0, 'C:/Users/jamie/PycharmProjects/Instagram/Insta files/scripts/Functions')
from Insta_functions import twilio, text_me, error_handling, open_chrome, remove_k_m_periods_commas
from Insta_functions import right_arrow, click_first_post

def sleep():
    time.sleep(randint(6, 9))

def overall_stats():
    # grab followers number
    global follower, following, posts

    follower = driver.find_element_by_xpath(
        '''//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span''')
    follower = follower.get_attribute('title')
    follower = follower.replace(',', '')  # Deletes the comma when over 1,000
    follower = int(follower)  # Turns the text into an integer
    # grab following number
    following = driver.find_element_by_xpath(
        '''//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span''').text
    following = following.replace(',', '')
    following = int(following)
    # Grab number of posts
    posts = driver.find_element_by_xpath(
        '''//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span/span''').text
    posts = posts.replace(',', '')
    posts = int(posts)
    sleep()

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
        global driver
        driver = open_chrome('GSheet_Profile')

        twilio()
        sleep()
        posts = follower = following = 0

        # go to profile
        driver.find_element_by_xpath('''//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a''').click()
        sleep()

        overall_stats()

        print(posts)
        print(follower)
        print(following)
        print('#'*40)

        likes = 0
        video_views = 0
        comments = 0

        # Click first post
        click_first_post()
        sleep()
        for picture in range(posts-1):
            #likes
            try:
                like_amount = driver.find_element_by_xpath('''/html/body/div[3]/div/div[2]/div/article/div[2]/section[2]/div/a/span''').text
                likes += remove_k_m_periods_commas(like_amount)
                    #likes += like_amount
            except:
                video_amount = driver.find_element_by_xpath(
                    '''/html/body/div[3]/div/div[2]/div/article/div[2]/section[2]/div/span/span''').text
                video_views += remove_k_m_periods_commas(video_amount)

            # Right arrow
            right_arrow()
            time.sleep(randint(3,4))

            #print(picture, likes)


#  ################################-----BELOW----SEND DATA TO GOOGLE SHEETS-----#####################################   #

        # use creds to create a client to interact with the Google Drive API
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('../../../API Keys/GSheet_client_secret', scope)
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
        print(err)
        issue = error_handling()
        error_log(issue)
        driver.close()
        msg = "Google API down.. reason=" + str(err)
        text_me(message=msg)
        print(msg)
        errors -= 1

