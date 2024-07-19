
import os

import discord 
import discord.ext import commands

import ollama
import dotenv import load_dotenv

load_dotenv()

intents = discord.intents.default()
intents.messages = True   # This will allow us to send and recieve messages.

response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])