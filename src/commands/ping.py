import discord
from discord import app_commands
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Replies with Pong!")
    async def ping(self, interaction: discord.Interaction):
        # Calculate Bot latency
        bot_latency = round(self.bot.latency * 1000, 2) 

        # Measure API latency
        before = discord.utils.utcnow()
        await interaction.response.send_message("Pong! 🏓")
        after = discord.utils.utcnow()
        api_latency = (after - before).total_seconds() * 1000 

        await interaction.followup.send(f'🏓 Pong!\nBot Latency: {bot_latency}ms\nAPI Latency: {api_latency:.2f}ms')

        

async def setup(bot):
    await bot.add_cog(Ping(bot))