import requests
from time import sleep

up = []

while True:
    try:
        datas = requests.get("http://localhost:808").json()
        if datas == up:
            continue

        print("data has been updated！")
        for each in datas:
            print(each)
        up = datas
    except:
        pass
    finally:
        sleep(1)