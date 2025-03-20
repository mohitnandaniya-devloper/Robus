import discord
from discord.ext import commands
from discord import app_commands

class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Check the bot's latency and responsiveness.")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000, 2)
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"Latency: `{latency}ms`",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Ping(bot))


