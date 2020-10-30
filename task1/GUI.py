from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from threading import Thread
from kivy.uix.button import Button
from matplotlib.figure import Figure
import time
import matplotlib.pyplot as plt
import pyrebase
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.app import App
from api import configNew, firebase, get_data, plot_data
import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')


class MyApp(App):

    def plot_data(self):

        self.y = []
        self.line1, = self.ax.plot([], [], label='toto', ms=10,
                                   color='red', marker='.', ls='-')

        self.idx = 0
        loop_thread = Thread(target=self.data_flow)
        loop_thread.daemon = True
        loop_thread.start()
        Clock.schedule_interval(self.data_flow, 1)

    def data_flow(self, dt):
        self.idx += 1
        updated_y = get_data()
        self.y.append(updated_y)
        x = list(range(len(self.y)))
        time.sleep(1)
        print(updated_y)

        self.line1.set_data(x, self.y)
        self.Figure.canvas.draw()
        self.ax.set_xlim(0, self.idx+10)
        self.Figure.canvas.flush_events()

        time.sleep(0.1)

    def build(self):
        layout = GridLayout(rows=2, spacing=[16, 10], padding=[10, 10])
        button = Button(text='Plot Live Data', font_size=14, color="red", background_color=[
                        200, 100, 137, 0.8], size_hint=(.15, .25), border=[20, 20, 20, 20])
        plt.style.use('dark_background')
        plt.ion()
        self.Figure = Figure(figsize=(12, 9))
        self.Figure.set_tight_layout(True)
        self.ax = self.Figure.add_subplot(111)
        self.ax.set_ylim(0, +70)
        self.ax.set_xlim(0, 20)
        self.ax.set_xlabel("Seconds", fontsize=10)
        self.ax.set_ylabel("Reading", fontsize=10)
        self.canvas = FigureCanvasKivyAgg(self.Figure)
        button.bind(on_press=self.callback)

        layout.add_widget(button)
        layout.add_widget(self.canvas)
        data_thread = Thread(target=get_data)
        data_thread.daemon = True
        data_thread.start()

        return layout

    def callback(self, value):
        print("pressed")
        self.plot_data()


if __name__ == '__main__':

    MyApp().run()
