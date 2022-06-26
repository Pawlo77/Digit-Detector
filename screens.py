from kivy.uix.screenmanager import Screen
from kivy.properties import BooleanProperty, ObjectProperty, ColorProperty

from settings import settings


class MyScreen():
    def __init__(self, **kwargs):
        self.settings = settings

class MainScreen(Screen, MyScreen):
    rubber = BooleanProperty(False)
    board = ObjectProperty(None)
    frame_color = ColorProperty("black")

