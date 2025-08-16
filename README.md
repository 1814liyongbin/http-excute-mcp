# HTTP Execute MCP Server

这是一个基于Python实现的HTTP请求执行服务器，遵循MCP (Machine Chat Protocol) 协议标准。该服务器提供了一个简单而强大的工具，允许客户端通过MCP协议发送各种HTTP请求。

## 项目概述

HTTP Execute MCP Server 是一个轻量级服务器，它将HTTP请求功能封装为MCP工具，使AI助手或其他MCP客户端能够轻松地执行网络请求操作。

## 功能特性

- 支持所有标准HTTP方法（GET, POST, PUT, DELETE等）
- 支持自定义请求头
- 支持JSON或普通文本格式的请求体
- 自动处理JSON格式的请求体
- 异步处理HTTP请求，提高性能
- 完全兼容MCP协议标准
- 支持作为Python模块运行 (`python -m http_execute_mcp`)

## 环境要求

- Python 3.8+
- 依赖包：
  - mcp==1.0.0
  - httpx==0.27.0

## 安装指南

### 方法一：从源码安装

1. 克隆仓库到本地：

```bash
git clone <repository-url>
cd http-execute-mcp
```

2. 创建并激活虚拟环境：

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# 或
.venv\Scripts\activate  # Windows
```

3. 安装依赖：

```bash
pip install -r requirements.txt
```

### 方法二：作为Python包安装

```bash
# 从源码目录安装
pip install -e .

# 或者从远程仓库安装
pip install git+https://github.com/yourusername/http-execute-mcp.git
```

## 使用方法

### 启动服务器

有多种方式可以启动服务器：

#### 1. 作为Python模块运行（推荐）

```bash
python -m http_execute_mcp
```

#### 2. 使用主脚本运行

```bash
python main.py
```

#### 3. 在代码中导入使用

```python
from http_execute_mcp.server import run_server

# 运行MCP服务器
run_server(transport='stdio')
```

默认情况下，服务器使用标准输入/输出(stdio)作为传输方式，适合与其他程序集成。

## MCP工具说明

### execute_http

执行HTTP请求的工具。

**参数：**
- `url` (string, 必需): 请求的URL
- `method` (string, 可选): HTTP方法，默认为GET
- `headers` (dict, 可选): 请求头
- `body` (string, 可选): 请求体（JSON字符串或普通文本）

**返回：**
- `status_code` (integer): HTTP状态码
- `headers` (dict): 响应头
- `body` (string): 响应体内容

## 客户端调用示例

### 在配置文件中引用

在MCP客户端配置中引用服务器：

```json
{
  "mcpServers": {
    "http": {
      "command": "python",
      "args": ["-m", "http_execute_mcp"]
    }
  }
}
```

### 工具调用示例

#### GET请求示例

```json
{
  "name": "execute_http",
  "arguments": {
    "url": "https://httpbin.org/get",
    "method": "GET"
  }
}
```

#### POST请求示例（JSON格式）

```json
{
  "name": "execute_http",
  "arguments": {
    "url": "https://httpbin.org/post",
    "method": "POST",
    "headers": {
      "Content-Type": "application/json"
    },
    "body": "{\"key\": \"value\"}"
  }
}
```

#### PUT请求示例（普通文本）

```json
{
  "name": "execute_http",
  "arguments": {
    "url": "https://httpbin.org/put",
    "method": "PUT",
    "headers": {
      "Content-Type": "text/plain"
    },
    "body": "Hello, world!"
  }
}
```

该脚本会执行GET和POST请求示例，并打印响应结果。

## 工作原理

1. 服务器使用FastMCP框架创建MCP服务
2. 注册execute_http工具，封装httpx库的HTTP请求功能
3. 接收客户端的工具调用请求
4. 异步执行HTTP请求并返回结果
5. 自动处理JSON格式的请求体，提高易用性

## 项目结构

```
http-execute-mcp/
├── http_execute_mcp/         # 主包目录
│   ├── __init__.py           # 包初始化文件
│   ├── __main__.py           # 模块入口点
│   └── server.py             # 服务器核心功能
├── main.py                   # 向后兼容的入口脚本
├── setup.py                  # 包安装配置
├── requirements.txt          # 依赖列表
├── test_client.py            # 测试客户端
└── README.md                 # 项目文档
```

## 扩展与定制

您可以通过修改 `http_execute_mcp/server.py` 文件来扩展功能，例如：
- 添加更多的HTTP相关工具
- 自定义请求处理逻辑
- 添加请求重试机制
- 实现请求缓存

## 许可证

[添加您的许可证信息]