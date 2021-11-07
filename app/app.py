import os


from flask import Flask
from flask import request


app = Flask(__name__)


SERVER_NAME = os.getenv("SERVER_NAME", "PYAPP")


@app.route("/", methods=['GET', 'POST',])
def hello():
    return "Hello World ! from {}".format(SERVER_NAME)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, use_reloader=False)