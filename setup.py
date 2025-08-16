"""HTTP Execute MCP Server 安装配置."""

from setuptools import setup, find_packages

setup(
    name="http_execute_mcp",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "mcp==1.0.0",
        "httpx==0.27.0",
    ],
    description="HTTP请求执行MCP服务器",
    author="liyongbin",
    author_email="2637230700@qq.com",
    url="https://github.com/yourusername/http-execute-mcp",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)