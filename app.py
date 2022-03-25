import imp
from flask import Flask, render_template
from flask_socketio import SocketIO
from engineio.payload import Payload
import random
from eventlet import wsgi
import eventlet


app = Flask(__name__)
# Payload.max_decode_packets = 999999
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/nezo")
def nezo():
    return render_template("nezo.html")


@app.route("/rajzolo")
def rajzolo():
    return render_template("rajzolo.html")

def give_random_word():
    dictionary = [
        "dog",
        "cat",
        "house",
        "head",
        "number",
        "tree",
        "sky",
        "sun",
        "boat",
        "elbow",
        "chimney",
        "computer",
        "flag",
        "bird",
        "fish",
        "money",
        "bow",
        "axe",
        "scissors",
        "glasses",
    ]
    return random.choice(dictionary)


@socketio.on("give_random_word")
def random_word(rnd_word=""):
    global global_word
    global_word=give_random_word()
    #print(f"fgv belül: {global_word}")
    socketio.emit("give_random_word", global_word)

@socketio.on("message")
def print_message(message):
    print(message)
    msg_index = int(message.index(':'))
    win_name = message[0:msg_index]
    winner_name(win_name)
    #print(f"Global_word:{global_word}, Msg_word:{msg_word}.")
    if str(global_word) in str(message):
        print("equal")
        game_end()
    socketio.emit("message", message)


@socketio.on("drawing")
def drawing(message):
    socketio.emit("drawing", message)

@socketio.on("game_end")
def game_end():
    print("Game over")
    socketio.emit("game_end")

@socketio.on("winner_name")
def winner_name(name):
    socketio.emit("winner_name", name)

@socketio.on("new_game")
def new_game():
    socketio.emit("new_game")

@socketio.on("viewer_joinned")
def viewer_joinned():
    print("viewer_joinned")
    #random_word()
    socketio.emit("viewer_joinned")

if __name__ == '__main__':
  app.debug=True
  wsgi.server(eventlet.listen(('',8080)), app)


