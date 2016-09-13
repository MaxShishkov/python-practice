from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

account_sid = "ACebfe6034f42608f44ec7f9fdafbdb6d7" # Your Account SID from www.twilio.com/console
auth_token  = "64e4cdc02959aecbac7d209e05228598"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

try:
    message = client.messages.create(body="My name is Ron Burgandy?",
        to="+19712398759",    # Replace with your phone number
        from_="+13185003321") # Replace with your Twilio number
except TwilioRestException as e:
    print(e)
