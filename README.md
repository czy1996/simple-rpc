# simple-rpc
简易的 rpc，包括服务器和客户端

### 实现
- socket
- json 作为数据传输格式

- 客户端
    - TCP client 只发送、接受数据
    - RPCStub 处理函数调用
    - rpcclient mixin 

- 服务端
    - TCP server 只发送接受数据
    - RPCStub 处理函数调用
    - rpcserver mixin