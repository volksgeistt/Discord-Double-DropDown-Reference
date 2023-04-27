import os
os.system("pip install -U nextcord")
import nextcord
from nextcord.ext import commands
from colorama import Fore

intents = nextcord.Intents.all()
intents.message_content = True
intents.members = True
intents.presences = True

prefxvent = ["???"]
tknxvent = ""

client = commands.Bot(command_prefix=prefxvent,intents=intents)
client.remove_command("help")
client.owner_ids = []

@client.event
async def on_ready():
  print("Online - Vent#1337")

# Class 1
class Vent1(nextcord.ui.Select):
  def __init__(self, embed=None):
    options = [nextcord.SelectOption(label="Vent1337",emoji=f"ADD_EMOJI_HERE",description="Vent Runs You"),]
    super().__init__(placeholder=f"Select From Main Module", max_values=1,min_values=1,options=options)
    self.embed = embed
  async def callback(self, interaction: nextcord.Interaction):
      
    if self.values[0] == "Vent1337":
      embed = self.embed or nextcord.Embed()
      embed.description = f"Menu Working Fine!\n[Follow vent On Github](https://github.com/vent69)"
      embed.set_author(name=f"{client.user.name} Help Panel",url=f"ADD_URL",icon_url=f"ADD_ICON_URL")
      await interaction.response.edit_message(embed=embed)

# Class 2
class Vent2(nextcord.ui.Select):
  def __init__(self, embed=None):
    options = [nextcord.SelectOption(label="Vent69",emoji=f"ADD_EMOJI_HERE",description="Vent Runs Your Mommy"),]
    super().__init__(placeholder=f"Select From Other Module",max_values=1,min_values=1,options=options)
    self.embed = embed
  async def callback(self, interaction: nextcord.Interaction):
    if self.values[0] == "Vent69":
      embed = self.embed or nextcord.Embed()
      embed.description = f"Menu Working Fine x2!\n[Follow vent On Github](https://github.com/vent69)"
      embed.set_author(name=f"{client.user.name} Help Panel x2",url=f"ADD_URL",icon_url=f"ADD_ICON_URL")
      await interaction.response.edit_message(embed=embed)

class SelectView(nextcord.ui.View):
  def __init__(self, *, timeout=300, embed=None):
    super().__init__(timeout=timeout)
    self.add_item(Vent1(embed=embed))
    self.add_item(Vent2(embed=embed))

@client.command(aliases=['h'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def help(ctx):
  embed = nextcord.Embed(
    description=
    f"Double DropDown",
    color=nextcord.Color.blurple())
  view = SelectView(embed=embed)
  embed.set_author(name=f"{client.user.name}'s Help Panel",
                   url=f"ADD_URL",
                   icon_url=f"ADD_ICON_URL")
  embed.set_footer(text=f"Requested By {ctx.author}",
                   icon_url=ctx.author.avatar.url)
  await ctx.send(embed=embed, view=view)

 client.run(tknxvent)
