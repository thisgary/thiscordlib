from typing import Union

import discord
from discord.ext import commands
from dscord.func import clamp, rng_str

AnyChannel = Union[
        discord.CategoryChannel, 
        discord.VoiceChannel, 
        discord.StageChannel, 
        discord.TextChannel]


class Channel(commands.Cog):
    @commands.command('ccat', brief='Create category')
    async def createCategory(self, ctx, name: str = rng_str()) -> None:
        await ctx.guild.create_category_channel(name)
 
    @commands.command('cstg', brief='Create stage chn')
    async def createStage(self, ctx, name: str = rng_str()) -> None:
        await ctx.guild.create_stage_channel(name)
   
    @commands.command('ctxt', brief='Create txt chn')
    async def createText(self, ctx, name: str = rng_str()) -> None:
        await ctx.guild.create_text_channel(name)

    @commands.command('ctxts', brief='Create txt chns')
    async def createTexts(self, ctx, count: int, *, name: str) -> None:
        category = await ctx.guild.create_category_channel(rng_str())
        for i in range(clamp(count, max_val=50)):
            if not name: name = rng_str()
            name += f'-{i}'
            await category.create_text_channel(name)

    @commands.command('cvo', brief='Create voice chn')
    async def createVoice(self, ctx, name: str = rng_str()) -> None:
        await ctx.guild.create_voice_channel(name)

    @commands.command('cdel', brief='Delete chn')
    async def deleteChannel(self, ctx, channel: AnyChannel = None) -> None:
        if not channel: channel = ctx.channel
        if isinstance(channel, discord.CategoryChannel):
            for c in channel.channels: await c.delete()
        await channel.delete()


def setup(bot):
    bot.add_cog(Channel())
