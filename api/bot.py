from pyrogram import Client, filters
from os import getenv
# from dotenv import load_dotenv

from shortner import shorten_url

import logging
import sys

from http.server import BaseHTTPRequestHandler, HTTPServer

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#loads environment variables
# load_dotenv()

#gets and assigns the env a variable
API_ID = getenv('API_ID')
API_HASH = getenv('API_HASH')
BOT_TOKEN = getenv("BOT_TOKEN")

app = Client("deby_bit",api_id=API_ID,api_hash=API_HASH, bot_token=BOT_TOKEN)

start_msg = '''Hellow this is a bot made by @DebyO2 , you can shorten your URLs here\n(use /help to see the list of commands available)'''

result = '''Your Given Link : {}\n\nYour circumcised link : {}\n\n ⭕DΣBY-BIƬ⭕'''

help_msg = "Commands available:\n🔘/start to start\n🔘/url www.example.com to shorten the link"

@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply(start_msg)

@app.on_message(filters.command("help"))
async def start_command(client, message):
    await message.reply(help_msg)

@app.on_message(filters.command("url"))
async def circumcised(client, message):
    # Extract the command and arguments
    # command = message.command[0]  # This is the command itself
    try:
        argument = message.command[1:][0]  # These are the arguments

        shortened_url = shorten_url(argument)
        await message.reply(result.format(argument,shortened_url))
    except Exception as e:
        print(e)
        await message.reply("Use it like this : /url www.example.com")

# app.run()
# Define the HTTP handler
class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            app.run()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')
        except Exception as e:
            logger.error(f"Error handling POST request: {e}")
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b'Internal Server Error')

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', int(os.getenv('PORT', 8000))), handler)
    logger.info("Starting server at port 8000")
    server.serve_forever()
