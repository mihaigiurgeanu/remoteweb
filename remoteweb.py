from bottle import route, run, template, static_file

@route('/hello/<name>')
def index(name):
  return template('<b>Hello {{name}}</b>!', name=name)


@route('/static/<filepath:path>')
def server_static(filepath):
  return static_file(filepath, root='C:\\Documents and Settings\\Work\\Projects\\remoteweb\\resources\\public')


run(host='localhost', port=8080)
