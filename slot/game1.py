from kivy.uix.widget import Widget
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.clock import Clock
import os

Window.maximize()


class Play1(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)
        self.pressed_keys = set()
        Clock.schedule_interval(self.update, 0)

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

    def update(self, dt):
        step = 1000 * dt

        if "w" in self.pressed_keys:
            self.ids.object.pos[1] -= step
        if "s" in self.pressed_keys:
            self.ids.object.pos[1] += step
        if "a" in self.pressed_keys:
            self.ids.object.pos[0] += step
        if "d" in self.pressed_keys:
            self.ids.object.pos[0] -= step


class Game1(App):
    def build(self):
        return Play1()


if __name__ == "__main__":
    Game1().run()
