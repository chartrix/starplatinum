from flask import Flask, escape, request
from PIL import Image, ImageDraw

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
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    d = ImageDraw.Draw(img)
    ticketValue = 'Hello Eder \n Telefono: {telephone}!'

    d.text((10, 10), ticketValue, fill=(255, 255, 0))
    img.save(telephone+'_ticket.png')


    # FASE 3 UTILS de COMUNICACION CON WHATSAPP/TELEGRAM/ETC
    # Input URL Imagen generada
    # Output: Salida a Telgram


    return '{status:ok}'