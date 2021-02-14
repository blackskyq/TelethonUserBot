import json
import logging
import requests
# import aiohttp
import asyncio
from userbot import bot
from userbot.util import admin_cmd
from urllib.request import Request, urlopen
WEB_HDRS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Accept': 'text/html,text/plain,application/xhtml+xml,application/xml,application/_json;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Charset': 'Windows-1252,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8;q=0.5',
    'Connection': 'keep-alive'
}
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
logger = logging.getLogger(__name__)



@bot.on(admin_cmd(pattern=("trlink ?(.*)")))
async def get_adzan(event):
  link = event.pattern_match.group(1)
  if link:
      api = f"https://ay.live/api/?api=458d6f3551527147e393b5fc9352dc600dc6aea2&url={link}&alias=&format=text&ct=1"
      r = requests.get(url = api, params = WEB_HDRS) 
      data = r.text
      await event.edit(data)
