from telethon import TelegramClient, events
from telethon.sessions import StringSession
import logging
from settings import (API_ID, API_HASH,
                      BOT_TOKEN, SESSION_STRING,
                      WATERMARK,
                      X_OFF, Y_OFF)
from watermark import watermark_gif, mp4_to_gif
from utils import download_image, files


logging.basicConfig(level=logging.INFO)

if BOT_TOKEN:
    client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
elif SESSION_STRING:
    client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)


@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Hi! I am alive.')
    raise events.StopPropagation


@client.on(events.NewMessage())
async def echo(event):
    if event.gif:
        await event.respond('Got a gif')
        mp4_file = await event.download_media('files/')
        gif_file = mp4_to_gif(mp4_file)
        outf = watermark_gif(gif_file, files('image.png'), X_OFF, Y_OFF)
        print(outf)
        await client.send_file(event.sender_id, outf)
    else:
        await event.respond('Not a gif')


def main():
    download_image(url=WATERMARK, filename=files('image.png'))
    client.run_until_disconnected()


if __name__ == '__main__':
    main()
