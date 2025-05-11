from flask import Flask, request, abort
import threading
import os
from dotenv import load_dotenv
load_dotenv()

from handlers.basic_routes import setup_basic_routes
from handlers.line_handler import setup_line_handlers
from handlers.discord_handler import setup_discord_bot

app = Flask(__name__)

# Setup handlers
setup_basic_routes(app)
setup_line_handlers(app)

discord_thread = threading.Thread(target=setup_discord_bot)
discord_thread.daemon = True
discord_thread.start()

if __name__ == "__main__":
    app.run(debug=True)
    