#!/usr/bin/python



from bottle import run, template, Bottle, route, static_file, request, redirect, response
import sqlite3
from os import path

DB = 'doorberry.db'

#@if not path.exists(USERDB):




#LOG: IBUTTON TEXT, DATE date
#MEMBERS FULLNAME text, EMAIL text, IBUTTON text, STATUS, text



@route('/')
def root():
  return template('index')


@route('/logs')
def logs():
  if not cookie_check(): redirect("/login")
  return template('index')

@route('/login')
def login():
  return '''<form method="POST" action="/login">
    <input name="name" type="text" />
    <input name="password" type="password" autocomplete="off"/>
    <input type="submit" />
   </form>'''

@route('/login', method='POST')
def login_submit():
  name = request.forms.get('name')
  password = request.forms.get('password')
  #password verification here
  if check_login(name, password):
    response.set_cookie("account", name, secret='berticusshairyupperlip')
    return "<P>You successfully logged in</P>"
  else:
    return "<P>Who the eff are you?</p>"
  


#static routes
@route('/css/<filename>')
def css(filename):
  return static_file(filename, root='css')

@route('/images/<filename>')
def images(filename):
  return static_file(filename, root='images')

@route('/js/<filename>')
def js(filename):
  return static_file(filename, root='js')


def check_login(name, password):
  #check username and password
  conn = sqlite3.connect(DB)
  results = conn.cursor().execute('SELECT username,password FROM users WHERE username=? AND password=?',(name, password)).fetchone()
  conn.close()

  if results:
    return True
  else:
    return False

def cookie_check():
  #check to see if they've received a cookie
  username = request.get_cookie("account", secret='berticusshairyupperlip')
  if username:
    return True
  else:
    return False


run(host='0.0.0.0', port=8080, debug=True)
