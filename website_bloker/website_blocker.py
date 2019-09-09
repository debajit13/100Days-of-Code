import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working Hour")

    else:
        print("Fun Hour")
    time.sleep(5)
