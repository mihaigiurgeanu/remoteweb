from bottle import route, run, template, static_file

@route('/hello/<name>')
def index(name):
  return template('<b>Hello {{name}}</b>!', name=name)

@route('/actions/on')
def lights_on():
  print "Lights on!"

@route('/actions/off')
def lights_off():
  print "Ligts off!"


@route('/static/<filepath:path>')
def server_static(filepath):
  return static_file(filepath, root='resources/public')


run(host="0.0.0.0", port=8080)

