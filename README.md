# FantasyWire Discord Bot

FantasyWire is a Discord bot that posts the latest Yahoo Fantasy Football league transactions to a Discord channel.

---

## Features

- Fetches recent transactions from Yahoo Fantasy Sports API
- Parses and formats transaction info (adds/drops)
- Posts updates to your Discord server

---

## Setup Guide

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/FantasyWire.git
cd FantasyWire
```

---

### 2. Install Dependencies

```sh
pip install -r requirements.txt
```

---

### 3. Yahoo OAuth Setup

Yahoo Fantasy Sports API requires OAuth2 authentication.

1. **Create a Yahoo Developer App:**  
   - Go to [Yahoo Developer Network](https://developer.yahoo.com/apps/)
   - Create a new app for Fantasy Sports
   - Set your `Redirect URI` (e.g., `https://localhost:8000/callback`)
   - Copy your `Client ID` and `Client Secret`

2. **Run the OAuth Setup Script:**  
   - Open `oauth_setup.py`
   - Replace `CLIENT_ID`, `CLIENT_SECRET`, and `REDIRECT_URI` with your values
   - Run the script:
     ```sh
     python oauth_setup.py
     ```
   - Follow the instructions to authorize the app and get your `refresh_token`

3. **Save Your Refresh Token:**  
   - Copy the `refresh_token` output by the script
   - You’ll use this in your `.env` file

---

### 4. Yahoo Fantasy Sports API League Key

- Log in to [Yahoo Fantasy Football](https://football.fantasysports.yahoo.com/)
- Go to your league page
- The league key is in the URL, e.g. `nfl.l.123456`
- Save this for your `.env` file

---

### 5. Discord Bot Setup

1. **Create a Discord Application & Bot:**
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application
   - Add a bot to your application
   - Copy the bot token

2. **Get Your Discord Channel ID:**
   - Enable Developer Mode in Discord (`Settings > Advanced > Developer Mode`)
   - Right-click your target channel and click "Copy ID"

---

### 6. Create a `.env` File

Create a `.env` file in the project root with the following:

```
YAHOO_CLIENT_ID=your_yahoo_client_id
YAHOO_CLIENT_SECRET=your_yahoo_client_secret
YAHOO_REFRESH_TOKEN=your_yahoo_refresh_token
DISCORD_TOKEN=your_discord_bot_token
DISCORD_CHANNEL_ID=your_discord_channel_id
LEAGUE_KEY=nfl.l.123456
```

---

### 7. Run the Bot

```sh
python main.py
```

---

## File Structure

- `main.py` — Entry point
- `discord_bot.py` — Discord bot logic
- `yahoo_api.py` — Yahoo API functions
- `transaction_parser.py` — XML parsing
- `oauth_setup.py` — One-time OAuth setup

---

## Troubleshooting

- Make sure your bot has permission to post in the target Discord channel.
- If you get authentication errors, re-run `oauth_setup.py` to refresh your token.
- Check your `.env` values for typos.

---
