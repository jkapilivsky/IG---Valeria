import time, sys
from twilio.rest import Client
import pandas as pd
from random import *

sys.path.insert(0, 'C:/Users/jamie/PycharmProjects/Instagram/Insta files/scripts/Functions')
from Insta_functions import error_handling, open_chrome

def twilio():
    global client
    twilio_dict = pd.read_pickle('../../../API Keys/Twilio_API.p')
    twilio_acc = list(twilio_dict.values())[0]
    twilio_cred = list(twilio_dict.values())[1]
    client = Client(twilio_acc, twilio_cred)  # For Twilio

def text_me(message):
    twilio_number = '+19562653630'
    jamie_number = '+19568214550'
    valeria_number = '+19564370322'
    #phone_number = '+1%s' % input('What is your phone number?')

    client.messages.create(to=valeria_number,
                           from_=twilio_number,
                           body=message)


insta_list = []



insta_list2 = []





#
influencers_list = insta_list + insta_list2
randomized_list = sorted(influencers_list, key=lambda x: random())

twilio()

didnt_like = []
'''
def like_unlike_check():
    like_elem = driver.find_elements_by_xpath("//a[@role = 'button']/span[text()='Like']")
    liked_elem = driver.find_elements_by_xpath("//a[@role = 'button']/span[text()='Unlike']")
    print(like_elem)

    if len(like_elem) == 1:
        driver.execute_script(
            "document.getElementsByClassName('" + like_elem[0].get_attribute("class") + "')[0].click()")
        print('--> Image Liked!')
        time.sleep(2)
    elif len(liked_elem) == 1:
        print('--> Already Liked!')
    else:
        print('--> Invalid Like Element!')
'''

def like_unlike_check():
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


driver = open_chrome('Liking_pics_Profile')
print(len(insta_list))
count = 0
for insta_picture in randomized_list:
    count+= 1
    print(count, insta_picture)
    try:
        driver.get(insta_picture)
        time.sleep(randint(1,3))
        like_unlike_check()
        time.sleep(randint(29,35))
    except:
        didnt_like.append(insta_picture)
        time.sleep(4)

text = 'Facebook pod likes complete!... We liked: ' + str(len(randomized_list) - len(didnt_like)) + ' pictures'
text_me(text)
print('didnt like', didnt_like)
driver.close()
print('Complete')

# ADD ABOVE TO FIX URLs
'''
# Fixing URLs
updated_insta_list = []
for url in insta_list:
    the_u = url.find('?u=')
    url = url[the_u+3:]

    url = url.replace('%3A' ,':')
    url = url.replace('%2F', '/')
    url = url.replace('%3F', '?')
    url = url.replace('%3D', '=')

    amper = url.find('&')
    updated_insta_list.append(url[:amper])

print(updated_insta_list)
'''