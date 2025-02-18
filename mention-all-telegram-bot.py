from telethon import TelegramClient, events
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Your API credentials (Replace these with environment variables)
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

# Initialize the Telegram bot
client = TelegramClient("bot_session", api_id, api_hash).start(bot_token=bot_token)

async def get_all_members(event):
    """Fetch all members of the group"""
    chat = await event.get_chat()
    members = []
    
    async for user in client.iter_participants(chat):
        if user.username:
            members.append(f"@{user.username}")
        else:
            members.append(f"[{user.first_name}](tg://user?id={user.id})")

    return members

@client.on(events.NewMessage(func=lambda e: e.is_group and "@all" in e.raw_text))
async def mention_all(event):
    """Reply to messages containing '@all' by mentioning all group members with constraints"""
    sender = await event.get_sender()
    members = await get_all_members(event)

    if not members:
        await event.reply("❌ No members found to mention.")
        return

    total_members = len(members)

    if total_members > 10:
        # If more than 10 members, do nothing
        return
    elif 5 <= total_members <= 10:
        # If members are between 5 and 10, send two separate messages
        first_batch = " ".join(members[:5])
        second_batch = " ".join(members[5:])

        await event.reply(f"👥 {sender.first_name} tagged everyone:\n\n{first_batch}", parse_mode="md")
        await asyncio.sleep(1)  # Small delay to avoid flooding
        await event.reply(f"👥 Continuing mentions:\n\n{second_batch}", parse_mode="md")
    else:
        # If members are less than 5, send a single message
        mention_text = " ".join(members)
        await event.reply(f"👥 {sender.first_name} tagged everyone:\n\n{mention_text}", parse_mode="md")

print("Bot is running...")
client.run_until_disconnected()
