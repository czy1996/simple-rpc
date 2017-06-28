import rpcstub
import tcpclient


class RPCClient(tcpclient.Client, rpcstub.RPCStub):
    pass
