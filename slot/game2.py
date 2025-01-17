from kivy.uix.widget import Widget
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

Window.maximize()


class Play2(Widget):
    pass


class Game2(App):
    def build(self):
        return Play2()


if __name__ == "__main__":
    Game2().run()
