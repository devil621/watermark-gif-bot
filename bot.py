from telethon import TelegramClient, events
from telethon.sessions import StringSession
from settings import API_ID,API_HASH,BOT_TOKEN,SESSION_STRING

if BOT_TOKEN:
    client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
elif SESSION_STRING:
    client = TelegramClient(StringSession(SESSION_STRING),API_ID,API_HASH)


@client.on(events.NewMessage())
async def echo(event):

    await event.respond(event.text)


def main():
    client.run_until_disconnected()

if __name__ == '__main__':
    main()
