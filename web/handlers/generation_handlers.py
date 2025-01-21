import json
from aiohttp import web
from typing import Dict
from g4f.client import AsyncClient

async def text_handler(request: web.Request) -> web.Response:
    """
    Handles the incoming HTTP request, uses g4f to generate a response to the user's request.

    Args:
        request (web.Request): The incoming HTTP request containing JSON data.

    Returns:
        web.Response: The HTTP response with g4f's generated text or error message.
    """
    try:
        # Parse JSON data from the request
        data: Dict = await request.json()

        
        # Get the user's request from the JSON data
        user_request = data.get('request')
        if not user_request:
            return web.Response(text="Missing 'request' parameter", status=400)

        # Initialize g4f async client
        async_client = AsyncClient()
        
        # Generate response using g4f
        response = await async_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"""You will be able to answer only once and then the interaction will be interrupted, 
                       this is not a chat, you will answer only once, so you only need to focus on one answer. 
                       Content from the user: 
                       {user_request} """}]
        )
        
        # Extract the generated text from response
        generated_text = response.choices[0].message.content

        # Return the generated response
        return web.Response(text=generated_text)
        
    except json.JSONDecodeError:
        return web.Response(text="Invalid JSON data", status=400)
    except Exception as e:
        return web.Response(text=f"Error generating response: {str(e)}", status=500)
