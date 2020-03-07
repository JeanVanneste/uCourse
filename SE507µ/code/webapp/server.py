# server.py
# Author: Sébastien Combéfis, Guillaume de Moffarts
# Version: February 24, 2019

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

form = '''<p>Enter your credentials to access secret information.</p>
<form id="login" action="login" method="post">
  <p><label for="username"><b>Username</b></label>
  <input type="text" placeholder="Enter your username" name="username" required></p>
  <p><label for="password"><b>Password</b></label>
  <input type="password" placeholder="Enter your password" name="password" required></p>
  <p><button type="submit">Connect</button></p>
</form>'''

ok = None 

@app.route('/')
def index():
    if ok is None:
        return form
    return form + '<h1 id="connected">{}</h1>'.format('OK' if ok else 'KO')

@app.route('/login', methods=['POST'])
def login():
    global ok
    if request.method == 'POST':
        ok = request.form['username'] == 'me' and request.form['password'] == 'mypwd'
    return redirect(url_for('index'))
