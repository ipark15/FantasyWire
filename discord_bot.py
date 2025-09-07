import os
import discord
from discord.ext import tasks
from dotenv import load_dotenv
from yahoo_api import refresh_access_token, get_transactions
from transaction_parser import parse_transactions
from datetime import datetime

# Load secrets from .env
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

intents = discord.Intents.default()
client = discord.Client(intents=intents)
last_seen = None

def transaction_to_embed(txn):
    embed = discord.Embed(
        title="Fantasy Transaction",
        color=discord.Color.blue()
    )
    embed.add_field(name="Team", value=txn["team_name"], inline=False)
    embed.add_field(name="Added", value=", ".join(f"`{name}`" for name in txn["added"]) if txn["added"] else "None", inline=True)
    embed.add_field(name="Dropped", value=", ".join(f"`{name}`" for name in txn["dropped"]) if txn["dropped"] else "None", inline=True)
    if "timestamp" in txn:
        dt = datetime.fromtimestamp(int(txn["timestamp"]))
        embed.timestamp = dt
    return embed

seen_ids = set()

@tasks.loop(minutes=1)
async def poll_yahoo():
    global last_seen, seen_ids
    await client.wait_until_ready()
    channel = client.get_channel(DISCORD_CHANNEL_ID)
    if channel is None:
        print("⚠️ Channel not found! Check ID and bot permissions.")
        return
    try:
        access_token = refresh_access_token()
        transactions_xml = get_transactions(access_token)
        transactions_list = parse_transactions(transactions_xml)
        new_txns = [txn for txn in transactions_list if txn["transaction_id"] not in seen_ids]
        if new_txns:
            for txn in new_txns:
                embed = transaction_to_embed(txn)
                await channel.send(embed=embed)
                seen_ids.add(txn["transaction_id"])
        elif last_seen is None:
            await channel.send("No recent transactions found.")
        last_seen = transactions_xml
    except Exception as e:
        await channel.send(f"⚠️ Error: {e}")

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")
    poll_yahoo.start()

def run():
    client.run(DISCORD_TOKEN)