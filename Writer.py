import configparser
from tkinter import *
import functools
import inspect
import json
from telethon import TelegramClient, events, sync
import logging
import random
import asyncio
import telethon
from telethon.tl.types import PeerUser, PeerChat, PeerChannel, UpdateNewChannelMessage
from telethon.tl.functions.messages import SendMessageRequest
from telethon.tl import types, functions
from telethon import utils
import re
import time
import syncasync

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
api_id = int(config['Telegram']['api_id'])
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)

root = Tk()

canvas = Canvas(root)
canvas.pack()

cpf_entry = Entry(root)
cpf_entry.pack()


@client.on(events.NewMessage('ConsignadoBot'))
async def my_event_handler(event):
    resposta_bot = event.message.message

    print(resposta_bot)
    file = open("respostas.txt", "a")

    file.write(resposta_bot + "\n")

    time.sleep(1)


client.start()
client.run_until_disconnected()
