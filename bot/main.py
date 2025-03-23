import discord
import asyncio
import os
import logging
from config import Config
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=intents) 
logging.basicConfig(filename="logs.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename != "__init__.py":
            cog = f"cogs.{filename[:-3]}"
            try:
                await bot.load_extension(cog)
                print(f"✅ Loaded {cog}")
            except Exception as e:
                print(f"❌ Failed to load {cog}: {e}")

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("✅ Slash commands synced!")
    print(f'🟢 {bot.user} is online.')

async def main():
    async with bot:
        await load_cogs()
        await bot.start(Config.DISCORD_TOKEN)

asyncio.run(main())
