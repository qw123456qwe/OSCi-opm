# curlbot/curlbot.py

import requests
import time
import json

class Message:
    def __init__(self, data):
        self.data = data
        self.text = data.get("text", "")
        self.chat_id = data["chat"]["id"]

class Callback:
    def __init__(self, data):
        self.data = data
        self.id = data["id"]
        self.chat_id = data["message"]["chat"]["id"]
        self.payload = data.get("data", "")

class CurlBot:
    def __init__(self, token):
        self.token = token

        self.commands = {}
        self.text_handlers = {}
        self.callback_handlers = {}

        self.offset = 0

    # =====================
    # COMMAND
    # =====================
    def command(self, cmd):
        def wrapper(func):
            self.commands[cmd] = func
            return func
        return wrapper

    # =====================
    # TEXT
    # =====================
    def xabar(self, text):
        def wrapper(func):
            self.text_handlers[text] = func
            return func
        return wrapper

    # =====================
    # CALLBACK
    # =====================
    def callback(self, key):
        def wrapper(func):
            self.callback_handlers[key] = func
            return func
        return wrapper

    # =====================
    # SEND MESSAGE
    # =====================
    def javob(self, chat_id, text, reply_markup=None):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"

        data = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML"
        }

        if reply_markup:
            data["reply_markup"] = json.dumps(reply_markup)

        requests.post(url, data=data)

    # =====================
    # CALLBACK ANSWER
    # =====================
    def answer(self, cb_id, text=""):
        url = f"https://api.telegram.org/bot{self.token}/answerCallbackQuery"
        requests.post(url, data={
            "callback_query_id": cb_id,
            "text": text
        })

    # =====================
    # KEYBOARDS
    # =====================
    def reply_keyboard(self, buttons):
        return {
            "keyboard": buttons,
            "resize_keyboard": True
        }

    def inline_keyboard(self, buttons):
        return {
            "inline_keyboard": buttons
        }

    # =====================
    # GET UPDATES
    # =====================
    def _updates(self):
        url = f"https://api.telegram.org/bot{self.token}/getUpdates"
        res = requests.get(url, params={"offset": self.offset + 1})
        return res.json().get("result", [])

    # =====================
    # START LOOP
    # =====================
    def start(self):
        print("🤖 CurlBot ishga tushdi...")

        while True:
            updates = self._updates()

            for u in updates:
                self.offset = u["update_id"]

                # MESSAGE
                if "message" in u:
                    msg = Message(u["message"])

                    if msg.text.startswith("/"):
                        cmd = msg.text.split()[0]
                        if cmd in self.commands:
                            self.commands[cmd](msg)
                            continue

                    if msg.text in self.text_handlers:
                        self.text_handlers[msg.text](msg)
                        continue

                # CALLBACK
                if "callback_query" in u:
                    cb = Callback(u["callback_query"])

                    if cb.payload in self.callback_handlers:
                        self.callback_handlers[cb.payload](cb)
                    else:
                        self.answer(cb.id, "❓ Unknown")

            time.sleep(1)
