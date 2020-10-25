# import kivy
# kivy.require('1.0.6') # replace with your current kivy version !

# from kivy.app import App
# from kivy.uix.label import Label


# class MyApp(App):

#     def build(self):
#         return Label(text='Hello world')


# if __name__ == '__main__':
#     MyApp().run()

# ================================

from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import matplotlib.pyplot as plt

plt.plot([1, 23, 2, 4])
plt.ylabel('some numbers')

class MyApp(App):

    def build(self):
        box = BoxLayout()
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        return box

MyApp().run()