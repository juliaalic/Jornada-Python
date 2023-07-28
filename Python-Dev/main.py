# Front-end -> o visual de um site
    # html, css, javascript

# Back-end -> a lógica de funcionamento por trás do site
    # python

# Framework -> Flask -> criar site

# ambiente virtual -> local no seu computador com instalações específicas

# site com os scripts -> https://cndjs.com

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast= True)

# criar a nossa 1 página = 1 rota
@app.route("/") # decorator
def homepage():
    return render_template("homepage.html")

# roda o nosso aplicativo
socketio.run(app, host="192.168.1.4")

# websocket -> tunel