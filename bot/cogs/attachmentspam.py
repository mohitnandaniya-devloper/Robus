import discord
from discord.ext import commands
from discord import app_commands

class AttachmentSpam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="attachmentspam", description="Set the spam detection rate.")
    @app_commands.describe(rate="Set the message spam rate limit (e.g., 5 per 10 seconds)")
    async def attachmentspam(self, interaction: discord.Interaction, rate: int):
        if rate < 1:
            await interaction.response.send_message("⚠️ The rate must be at least **1**.", ephemeral=True)
            return
        
        await interaction.response.send_message(f"✅ **Attachment spam rate set to {rate} messages per 10 seconds.**")

async def setup(bot):
    await bot.add_cog(AttachmentSpam(bot))
