function fetchPorts() {
    fetch('/api/list_ports')
        .then(response => response.json())
        .then(data => {
            const portsDropdown = document.getElementById('ports');
            portsDropdown.innerHTML = '';
            data.forEach(port => {
                const option = document.createElement('option');
                option.value = port;
                option.text = port;
                portsDropdown.appendChild(option);
            });
        });
}

function connectPort() {
    const port = document.getElementById('ports').value;
    const baudrate = document.getElementById('baudrate').value;

    fetch('/api/connect', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({port: port, baudrate: baudrate})
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'connected') {
            alert('Connected to port');
        } else {
            alert('Failed to connect');
        }
    });
}

function disconnectPort() {
    fetch('/api/disconnect', {method: 'POST'})
        .then(() => alert('Disconnected'));
}

function sendData() {
    const dataInput = document.getElementById('dataToSend');
    const data = dataInput.value;

    fetch('/api/send_data', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({data: data})
    })
    .then(() => {
        // Clear the input field after sending the data
        dataInput.value = '';
    });
}

function receiveData() {
    fetch('/api/receive_data')
        .then(response => response.json())
        .then(data => {
            if (data.data) {
                const terminal = document.getElementById('terminal');
                terminal.value += '\n' + data.data;

                // Auto-scroll if the checkbox is checked
                const autoScroll = document.getElementById('autoScroll').checked;
                if (autoScroll) {
                    terminal.scrollTop = terminal.scrollHeight;
                }
            }
        });
}

setInterval(receiveData, 50);
fetchPorts();
