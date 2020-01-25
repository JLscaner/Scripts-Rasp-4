#Importamos el modulo que permite que controlemos los pines
import RPi.GPIO as GPIO
#Usaremos el pin de posicion 7
pin = 7
#Definimos la numeracion de los pines con la cual se va a trabajar
GPIO.setmode(GPIO.BOARD)
#Definimos el pin 7 como salida
GPIO.setup(pin, GPIO.OUT)
#Asignamos un valor HIGH al pin 7
GPIO.output(pin, GPIO.HIGH)
#Asignamos un valor LOW al pin 7
GPIO.output(pin, GPIO.LOW)