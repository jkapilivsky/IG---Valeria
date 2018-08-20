import pandas as pd
import datetime
import pickle
import numpy as np

date = datetime.date.today()

# df = pd.read_pickle('Official_friends_df.p')
# df.reset_index(inplace=True)
# del df['index']
# pickle.dump(df, open('Official_friends_df.p', 'wb'))
# pickle.dump(df, open('Official_friends_df_backup.p', 'wb'))
# pickle.dump(df, open('Instagram_data.p', 'wb'))
# pickle.dump(df, open('Instagram_data_backup.p', 'wb'))


# RESET INSTA_DATA
'''
df = df.iloc[0:0]
df.to_pickle('Instagram_data.p')
quit()
'''