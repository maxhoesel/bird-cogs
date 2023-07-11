from redbot.core.bot import Red

from .aaa import AAA


async def setup(bot: Red):
    await bot.add_cog(AAA(bot))
