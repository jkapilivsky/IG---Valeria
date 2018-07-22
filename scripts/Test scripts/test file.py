import pandas as pd
import pickle
from selenium import webdriver
import platform

cookies = pickle.load(open("../../assets/cookies.p", "rb"))
for cookie in cookies:
    print(cookie)

options = webdriver.ChromeOptions()
# default directory. Personal desktop at home
dir = "user-data-dir=C:/Users/jamie/PycharmProjects/Instagram/Profiles/"

# Identify Solarwinds computer to change directory
if platform.processor() == 'Intel64 Family 6 Model 78 Stepping 3, GenuineIntel':
    dir = "user-data-dir=C:/Users/jamie.kapilivsky/PycharmProjects/Instagram/Profiles/"

options.add_argument(dir + 'Extra_Profile')  # Path to your chrome profile
driver = webdriver.Chrome(executable_path='../../assets/chromedriver', chrome_options=options)

driver.get('https://www.instagram.com')

