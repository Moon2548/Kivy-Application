from kivy.uix.widget import Widget
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
import slot
from slot import game1, game2, game3, game4, game5

Window.maximize()
Builder.load_file("display_screen.kv")


class Screenmanager(ScreenManager):
    pass


class PlayScreen(Screen):
    def play_game1(self):
        with open("slot/slot1.kv", "r") as f:
            copy = f.read()
        with open("slot/slot1_copy.kv", "w") as f:
            f.write(copy)
        Builder.load_file("slot/slot1_copy.kv")
        App.get_running_app().stop()
        return game1.Game1().run()


class SettingScreen(Screen):
    def slide_test(self, *args):
        self.ids.slider_label.text = "wow" + str(int(args[1]))
        self.ids.setslide.font_size = int(args[1])

    def checkbox_click(self, instance, value):
        if value == True:
            print("hi")
            self.ids.check_label.text = "True"
        elif value == False:
            self.ids.check_label.text = "False"
            print("hello")

    def check_group_click(self, instance, value):
        if value == True:
            self.ids.check_group.text = "1"


class MainScreen(Screen):
    def close_app(self):
        App.get_running_app().stop()


class MyApp(App):
    def build(self):
        return Builder.load_file("my.kv")


if __name__ == "__main__":
    MyApp().run()
