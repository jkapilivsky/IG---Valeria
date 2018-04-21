from twilio.rest import Client
import pandas as pd
import pickle

account = "AC9709d76b68dc19ec27d6e6f7110bff97"
token = "b1e1c73b81733409ed8dcf18fa510ba0"
client = Client(account, token)

#message = client.messages.create(to="+19562259331", from_="+19562653630",
 #                                body="Hello there! - From Python")

twilio_dict = pd.read_pickle('../../../API Keys/Twilio_API.p')
print(twilio_dict)
quit()

print(twilio_dict['twilio_account'])

twilio_dict['twilio_account'] = account
twilio_dict['twilio_key_cred'] = token


with open('../../../API Keys/Twilio_API.p', 'wb') as handle:
    pickle.dump(twilio_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
