import discord, os
from instaloader import Instaloader, Profile
from discord.ext import commands,tasks
from discord import Intents, Embed
from resources.Lists import *


client = commands.Bot(case_insensitive=True, command_prefix=['spike ', 'Spike '], intents=discord.Intents.all())
client.remove_command('help')


@client.event
async def on_ready():
  print('We have logged in as {0.user}!'.format(client))
  await client.change_presence(activity=discord.Game(name="as an old-fashioned cowboy🚬"))


async def is_it_me(ctx):
  if ctx.author.id == 463780399437447200:
    return ctx.author.id == 463780399437447200
  
  elif ctx.author.id == 310366898678136832:
    return ctx.author.id == 310366898678136832
  
  else:
    await ctx.send("You can't do that!")

    
async def stunner(ctx):
  if ctx.author.id == 436388529451302913:
    return ctx.author.id == 436388529451302913
	
  elif ctx.author.id == 772413115207516200:
    return ctx.author.id == 772413115207516200

    
async def is_it_trustees(ctx):
  if ctx.author.id == 463780399437447200:
    return ctx.author.id == 463780399437447200
  
  elif ctx.author.id == 310366898678136832:
    return ctx.author.id == 310366898678136832

  elif ctx.author.roles == 414065220495998977:
    return ctx.author.roles == 414065220495998977

  else:
    await ctx.send("You can't do that!")  


@client.command()
@commands.check(is_it_me)
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')
  await ctx.send(f'Loaded **{extension}**!')


@client.command()
@commands.check(is_it_me)
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  await ctx.send(f'Unloaded **{extension}**!')


@client.command()
@commands.check(is_it_me)
async def reload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  client.load_extension(f'cogs.{extension}')
  await ctx.send(f'Reloaded **{extension}**!')
  

@client.command()
@commands.check(stunner)
async def remusic(ctx, extension):
  client.unload_extension(f'cogs.Music')
  client.load_extension(f'cogs.Music')
  await ctx.send(f'Reloaded **Music**!')


@client.command()
@commands.check(is_it_me)
async def shutdown(ctx):
  await ctx.send('Shutting down the bot!')
  await client.logout()


@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('I cannot do that without the requirements!')


@client.event
async def on_guild_join(guild):
  for channel in guild.text_channels:
    if channel.permissions_for(guild.me).send_messages:
      await channel.send("Hello! My prefix is `spike <command>`. For help, check `spike help`!")
      await channel.send('Moderators, please check my `spike mod` command before using any moderation commands.')
    break


for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_member_join(member):
  guild = client.get_guild(414057277050585088)
  total_channel = guild.get_channel(840917507266707456)
  member_channel = guild.get_channel(840916757593849916)
  bot_channel = guild.get_channel(840917190378651708)
  await member_channel.edit(name=f'👥 Members: {len(list(filter(lambda m: not m.bot,guild.members)))}')
  await bot_channel.edit(name=f'🤖 Kaikoolis: {len(list(filter(lambda m: m.bot,guild.members)))}')
  await total_channel.edit(name=f'📈 Total: {guild.member_count}')


@client.event
async def on_member_remove(member):
  guild = client.get_guild(414057277050585088)
  total_channel = guild.get_channel(840917507266707456)
  bot_channel = guild.get_channel(840917190378651708)
  member_channel = guild.get_channel(840916757593849916)
  await member_channel.edit(name=f'👥 Members: {len(list(filter(lambda m: not m.bot,guild.members)))}')
  await bot_channel.edit(name=f'🤖 Kaikoolis: {len(list(filter(lambda m: m.bot,guild.members)))}')
  await total_channel.edit(name=f'📈 Total: {guild.member_count}')


@tasks.loop(minutes=5.0)
async def followers():
  await client.wait_until_ready()
  guild = client.get_guild(int(414057277050585088))
  Insta = Instaloader()
  profile = Profile.from_username(Insta.context, 'otaku_nadu')
  followcount = str(profile.followers)
  instagram_channel = guild.get_channel(int(840917916320923698))
  await instagram_channel.edit(name=f'📷 Instagram: {followcount}')


followers.start()



client.run(os.getenv('TOKEN'))
