import discord
from discord import app_commands
from discord.ext import commands
import os
import random

def setup_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    
    # discord_bot = discord.Client(command_prefix='/', description='A simple Discord bot', intents=intents)
    discord_bot = commands.Bot(command_prefix='!', description='A simple Discord bot', intents=intents)

    @discord_bot.event
    async def on_ready():
        print(f'Logged in as {discord_bot.user}')
        try:
            synced = await discord_bot.tree.sync()
            print(f'Synced {len(synced)} command(s)')
        except Exception as e:
            print(e)

    @discord_bot.tree.command(name='hello', description='Say hello')
    async def hello(interaction: discord.Interaction):
        await interaction.response.send_message(f'Hello {interaction.user.mention}', ephemeral=True)
    
    @discord_bot.event
    async def on_message(message):
        if message.author == discord_bot.user:
            return        
        if message.content == '!hi':
            await message.channel.send('Hello from Discord Bot!')
            return
        if message.content.startswith('!end'):
            await message.channel.send('Goodbye!')
            await discord_bot.close()
            return
        else:
            await discord_bot.process_commands(message)
            return        

    @discord_bot.command(description='Simple Ping')
    async def ping(ctx):
        latency = discord_bot.latency * 1000
        await ctx.send('Pong!' + f' ping: {latency:.2f} ms')
        return

    @discord_bot.command(description='Roll a dice')
    async def rolls(ctx, dice: str):
        # Format: NdN ie: !roll 2d6 means 2 dice with 6 sides each
        # will return a random number between 1 and 6
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN, ie: 2d6 2 dice of 6 faces!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    return discord_bot