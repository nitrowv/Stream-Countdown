#Stream Countdown, created by Tanner Johnston, nitrowv on Github.
#Designed to accept user input for countdown timer in GUI and write to text file.

import time
from kivy.config import Config
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '160')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class StreamCountdown(Widget):
    pass


class StreamCountdownApp(App): #Creates Kivy App and Layout
    def build(self):
        layout = GridLayout(cols=2, row_force_default=True, row_default_height=40)
        layout.add_widget(Label(text="Minutes: ", size_hint_x=None, width=100))
        self.minutesInput = TextInput(multiline=False, input_filter='int', size_hint_x=None, width=40)
        layout.add_widget(self.minutesInput)
        layout.add_widget(Label(text="Seconds: ", size_hint_x=None, width=100))
        self.secondsInput = TextInput(multiline=False, input_filter='int', size_hint_x=None, width=40)
        layout.add_widget(self.secondsInput)
        layout.add_widget(Label(text="End Message: ", size_hint_x=None, width=100))
        self.messageInput = TextInput(multiline=False, size_hint_x=None, width=200)
        layout.add_widget(self.messageInput)
        submit = Button(text='Set Timer', size_hint_x=None, width=100)
        clear = Button(text='Clear Timer', size_hint_x=None, width=100)
        submit.bind(on_press=self.initiateCountdown)
        clear.bind(on_press=self.initiateClear)
        layout.add_widget(submit)
        layout.add_widget(clear)
        return layout

    def initiateCountdown(self, instance): #Initiates countdown function.
        minutes = self.minutesInput.text
        seconds = self.secondsInput.text
        message = self.messageInput.text
        countdown(minutes, seconds, message)
        return

    def initiateClear(self, instance): #Clears timer.txt.
        f = open("timer.txt", "w")
        f.truncate(0)
        return


def countdown(minutes, seconds, message): #Countdown function takes provided minutes, seconds, and optional end message; and writes it to timer.txt.
    t = ((int(minutes) * 60) + int(seconds) + 1)
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r", file=open("timer.txt", "w"))
        time.sleep(1)
        t -= 1
        if t == 0:
            if message == '':
                messagePrint = "00:00"
            else:
                messagePrint = message
            print(messagePrint, end="\r", file=open("timer.txt", "w"))
    return


if __name__ == '__main__':
    StreamCountdownApp().run()
