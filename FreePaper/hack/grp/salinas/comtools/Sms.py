from twilio.rest import Client
import configparser

class Sms:
    def __init__(self):
        self.clientSMS = None
        self.config = configparser.ConfigParser()

    def setupSms(self):

        self.config.sections()
        self.config.read('conf/credentials.ini')
        print("TWILIO_ACCOUNT_SID=" + self.config['SMS']['TWILIO_ACCOUNT_SID'])
        print("TWILIO_AUTH_TOKEN=" + self.config['SMS']['TWILIO_AUTH_TOKEN'])

    def sendMessage(self,msg,destinatary):
        self.clientSMS = Client(self.config['SMS']['TWILIO_ACCOUNT_SID'], self.config['SMS']['TWILIO_AUTH_TOKEN'])
        message = self.clientSMS.messages \
            .create(
            body=msg,
            from_='+12013971707',
            to="+52"+destinatary
        )
        print(message.sid)