import json


class RPCStub:
    def __getattr__(self, item):
        def remote_call(*args, **kwargs):
            d = {
                'function_name': item,
                'function_args': args,
                'function_kwargs': kwargs,
            }
            msg = json.dumps(d)
            self.send(msg.encode('utf-8'))

        setattr(self, item, remote_call)
        return remote_call
