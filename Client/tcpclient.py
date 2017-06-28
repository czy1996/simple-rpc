import socket


class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host='localhost', port=5000):
        self.sock.connect((host, port))

    def send(self, data):
        """

        :param data: bytes
        :return:
        """
        self.sock.sendall(data)


if __name__ == '__main__':
    client = Client()
    client.connect()
    client.send('shit'.encode('utf-8'))
