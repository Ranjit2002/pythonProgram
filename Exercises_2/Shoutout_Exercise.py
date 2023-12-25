import win32com.client as win

speaker = win.Dispatch("SAPI.SpVoice")

l1 = ["Ranjit", "Elon Musk", "Jeff Bezos", "Bill Gates", "Steve Jobs"]

for i in l1:
    speaker.Speak(f"Shoutout to {i}")
