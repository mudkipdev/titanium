from typing import override
from main import TitaniumBot

import logging
import traceback

import discord
from discord.ext import commands, tasks


class StatusUpdate(commands.Cog):
    def __init__(self, bot: TitaniumBot) -> None:
        self.bot = bot
        self.status_update.start()

    @override
    async def cog_unload(self) -> None:
        self.status_update.cancel()

    # Uptime Kuma Ping
    @tasks.loop(hours=1)
    async def status_update(self):
        await self.bot.wait_until_ready()

        try:
            # Count members
            members: int = sum(guild.member_count for guild in self.bot.guilds)

            # Update status
            await self.bot.change_presence(
                activity=discord.Activity(
                    type=discord.ActivityType.listening,
                    name=f"{members} users in {len(self.bot.guilds)} servers - / to see commands",
                )
            )
        except Exception as e:
            logging.error(
                f"Failed to update status:\n\n```python\n{traceback.format_exc()}```"
            )


async def setup(bot: TitaniumBot) -> None:
    await bot.add_cog(StatusUpdate(bot))
