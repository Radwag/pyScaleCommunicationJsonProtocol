import json
import socket
import sys
import logging
import time

import crc8 as crc8


class SocketRdgJson:



    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, ipAddress):
        HOST, PORT = ipAddress, 4001

        # Connect to server
        self.sock.connect_ex((HOST, PORT))

        return self.sock

    def get_sock(self):
        return self.sock

    def send(self, message):
        # Send data to server
        self.sock.sendall(bytes(message + self.calculate_crc(message) + "\r\n", "utf-8"))

    def reciv(self):
        # Receive data from the server
        time.sleep(0.05)
        return json.loads(self.remove_crc(str(self.sock.recv(32768), "utf-8")))

    def calculate_crc(self, message):
        hash = crc8.crc8()
        hash.update(bytes(message + "\n", "utf-8"))
        return hash.hexdigest()

    def remove_crc(self, respond):
        respond1 = respond[:-4]
        return respond1

