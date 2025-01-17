from kivy.uix.widget import Widget
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

Window.maximize()


class Play4(Widget):
    pass


class Game4(App):
    def build(self):
        return Play4()


if __name__ == "__main__":
    Game4().run()
