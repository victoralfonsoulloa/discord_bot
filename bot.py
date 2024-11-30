import discord
import os
import random
from dotenv import load_dotenv
from ec2_metadata import ec2_metadata  # Use ec2_metadata for EC2 instance metadata
import requests  # Required for weather API

# Load environment variables from the .env file
load_dotenv()

# Create an instance of Intents
intents = discord.Intents.default()
intents.message_content = True

# Pass intents when creating the client
client = discord.Client(intents=intents)

# Load the bot token and OpenWeather API key from the .env file
token = os.getenv('TOKEN')
weather_api_key = os.getenv('OPENWEATHER_API_KEY')

if not token:
    print("Error: TOKEN is missing in .env file.")
    exit(1)

if not weather_api_key:
    print("Error: OPENWEATHER_API_KEY is missing in .env file.")
    exit(1)

# Function to fetch weather data
def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    try:
        response = requests.get(base_url, params={
            "q": city,
            "appid": weather_api_key,
            "units": "metric"  # Metric units for Celsius
        })
        data = response.json()
        if response.status_code == 200:
            # Extract weather details
            weather_desc = data['weather'][0]['description']
            temperature = data['main']['temp']
            feels_like = data['main']['feels_like']
            city_name = data['name']
            
            return (f"Weather in {city_name}:\n"
                    f"Description: {weather_desc.capitalize()}\n"
                    f"Temperature: {temperature}°C\n"
                    f"Feels like: {feels_like}°C")
        else:
            # Handle errors (e.g., invalid city name)
            return f"Couldn't find weather data for '{city}'. Please check the city name."
    except Exception as e:
        return f"Error retrieving weather data: {e}"

@client.event
async def on_ready():
    print(f"Logged in as a bot {client.user}")

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Message {user_message} by {username} on {channel}')

    # Prevent bot from responding to its own messages
    if message.author == client.user:
        return

    # Respond based on the message content
    if channel == "testing":
        if user_message.lower() in ["hello world", "hi world", "hello", "hi"]:
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f'Bye {username}')
        elif user_message.lower() == "tell me a joke":
            jokes = [
                "Why don’t eggs tell jokes? Because they might crack up!",
                "Why don’t skeletons fight each other? They don’t have the guts.",
                "What do you call fake spaghetti? An impasta!"
            ]
            await message.channel.send(random.choice(jokes))
        elif user_message.lower() == "tell me about my server":
            try:
                # Fetch EC2 metadata using ec2_metadata
                ip_address = ec2_metadata.public_ipv4
                private_ip = os.popen("hostname -I").read().strip()
                region = ec2_metadata.region
                availability_zone = ec2_metadata.availability_zone

                response = (
                    f"Server Info:\n"
                    f"Public IP Address: {ip_address}\n"
                    f"Private IP Address: {private_ip}\n"
                    f"Region: {region}\n"
                    f"Availability Zone: {availability_zone}"
                )
            except Exception as e:
                response = f"Sorry, I couldn't retrieve server info right now. Error: {e}"

            await message.channel.send(response)
        elif user_message.lower().startswith("weather "):  # Weather command
            city = user_message[8:].strip()  # Extract city name
            weather_info = get_weather(city)
            await message.channel.send(weather_info)
        else:
            await message.channel.send("I'm not sure what you mean. Try using a valid command!")

# Run the bot with the token
client.run(token)