from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.widget import Widget
from kivy.properties import ColorProperty, StringProperty
from kivy.uix.popup import Popup

from io import BytesIO

from settings import settings
from processing import predictor


class MyPopup(Popup):
    text = StringProperty("")

    def __init__(self, text, **kwargs):
        super(MyPopup, self).__init__(**kwargs)
        self.text = text


class Board(Widget):
    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            if settings.rubber:
                color = [255, 255, 255]
                d = settings.rubber_size
            else:
                color = settings.color
                d = settings.paint_size

            with self.canvas:
                Color(*color)
                Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
                touch.ud["line"] = Line(points=(touch.x, touch.y), width=d)
    
    def on_touch_move(self, touch):
        if self.collide_point(touch.x, touch.y):
            touch.ud["line"].points += [touch.x, touch.y]

    def preprocess(self):    
        stream = BytesIO()  
        img = self.export_as_image()
        img.save(stream, fmt="png")

        res = predictor.predict(stream)
        
        if res == "Wrong data provided":
            MyPopup(title="Unable to detect.", text=res).open()
        else:
            MyPopup(title="Result:", text=res).open()


class ColorBar(GridLayout):
    def __init__(self, **kwargs):
        super(ColorBar, self).__init__(**kwargs)

        self.rows = 1
        opt = sorted([
            "aqua",
            "blue",
            "brown", 
            "black",
            "darkgrey",
            "gold",
            "green",
            "greenyellow",
            "hotpink",
            "lawngreen",
            "yellow",
            "white",
            "violet",
            "tomato",
            "teal",
            "skyblue",
            "silver",
            "sienna",
            "red", 
            "purple",
            "pink",
            "plum",
            "orange",
            "olive",
            "navy",
            "magenta",
            "lime",
        ])
        self.cols = len(opt)

        for color in opt:
            self.add_widget(ColorOption(color))


class ColorOption(Widget):
    choose_color = ColorProperty("black")

    def __init__(self, color, **kwargs):
        super(ColorOption, self).__init__(**kwargs)

        self.choose_color = color
        if color == settings.default_color:
            settings.color = self.choose_color
    
    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            settings.color = self.choose_color
