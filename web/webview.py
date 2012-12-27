



from bottle import run, template, Bottle, route, static_file
from bottle.ext import sqlite

app = Bottle()
authdb = sqlite.Plugin(dbfile='users.db')
app.install(authdb)


@route('/')
def root():
  return template('interlock')


@route('/logs')
def logs():
  return template('interlock')


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


run(host='0.0.0.0', port=80, debug=True)
