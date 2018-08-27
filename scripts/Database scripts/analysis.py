import pickle
import pandas as pd
import os
import datetime
print(len('https://www.instagram.com/'))

test = 'https://www.instagram.com/jamie'
print(test[26:])

insta_data = pickle.load(open("../../data/Instagram_data.p", "rb"))
print(insta_data.head())
print(insta_data['user_url'].head())
print(insta_data.columns)

# linethmm_df = pd.DataFrame([['Yes', 'NaN', '', 'https://www.instagram.com/linethmm',
#                             '4/5/1993', '4/5/1993', 1000, 10000000, 10000000, 1000000]], columns=
#                             ['Official_Friend', 'acquisition', 'status', 'user_url',
#                              'first_interacted_time', 'last_interacted_time',
#                              'number_of_interactions', 'posts', 'followers', 'following']
#                            )
# merge = pd.concat([insta_data, linethmm_df])
# print(merge[merge['user_url'] == 'https://www.instagram.com/linethmm'])
# pickle.dump(merge, open("../../data/Instagram_data.p", "wb"))
quit()
datetime.datetime.now()


# ########################## UPDATE interaction amount ##########################
test_df = pd.DataFrame([[1, 'jamie', datetime.datetime.now()-datetime.timedelta(days=1), datetime.datetime.now()-datetime.timedelta(days=1)]],
                       columns=['interacted','username', 'first_time', 'last_time'])
new_row = pd.DataFrame([[2, 'jamie', datetime.datetime.now(), datetime.datetime.now()]],
                       columns=['interacted','username', 'first_time', 'last_time'])

appended_df = test_df.append(new_row)

grouped_df = appended_df.groupby(appended_df['username']).sum()
grouped_df['username'] = grouped_df.index
del test_df['interacted']
del new_row['interacted']
merged_df = pd.merge(appended_df, grouped_df, how='left', on=['username'])
# ########################## UPDATE interaction amount ##########################
print(merged_df)

################### GET MAX TIME for last interacted time #######################
# TODO - just use the time from the new merge? and keep the old time from the original row?



################### GET MAX TIME for last interacted time #######################

# TODO - new columns
# number of times interacted
# last time interacted with (time_stamp)

# TODO - daily job to create backup of instagram data?


