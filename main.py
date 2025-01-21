import asyncio
from web.server import init_web_server

async def main():
    config = {
        'host': 'localhost',
        'port': 8090,
        'timeout': 60,
        'max_connections': 10000
    }
    
    await init_web_server(config)
    
    while True:
        await asyncio.sleep(3600)

if __name__ == '__main__':
    asyncio.run(main())
