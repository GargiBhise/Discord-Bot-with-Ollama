
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

@bot.command(name="ask")
async def ask(ctx, *, message):
    print(message)
    print("*************************************")
    response = ollama.chat(model='llama3', messages=[
         {
        'role': 'system',
        'content': 'You are a helpful assistant who provides an answer to questions concisely in no more than 1000 words.'
       },
       { 'role': 'user',
        'content' : message,
       },
    ])
    print(response['message']['content'])
    await ctx.send(response['message']['content'])

bot.run(os.getenv('DISCORD_BOT_TOKEN'))

# response = ollama.chat(model='llama3', messages=[
#   {
#     'role': 'user',
#     'content': 'Why is the sky blue?',
#   },
# ])
# print(response['message']['content'])