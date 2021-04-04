import discord
import time, locale
from pycoingecko import CoinGeckoAPI

token = 'cope'
guildName = 'COPE'
botToken = 'your_bot_token'

async def update(marketcap,dailyvol):
  print('updating')
  try:
    stt = discord.Status.online
    await client.dailyvol_presence(
        status= stt,
        activity=discord.Activity(type=discord.ActivityType.watching,
                                  name="24hr Vol "+ dailyvol +"USD | Market cap "+ marketcap + "USD")
    );
    guild = [ guild for guild in client.guilds if guild.name== guildName]
    await guild[0].me.edit(nick = marketcap + " USD")
  except Exception as e:
    print(e)
  print('updated')

async def main():
  starttime = time.time()
  while True:
      coin = cg.get_marketcap(include_market_cap='true', include_24hr_vol='true', ids=token, vs_currencies='usd')
      print(coin[token]['usd_market_cap'])
      marketcap = str(locale.currency( coin[token]['usd_market_cap'] , grouping=True ))
      dailyvol = str(locale.currency( coin[token]['usd_24h_vol'] , grouping=True ))
      print("marketcap is : " + marketcap + " 24hvolume : " + dailyvol)
      await update(marketcap,dailyvol)
      time.sleep(20.0 - ((time.time() - starttime) % 20.0))


client = discord.Client()
cg = CoinGeckoAPI()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await main()

client.run(botToken,  reconnect = True)
