import time
from twilio.rest import Client
from random import *

def sleep():
    time.sleep(randint(3, 6))


def text_me(message):
    twilio_number = '+19562720613'
    jamie_number = '+19568214550'
    valeria_number = '+19564370322'
    #phone_number = '+1%s' % input('What is your phone number?')

    client.messages.create(to=jamie_number,
                           from_=twilio_number,
                           body=message)

client = Client('AC190d9ac5ae8e8d522ee14d55704ae686', 'cc9f66925040f499193c5cd92427b1a2')  # For Twilio

error = 1
while error == 1:
    try:
        text_me('Python still working :)')
    except Exception as err:
        text_me('Python error :(' + repr(err))
        error -= 1
    time.sleep(3600)

# Comments -