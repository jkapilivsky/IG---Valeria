import pandas as pd
import pickle


# Begin pickle
data = pickle.load(open("../../data/Instagram_data.p", "rb"))
official_friends = data['username'][data['status'] == 'official_friend'].tolist()

print(official_friends)