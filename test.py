import serial
import requests
import json

#lee los datos del puerto serial
arduino = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=10.0)


while True:
    #lee las lineas de la salida del arduino
    line = arduino.readline()
    #decodifica la salida en UTF-8
    print(line.decode('utf-8'))
    #Armar un json de ejemplo
    payload = {"Age": line.decode('utf-8'), "Sex":"male", "Embarked":"S"}
    #Hace el request al api
    r = requests.post("http://127.0.0.1:12345/write_csv", json=payload)
    #imprime la respuesta del api
    print(r.text)
    print(line)