import discord
import psutil
import time
from discord.ext import commands
from discord import app_commands
from utils import geminiutils

class Support(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()

    @app_commands.command(name="robus_about", description="View bot statistics, performance, and useful links.")
    async def robus_about(self, interaction: discord.Interaction):
        links = {
            "Dashboard": "https://dashboard.example.com",
            "Invite": "https://discord.com/oauth2/authorize?client_id=1352323780092887140&permissions=8&integration_type=0&scope=bot",
            "Commands": "https://bot.example.com/commands",
            "Support": "https://discord.gg/support",
            "Vote": "https://top.gg/bot/YOUR_BOT_ID/vote",
            "Patreon": "https://patreon.com/YOUR_BOT"
        }

        process_memory = psutil.Process().memory_info().rss / (1024 * 1024)
        cpu_usage = psutil.cpu_percent(interval=1)
        total_servers = len(self.bot.guilds)
        total_shards = self.bot.shard_count or 1

        uptime_seconds = time.time() - self.start_time
        uptime_str = time.strftime("%j days, %Hh %Mm %Ss", time.gmtime(uptime_seconds))

        embed = discord.Embed(
            title="🤖 About Robus",
            description="Robus is a powerful, efficient, and spam-free Discord bot designed to enhance your server experience!",
            color=discord.Color.purple()
        )

        embed.add_field(
            name="🌐 Links",
            value="\n".join([f"[{name}]({url})" for name, url in links.items()]),
            inline=False
        )

        embed.add_field(name="💾 System Usage", value=f"**RAM:** {process_memory:.2f} MiB\n**CPU:** {cpu_usage:.2f}%", inline=True)
        embed.add_field(name="📡 Servers", value=f"**Total:** {total_servers:,}\n**Shards:** {total_shards}", inline=True)
        embed.add_field(name="⏳ Uptime", value=f"{uptime_str}", inline=False)
        embed.set_footer(text="Made with ❤️ by Mohit Nandaniya - Developer", icon_url="https://cdn-icons-png.flaticon.com/512/5968/5968350.png")

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="robus_help", description="Get assistance and support for Robus AI.")
    @app_commands.describe(prompt="Provide a detailed query for better assistance.")
    async def robus_help(self, interaction: discord.Interaction, prompt: str):
        await interaction.response.defer()

        try:
            if len(prompt) > 4000:
                await interaction.followup.send("Error: Your input is too long! Please limit it to 4000 characters.")
                return

            response = geminiutils.getResponse(prompt)
            if not response:
                await interaction.followup.send("Error: No response from AI.")
                return

            for chunk in [response[i:i+2000] for i in range(0, len(response), 2000)]:
                await interaction.followup.send(chunk)

        except Exception as e:
            await interaction.followup.send(f"Error: {str(e)}")

    @app_commands.command(name="robus_ping", description="Check the bot's latency and responsiveness.")
    async def robus_ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000, 2)
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"Latency: `{latency}ms`",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Support(bot))
