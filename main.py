from kivy.uix.widget import Widget
from kivy.app import App
from kivy.core.window import Window

Window.maximize()


class MainWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)
        self.pressed_keys = set()

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        print("down", text)
        self.pressed_keys.add(text)

    def _on_key_up(self, keyboard, keycode):
        text = keycode[1]
        print("up", text)

        if text in self.pressed_keys:
            self.pressed_keys.remove(text)

    def close_app(self):
        App.get_running_app().stop()


class MyApp(App):
    def build(self):
        return MainWidget()


if __name__ == "__main__":
    MyApp().run()
