# curlbot/context.py

class Context:
    def __init__(self, bot, update):
        self.bot = bot
        self.update = update

        self.message = update.get("message")
        self.callback = update.get("callback_query")

        if self.message:
            self.text = self.message.get("text", "")
            self.chat_id = self.message["chat"]["id"]
        elif self.callback:
            self.data = self.callback.get("data", "")
            self.chat_id = self.callback["message"]["chat"]["id"]
            self.cb_id = self.callback["id"]
