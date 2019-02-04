import serial, requests, json


URL_API = "http://localhost:12345/write_csv"
SERIAL_PORT = "/dev/ttyUSB0"
#lee los datos del puerto serial
arduino_data = serial.Serial(SERIAL_PORT, baudrate=9600, timeout=10.0)


while True:
    #lee las lineas de la salida del arduino
    arduino_scope = arduino_data.readline()
    decoded_bytes = float(arduino_scope[0:len(line)-2].decode("utf-8"))
    data_to_request = {
        "temp": decoded_bytes
    }
    #Hace el request al api
    try:
        response = requests.post(
            URL_API, 
            json=data_to_request
        )
    except requests.exceptions.RequestException as error:  
        print(error)
        sys.exit(1)