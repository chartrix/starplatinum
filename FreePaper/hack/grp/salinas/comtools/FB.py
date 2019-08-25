from fbchat import Client
from fbchat.models import *
import configparser

class FB:
    def __init__(self):
        self.clientFB = None
        self.config = configparser.ConfigParser()

    def setuFB(self):
        self.config.sections()
        self.config.read('conf/credentials.ini')
        print("FACEBOOK_ACCOUNT_SID=" + self.config['FB']['FACEBOOK_ACCOUNT_SID'])
        print("FACEBOOK_AUTH_TOKEN=" + self.config['FB']['FACEBOOK_AUTH_TOKEN'])

    def sendMessage(self,msg,destinatary):
        self.clientFB = Client(self.config['FB']['FACEBOOK_ACCOUNT_SID'], self.config['FB']['FACEBOOK_AUTH_TOKEN'])

        self.clientFB.sendRemoteImage(
            "https://bit.ly/2HparJQ",
            message=Message(text=msg),
            thread_id=self.clientFB.uid,
            thread_type=ThreadType.USER)

        self.clientFB.logout()