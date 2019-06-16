#!/usr/bin/python
# -*- Coding: utf-8 -*-

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)

ConnectedClinets = []


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("require", namespace="/test")
def message(message):
    print(message)

    if message["to"]:
        print("send to")

        client = list(
            filter(lambda client: client["name"] == message["to"], ConnectedClinets)
        )

        if len(client) == 1:
            print("ok")
            sid = client[0]["sid"]
            emit("response", {"data": message["data"]}, room=sid)
            pass
        else:
            emit("response", {"data": "error response"})
            pass
        # emit("response", {"data": message["data"]})
        pass
    else:
        print("send broadcaset")
        emit("response", {"data": message["data"]}, broadcast=True)
        pass


@socketio.on("clinet name", namespace="/test")
def clinet_name(message):
    # print(message["name"])
    # print(request.sid)
    clinet = {"name": message["name"], "sid": request.sid}
    ConnectedClinets.append(clinet)


@socketio.on("connect", namespace="/test")
def connect():
    print("Clinet connected")
    print(ConnectedClinets)


@socketio.on("disconnect", namespace="/test")
def disconnect():
    print("Client disconnected")

    client = list(filter(lambda client: client["sid"] == request.sid, ConnectedClinets))
    ConnectedClinets.remove(client[0])
    print(ConnectedClinets)


if __name__ == "__main__":
    socketio.run(app, host="localhost", port=8000, debug=True)

