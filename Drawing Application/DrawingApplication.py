from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivymd.uix.chip import MDChip
from kivy.graphics import Canvas
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Ellipse, Line, Rectangle
from time import sleep
from threading import Timer
from kivy.graphics.scissor_instructions import ScissorPush,ScissorPop



class MyWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = (.1, .1, .1)
        self.draw = True
        self.erase = False
        self.cut = False
        self.list = []

    def on_touch_down(self, touch):
        with self.canvas:
            if self.erase is True:
                Color(*self.color)
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=30)

            elif self.cut is True:
                pass

            elif self.draw is True:
                Color(*self.color)
                touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):

        if self.draw is True or self.erase is True:
            touch.ud['line'].points += [touch.x, touch.y]

        if self.cut is True:
            dx = touch.x - touch.opos[0]
            dy = touch.y - touch.opos[1]
            coorList = []
            coorList.append(dx)
            coorList.append(dy)
            self.list.append(coorList)
            for index in self.list:
                print(index)


    def on_touch_up(self, touch):
        # Creating a small
        if self.cut is True:
            dx = touch.x - touch.opos[0]
            dy = touch.y - touch.opos[1]
            if abs(dx) > 32 and abs(dy) > 32:
                print(touch.opos[0])
                print(touch.opos[1])
                with self.canvas:
                    Color(.1, .1, .1)
                    self.Frame = Line(points= [touch.opos[0], touch.opos[1], touch.x, touch.opos[1], touch.x, touch.y, touch.opos[0], touch.y, touch.opos[0], touch.opos[1]], width= 1, dash_length = 4, dash_offset= 1)


    #Create a method to check on mouse pos
    def mouse_pos(self, window, pos):
        pass

    def startDraw(self):
        self.draw = True
        self.cut = False
        self.erase = False
        self.color = (.1, .1, .1)

    def eraseDraw(self):
        self.draw = False
        self.erase = True
        self.cut = False
        self.color = (1, 1, 1)

    def cutDraw(self):
        self.draw = False
        self.erase = False
        self.cut = True



class drawingApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "My Drawing Application"
        super().__init__(**kwargs)

    def build(self):
        self.root = Builder.load_file("drawing.kv")


if __name__ == "__main__":
    drawingApp().run()
