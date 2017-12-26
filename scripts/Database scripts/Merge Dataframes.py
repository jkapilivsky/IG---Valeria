import pickle
import pandas as pd

data_desktop = pickle.load(open("../../data/Instagram_data.p", "rb"))
data_mac = pickle.load(open('../../data/Instagram_data_mac.p', 'rb'))

merge_data = pd.concat([data_desktop, data_mac])
del merge_data['index']
del merge_data['level_0']

merge_data = merge_data.sort_values(by='time_stamp', ascending=True)
merge_data = merge_data.reset_index()
del merge_data['index']

merge_data.drop_duplicates(subset='username', keep='last', inplace=True)
merge_data = merge_data.reset_index()
del merge_data['index']

pickle.dump(merge_data, open("../../data/Instagram_data.p", "wb"))