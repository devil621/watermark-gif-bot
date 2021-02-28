from telethon import TelegramClient, events
from telethon.sessions import StringSession
import logging
from settings import API_ID,API_HASH,BOT_TOKEN,SESSION_STRING


logging.basicConfig(level=logging.INFO)

if BOT_TOKEN:
    client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
elif SESSION_STRING:
    client = TelegramClient(StringSession(SESSION_STRING),API_ID,API_HASH)


@client.on(events.NewMessage())
async def echo(event:events.NewMessage):
    if event.gif:
        await event.respond('Got a gif')
        gif_file = await event.download_media()
        print(gif_file)

    else:
        await event.respond('Not a gif')




def main():
    client.run_until_disconnected()

if __name__ == '__main__':
    main()
