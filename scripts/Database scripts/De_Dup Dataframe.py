import pickle
import pandas as pd

# TODO -  need to fix to increase number of interactions if duplicate!


data = pickle.load(open("../../data/Instagram_data.p", "rb"))
data.drop_duplicates(subset='username', keep='last', inplace=True)
pickle.dump(data, open("../../data/Instagram_data.p", "wb"))

data = pickle.load(open("../../data/Instagram_data.p", "rb"))
pickle.dump(data, open("../../data/Instagram_data_backup.p", "wb"))

error_log = pickle.load(open('../../data/Instagram_error_log.p', 'rb'))
pickle.dump(error_log, open('../../data/Instagram_error_log_backup.p', 'wb'))




#script used to create new pickle!
'''
old_data = pickle.load(open("../../data/Instagram_data_start_12_25_2017.p", "rb"))
df = old_data[old_data['status'].isin(['official_friend'])]

new_df = pd.DataFrame(columns=['username', 'status', 'time_stamp', 'acquisition'])

new_df = new_df.append(df)
pickle.dump(new_df, open('../../data/Instagram_data_backup.p', 'wb'), protocol=pickle.HIGHEST_PROTOCOL)
'''
