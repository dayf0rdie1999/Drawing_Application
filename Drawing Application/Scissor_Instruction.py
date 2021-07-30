import kivy
from kivy.app import App
from kivy.uix.widget import  Widget
from kivy.graphics.scissor_instructions import ScissorPush, ScissorPop, ScissorStack
from kivy.graphics import Ellipse, Color
from kivy.lang import Builder



class myWidget(Widget):

    def on_touch_down(self, touch):
        with self.canvas.after:
            # If our widget is inside another widget that modified the coordinates
            # spacing (such as ScrollView) we will want to convert to Window coords
            x, y = self.to_window(*self.pos)
            width, height = self.size
            # We must convert from the possible float values provided by kivy
            # widgets to an integer screenspace, in python3 round returns an int so
            # the int cast will be unnecessary.
            ScissorPush(x=int(round(x)), y=int(round(y)),
                        width=int(round(width)), height=int(round(height)))
            Color(rgba=(1., 0., 0., .5))
            Ellipse(size=(width* 2., height *2.),
                    pos=self.center)
            ScissorPop()


class testApp(App):
    def build(self):
        return myWidget()


if __name__== "__main__":
    testApp().run()