import requests
from concurrent.futures import ThreadPoolExecutor

"""
接口并发调用
"""

# 定义接口URL
url = "https://pdd-station-supercharge-test.catles.com/fault/api/fault/feign/handle/recover"

# 定义请求数据
data = {
    "deviceCode": "BSS-CLOUD",
    "deviceNo": 1,
    "faultCode": "18"
}
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0Iiwic3ViIjoie1wiaWRcIjo0LFwidW5pb25JZFwiOm51bGwsXCJwbGF0Zm9ybVR5cGVcIjoxLFwicmVhbE5hbWVcIjpcIueuoeeQhuWRmFwiLFwiYWNjb3VudFwiOlwiR0xZXCIsXCJjbGllbnRJZFwiOm51bGwsXCJzb3VyY2VVc2VySWRcIjpudWxsLFwiYXZhdGFyXCI6bnVsbCxcInRlbmFudElkXCI6bnVsbCxcInRlbmFudEx2XCI6bnVsbCxcImRlcHRJZFwiOm51bGwsXCJyb2xlQ29kZXNcIjpudWxsLFwicm9sZUlkc1wiOm51bGwsXCJwZXJtc1wiOm51bGwsXCJtZW51c1wiOm51bGx9IiwiaWF0IjoxNzQ0NjAxNjY2LCJleHAiOjE3NDQ2MDIwMjZ9.KyvO3BE1T8rp5sRm-NltvQU3oEIymHH4082VzWpINIU'
}


# 定义发送请求的函数
def send_request():
    response = requests.request(url=url, method='POST', headers=headers, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")


# 使用ThreadPoolExecutor并发调用接口两次
with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(send_request) for _ in range(4)]

# 等待所有任务完成
for future in futures:
    future.result()
