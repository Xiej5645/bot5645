from flask import Flask, request, abort

import os
from dotenv import load_dotenv
load_dotenv()

from handlers.line_handler import setup_line_handlers
from handlers.basic_routes import setup_basic_routes
from handlers.discord_handler import setup_discord_bot

app = Flask(__name__)

# Setup handlers
setup_line_handlers(app)
setup_basic_routes(app)
setup_discord_bot()

if __name__ == "__main__":
    app.run()
    