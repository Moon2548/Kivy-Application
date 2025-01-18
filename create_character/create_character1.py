from kivy.uix.widget import Widget
from kivy.app import App
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.properties import StringProperty

Window.maximize()


class CreateCharacter1(Widget):
    my_source = StringProperty("image/slime_test0.png")
    count = 0
    a = "image/"
    b = ["slime_test0.png", "slime_test1.png", "slime_test2.png"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Clock.schedule_interval(self.ani_slime, 0.1)

    def ani_slime(self, dt):
        self.count += 1
        if self.count >= len(self.b):
            self.count = 0
        self.my_source = self.a + self.b[self.count]

    def animate_slime(self, widget, *args):
        animate = Animation(pos=(0, 0), duration=1)
        animate.start(widget)

    def select_slime(self):
        self.ids.slime.pos = -10000, -10000
        self.ids.tribe.pos = -10000, -10000
        self.ids.role_select.pos = Window.width / 2, 0
        with open("slot/slot1.kv", "r") as f:
            tribe = f.read()
        update_tribe = tribe.replace("#tribe: -", "#tribe: slime")
        with open("slot/slot1.kv", "w") as f:
            f.write(update_tribe)

    def animate_ranger(self, widget, *args):
        animate = Animation(pos=(0, 0), duration=1)
        animate.start(widget)

    def select_ranger(self):
        with open("slot/slot1.kv", "r") as f:
            tribe = f.read()
        update_tribe = tribe.replace("#role: -", "#role: ranger")
        with open("slot/slot1.kv", "w") as f:
            f.write(update_tribe)
        with open("slot/slot1.kv", "r") as f:
            start = f.read()
            update_start = start.replace("#status: free slot", "#status: use slot")
        with open("slot/slot1.kv", "w") as f:
            f.write(update_start)

    def close_create(self):
        App.get_running_app().stop()

    def open_menu(self):
        return True


class CreateCharacterRun1(App):
    def build(self):
        return CreateCharacter1()


if __name__ == "__main__":
    CreateCharacterRun1().run()
