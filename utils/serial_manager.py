import serial
import serial.tools.list_ports

class SerialManager:
    def __init__(self):
        self.serial_port = None

    def list_ports(self):
        """List all available serial ports."""
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]

    def connect(self, port, baudrate=115200):
        """Connect to the selected serial port."""
        try:
            self.serial_port = serial.Serial(port, baudrate, timeout=1)
            return True
        except serial.SerialException as e:
            print(f"Error: {e}")
            return False

    def disconnect(self):
        """Disconnect the serial port."""
        if self.serial_port:
            self.serial_port.close()

    def send_data(self, data):
        """Send data through the serial port."""
        if self.serial_port:
            self.serial_port.write(data.encode())

    def receive_data(self):
        """Receive data from the serial port."""
        if self.serial_port:
            data = self.serial_port.readline().decode().strip()
            return data
        return None
