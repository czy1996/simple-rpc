import json


class JSONRPC:
    def __init__(self):
        self.data = None

    def from_data(self, data):
        self.data = json.loads(data.decode('utf-8'))

    def call_func(self):
        function_name = self.data['function_name']
        function_args = self.data['function_args']
        function_kwargs = self.data['function_kwargs']

        getattr(self, function_name)(*function_args, **function_kwargs)
