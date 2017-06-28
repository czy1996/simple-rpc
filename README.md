# simple-rpc
简易的 rpc，包括服务器和客户端

### 想达成的效果
- 客户端有一个对象，比如```client```
- 调用 ```client.fuck('shit')```
- 发送消息给服务器端
- 服务器端处理逻辑，返回消息给客户端
- 客户端拿到返回值 Todo
- Rpc decorator 将一个方法变为 RPC 方法 Todo

### 实现
- socket
- json 作为数据传输格式
    ```json
    {
        "function_name": name,
        "function_args": args,
        "function_kwargs": kwargs,
    }
    ```
- 客户端
    - TCP client 只负责发送、接受数据 ```bind accept recv```
    - RPCStub 处理函数调用 ```parse call```
    - rpcclient mixin
- 服务端
    - TCP server 只发送接受数据 ```connect send data```
    - RPCStub 处理函数调用
    - rpcserver mixin