from redbot.core import commands

class Products(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_group(name="product")
    async def product(self, ctx: commands.Context):
        await ctx.send("What would you like to learn more about?")

    @product.command(name="antivirus")
    async def antivirus(self, ctx: commands.Context):
        await ctx.send("antivirus test message lol")
    
    @product.command(name="vulnerabilityscanning")
    async def vulnerabilityscanning(self, ctx: commands.Context):
        await ctx.send("vuln scanning test message")