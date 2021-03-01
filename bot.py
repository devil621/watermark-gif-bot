from telethon import TelegramClient, events
from telethon.sessions import StringSession
import logging
from settings import API_ID,API_HASH,BOT_TOKEN,SESSION_STRING
from watermark import watermark_mp4,watermark_gif,mp4_to_gif

logging.basicConfig(level=logging.INFO)

if BOT_TOKEN:
    client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
elif SESSION_STRING:
    client = TelegramClient(StringSession(SESSION_STRING),API_ID,API_HASH)


@client.on(events.NewMessage())
async def echo(event:events.NewMessage):
    if event.gif:
        await event.respond('Got a gif')
        mp4_file = await event.download_media()
        gif_file = mp4_to_gif(mp4_file)
        outf = watermark_gif(gif_file,'image.png',10,10)
        await client.send_file(event.sender,'out.gif')


    else:
        await event.respond('Not a gif')




def main():
    client.run_until_disconnected()

if __name__ == '__main__':
    main()
