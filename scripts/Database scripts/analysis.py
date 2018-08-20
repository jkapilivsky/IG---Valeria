import pickle
import pandas as pd

insta_data = pickle.load(open("../../data/Instagram_data.p", "rb"))
print(insta_data.head())
print(insta_data.describe())

# TODO - new columns
# number of times interacted
# last time interacted with (time_stamp)

# TODO - daily job to create backup of instagram data?


