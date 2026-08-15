from datetime import datetime

import requests
from concurrent.futures import ThreadPoolExecutor

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0Iiwic3ViIjoie1wiaWRcIjo0LFwidW5pb25JZFwiOm51bGwsXCJwbGF0Zm9ybVR5cGVcIjoxLFwicmVhbE5hbWVcIjpcIueuoeeQhuWRmFwiLFwiYWNjb3VudFwiOlwiR0xZXCIsXCJjbGllbnRJZFwiOm51bGwsXCJzb3VyY2VVc2VySWRcIjpudWxsLFwiYXZhdGFyXCI6bnVsbCxcInRlbmFudElkXCI6bnVsbCxcInRlbmFudEx2XCI6bnVsbCxcImRlcHRJZFwiOm51bGwsXCJyb2xlQ29kZXNcIjpudWxsLFwicm9sZUlkc1wiOm51bGwsXCJwZXJtc1wiOm51bGwsXCJtZW51c1wiOm51bGx9IiwiaWF0IjoxNzQ0NjAxNjY2LCJleHAiOjE3NDQ2MDIwMjZ9.KyvO3BE1T8rp5sRm-NltvQU3oEIymHH4082VzWpINIU'
}


def send_request_1():
    url = "https://pdd-station-supercharge-test.catles.com/battery/api/batteryControl/clearFault"
    data = {
        "commandSubType": "AUTO",
        "positionList": [1],
        "requestEnum": "ALL"
    }
    response = requests.request(url=url, method='POST', headers=headers, json=data)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Status Code: {current_time}-{response.status_code}")
    print(f"Response: {current_time}-{response.json()}")


def send_request_2():
    url = "https://pdd-station-supercharge-test.catles.com/battery/api/batteryControl/clearFault"
    data = {
        "commandSubType": "MANUAL",
        "positionList": [2],
        "requestEnum": "ALL"
    }
    response = requests.request(url=url, method='POST', headers=headers, json=data)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Status Code: {current_time}-{response.status_code}")
    print(f"Response: {current_time}-{response.json()}")


# 使用ThreadPoolExecutor并发调用接口两次
with ThreadPoolExecutor(max_workers=2) as executor:
    futures = [
        executor.submit(send_request_1),
        executor.submit(send_request_2)
    ]

# 等待所有任务完成
for future in futures:
    future.result()
