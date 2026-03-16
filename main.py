import asyncio
import traceback

from mcp_client import MCPClient


def init_client() -> MCPClient:
    """创建客户端实例"""
    client = MCPClient()
    return client


async def run_client():
    """运行客户端"""
    """运行客户端"""
    client = MCPClient()
    try:
        print("连接 MCP 服务器...")
        await client.connect()
    except KeyboardInterrupt:
        print("\n用户中断")
    except Exception as e:
        print(f"运行过程中出错: {e}")
        traceback.print_exc()
    finally:
        # 确保断开连接
        pass


if __name__ == "__main__":
    asyncio.run(run_client())
