import pickle

data = pickle.load(open("../../data/Instagram_data.p", "rb"))
data.drop_duplicates(subset='username', keep='last', inplace=True)
pickle.dump(data, open("../../data/Instagram_data.p", "wb"))

data = pickle.load(open("../../data/Instagram_data.p", "rb"))
pickle.dump(data, open("../../data/Instagram_data_backup.p", "wb"))

error_log = pickle.load(open('../../data/Instagram_error_log.p', 'rb'))
pickle.dump(error_log, open('../../data/Instagram_error_log_backup.p', 'wb'))
