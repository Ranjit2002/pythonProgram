# Whatsapp --> voice call, video call, chat, status, payment
# Telegram doesn't supports payment

class Whatsapp:
    def __init__(self, App_name):
        self.app = App_name
    def voice_call(self):
        print(f"{self.app} support voice call")

    def video_call(self):
        print(f"{self.app} support video call")

    def chat(self):
        print(f"{self.app} support chat")

    def status(self):
        print(f"{self.app} support status")

    def payment(self):
        print(f"{self.app} support payment")


class Telegram(Whatsapp):
    def payment(self):
        print(f"{self.app} doesn't support payment")


whatsapp = Whatsapp("Whatsapp")
whatsapp.voice_call()
whatsapp.video_call()
whatsapp.chat()
whatsapp.status()
whatsapp.payment()
print()

telegram = Telegram("Telegram")
telegram.voice_call()
telegram.video_call()
telegram.chat()
telegram.status()
telegram.payment()
