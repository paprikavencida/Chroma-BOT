import discord
from discord import app_commands

class BOT(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix="C",
            intents=intents
        )

        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print(f"{self.user} on.")

bot = BOT()

@bot.tree.command(name="olha-ele-ai", description="tome")
async def olhaele(interaction:discord.interactions):
    await interaction.response.send_message(f"ESTA LIGADO!!!! {interaction.user.mention}")

bot.run("SEU_TOKEN_AQUI")