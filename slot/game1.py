from kivy.uix.widget import Widget
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.graphics import Ellipse
from kivy.uix.boxlayout import BoxLayout
from kivy.vector import Vector
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
    bullet_count = 0
    click = Window.width / 2, Window.height / 2

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)
        self.pressed_keys = set()
        Clock.schedule_interval(self.update, 0)
        Clock.schedule_interval(self.bullet_move, 0)
        Clock.schedule_interval(self.respawn_enemy, 1)

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
        self.ids.bullet0.pos = Window.width / 2, Window.height / 2
        # with open("slot/slot1_copy.kv", "r") as f:
        #     a = f.read()
        #     update_a = a.replace(
        #         f"""        BoxLayout:
        #     orientation:'vertical'
        #     id: bullet{self.bullet_count}
        #     canvas:
        #         Color:
        #             rgba: 0, 1, 0, 1
        #         Ellipse:
        #             pos: 10000, 10000
        #             size: 20, 20""",
        #         f"""        BoxLayout:
        #     orientation:'vertical'
        #     id: bullet{self.bullet_count}
        #     canvas:
        #         Color:
        #             rgba: 0, 1, 0, 1
        #         Ellipse:
        #             pos: 10000, 10000
        #             size: 20, 20
        # BoxLayout:
        #     orientation:'vertical'
        #     id: bullet{self.bullet_count + 1}
        #     canvas:
        #         Color:
        #             rgba: 0, 1, 0, 1
        #         Ellipse:
        #             pos: 10000, 10000
        #             size: 20, 20""",
        #     )
        # with open("slot/slot1_copy.kv", "w") as f:
        #     f.write(update_a)
        # self.bullet_count += 1
        return super().on_touch_down(touch)

    def bullet_move(self, dt):
        step = 100
        self.ids.bullet0.pos = (
            Vector(
                (self.click[0] - self.ids.player.pos[0]) / step,
                (self.click[1] - self.ids.player.pos[1]) / step,
            )
            + self.ids.bullet0.pos
        )
        if coliddes(
            (self.ids.bullet0.pos, self.ids.bullet0.size),
            (self.ids.enemy.pos, self.ids.enemy.size),
        ):
            self.ids.enemy.size = 0, 0
            self.ids.enemy.c = 0

    def respawn_enemy(self, dt):
        self.ids.enemy.c += 1
        print(self.ids.enemy.c)
        if self.ids.enemy.c == 5:
            self.ids.enemy.size = 100, 100

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
