#!/usr/bin/env python3

import socket
import sys
from datetime import datetime

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        s.close()

        if result == 0:
            return True
        else:
            return False
    except:
        return False

print("\n--- Mini Port Scanner ---\n")

target = input("Target IP or domain: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print("\nScanning target:", target)
print("Time started:", datetime.now())
print("\nOpen ports:\n")
open_ports = []

for port in range(start_port, end_port + 1):
    if scan_port(target, port):
        print("Port", port, "OPEN")
        open_ports.append(port)

print("\nScan finished.")
print("Open ports found:", open_ports)