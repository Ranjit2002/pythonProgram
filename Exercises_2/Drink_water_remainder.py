"""
Write a python program which reminds you of drinking water every hour or two. Your program can either beep
or send desktop notifications for a specific operating system.

Import module
Get time interval from the user, it asks user to input hour, minutes and seconds
Convert them to seconds and return time to main function.
Add loop to start timer and generate a toast message when timer reaches the set time
After sending notification program will call to function to write log file. This function will get current time and date
Create a .txt file and append drink water log to it.
"""

# import time
# from win10toast import ToastNotifier
# import datetime
#
#
# def getTimeInput():
#     minutes = int(input("Enter minute of interval:- "))
#     # seconds = int(input("Enter seconds of interval:- "))
#     time_interval = (minutes * 60)
#     return time_interval
#
#
# def log(self):
#     now = datetime.datetime.now()
#     start_time = now.strftime("%H:%M:%S")
#     with open("log.txt", 'a') as f:
#         f.write(f"You drank water {now} \n")
#     return 0
#
#
# def notify():
#     notification = ToastNotifier()
#     notification.show_toast("Time to drink water")
#     log()
#     return 0
#
#
# def starttime(time_interval):
#     while True:
#         time.sleep(time_interval)
#         notify()
#
#
# if __name__ == '__main__':
#     time_interval = getTimeInput()
#     starttime(time_interval)

import time
from win10toast import ToastNotifier
import datetime
import pygame


class Drink_water_notification:
    def time_input(self):
        while True:
            try:
                global total_time
                hour = int(input("Enter after how many hour do you want to drink water: "))
                minute = int(input("Enter after how many minute do you want to drink water: "))
                total_time = (hour * 3600) + (minute * 60)
                break
            except Exception as ex:
                print('\n', type(ex))
                print(ex, '\n')

    def show_notification(self):
        toaster = ToastNotifier()
        toaster.show_toast("Water Drinking Remainder", "Time to drink water", duration=0)
        time.sleep(total_time)

    # def play_sound(self, file_path):
    #     pygame.mixer.init()
    #     pygame.mixer.music.load(file_path)
    #     self.show_notification()
    #     pygame.mixer.music.play()
    #     time.sleep(10)
    #     pygame.mixer.music.stop()


if __name__ == '__main__':
    a = Drink_water_notification()
    a.time_input()
    while True:
        try:
            a.show_notification()
            # a.play_sound(r"D:\songs\spectre.mp3")
        except Exception as e:
            print(type(e))
            print(e)
