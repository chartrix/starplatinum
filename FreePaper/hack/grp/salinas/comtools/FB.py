from fbchat import Client
from fbchat.models import *
import os
from os.path import join, dirname
from dotenv import load_dotenv


class FB:
    def __init__(self, account, auth):
        self.__account = account
        self.__auth = auth
        self.__clientFB

    def setuFB(self):
        self.__clientFB = Client(self.__account, self.__auth )

    def sendMessage(self,msg,destinatary):
        client = self.__clientFB.uid
        self.__clientFB.sendRemoteImage(
            "https://bit.ly/2HparJQ",
            message=Message(text=msg),
            thread_id=client.uid,
            thread_type=ThreadType.USER)
