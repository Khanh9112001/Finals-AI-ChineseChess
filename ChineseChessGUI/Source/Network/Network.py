# /usr/bin/python3

import json
import socket


class Client:
    def __init__(self, port=8080):
        self.socket = socket.socket()
        self.addrHost = (socket.gethostname(), port)
        self.socket.connect(self.addrHost)

    def send(self, data):
        jsonObj = json.dumps(data)
        # self.socket.send(bytes(jsonObj, 'utf-8'))
        self.socket.sendto(bytes(jsonObj, 'utf-8'), self.addrHost)

    def receive(self):
        dataReceive = str(self.socket.recv(1024))
        return json.loads(dataReceive[2:len(dataReceive) - 1])

    def close(self):
        self.socket.close()
