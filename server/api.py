import datetime
from flask import Flask, render_template, redirect
from flask import Blueprint, request, jsonify, abort
from config import config
from urllib.parse import quote, urlencode
from random_string import generate_random

app = Flask(__name__)
# app.config.update(**config)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    app_id = app.config['APP_ID']
    app_secret = app.config['APP_SECRET']
    redirect_url = app.config['REDIRECT_URL']
    state = generate_random(10)
    params = {'client_id': app_id, 'client_secret': app_secret, 'redirect_url': redirect_url,  'state': state}
    return redirect(app.config['AUTH_URL'] + '?' + urlencode(params, quote_via=quote), code=302)

@app.route("/callback")
def loggedin():
    token = request.args.get('token')
    if token:
        return render_template('loggedin.html')
    else:
        return redirect('/')

@app.route("/logout")
def logout():
    return redirect(app.config['AUTH_URL'] + '/logout')