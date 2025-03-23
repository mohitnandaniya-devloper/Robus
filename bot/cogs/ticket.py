import discord
from discord.ext import commands
from discord import app_commands

class Ticket(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ticket_create", description="Creates a new support ticket.")
    @app_commands.describe(
        user="Which Member do you want to add to the Ticket?",
        type="(Optional) Select the type of issue",
        reason="(Optional) Briefly describe the reason for the ticket"
    )
    async def ticket_create(
        self, interaction: discord.Interaction,
        user: discord.Member,
        type: str = "Ticket",
        reason: str = "No reason provided."
    ):
        guild = interaction.guild
        category = discord.utils.get(guild.categories, name="Tickets")

        if category is None:
            category = await guild.create_category("Tickets", reason=reason)

        ticket_channel = await guild.create_text_channel(
            name=f"{type}-{user.name}",
            category=category,
            overwrites={
                guild.default_role: discord.PermissionOverwrite(view_channel=False),
                user: discord.PermissionOverwrite(view_channel=True, send_messages=True),
                interaction.user: discord.PermissionOverwrite(view_channel=True, send_messages=True),
                guild.me: discord.PermissionOverwrite(view_channel=True, send_messages=True, manage_channels=True)
            }
        )

        # Notify user in DM
        go_to_ticket_view = discord.ui.View()
        go_to_ticket_button = discord.ui.Button(
            label="Go to Ticket",
            style=discord.ButtonStyle.link,
            url=ticket_channel.jump_url
        )
        go_to_ticket_view.add_item(go_to_ticket_button)

        await interaction.response.send_message(
            content=f"{interaction.user.mention}, your ticket has been created in {ticket_channel.mention}!",
            view=go_to_ticket_view,
            ephemeral=True
        )

        # ✅ Ticket Embed with Mention
        ticket_embed = discord.Embed(
            title=f"🎟️ {type.capitalize()} Ticket Open",
            description=f"Hello {user.mention}, our support team will assist you soon.\n\n**Reason:** {reason}",
            color=discord.Color.blue()
        )

        # ✅ Ticket Action Buttons
        class TicketButtons(discord.ui.View):
            def __init__(self, channel):
                super().__init__()
                self.channel = channel
                self.claimed = False

            @discord.ui.button(label="🔒 Close Ticket", style=discord.ButtonStyle.danger)
            async def close_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
                await self.channel.delete(reason="Ticket closed by user.")

            @discord.ui.button(label="🎫 Claim Ticket", style=discord.ButtonStyle.blurple)
            async def claim_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
                if not self.claimed:
                    self.claimed = True
                    button.disabled = True
                    button.label = f"🎟️ Claimed by {interaction.user.name}"
                    await interaction.response.edit_message(view=self)
                    await interaction.channel.send(f"{interaction.user.mention} has claimed this ticket!")

        view = TicketButtons(ticket_channel)
        await ticket_channel.send(
            content=f"🔔 {interaction.user.mention}, your ticket has been created!",
            embed=ticket_embed,
            view=view
        )

async def setup(bot: commands.Bot):
    await bot.add_cog(Ticket(bot))
