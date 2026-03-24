## 是什么
MCP协议的客户端，支持连接本地 MCP-Server，并调用 MCP-Server提供的工具。


## 有什么能力
1. 连接 本地 MCP-Server [DarcyMCPServer](https://github.com/darcycui/DarcyAIMCPServer)
2. 查询 DarcyMCPServer 提供的全部工具
3. 调用 DarcyMCPServer 提供的工具 get_forecast

## 怎么用
### 远程 MCP(推荐)
1. 直接运行 ./main_remote.py

### 本地 MCP
1. clone 这个项目到本地路径
2. clone [DarcyMCPServer](https://github.com/darcycui/DarcyAIMCPServer)
3. 修改 main_local.py，全局变量 MCP_SERVER_FOLDER 为你本地 DarcyMCPServer 的路径
4. 运行 main_local.py

## 运行结果
1. 远程 MCP Server
![运行结果](docs/MCP-Client运行效果(远程).png)

2. 本地 MCP Server
![运行结果](docs/MCP-Client运行效果(本地).png)

## 参考文档
[MCP官网 创建MCP客户端](https://modelcontextprotocol.io/docs/develop/build-client)

[快速上手：实现你的第一个 MCP Client](https://zhuanlan.zhihu.com/p/21166726702)

[用最简单的方式教你用Python搭建第一个MCP服务器](https://juejin.cn/post/7496341504849330214)
