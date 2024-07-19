
import os
import discord 
from discord.ext import commands

import ollama
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True   # This will allow us to send and recieve messages.

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready as {bot.user.name}")

@bot.command(name="hello")
async def hello(ctx):
    await ctx.send("Hello, I am a Bot!!!")

bot.run(os.getenv('DISCORD_BOT_TOKEN'))

# response = ollama.chat(model='llama3', messages=[
#   {
#     'role': 'user',
#     'content': 'Why is the sky blue?',
#   },
# ])
# print(response['message']['content'])