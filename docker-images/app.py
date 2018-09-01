from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized version 2 from hostname '+socket.gethostname()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
