import discord
from discord.ext import commands
import os
import random

def setup_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    
    discord_bot = commands.Bot(command_prefix='!', description='A simple Discord bot', intents=intents)

    @discord_bot.event
    async def on_ready():
        print(f'Logged in as {discord_bot.user}')

    @discord_bot.event
    async def on_message(message):
        if message.author == discord_bot.user:
            return
        
        if message.content.startswith('!hi'):
            await message.channel.send('Hello from Discord Bot!')
            return
        else:
            await discord_bot.process_commands(message)
    @discord_bot.command(description='Roll a dice')
    async def rolls(ctx, dice: str):
        # Format: NdN ie: !roll 2d6 means 2 dice with 6 sides each
        # will return a random number between 1 and 6
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    discord_bot.run(os.environ.get('DISCORD_TOKEN'))