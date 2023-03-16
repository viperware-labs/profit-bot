import discord
from discord.ext import commands
import requests
from io import BytesIO
import sys

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.hybrid_command()
async def test(ctx):
    await ctx.send("This is a hybrid command!")

    
@client.hybrid_command()
async def image(ctx):
    # Download the image from a URL
    url = 'https://picsum.photos/200'
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Convert the response content into bytes
        image_bytes = response.content
        
        # Create a BytesIO object from the bytes
        file = BytesIO(image_bytes)
        
        # Send the image file as a message
        await ctx.send(file=discord.File(file, filename='image.jpg'))
    else:
        await ctx.send("Failed to download the image")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide bot token as command-line argument")
    else:
        client.run(sys.argv[1])
