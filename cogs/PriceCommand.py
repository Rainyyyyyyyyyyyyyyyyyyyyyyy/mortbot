import discord
import datetime
import requests as rq
from discord.ext import commands

class PriceCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def info(self, ctx, *, item:str):
        item = item.replace(" ", "_").upper()
        # Get api
        weburl = rq.get("https://sky.shiiyu.moe/api/v2/bazaar").json()

        # Get data of item
        bzid = weburl[item]["id"]
        bzname = weburl[item]["name"]
        bzbprice = weburl[item]["buyPrice"]
        bzsprice = weburl[item]["sellPrice"]
        bzbvol = weburl[item]["buyVolume"]
        bzsvol = weburl[item]["sellVolume"]
        buy64 = bzbprice * 64
        sell64 = bzsprice * 64

        # All the data in one line so easy print / send embed
        fulldata = (f"\n**ID of item**: {bzid} \n**Name of item**: {bzname} \n**Bazzar buy price**: {bzbprice} \n**Bazzar sell price**: {bzsprice} \n**Bazzar buy volume**: {bzbvol} \n**Bazzar sell volume**: {bzsvol} \n**How much it costs for 64**: {buy64} \n**How much 64 sells for**: {sell64}")

        # Send embed
        date = datetime.date.today()
        embed=discord.Embed(title=f"Mort", description=f"**Bazzar info.**", color=0xB71100)
        embed.add_field(name=f"{item}", value=f"{fulldata}", inline=False)
        embed.set_footer(text=f"$info [item] | {date}")
        await ctx.send(embed=embed)
        




def setup(bot):
    bot.add_cog(PriceCommand(bot))