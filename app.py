from quart import Quart
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()


from handlers.basic_routes import setup_basic_routes
from handlers.line_handler import setup_line_handlers
# from handlers.discord_handler import setup_discord_bot

app = Quart(__name__)

# intents = discord.Intents.default()
# intents.message_content = True
# intents.members = True
# discord_bot = discord.Client(command_prefix='!', description='A simple Discord bot', intents=intents)

# Setup handlers
setup_basic_routes(app)
setup_line_handlers(app)
# discord_bot = setup_discord_bot()        

async def main():
    await asyncio.gather(
        app.run_task(debug=True)        
        # discord_bot.start(os.environ.get('DISCORD_TOKEN'))
    )
if __name__ == "__main__":
    asyncio.run(main())