import random
from typing import List

from redbot.core import commands

from .responses import RESPONSES


class Response:
    def __init__(self, start: str, repeat_seq: str, end: str, max_repeats: int = 20):
        self.start = start
        self.repeat_seq = repeat_seq
        self.max_repeats = max_repeats
        self.end = end

    def get_response(self):
        repeat = "".join(self.repeat_seq * random.randint(1, self.max_repeats))
        response = f"{self.start}{repeat}{self.end}"
        return response


class AAA(commands.Cog):
    """AAA. Make the bot scream."""

    def __init__(self, bot):
        self.bot = bot
        self.responses: List[Response] = []
        for response in RESPONSES:
            self.responses.append(Response(**response))

    @commands.command()
    async def aaa(self, ctx):
        response_obj = random.choice(self.responses)
        await ctx.send(response_obj.get_response())
