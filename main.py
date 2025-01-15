from kivy.uix.widget import Widget
from kivy.app import App
from kivy.core.window import Window

Window.maximize()


class MainWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MyApp(App):
    def build(self):
        return MainWidget()


if __name__ == "__main__":
    MyApp().run()
