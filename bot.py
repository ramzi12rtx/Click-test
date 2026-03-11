import requests
import time

url = "https://thenanobutton.com"

headers = {
    "User-Agent": "Mozilla/5.0"
}

count = 0

while True:
    try:
        requests.get(url, headers=headers)
        count += 1
        print("click:", count)
    except:
        print("error")

    time.sleep(1)
