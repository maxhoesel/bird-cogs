from redbot.core import commands

from .responses import get_response


class AAA(commands.Cog):
    """AAA. Make the bot scream."""

    def __init__(self, bot):
        self.bot = bot

    # aaa
    @commands.command(name="aaa")
    async def aaa(self, ctx):
        await ctx.send(get_response("aaa"))

    @commands.command(name="aaaa")
    async def aaaa(self, ctx):
        self.aaa(ctx)

    @commands.command(name="aaaaa")
    async def aaaaa(self, ctx):
        self.aaa(ctx)

    @commands.command(name="aaaaaa")
    async def aaaaaa(self, ctx):
        self.aaa(ctx)

    @commands.command(name="AAA")
    async def AAA(self, ctx):
        self.aaa(ctx)

    @commands.command(name="AAAA")
    async def AAAA(self, ctx):
        self.aaa(ctx)

    @commands.command(name="AAAAA")
    async def AAAAA(self, ctx):
        self.aaa(ctx)

    @commands.command(name="AAAAAA")
    async def AAAAAA(self, ctx):
        self.aaa(ctx)

    # yarr
    @commands.command(name="yarr")
    async def yarr(self, ctx):
        await ctx.send(get_response("yarr"))

    @commands.command(name="YARR")
    async def YARR(self, ctx):
        self.yarr(ctx)
