import datetime
import  pickle

today = datetime.date.today()  # Gets today's date
yesterday = datetime.date.today() - datetime.timedelta(days=1)

data = pickle.load(open("../../data/Instagram_data.p", "rb"))

official_friend_df = data[data['status'].isin(['official_friend'])]
follow_unfollow_df = data[data['status'].isin(['Unfollowed', 'Following'])]

# yesterday_df = normal[normal['time_stamp'].str.contains(str(today-yesterday))]
today_df = data[data['time_stamp'].str.contains(str(today))]

following_today = today_df[today_df['status'].isin(['Following'])]
unfollowed_today = today_df[today_df['status'].isin(['Unfollowed'])]

print(following_today.count())
print(unfollowed_today.count())