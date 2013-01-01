#!/usr/bin/python

from bottle import run, template, Bottle, route, get, static_file, request, redirect, response
from bottle.ext.websocket import GeventWebSocketServer, websocket
from gevent import sleep

import sqlite3, hashlib
from os import path

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


# test websocket route with a plain logfile streamed to clients
# append text to said file while connected to said socket
logfile = open("./test.log")
logfile.seek(0,2)      # Go to the end of the file

sockets = set()

@get('/logsocket', apply=[websocket])
def handle_logsocket(ws):
    sockets.add(ws)
    try:
        while True:
            line = logfile.readline()
            if not line:
                sleep(0.1)
                continue
            for socket in sockets:
                socket.send(line)
                socket.send(str(len(sockets)))
    finally:
        sockets.discard(ws)


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
run(host='0.0.0.0', port=8080, server=GeventWebSocketServer, debug=True, reloader=True)
