from quart import Quart, Response
import requests
import os
from handlers.discohook_handler import setup_discohook_bot

def setup_basic_routes(app):
    @app.route("/")
    def hello_world():
        setup_discohook_bot()
        return "Hello, World!"

    @app.route("/testing")
    def testing():
        if os.environ.get('Testing_KEY') == "55645":
            return "key founded!"
        return "key not found!"
    
    @app.route("/favicon.ico")
    @app.route("/favicon.png")
    @app.route("/favicon.jpg")    
    def favicon():        
        image_url = "https://twenty-icons.com/vercel.com/128"
        resp = requests.get(image_url)
        return Response(resp.content, content_type="image/png")