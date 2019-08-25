from flask import Flask, request
from hack.grp.salinas.comtools.Sms import Sms
from hack.grp.salinas.comtools.FB import FB


app = Flask(__name__)


@app.route('/turnos')
def turno():
    name = request.args.get("name", "turno")

    return '{status:ok}'


# Funcionalidad SMS https://bit.ly/2HparJQ
@app.route('/tickets/sms/<telephone>')
def ticket_by_sms(telephone):

    print("Telephone ID=" + telephone)

    msg = ("Hola Felipe. Consulta tu recibo de Banco Azteca por el movimiento de deposito en efectivo: " +
            "https://bit.ly/2HparJQ" )

    smsTool = Sms()
    smsTool.setupSms()
    smsTool.sendMessage( msg,telephone)

    return '{status:ok}'

@app.route('/tickets/fb/<fbid>')
def ticket_by_fb(fbid):
    msg = ("Hola Felipe. Consulta tu recibo de Banco Azteca por el movimiento de deposito en efectivo: " +
           "https://bit.ly/2HparJQ")

    fbTool = FB()
    fbTool.setuFB()
    fbTool.sendMessage(msg,fbid)


    return '{status:ok}'