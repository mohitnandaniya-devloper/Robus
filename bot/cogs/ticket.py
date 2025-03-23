import discord
from discord.ext import commands
from discord import app_commands

class Ticket(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ticket_show", description="Displays a list of open tickets.")
    async def ticket_show(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="🎫 Open Tickets",
            description="Here is the list of open tickets:",
            color=discord.Color.blue()
        )
        embed.add_field(name="Ticket #1", value="Created by @User1", inline=False)
        embed.add_field(name="Ticket #2", value="Created by @User2", inline=False)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="ticket_create", description="Creates a new support ticket.")
    async def ticket_create(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="✅ Ticket Created",
            description=f"{interaction.user.mention}, your ticket has been created. Our team will assist you shortly!",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="ticket_cancel", description="Cancels an open support ticket.")
    async def ticket_cancel(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="❌ Ticket Canceled",
            description=f"{interaction.user.mention}, your ticket has been successfully canceled.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Ticket(bot))
