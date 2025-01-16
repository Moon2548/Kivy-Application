from kivy.uix.widget import Widget
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

Window.maximize()


class Screenmanager(ScreenManager):
    pass


class SettingScreen(Screen):
    pass


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def close_app(self):
        App.get_running_app().stop()


class MyApp(App):
    def build(self):
        return Builder.load_file("my.kv")


if __name__ == "__main__":
    MyApp().run()
