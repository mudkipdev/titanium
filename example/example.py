import discord
from discord import app_commands
from discord.ext import commands

from main import TitaniumBot


class Example(commands.Cog):
    def __init__(self, bot: TitaniumBot) -> None:
        self.bot = bot

    @app_commands.command(name="hello", description="hello")
    async def hello(self, interaction: discord.Interaction) -> None:
        await interaction.response.defer()
        embed = discord.Embed(title="Hello!")
        await interaction.followup.send(embed=embed)


async def setup(bot: TitaniumBot) -> None:
    await bot.add_cog(Example(bot))
