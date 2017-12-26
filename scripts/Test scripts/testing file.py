import pickle
import pandas as pd
df = pd.DataFrame(columns=['error message', 'script', 'time_stamp'])

#error_log = pickle.load(open("../data/Instagram_error_log.p", "rb"))
# df = pd.DataFrame([[err, 'new FOLLOW script', str(datetime.datetime.now())]],
#                   columns=['error message', 'script', 'time_stamp'])
# error_log = error_log.append(df)
#pickle.dump(df, open("../data/Instagram_error_log.p", "wb"))
pickle.dump(df, open('../../data/Instagram_error_log.p', 'wb'))