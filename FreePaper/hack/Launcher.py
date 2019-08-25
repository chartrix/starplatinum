from flask import Flask, escape, request
from hack.grp.salinas.comtools import Sms
import configparser

app = Flask(__name__)

config = configparser.ConfigParser()
config.sections()
config.read('conf/credentials.ini')



@app.route('/turnos')
def turno():
    name = request.args.get("name", "turno")

    #sendMsg = Sms()
    print("TWILIO_ACCOUNT_SID" + config['SMS']['TWILIO_ACCOUNT_SID'] )
    print("TWILIO_AUTH_TOKEN" + config['SMS']['TWILIO_AUTH_TOKEN'])
    return f'Hello, {escape(name)}!'