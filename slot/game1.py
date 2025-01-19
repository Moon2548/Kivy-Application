from kivy.uix.widget import Widget
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.graphics import Ellipse
from kivy.uix.boxlayout import BoxLayout
from kivy.vector import Vector
from kivy.animation import Animation
import os

Window.maximize()


def coliddes(rect1, rect2):
    r1x = rect1[0][0]
    r1y = rect1[0][1]
    r2x = rect2[0][0]
    r2y = rect2[0][1]
    r1w = rect1[1][0]
    r1h = rect1[1][1]
    r2w = rect2[1][0]
    r2h = rect2[1][1]

    if r1x < r2x + r2w and r1x + r1w > r2x and r1y < r2y + r2h and r1y + r1h > r2y:
        return True
    return False


class Play1(Widget):
    click = Window.width / 2 - 10, Window.height / 2 - 10

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)
        self.pressed_keys = set()
        Clock.schedule_interval(self.update, 0)
        Clock.schedule_interval(self.bullet_move, 0)
        Clock.schedule_interval(self.clock_count, 1)

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
        step = 500 * dt

        if "w" in self.pressed_keys:
            self.ids.object.pos[1] -= step
            self.ids.bullet0.pos[1] -= step
            self.ids.enemy.pos[1] -= step

        if "s" in self.pressed_keys:
            self.ids.object.pos[1] += step
            self.ids.bullet0.pos[1] += step
            self.ids.enemy.pos[1] += step

        if "a" in self.pressed_keys:
            self.ids.object.pos[0] += step
            self.ids.bullet0.pos[0] += step
            self.ids.enemy.pos[0] += step

        if "d" in self.pressed_keys:
            self.ids.object.pos[0] -= step
            self.ids.bullet0.pos[0] -= step
            self.ids.enemy.pos[0] -= step

    def on_touch_down(self, touch):
        self.click = touch.pos
        self.ids.bullet0.pos = Window.width / 2 - 10, Window.height / 2 - 10
        self.ids.bullet0.size = 20, 20
        bullet_ani = Animation(size=(0, 0), duration=2)
        bullet_ani.start(self.ids.bullet0)
        return super().on_touch_down(touch)

    def bullet_move(self, dt):
        step = 100
        self.ids.bullet0.pos = (
            Vector(
                (self.click[0] - Window.width / 2 - 10) / step,
                (self.click[1] - Window.height / 2 - 10) / step,
            )
            + self.ids.bullet0.pos
        )
        if coliddes(
            (self.ids.bullet0.pos, self.ids.bullet0.size),
            (self.ids.enemy.pos, self.ids.enemy.size),
        ):
            self.ids.bullet0.pos = 100000, 100000
            self.ids.enemy.hp -= 1
            if self.ids.enemy.hp == 0:
                self.ids.enemy.c = 0
                self.ids.enemy.size = 0, 0
                self.ids.enemy.pos = 100000, 100000

    def clock_count(self, dt):
        self.ids.enemy.c += 1
        print(self.ids.enemy.c)
        if self.ids.enemy.c == 5:
            self.ids.enemy.size = 100, 100
            self.ids.enemy.pos = self.ids.object.pos
            self.ids.enemy.hp = 5

    def close_play(self):
        App.get_running_app().stop()
        os.remove("slot/slot1_copy.kv")

    def open_menu(self):
        return True


class Game1(App):
    def build(self):
        return Play1()


if __name__ == "__main__":
    Game1().run()
