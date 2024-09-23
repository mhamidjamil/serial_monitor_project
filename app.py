from flask import Flask, render_template, jsonify, request
from utils.serial_manager import SerialManager

app = Flask(__name__)
serial_manager = SerialManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/list_ports', methods=['GET'])
def list_ports():
    ports = serial_manager.list_ports()
    return jsonify(ports)

@app.route('/api/connect', methods=['POST'])
def connect():
    data = request.json
    port = data.get('port')
    baudrate = data.get('baudrate', 115200)
    if serial_manager.connect(port, baudrate):
        return jsonify({'status': 'connected'})
    else:
        return jsonify({'status': 'error'}), 400

@app.route('/api/disconnect', methods=['POST'])
def disconnect():
    serial_manager.disconnect()
    return jsonify({'status': 'disconnected'})

@app.route('/api/send_data', methods=['POST'])
def send_data():
    data = request.json.get('data')
    serial_manager.send_data(data)
    return jsonify({'status': 'data sent'})

@app.route('/api/receive_data', methods=['GET'])
def receive_data():
    data = serial_manager.receive_data()
    if data:
        return jsonify({'data': data})
    else:
        return jsonify({'data': None}), 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
