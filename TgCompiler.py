from telethon import TelegramClient, events, sync
from telethon.tl.types import InputChannel, InputPeerUser
import yaml
import sys
from telethon.sessions import StringSession
import logging
import  configparser
import  json, requests
from threading import Thread
from  telethon  import  TelegramClient , events
from  telethon . errors  import  SessionPasswordNeededError
import os
import  telethon . sync
import subprocess

from  pprint  import  pprint
        

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("telethon").setLevel(level=logging.WARNING)
logger = logging.getLogger(__name__)


def start(config):
    client = TelegramClient(
        StringSession(config["session_name"]), config["api_id"], config["api_hash"]
    )
    client.start()

    @client.on(events.NewMessage(pattern="/py"))
    async def add_py(event):
        if str(event.sender_id) == "503607829" or str(event.sender_id) == "1255422851" or str(event.sender_id) == "1449695176":

            msg = event.message.message
            await event.reply("Running python command . . .")
            try:
                code = msg.lstrip('/py')
            except IndexError:
                await event.reply("No arguments given (Py)")
            command = "".join(f"\n {x}" for x in code.split("\n.strip()"))
            indexofip = command.find("py_input_vars")
            ip=""
            if indexofip!=-1:
                user_in = command[indexofip+len("py_input_vars:"):].strip()
                command = command[:indexofip]
                ip = user_in.encode("utf-8")
            # skipcq: BAN-B603
            """
                print(input())

                py_input_vars:
                1 2 3 4 5
                3 4 5 6 7
            """

            data = {
                "lang": "python3",
                "code": command,
                "input": ip
            }

            result = json.loads(requests.post(
                "https://compilethis.herokuapp.com/", data=data).content).get("result")

            if len(result) > 2500:
                await event.reply("Results too big... Sending as file")
                with open("output.txt", "w+") as f:
                    f.write(result)
                await client.send_file(event.chat_id, 'output.txt')
                os.remove("output.txt")
            else:
                try:
                    await event.reply(result)
                except TelegramError as excp:
                    await event.reply(str(excp.message))
        else:
            await event.reply("I only execute EdwardROCKS Commands, So Sorry")
            
    @client.on(events.NewMessage(pattern="/c"))
    async def add_c(event):
        if str(event.sender_id) == "503607829" or str(event.sender_id) == "1255422851" or str(event.sender_id) == "1449695176":

            msg = event.message.message
            await event.reply("Running c command . . .")
            try:
                code = msg.lstrip('/c')
            except IndexError:
                await event.reply("No arguments given (c)")
            command = "".join(f"\n {x}" for x in code.split("\n.strip()"))
            indexofip = command.find("c_input_vars")
            ip=""
            if indexofip!=-1:
                user_in = command[indexofip+len("c_input_vars:"):].strip()
                command = command[:indexofip]
                ip = user_in.encode("utf-8")
            # skipcq: BAN-B603
            """
                printf("hello");

                c_input_vars:
                1 2 3 4 5
                3 4 5 6 7
                
            """

            data = {
                "lang": "c",
                "code": command,
                "input": ip
            }

            result = json.loads(requests.post(
                "https://compilethis.herokuapp.com/", data=data).content).get("result")

            if len(result) > 2500:
                await event.reply("Results too big... Sending as file")
                with open("output.txt", "w+") as f:
                    f.write(result)
                await client.send_file(event.chat_id, 'output.txt')
                os.remove("output.txt")
            else:
                try:
                    await event.reply(result)
                except TelegramError as excp:
                    await event.reply(str(excp.message))


    @client.on(events.NewMessage(pattern="/ac"))
    async def add_cpp(event):
        if str(event.sender_id) == "503607829" or str(event.sender_id) == "1255422851" or str(event.sender_id) == "1449695176":

            msg = event.message.message
            await event.reply("Running cpp command . . .")
            try:
                code = msg.lstrip('/ac')
            except IndexError:
                await event.reply("No arguments given (cpp)")
            command = "".join(f"\n {x}" for x in code.split("\n.strip()"))
            indexofip = command.find("cpp_input_vars")
            ip=""
            if indexofip!=-1:
                user_in = command[indexofip+len("cpp_input_vars:"):].strip()
                command = command[:indexofip]
                ip = user_in.encode("utf-8")
            # skipcq: BAN-B603
            """
                cout << "hello" << endl;

                cpp_input_vars:
                1 2 3 4 5
                3 4 5 6 7
            """

            data = {
                "lang": "cpp",
                "code": command,
                "input": ip
            }

            result = json.loads(requests.post(
                "https://compilethis.herokuapp.com/", data=data).content).get("result")

            if len(result) > 2500:
                await event.reply("Results too big... Sending as file")
                with open("output.txt", "w+") as f:
                    f.write(result)
                await client.send_file(event.chat_id, 'output.txt')
                os.remove("output.txt")
            else:
                try:
                    await event.reply(result)
                except TelegramError as excp:
                    await event.reply(str(excp.message))

    client.run_until_disconnected()

if __name__ == "__main__":
    config = {
        "api_id": os.environ.get("api_id"),
        "api_hash": os.environ.get("api_hash"),
        "session_name": os.environ.get("session_name"),
    }

    start(config)
    
