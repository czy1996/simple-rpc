import rpcstub
import tcpserver
import jsondecode


class RPCServer(tcpserver.Server, jsondecode.JSONRPC, rpcstub.RPCStub):
    def __init__(self):
        super(RPCServer, self).__init__()

    def loop(self):
        self.bind()
        while True:
            self.accept_receive_close()

    def on_msg(self, data):
        self.from_data(data)
        self.call_func()
