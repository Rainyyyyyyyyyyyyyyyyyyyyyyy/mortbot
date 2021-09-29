import discord
import datetime
from discord.ext import commands

class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def help(self, ctx):
        date = datetime.date.today()
        embed=discord.Embed(title=f"Mort", description=f"**Main Help Menu.**", color=0xB71100)
        embed.add_field(name="Bazzar commands: ", value=f"**$info [item]** - Displays info about the item", inline=False)
        embed.set_footer(text=f"$help | {date}")
        await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(HelpCommands(bot))