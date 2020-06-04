from telethon import TelegramClient, events, sync
from tkinter import *
import tkinter
import asyncio


# TELEGRAM SETUP
api_id = XXX
api_hash = 'XXXX'

client = TelegramClient('session_name', api_id, api_hash)
client.start()


# TKINTER SETUP
root = Tk()

canvas = Canvas(root)
canvas.pack()

cpf_entry = Entry(root)
cpf_entry.pack()


def send_telegram():
    cpf = cpf_entry.get()
    client.send_message('ConsignadoBot', cpf)


search_btn = Button(root, text='Consultar', command=send_telegram)
search_btn.pack()


def main():
    try:
        while True:
            root.update()
    except KeyboardInterrupt:
        pass
    except tkinter.TclError as e:
        if 'application has been destroyed' not in e.args[0]:
            raise
    finally:
        client.disconnect()


client.loop.run_until_complete(main())
