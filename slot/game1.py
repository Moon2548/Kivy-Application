from kivy.uix.widget import Widget
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
import os

Window.maximize()


class Play1(Widget):
    def write(self):
        print("Play!")

    def close_app(self):
        App.get_running_app().stop()
        os.remove("slot/slot1_copy.kv")


class Game1(App):
    def build(self):
        return Play1()


if __name__ == "__main__":
    Game1().run()
