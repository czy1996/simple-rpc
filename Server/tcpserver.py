import socket


class Server:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind(self, host='localhost', port='5000'):
        self.sock.bind((host, port))
        self.sock.listen(5)

    def accept_receive_close(self):
        (client_socket, address) = self.sock.accept()
