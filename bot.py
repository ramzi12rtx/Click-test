import requests
import time
from datetime import datetime

url = "https://thenanobutton.com/tgElKw"

headers = {
    "User-Agent": "Mozilla/5.0"
}

count = 0

while True:
    try:
        requests.get(url, headers=headers)
        count += 1
        print(f"Click {count} at {datetime.now()}")
    except:
        print("Connection error")
    
    time.sleep(1)  # ضغطه واحدة كل ثانية
