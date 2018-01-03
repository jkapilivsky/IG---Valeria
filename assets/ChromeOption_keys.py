import pandas as pd
import pickle

dict = {}
dict['Jamie_Desktop_Extra_Profile'] = 'user-data-dir=C:/Users/jamie/PycharmProjects/Instagram/Profiles/Extra_Profile'
dict['Jamie_Work_Laptop_Extra_Profile'] = 'user-data-dir=C:/Users/jamie.kapilivsky/PycharmProjects/Instagram/Profiles/Extra_Profile'

with open('ChromeOptions.p', 'wb') as handle:
    pickle.dump(dict, handle, protocol=pickle.HIGHEST_PROTOCOL)