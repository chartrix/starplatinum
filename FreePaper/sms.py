# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hola Felipe. Consulta tu recibo de Banco Azteca por el movimiento de deposito en efectivo: "
                          "https://bit.ly/2HparJQ",
                     from_='+12013971707',
                     to='+525545037836'
                 )

print(message.sid)