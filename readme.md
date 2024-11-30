# Discord Bot with Weather and EC2 Info

## Overview

This is a simple Discord bot built with Python, designed to provide basic interactions, tell jokes, fetch weather information, and display server metadata for an EC2 instance.

## Features

- **Basic Chat**: Responds to greetings like `hello` or `bye`.
- **Joke Teller**: Shares random jokes when prompted with "tell me a joke."
- **Weather Information**: Fetches current weather details for a given city using the OpenWeather API.
- **Server Metadata**: Displays the IP address, region, and availability zone of the EC2 server where the bot is hosted.
- **Customizable**: Easily extendable to include more commands or functionalities.

## Prerequisites

- Python 3.8 or above
- Discord Developer Account
- OpenWeather API Key
- AWS EC2 Instance (if using server metadata functionality)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/victoralfonsoulloa/discord_bot.git
cd discord_bot
```

### 2. Install Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` File

In the root directory, create a `.env` file to securely store your API keys and bot token:

```
TOKEN=your_discord_bot_token
OPENWEATHER_API_KEY=your_openweather_api_key
```

### 4. Run the Bot

Start the bot using:

```bash
python bot.py
```

### 5. Add the Bot to a Discord Server

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Create an application, add a bot, and copy its token to the `.env` file.
3. Use the OAuth2 tab to generate an invite link and add the bot to your server.

## Commands

| **Command**                    | **Description**                                                                          |
| ------------------------------ | ---------------------------------------------------------------------------------------- |
| `hello` / `hi` / `hello world` | Bot responds with a greeting.                                                            |
| `bye`                          | Bot says goodbye.                                                                        |
| `tell me a joke`               | Bot tells a random joke.                                                                 |
| `tell me about my server`      | Fetches and displays metadata (IP, region, availability zone) of the hosting EC2 server. |
| `weather <city>`               | Fetches current weather information for the specified city.                              |

## Dependencies

- `discord.py`: Library for interacting with the Discord API.
- `dotenv`: For managing environment variables securely.
- `ec2_metadata`: For fetching EC2 instance metadata.
- `requests`: For making HTTP requests to APIs.

Install dependencies using:

```bash
pip install discord.py python-dotenv ec2-metadata requests
```

## Error Handling

- Ensures required API keys are present; exits if missing.
- Handles API request errors gracefully, providing meaningful feedback to users.
- Prevents the bot from responding to its own messages to avoid loops.

## Customization

You can extend the bot's functionality by adding more commands in the `on_message` event handler. Use the Discord API documentation and `discord.py` library to create rich interactions.

## Example Usage

### Weather Command

User: `weather New York`  
Bot:

```
Weather in New York:
Description: Clear sky
Temperature: 22°C
Feels like: 21°C
```

### EC2 Metadata

User: `tell me about my server`  
Bot:

```
Server Info:
Public IP Address: 98.82.13.68
Private IP Address: 172.31.89.89
Region: us-east-1
Availability Zone: us-east-1a
```
