"""Emoji

Available Commands:

.lmfao """

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1
    

    animation_ttl = range(0, 75)

    input_str = event.pattern_match.group(1)

    if input_str == "lmfao":

        await event.edit(input_str)

        animation_chars = [

            "L",
            "Lm",    
            "Lmf",
            "Lmfao",
            "Lmfaoo",
            "Lmfaooo🤣",
            "Lmfaooo😂🤣",
            "Lmfaooo🤣😂🤣",
            "Lmfaooo🤣😂🤣😂",    
            "Lmfaooo🤣😂🤣😂🤣🤣🤣",
            
        ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 75])
