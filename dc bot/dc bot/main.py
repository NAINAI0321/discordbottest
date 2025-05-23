import os
import asyncio
import discord
from discord.ext import commands
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Replit keep-alive 功能
keep_alive()


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename != "counter.py":
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with bot:
        await load_extensions()
        await bot.start(os.environ["DISCORD_TOKEN"])  # 從環境變數讀取 token，安全性高


if __name__ == "__main__":
    asyncio.run(main())
