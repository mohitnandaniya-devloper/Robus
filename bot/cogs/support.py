import discord
from discord.ext import commands
from discord import app_commands

class Support(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="support", description="Get assistance and support for Robus AI.")
    async def support(self, interaction: discord.Interaction):
        await interaction.response.send_message("How can I help you?")

async def setup(bot):
    await bot.add_cog(Support(bot))
