from twilio.rest import Client
import os
from os.path import join, dirname
from dotenv import load_dotenv

class Sms:
    def __init__(self,account_sid,auth_token):
        self.__account_sid = account_sid
        self.__auth_token = auth_token
        self.__clientSMS

    def setupSms(self):
        self.__clientSMS = Client(self.__account_sid, self.__auth_token)

    def sendMessage(self,msg,destinatary):
        message = self.__clientSMS.messages \
            .create(
            body=msg,
            from_='+12013971707',
            to=destinatary
        )