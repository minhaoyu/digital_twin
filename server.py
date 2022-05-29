import os
import sys
import time
from flask import Flask, jsonify
from threading import Thread
import csv

app = Flask(__name__)


def load_data(index):
    datas = []
    for each in os.listdir(data_dirs[index]):
        path = os.path.join(data_dirs[index], each)
        # print("path",path)
        with open(path, "r") as file:
            data = csv.reader(file)
            next(data)
            datas.extend(list(data))

    while True:
        for each in datas:
            # print(each)
            result[index] = process_data(each,index)
            if index == 0:
                print("data updated，from battery_reading thread")
                # battery = result[index]
                # statue_dic['battery'] = 'true'
            elif index == 1:
                print("data updated，from Bldng_049_reading thread")
                # Bldng049 = result[index]
                # statue_dic['Bldng049'] = 'true'
            elif index == 2:
                print("data updated，from Bldng_078_reading thread")
                # Bldng078 = result[index]
                # statue_dic['Bldng078'] = 'true'
            print(result[index])
            time.sleep(60)


def process_data(data,index):
    # processing data here
    # print("coming")
    # while True:
    #     if statue_dic['battery'] == 'true':
    #         print(battery)
    #         statue_dic['battery'] = 'false'
    return data


@app.route("/")
def index():
    return jsonify(result)


if __name__ == "__main__":
    # global battery
    # global Bldng049
    # global Bldng078
    # battery = []
    # Bldng049 = []
    # Bldng078 = []
    # statue_dic = {'battery': 'false', 'Bldng049': 'false', 'Bldng078': 'false'}
    print("server is loading data！")
    root = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(root, "data")

    data_dirs = [os.path.join(data_dir, each) for each in os.listdir(data_dir)]

    result = [0] * len(data_dirs)

    threads = []

    for i in range(len(data_dirs)):
        thread = Thread(target=load_data, args=(i,))
        thread.start()
        threads.append(thread)


    print("Loading completed！")
    print("server started！")
    app.run(
        "0.0.0.0",
        808,
        debug=False
    )
