from picar import app, socketio


flask_test_client = app.test_client()

# connect to Socket.IO without being logged in
socketio_test_client = socketio.test_client(app, flask_test_client=flask_test_client)

assert not socketio_test_client.is_connected()