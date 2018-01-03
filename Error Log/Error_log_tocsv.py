import pickle
import pandas as pd
import datetime

date = datetime.date.today()
error_df = pd.read_pickle('../data/Instagram_error_log.p')
print(error_df)
error_df.to_csv('Error logs/Error_log_' + str(date) + '.csv')


#Need to clear logs!
# new_error_log_df = pd.DataFrame(columns=['error message', 'script', 'timestamp'])
# print(new_error_log_df)
# pickle.dump(new_error_log_df, open('../Insta files/data/Instagram_error_log.p', 'wb'), protocol=pickle.HIGHEST_PROTOCOL)
