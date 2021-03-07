from telethon import TelegramClient, events, utils
from telethon.sessions import StringSession
import logging
from settings import (API_ID, API_HASH,
                      BOT_TOKEN, SESSION_STRING,
                      WATERMARK)
from watermark import watermark
from utils import download_image
import os

logging.basicConfig(level=logging.INFO)

if BOT_TOKEN:
    client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
elif SESSION_STRING:
    client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)


@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Hi! I am alive.')
    raise events.StopPropagation


@client.on(events.NewMessage(pattern='/setimage'))
async def set_image(event):
    await event.respond('Hi! I am alive.')
    raise events.StopPropagation


@client.on(events.NewMessage(pattern='/setpos'))
async def set_pos(event):
    await event.respond('Hi! I am alive.')
    raise events.StopPropagation


@client.on(events.NewMessage())
async def echo(event):
    if event.gif or event.video:

        mp4_file = await event.download_media('')
        outf = watermark(mp4_file)
        print(outf)
        await client.send_file(event.sender_id, outf)
        os.remove(mp4_file)
        os.remove(outf)
    else:
        await event.respond('Not a valid file')


def main():
    if WATERMARK:
        download_image(url=WATERMARK, filename='image.png')
    client.run_until_disconnected()


if __name__ == '__main__':
    main()
