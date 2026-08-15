import concurrent.futures
import json
import subprocess
import time

"""
启动充电压力测试
linux环境
"""

def send_request(url, authorization, data):
    curl_command = [
        'curl',
        url,
        '-X', 'POST',
        '-H', 'content-type: application/json',
        '-H', f'Authorization: {authorization}',
        '--data-raw', data,
        '--compressed'
    ]
    process = subprocess.Popen(curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        print("请求成功")
        print(stdout.decode('utf-8'))
        return stdout.decode('utf-8')
    else:
        print(f"请求失败，返回码：{process.returncode}")
        print(stderr.decode('utf-8'))


def get_chargeStatus(host, authorization, campNoList):
    chargeStatusList = []
    for position in campNoList:
        url = host + f'/dcci/api/chargerQuery/feign/getGunInfoByPosition?position={position}'
        res = json.loads(send_request(url=url, authorization=authorization, data=''))['data']['chargeStatus']
        chargeStatusList.append(res)
    return chargeStatusList


def charge(host, authorization, campNoList, timeSleep):
    # 启动充电
    url = host + '/api/batteryCampManage/batteryCharge'
    data_str = json.dumps({"campNoList": campNoList, "chargeLimit": 1, "chargeType": 2, "socLimit": 100})
    send_request(url=url, authorization=authorization, data=data_str)

    time.sleep(timeSleep)  # 充电时间

    # 获取充电状态
    chargeStatus = get_chargeStatus(host, authorization, campNoList)

    # 停止充电
    datas = []
    for campNo in campNoList:
        index = campNo - 1
        if chargeStatus[index] not in [1, 2, 3]:
            url = host + '/dcci/api/dcci/local/stopCharge'
            data_str = json.dumps({"flowNo": "1111111111", "position": campNo, "stopReason": 0, "subType": "MANUAL_JOB"})
            datas.append(data_str)
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(campNoList)) as executor:
        future_to_url = {executor.submit(send_request, url, authorization, data): data for data in datas}
    time.sleep(5)


def main():
    host = 'https://pdd-station-supercharge-test03.catles.com'
    authorization = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0Iiwic3ViIjoie1wiaWRcIjo0LFwidW5pb25JZFwiOm51bGwsXCJwbGF0Zm9ybVR5cGVcIjoxLFwicmVhbE5hbWVcIjpcIueuoeeQhuWRmFwiLFwiYWNjb3VudFwiOlwiR0xZXCIsXCJjbGllbnRJZFwiOm51bGwsXCJzb3VyY2VVc2VySWRcIjpudWxsLFwiYXZhdGFyXCI6bnVsbCxcInRlbmFudElkXCI6bnVsbCxcInRlbmFudEx2XCI6bnVsbCxcImRlcHRJZFwiOm51bGwsXCJyb2xlQ29kZXNcIjpudWxsLFwicm9sZUlkc1wiOm51bGwsXCJwZXJtc1wiOm51bGwsXCJtZW51c1wiOm51bGx9IiwiaWF0IjoxNzQ4OTQyMDIwLCJleHAiOjE3NDkwMjg0MjB9.oGYnlDqSyRpMVINzCquDKCgE1xbLP8BVTXqXqkPyHeQ'
    campNoList = [3, 4, 5]  # 充电机
    timeSleep = 10  # 启动充电至停止充电间隔
    times = 5  # 循环次数
    for i in range(times):
        charge(host, authorization, campNoList, timeSleep)


if __name__ == '__main__':
    main()
