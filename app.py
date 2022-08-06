from twilio.rest import Client
from config import *

# Account sid + authorization token = sensitive data. Found in the account section. Sent to the config file
# account_sid = "AC654ba7dece7053bcfff2bea83be84665"
# auth_token = "0929c146735064869ac0657fcfd3cb0b"
client = Client(account_sid, auth_token)


# Access messages and create functions of the client object
call = client.messages.create(
    to="440-596-9476", from_="19093215097", body="Yo what's up sexy")
