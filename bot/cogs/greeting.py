import discord
from discord.ext import commands
from discord import app_commands

class Greeting(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="greeting", description="Get a warm welcome from Robus! 🤖")
    async def greeting(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hello, {interaction.user.mention}! 👋 Hope you're having a great day!")

async def setup(bot: commands.Bot):
    await bot.add_cog(Greeting(bot))
