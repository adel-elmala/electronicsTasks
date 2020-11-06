import pyrebase
import matplotlib.pyplot as plt
import time
import numpy as np


configNew = {
    "apiKey": "AIzaSyBIFhbwdIXRf-TRlSvieuhw5VgnN4u9pp8",
    "authDomain": "esp32data-e59a5.firebaseio.com",
    "databaseURL": "https://esp32data-e59a5.firebaseio.com/",
    "projectId": "esp32data-e59a5",
    "storageBucket": "esp32data-e59a5.firebaseio.com",
}

firebase = pyrebase.initialize_app(configNew)


def get_data():
    db = firebase.database()
    data = db.child("readings").get()
    return(data.val())


def plot_data():
    plt.style.use('ggplot')
    plt.ion()
    y = []
    figure, ax = plt.subplots(figsize=(8, 6))
    line1, = ax.plot([], [], label='toto', ms=10,
                     color='red', marker='.', ls='')
    ax.set_ylim(0, +70)
    ax.set_xlim(0, 20)
    plt.title("Sensor Readings", fontsize=20)
    plt.xlabel("seconds", fontsize=14)
    plt.ylabel("Reading", fontsize=14)
    idx = 0
    while True:
        idx += 1
        ax.set_xlim(0, 5+idx)
        updated_y = get_data()
        y.append(updated_y)
        x = list(range(len(y)))
        time.sleep(0.5)
        print(updated_y)
        line1.set_data(x, y)
        # line1.set_ydata(y)

        figure.canvas.draw()

        figure.canvas.flush_events()
        time.sleep(0.1)


