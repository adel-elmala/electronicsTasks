
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.anchorlayout import AnchorLayout

from kivy.uix.label import Label

import matplotlib.pyplot as plt
import  numpy as np

# plt.plot([1, 23,8, 2, 4])
x = np.arange(0, 5, 0.1)  
y = np.sin(x)  
plt.plot(x, y)
plt.ylabel('some numbers')

class MyApp(App):

    def build(self):
        layout = BoxLayout()
        # layout = FloatLayout()
        # layout = AnchorLayout(anchor_x='right', anchor_y='bottom')
        
        # Could get rid off the label and add a legend to the plot that can be dynamically updated // Too lazy to do it now 
        label = Label(text='Sensor Reading',pos=(50, 50))
        plot = FigureCanvasKivyAgg(plt.gcf())
        
        layout.add_widget(label)
        layout.add_widget(plot)
        
        return layout

if __name__ == '__main__':
    MyApp().run()
