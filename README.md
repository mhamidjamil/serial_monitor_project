# Serial Monitor for Orange Pi

This project provides a web-based serial monitor for communicating with devices like Arduino, ESP32, and other microcontrollers connected via USB to an Orange Pi running Ubuntu. It allows users to choose the serial port, change the baud rate, send and receive data, and optionally view the data in different colors for sent and received inputs. Additionally, it offers a RESTful API for interacting with serial ports.

## Features

- **Serial Monitor**: Communicate with connected devices via USB.
- **Baud Rate and Port Selection**: Dynamically change the baud rate and port through the web interface.
- **Auto Scroll**: Optionally enable/disable automatic scrolling in the terminal.
- **API**: Exposes APIs to check available ports, send data, and receive data.
- **Clear Input**: Automatically clears the input field after sending data.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Requirements

- Orange Pi running Ubuntu
- Python 3.x
- Flask
- `pyserial` library for serial communication

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/serial-monitor.git
    cd serial-monitor
    ```

2. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask server:

    ```bash
    python app.py
    ```

4. Access the web interface in your browser:

    ```
    http://localhost:5000
    ```

## Usage

1. Connect your device (Arduino, ESP32, etc.) to the Orange Pi via USB.
2. Open the web interface and select the serial port and baud rate.
3. Use the input field to send data to the connected device, and the terminal will display received data.
4. Toggle auto-scroll if needed, and clear the input field after sending data.

## API Endpoints

### Get Available Ports

**Endpoint**: `/api/get_ports`
**Method**: `GET`
**Description**: Fetches the list of available serial ports.

**Example**:

```bash
curl http://localhost:5000/api/get_ports
