""" Send automatically Star Wars wallpapers

Command: .autoswars

credit: @One_m4x1m """

import random, requests, re, os, urllib, inspect, traceback, asyncio, sys, io
from telethon import events, errors, functions, types
from telethon.tl import functions
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="autoswars"))
async def _(event):

    counter = -30
    COLLECTION_STRING = [
        "star-wars-wallpaper-1080p",
        "4k-sci-fi-wallpaper",
        "star-wars-iphone-6-wallpaper",
        "kylo-ren-wallpaper",
        "darth-vader-wallpaper",
    ]
    chat = event.chat.id
    while True:
        rnd = random.randint(0, len(COLLECTION_STRING) - 1)
        pack = COLLECTION_STRING[rnd]
        pc = requests.get("http://getwallpapers.com/collection/" + pack).text
        f = re.compile("/\w+/full.+.jpg")
        f = f.findall(pc)
        url = "http://getwallpapers.com" + random.choice(f)
        file_name = os.path.basename(url)
        to_download_directory = "/tmp/"
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        urllib.request.urlretrieve(url, downloaded_file_name)
        try:
            await borg.send_file(chat, downloaded_file_name)
            os.remove(downloaded_file_name)
            counter -= 30
            await asyncio.sleep(15)
        except:
            return