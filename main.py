from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import ObjectProperty, NumericProperty
#from kivy.graphics import Color
import math

class SSObject(Widget):
    pos_x = NumericProperty(0)
    pos_y = NumericProperty(0)
    #pos = ReferenceListProperty(pos_x, pos_y)
    angle = NumericProperty(0)
    color = (1,1,1)
    
    def move(self):
        self.color = (0,0,1)
        self.angle += self.rot_speed
        if self.angle >= 360:
            self.angle = 0
        x = math.cos(math.radians(self.angle))*self.radius
        y = math.sin(math.radians(self.angle))*self.radius
        self.pos = (self.pos_x+x, self.pos_y+y)
        
               

class SolarSystem(Widget):
    sun = ObjectProperty(None)
    earth = ObjectProperty(None)
    moon = ObjectProperty(None)
    venus = ObjectProperty(None)
    mercury = ObjectProperty(None)
    
    def update(self, dt):
        self.earth.move()
        self.moon.move()
        self.venus.move()
        self.mercury.move()
    
class SolarSystemApp(App):
    def build(self):
        ourSS = SolarSystem()
        Clock.schedule_interval(ourSS.update, 1.0/60)
        return ourSS

if __name__=='__main__':
    SolarSystemApp().run() 
