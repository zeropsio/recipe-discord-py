import discord
from discord.ext import commands
from src import config, setup

intents = discord.Intents.all()

class MyDiscordBot(commands.Bot):
    async def setup_hook(self):
        await setup.load_cogs(self)
        await bot.tree.sync()
        print("Commands synced!")

    async def on_ready(self):
        custom_activity = discord.CustomActivity(name="Waking up ⛔")
        await self.change_presence(status=discord.Status.do_not_disturb, activity=custom_activity)
        print('Discord bot is ready!')
        await self.change_presence(activity=discord.Game(name="on zerops.io", status=discord.Status.online))
        print("Bot is Online!")

bot = MyDiscordBot(command_prefix=['!'], intents=intents)

bot.run(config.BOT_TOKEN)