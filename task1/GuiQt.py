import os
import sys
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from PySide2 import QtCore, QtWidgets, QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide2.QtWidgets import QWidget, QPushButton, QLabel, QMessageBox, QHBoxLayout, QVBoxLayout, QGridLayout
matplotlib.use('Qt5Agg')
plt.style.use('ggplot')
from api import configNew ,firebase, get_data
import time

CONNECTION =True


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()
        self.setWindowTitle("Sensor Live Plotting")
        self.msg = QMessageBox()
        self.setIconSize(QtCore.QSize(500, 500))
        self.main_widget = QtWidgets.QWidget(self)
        self.resize(900, 600)
        self.Stylize()
        self.InitLineEdit()
        self.InitFig()
        self.InitButton()
        self.InitLayouts()
        self.setCentralWidget(self.main_widget)
        self.show()


    def InitLayouts(self):

        self.layout = QtWidgets.QGridLayout(self.main_widget)
        self.layout.addWidget(self.Title, 0, 0)
        self.layout.addWidget(self.PlotButton, 0, 1)
        self.layout.addWidget( self.stopButton, 0, 2)
        self.layout.addWidget(self.canvas, 1, 0,1,3)
        self.layout.setHorizontalSpacing(3)
        self.layout.setMargin(20)

    def InitLineEdit(self):
            self.Title = QLabel(self)
            self.Title.setMargin(10)
            self.Title.setText("Sensor Plotting")
            font = self.Title.font()      # lineedit current font
            font.setPointSize(15)               # change it's size
            font.setBold(True)
            self.Title.setFont(font)

    def InitFig(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setStyleSheet(
            "background-color: black;  border: 15px solid black; border-radius: 1px")
        self.canvas.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                  QtWidgets.QSizePolicy.Expanding)
        self.canvas.updateGeometry()

    def InitButton(self):
        self.PlotButton = QPushButton("Plot", self)
        self.stopButton = QPushButton("Stop", self)
         
        self.PlotButton.setShortcut("Ctrl+P")
        self.PlotButton.setToolTip("CTRL+P")
        self.PlotButton.clicked.connect(self.plot_data) 
        self.PlotButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stopButton.clicked.connect(self.stop_plot)
    
    def stop_plot(self):
        CONNECTION = False

    def connection_stat(self):
        return CONNECTION



    def Stylize(self):
        self.main_widget.setStyleSheet("QPushButton{\n"

                                       "    background:linear-gradient(to bottom, #ededed 5%, #bab1ba 100%);\n"
                                       "    background-color:#ededed;\n"
                                       "    border-radius:15px;\n"
                                       "    border:2px solid #d6bcd6;\n"
                                       "    color:#db2525;\n"
                                       "    font-family:segoe print;\n"
                                       "    font-size:17px;\n"
                                       "    padding:7px 25px;\n"
                                       "    text-decoration:none;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "        background:linear-gradient(to bottom, #e371e3 5%, #ededed 100%);\n"
                                       "    background-color:#bab1bf;\n"
                                       "}\n"
                                       "QPushButton:pressed{\n"
                                       "    position:absolute;\n"
                                       "    top:-5px;\n"
                                       "    border-style: ridge;\n"
                                       "}\n"
                                       "")

    def plot_data(self):
        CONNECTION=True
        plt.ion()
        y = []
        line1, = self.ax.plot([], [], label='toto', ms=10,
                        color='red', marker='.', ls='')
        self.ax.set_ylim(0, +70)
        self.ax.set_xlim(0, 20)
        self.ax.set_title("Sensor Readings", fontsize=20)
        self.ax.set_xlabel("seconds", fontsize=14)
        self.ax.set_ylabel("Reading", fontsize=14)
        idx = 0
        while self.connection_stat()==True:
            idx += 1
            self.ax.set_xlim(0, 5+idx)
            updated_y = get_data()
            y.append(updated_y)
            x = list(range(len(y)))
            time.sleep(0.5)
            print(updated_y)
            line1.set_data(x, y)
            self.fig.canvas.draw()

            self.fig.canvas.flush_events()
            time.sleep(0.1)


if __name__ == '__main__':

    # To load the source Code absolute directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.setStyleSheet("background-color: gray;")
    w.show()
    app.exec_()