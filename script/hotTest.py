import json
import subprocess
import time

"""
启动脉冲加热压力测试
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
    # 调用带有参数的命令
    process = subprocess.Popen(curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        print("请求成功")
        print(stdout.decode('utf-8'))  # 打印标准输出
    else:
        print(f"请求失败，返回码：{process.returncode}")
        print(stderr.decode('utf-8'))  # 打印标准错误输出


def start_hot(host, authorization):
    url = host + '/manager/api/hot/startHot'
    data_str = json.dumps({
        "no": 1,
        "postions": [
            {
                "chargeMagnification": 1,
                "dischargeMagnification": 1,
                "pos": 1
            }
        ],
        "subType": "MANUAL_JOB"
    })
    send_request(url=url, authorization=authorization, data=data_str)


def stop_hot(host, authorization):
    url = host + '/manager/api/hot/stoptHot'
    data_str = json.dumps({"chargerNo": 0})
    send_request(url=url, authorization=authorization, data=data_str)


def test_hot(host, authorization, timeSleep, times):
    for i in range(times):
        start_hot(host, authorization)
        time.sleep(timeSleep)
        stop_hot(host, authorization)
        time.sleep(5)


def main():
    host = 'http://172.0.10.18'
    authorization = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0Iiwic3ViIjoie1wiaWRcIjo0LFwidW5pb25JZFwiOm51bGwsXCJwbGF0Zm9ybVR5cGVcIjoxLFwicmVhbE5hbWVcIjpcIueuoeeQhuWRmFwiLFwiYWNjb3VudFwiOlwiR0xZXCIsXCJjbGllbnRJZFwiOm51bGwsXCJzb3VyY2VVc2VySWRcIjpudWxsLFwiYXZhdGFyXCI6bnVsbCxcInRlbmFudElkXCI6bnVsbCxcInRlbmFudEx2XCI6bnVsbCxcImRlcHRJZFwiOm51bGwsXCJyb2xlQ29kZXNcIjpudWxsLFwicm9sZUlkc1wiOm51bGwsXCJwZXJtc1wiOm51bGwsXCJtZW51c1wiOm51bGx9IiwiaWF0IjoxNzUyOTI5MDI3LCJleHAiOjE3NTMwMTU0Mjd9.3_8ugPn53RPpoJrClMcAiOrHdWzfAQJceX34Ga8HpGo'
    timeSleep = 90  # 启动至停止间隔
    times = 10000  # 循环次数
    test_hot(host, authorization, timeSleep, times)


if __name__ == '__main__':
    main()
