from flask import Flask, escape, request
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

app = Flask(__name__)


@app.route('/turnos')
def turno():
    name = request.args.get("name", "turno")
    return f'Hello, {escape(name)}!'


@app.route('/tickets/<telephone>')
def ticket_by_telephone(telephone):
    name = request.args.get("name", "tickets")

    # FASE 1 BUSQUEDA DE TICKETS POR TELEPHONO
    # Input numero tel,num ticket
    # Output: ticket en Texto

    # FASE 2 CREACION DE TICKET EN IMAGEN SAVE LOCAL
    # Input TEXTO q es ticket
    # Output ticket en imagen

    return '{status:ok}'

    # FASE 3 UTILS de COMUNICACION CON WHATSAPP/TELEGRAM/ETC
    # Input URL Imagen generada
    # Output: Salida a Telgram

# Funcionalidad SMS https://bit.ly/2HparJQ
@app.route('tickets/sms/<telephone>')
def ticket_by_sms(telephone):


    return '{status:ok}'
