import os

async def load_cogs(self):
    for filename in os.listdir('./src/commands'):
        if filename.endswith('.py'):
            try:
                await self.load_extension(f"src.commands.{filename[:-3]}")
            except Exception as e:
                print(f"Failed to load {filename[:-3]} cog: {e}")
    print("All cogs loaded")