"""HTTP Execute MCP Server 入口模块.

此模块允许通过 `python -m http_execute_mcp` 命令运行服务器。
"""

from http_execute_mcp.server import run_server

if __name__ == "__main__":
    # 运行MCP服务器
    run_server(transport='stdio')