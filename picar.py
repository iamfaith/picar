from flask import Flask, request, jsonify
from flask_socketio import SocketIO, join_room, emit, send
# from test_twowheel import test_controller
from two_wheel import TwoWheelController
import signal
import sys

controller = TwoWheelController()

app = Flask(__name__, static_url_path="")
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route("/")
def index():
    return app.send_static_file("index.html")


@socketio.on("set_axis")
def set_axis(data):
    print(data)
    controller.set_axis(x=data["x"], y=data["y"])


# @socketio.on('connect')
# def test_connect():
#     emit('after connect',  {'data':'Lets dance'})

if __name__ == "__main__":
    # test_controller(controller)
    socketio.run(app, debug=True, host="0.0.0.0")
