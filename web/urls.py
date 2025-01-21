from typing import Dict, List
from aiohttp import web

from web.handlers.generation_handlers import text_handler

# Define URL route configurations for the web server
urls: List[Dict[str, str]] = [
    {
        'method': 'POST',               # HTTP method type
        'path': '/text_generation',     # URL path to handle
        'handler': text_handler    # Function that handles requests to this path
    },
]
