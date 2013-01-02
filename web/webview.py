#!/usr/bin/python

from os import path
from bottle import run, template, Bottle, route, static_file, request, redirect, response

import sqlite3, hashlib

DATABASE = 'doorberry.db'

# TODO: check for db existence and initialize or barf

#DB Setup
#LOG:     DATE date, INFO text
#MEMBERS: FULLNAME text, IBUTTON text, AUTHORIZED boolean


@route('/')
def index():
    if not check_cookie():
        return template('login', note='please log in')
    else:
        return template('index', note='welcome, slacker')

@route('/', method='POST')
def login():
    name = request.forms.get('name')
    password = request.forms.get('password')

    if check_login(name, password):
        response.set_cookie("login", name, secret='berticusshairyupperlip')
        return template('index', note='login successful')
    else:
        return template('login', note='login failed')


# static routes
@route('/css/<filename>')
def css(filename):
    return static_file(filename, root='css')

@route('/images/<filename>')
def images(filename):
    return static_file(filename, root='images')

@route('/js/<filename>')
def js(filename):
    return static_file(filename, root='js')

@route('/font/<filename>')
def font(filename):
    return static_file(filename, root='font')

# helper functions
def check_login(name, password):
    #check username and password
    salt = '*s90'
    conn = sqlite3.connect(DATABASE)
    hashpass = hashlib.md5(salt + password).hexdigest()
    results = conn.cursor().execute('SELECT username,password FROM users WHERE username=? AND password=?',(name, hashpass)).fetchone()
    conn.close()

    if results:
        return True
    else:
        return False

def check_cookie():
    #check to see if they've received a cookie
    username = request.get_cookie("login", secret='berticusshairyupperlip')
    if username:
        return True
    else:
        return False


# run the durn server
run(host='0.0.0.0', port=8080, debug=True, reloader=True)
