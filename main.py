import discord
from discord.ext import commands
import os

api_key = os.environ.get("discbot")

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.command()
async def p(ctx, system_name):
  """
  sends emebed image with likly wh spawns close to the system if the system is in sys.txt file
  """
  with open('sys.txt') as file:
    contents = file.read()
    search_word = system_name
    if search_word in contents:
        file.close()
        embed = discord.Embed(description=f"Here's the exit map for {system_name}")
        embed.set_image(url=f'https://pochven.goryn.wtf/img/{system_name}.png')
        await ctx.send(embed=embed)
    else:
        file.close()
        pass

def main():
    
    bot.run(api_key)

if __name__ == "__main__":
    main()