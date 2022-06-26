import kivy
kivy.require("2.1.0")

from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '800')


from kivy.uix.screenmanager import ScreenManager
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

from screens import *
from widgets import *


Builder.load_file("style.kv")


class PaintApp(App):
    def build(self):
        sc = ScreenManager()

        sc.add_widget(MainScreen(name="main"))
        
        return sc


if __name__ == '__main__':
    PaintApp().run()