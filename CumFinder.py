import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
Listed_Ports = [(port) for port, desc, hwid in sorted(ports)]
