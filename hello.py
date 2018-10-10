import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    if request.values:
        return "username is " + request.values["username"]
    return '<form method="get" action="/login"><input type="text" name="username" /><p><button type="submit">Submit</button></form>'

if __name__ == '__main__':
    # set up IP address and port
    # host = os.getenv("IP", "0.0.0.0")
    # port = int(os.getenv("PORT", 5000))

    # debug mode, should be false at production env
    app.debug = True
    app.run()