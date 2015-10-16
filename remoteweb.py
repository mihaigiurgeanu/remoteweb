from bottle import route, run, template, static_file
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setmode(4, GPIO.OUT)
GPIO.output(4, False)

@route('/hello/<name>')
def index(name):
  return template('<b>Hello {{name}}</b>!', name=name)

@route('/actions/on')
def lights_on():
  print "Lights on!"
  GPIO.output(4, True)

@route('/actions/off')
def lights_off():
  print "Ligts off!"
  GPIO.output(4, False)


@route('/static/<filepath:path>')
def server_static(filepath):
  return static_file(filepath, root='resources/public')


run(host="0.0.0.0", port=8080)

