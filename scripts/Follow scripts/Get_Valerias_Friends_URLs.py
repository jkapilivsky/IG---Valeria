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

driver = open_chrome('Extra_Profile')
time.sleep(2)
twilio()
# go to profile
driver.get('https://www.instagram.com/linethmm')
sleep()
# Get's people to follow!
click_posts_followers_followings('followings')
sleep()

repeat_space_bar(311/4)

names = []
for people in range(311):
    name = driver.find_elements_by_class_name('FPmhX')
    names.append(name[people].text)

print(names)
print('total friends', len(names))
text_me('here!')
friend_urls = []
for name in names:
    url = 'https://www.instagram.com/' + name
    friend_urls.append(url)

print(friend_urls)
print('total_urls', len(friend_urls))
quit()

#TODO - doesnt work!
friend_df = pd.DataFrame(columns=['user_url', 'status', 'time_stamp', 'Official_Friend'])
for url in friend_urls:
    df = pd.DataFrame(
        [[url, 'Official_Friend', str(datetime.datetime.now()), 'Follow_Like_150']],
        columns=['user_url', 'status', 'time_stamp', 'Official_Friend'])

    friend_df.append(df)

print(friend_df)
pickle.dump(friend_df, open("../../data/Instagram_data.p", "wb"))

print('Complete')
text_me('Friends URLs complete!')