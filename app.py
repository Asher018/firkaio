from flask import Flask, render_template
from flask_socketio import SocketIO
from engineio.payload import Payload


app = Flask(__name__)
#Payload.max_decode_packets = 999999
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/nezo")
def nezo():
    return render_template('nezo.html')

@app.route("/rajzolo")
def rajzolo():
    return render_template('rajzolo.html')

@socketio.on('message')
def print_message(message):
    print(message)
    socketio.emit("message", message)

@socketio.on('drawing')
def drawing(message):
    socketio.emit('drawing', message)



