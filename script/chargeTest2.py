import concurrent.futures
import json
import requests
import time

"""
启动充电压力测试
windows环境
"""


def send_request(url, authorization, data):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': authorization
    }

    response = requests.request(url=url, method='POST', headers=headers, data=data)
    if response.status_code == 200:
        print("请求成功")
        print(response.text)
    else:
        print(f"请求失败，返回码：{response.status_code}")
        print(response.text)


def start_charge(host, authorization, campNoList):
    url = host + '/api/batteryCampManage/batteryCharge'
    data_str = json.dumps({"campNoList": campNoList, "chargeLimit": 1, "chargeType": 2, "socLimit": 100})
    send_request(url=url, authorization=authorization, data=data_str)


def stop_charge(host, authorization, campNoList):
    url = host + '/dcci/api/dcci/local/stopCharge'
    datas = []
    for position in campNoList:
        data_str = json.dumps({"flowNo": "1111111111", "position": position, "stopReason": 0, "subType": "MANUAL_JOB"})
        datas.append(data_str)

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(campNoList)) as executor:
        future_to_url = {executor.submit(send_request, url, authorization, data): data for data in datas}


def test_charge(host, authorization, campNoList, timeSleep, times):
    for i in range(times):
        start_charge(host, authorization, campNoList)
        time.sleep(timeSleep)
        stop_charge(host, authorization, campNoList)
        time.sleep(5)


def main():
    host = 'https://pdd-station-supercharge-test03.catles.com'
    authorization = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0Iiwic3ViIjoie1wiaWRcIjo0LFwidW5pb25JZFwiOm51bGwsXCJwbGF0Zm9ybVR5cGVcIjoxLFwicmVhbE5hbWVcIjpcIueuoeeQhuWRmFwiLFwiYWNjb3VudFwiOlwiR0xZXCIsXCJjbGllbnRJZFwiOm51bGwsXCJzb3VyY2VVc2VySWRcIjpudWxsLFwiYXZhdGFyXCI6bnVsbCxcInRlbmFudElkXCI6bnVsbCxcInRlbmFudEx2XCI6bnVsbCxcImRlcHRJZFwiOm51bGwsXCJyb2xlQ29kZXNcIjpudWxsLFwicm9sZUlkc1wiOm51bGwsXCJwZXJtc1wiOm51bGwsXCJtZW51c1wiOm51bGx9IiwiaWF0IjoxNzQ5NjMyNDkxLCJleHAiOjE3NDk3MTg4OTF9.Jarp23HLgpzVVxPPvwiX4r94IJRXRpieh60Bk5AkW9A'
    campNoList = [7]  # 充电机
    timeSleep = 90  # 启动充电至停止充电间隔
    times = 10000  # 循环次数
    test_charge(host, authorization, campNoList, timeSleep, times)


if __name__ == '__main__':
    main()
