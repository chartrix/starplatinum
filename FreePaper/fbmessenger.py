from fbchat import Client
from fbchat.models import *
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

client = Client(os.environ.get('FB_USR'), os.environ.get('FB_PSSWD'))

#msg = "Hola Felipe. Consulta tu recibo de Banco Azteca por el movimiento de deposito en efectivo: https://bit.ly/2HparJQ"

msg_woi = "Hola Felipe. Consulta tu recibo de Banco Azteca por el movimiento de deposito en efectivo."

#client.send(Message(text=msg), thread_id=client.uid, thread_type=ThreadType.USER)

client.sendRemoteImage(
    "https://bit.ly/2HparJQ",
    message=Message(text=msg_woi),
    thread_id=client.uid,
    thread_type=ThreadType.USER)

client.logout()
