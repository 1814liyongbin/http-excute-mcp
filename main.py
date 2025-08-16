"""HTTP Execute MCP Server 启动脚本.

此脚本提供了向后兼容性，允许通过 `python main.py` 命令运行服务器。
推荐使用 `python -m http_execute_mcp` 命令运行。
"""

from http_execute_mcp.server import run_server

if __name__ == "__main__":
    # 运行MCP服务器
    run_server(transport='stdio')