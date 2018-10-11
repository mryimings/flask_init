import os

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "User %s logged in" % request.form['username']
    else:
        return render_template('login.html')

if __name__ == '__main__':
    # set up IP address and port
    # host = os.getenv("IP", "0.0.0.0")
    # port = int(os.getenv("PORT", 5000))

    # debug mode, should be false at production env
    app.debug = True
    app.run()