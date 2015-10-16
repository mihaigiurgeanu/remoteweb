from bottle import route, run, template

@route('/hello/<name>')
def index(name):
  return template('<b>Hello {{name}}</b>!', name=name)


@route('/static/<filepath:path>')
def server_static(filepath):
  return static_file(filepath, root='resources/public')


run(host='localhost', port=8080)

