import discord
from discord.ext import commands
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

#Intents are required
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    logger.debug(f'Logged in as {bot.user.name} - {bot.user.id}')


# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return  # Ignore messages sent by the bot itself
#     await message.channel.send("Hello!")

@bot.command()
async def hello(ctx):
    logger.debug(f'Received command "hello"')
    await ctx.send(f"Hello {ctx.author.name}!")

TOKEN = os.environ.get('BOT_TOKEN')
logger.debug(f'Starting bot...')
bot.run(TOKEN)
