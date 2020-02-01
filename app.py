from flask import Flask, render_template, request
import serial

app = Flask(__name__)

ser1 = serial.Serial('/dev/cu.usbserial-DA01MAPZ', 9600)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/led', methods=['POST'])
def toogle_led():
    isOn = request.get_json()['isOn']
    print(isOn)
    if isOn:
        ser1.write('o'.encode())
    else:
        ser1.write('s'.encode())
    return request.get_json()

if __name__ == '__main__':
    app.run()
