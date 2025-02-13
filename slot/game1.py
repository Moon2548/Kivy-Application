from kivy.uix.widget import Widget
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.graphics import Ellipse, Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.vector import Vector
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.properties import StringProperty, ObjectProperty
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
    play_game = False
    my_source = StringProperty("")
    my_portal = StringProperty("")
    my_dummy = StringProperty("")
    imagess = "image/"
    slimes_s = [
        "slime/slime_02.png",
        "slime/slime_03.png",
        "slime/slime_04.png",
        "slime/slime_05.png",
    ]
    slimes_d = [
        "slime/slime_08.png",
        "slime/slime_09.png",
        "slime/slime_10.png",
        "slime/slime_11.png",
    ]
    slimes_a = [
        "slime/slime_13.png",
        "slime/slime_14.png",
        "slime/slime_15.png",
        "slime/slime_16.png",
    ]
    slimes_w = [
        "slime/slime_18.png",
        "slime/slime_19.png",
        "slime/slime_20.png",
        "slime/slime_21.png",
    ]
    portal = [
        "portal/0.png",
        "portal/1.png",
        "portal/2.png",
        "portal/3.png",
        "portal/4.png",
        "portal/5.png",
        "portal/6.png",
        "portal/7.png",
        "portal/8.png",
    ]
    dummy = [
        "dummy/0.png",
        "dummy/1.png",
        "dummy/2.png",
        "dummy/3.png",
    ]
    frame_slime = 0
    frame_portal = 0
    frame_dummy = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)
        self.pressed_keys = set()
        self.bullets = []
        self.mushrooms = []
        Clock.schedule_interval(self.update, 0)
        Clock.schedule_interval(self.bullet_move, 0)
        Clock.schedule_interval(self.clock_count, 1)
        Clock.schedule_interval(self.spawn_mushroom, 2)
        Clock.schedule_interval(self.move_mushrooms, 0)

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        self.pressed_keys.add(text)

    def _on_key_up(self, keyboard, keycode):
        text = keycode[1]
        if text in self.pressed_keys:
            self.pressed_keys.remove(text)

    def update(self, dt):
        step = 500 * dt

        if (
            coliddes(
                (self.ids.player.pos, self.ids.player.size),
                (self.ids.portal.pos, self.ids.portal.size),
            )
            == True
        ):
            self.ids.play.pos = (
                self.ids.portal.pos[0] + 100,
                self.ids.portal.pos[1] + 100,
            )
        else:
            self.ids.play.pos = (100000, 100000)

        if "w" in self.pressed_keys:
            self.ids.object.pos[1] -= step
            self.ids.dungeon.pos[1] -= step
            self.frame_slime += 0.1
            if self.frame_slime >= 4:
                self.frame_slime = 0
            self.my_source = self.imagess + self.slimes_w[int(self.frame_slime)]
        if "s" in self.pressed_keys:
            self.ids.object.pos[1] += step
            self.ids.dungeon.pos[1] += step
            self.frame_slime += 0.1
            if self.frame_slime >= 4:
                self.frame_slime = 0
            self.my_source = self.imagess + self.slimes_s[int(self.frame_slime)]
        if "a" in self.pressed_keys:
            self.ids.object.pos[0] += step
            self.ids.dungeon.pos[0] += step
            self.frame_slime += 0.1
            if self.frame_slime >= 4:
                self.frame_slime = 0
            self.my_source = self.imagess + self.slimes_a[int(self.frame_slime)]
        if "d" in self.pressed_keys:
            self.ids.object.pos[0] -= step
            self.ids.dungeon.pos[0] -= step
            self.frame_slime += 0.1
            if self.frame_slime >= 4:
                self.frame_slime = 0
            self.my_source = self.imagess + self.slimes_d[int(self.frame_slime)]

        self.frame_portal += 0.1
        if self.frame_portal >= 9:
            self.frame_portal = 0
        self.my_portal = self.imagess + self.portal[int(self.frame_portal)]

        self.frame_dummy += 0.1
        if self.frame_dummy >= 4:
            self.frame_dummy = 0
        self.my_dummy = self.imagess + self.dummy[int(self.frame_dummy)]

    def on_touch_down(self, touch):
        bullet = Widget(
            size=(20, 20),
            pos=(self.ids.player.pos[0] + 50, self.ids.player.pos[1] + 50),
        )
        with bullet.canvas:
            Color(0, 1, 0, 1)
            bullet.shape = Ellipse(pos=bullet.pos, size=bullet.size)
        self.add_widget(bullet)
        self.bullets.append(
            (
                bullet,
                Vector((touch.x - bullet.pos[0]) / 50, (touch.y - bullet.pos[1]) / 50),
            )
        )
        return super().on_touch_down(touch)

    def spawn_mushroom(self, dt):
        if self.play_game:
            mushroom = Widget(
                size=(100, 100),
                pos=(self.ids.dungeon.pos[0] + 50, self.ids.dungeon.pos[1] + 50),
            )
            with mushroom.canvas:
                Color(1, 1, 1, 1)
                mushroom.shape = Rectangle(
                    pos=mushroom.pos, size=mushroom.size, source="image/mushroom/1.png"
                )
            self.add_widget(mushroom)
            self.mushrooms.append(mushroom)

    def move_mushrooms(self, dt):
        player_pos = self.ids.player.pos
        speed = 2

        for mushroom in self.mushrooms:
            mushroom_pos = mushroom.pos
            direction = Vector(player_pos) - Vector(mushroom_pos)
            if direction.length() > 1:
                direction = direction.normalize() * speed
                mushroom.pos = Vector(mushroom.pos) + direction
                mushroom.shape.pos = mushroom.pos

    def bullet_move(self, dt):
        for bullet, velocity in self.bullets[:]:
            bullet.pos = Vector(*bullet.pos) + velocity
            bullet.shape.pos = bullet.pos
            if coliddes(
                (bullet.pos, bullet.size), (self.ids.dummy.pos, self.ids.dummy.size)
            ):
                self.remove_widget(bullet)
                self.bullets.remove((bullet, velocity))
                self.ids.dummy.hp -= 1
                if self.ids.dummy.hp <= 0:
                    self.ids.dummy.c = 0
                    self.ids.dummy.size = (0, 0)
                    self.ids.dummy.pos = (100000, 100000)
            for mushroom in self.mushrooms[:]:
                if coliddes(
                    (bullet.pos, bullet.size),
                    (mushroom.pos, mushroom.size),
                ):
                    self.remove_widget(bullet)
                    self.bullets.remove((bullet, velocity))
                    self.remove_widget(mushroom)
                    self.mushrooms.remove(mushroom)

    def clock_count(self, dt):
        self.ids.dummy.c += 1
        print(
            coliddes(
                (self.ids.player.pos, self.ids.player.size),
                (self.ids.portal.pos, self.ids.portal.size),
            )
        )
        if self.ids.dummy.c == 5:
            self.ids.dummy.size = (100, 100)
            self.ids.dummy.pos = self.ids.object.pos
            self.ids.dummy.hp = 5

    def start(self):
        self.play_game = True
        self.ids.object.pos = 100000, 1000000
        self.ids.dungeon.pos = 0, 0

    def close_play(self):
        App.get_running_app().stop()
        if os.path.exists("slot/slot1_copy.kv"):
            os.remove("slot/slot1_copy.kv")

    def open_menu(self):
        return True


class Game1(App):
    def build(self):
        return Play1()


if __name__ == "__main__":
    Game1().run()
