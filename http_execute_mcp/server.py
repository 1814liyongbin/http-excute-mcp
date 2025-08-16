"""HTTP Execute MCP Server 核心功能模块."""

from mcp.server import FastMCP
import httpx
import json

# 创建FastMCP实例
mcp = FastMCP()

@mcp.tool()
async def execute_http(url: str, method: str = "GET", headers: dict = None, body: str = None):
    """执行HTTP请求的工具
    
    Args:
        url (str): 请求的URL
        method (str, optional): HTTP方法，示例GET POST DELETE，默认为GET
        headers (dict, optional): 请求头
        body (str, optional): 请求体
    
    Returns:
        dict: 包含状态码、响应头和响应体的字典
    """
    async with httpx.AsyncClient() as client:
        # 准备请求参数
        request_kwargs = {
            "url": url,
            "method": method,
        }
        
        # 添加请求头
        if headers:
            request_kwargs["headers"] = headers
            
        # 添加请求体
        if body:
            # 尝试解析JSON字符串
            try:
                request_kwargs["json"] = json.loads(body)
            except json.JSONDecodeError:
                # 如果不是有效的JSON，则作为普通文本发送
                request_kwargs["content"] = body
        
        # 发送请求
        response = await client.request(**request_kwargs)
        
        # 返回响应信息
        return {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "body": response.text
        }

def run_server(transport='stdio'):
    """运行MCP服务器
    
    Args:
        transport (str, optional): 传输方式，默认为stdio
    """
    mcp.run(transport=transport)