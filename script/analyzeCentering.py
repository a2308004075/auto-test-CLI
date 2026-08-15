import json
import subprocess
import sys
import time
import pandas as pd


def curl(url, headers=None, data=None):
    if data:
        curl_command = [
                           "curl", url
                       ] + headers + list(data)
    else:
        curl_command = ["curl", url]
    result = subprocess.run(curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, timeout=5)
    return result.stdout


def analyzeCenteringPost(IP):
    url = f"http://{IP}:6015/camera/api/video/analyzeCentering"
    headers = [
        "-H", "Content-Type: application/json",
        "-H", "Postman-Token: 29af74ce-43e2-4835-acdf-4a4049f48dcb",
        "-H", "cache-control: no-cache"
    ]
    data = "-d", "{\"msgId\":\"angle\",\"cameraSubTypeEnum\":\"MANUAL_JOB\"}"
    return curl(url, headers, data)


def triggerAnalyzeGet(IP):
    url = f"http://{IP}:6015/scs-arithmetic/api/trigger_analyze"
    return curl(url)


def assessAngle(angle):
    if angle > 40 and angle < 50:
        angle_flag = "符合"
    elif angle > 130 and angle < 140:
        angle_flag = "符合"
    else:
        angle_flag = "不符合"
    return angle_flag


def run(ip):
    try:
        analyzeCentering_result = analyzeCenteringPost(ip)
        analyzeCentering_result = json.loads(analyzeCentering_result)
        analyzeCentering_code = analyzeCentering_result["code"]
    except Exception:
        analyzeCentering_code = 0

    if analyzeCentering_code == 200:
        time.sleep(2)
        try:
            triggerAnalyze_result = triggerAnalyzeGet(ip)
            triggerAnalyze_result = json.loads(triggerAnalyze_result)
        except Exception:
            triggerAnalyze_result = {}

        try:
            angle_camera1 = triggerAnalyze_result["step2_camera1"]["data"][0]['angle']
            angle_camera1_flag = assessAngle(angle_camera1)
        except:
            angle_camera1 = "angle_camera1获取不到"
            angle_camera1_flag = "angle_camera1获取不到"
        try:
            angle_camera2 = triggerAnalyze_result["step3_camera2"]["data"][0]['angle']
            angle_camera2_flag = assessAngle(angle_camera2)
        except:
            angle_camera2 = "angle_camera2获取不到"
            angle_camera2_flag = "angle_camera2获取不到"
    else:
        angle_camera1 = "analyzeCentering调用失败"
        angle_camera1_flag = "analyzeCentering调用失败"
        angle_camera2 = "analyzeCentering调用失败"
        angle_camera2_flag = "analyzeCentering调用失败"
    return angle_camera1, angle_camera1_flag, angle_camera2, angle_camera2_flag


def allStation(resource_path, result_path):
    df = pd.read_excel(resource_path)
    column_a = df.iloc[:, 0]
    column_b = df.iloc[:, 1]
    combined_list = list(zip(column_a, column_b))

    with open(result_path, "w", encoding="utf-8") as file:
        for ip, station in combined_list:
            angle_camera1, angle_camera1_flag, angle_camera2, angle_camera2_flag = run(ip)
            file.write(f"\nIP：{ip},站名：{station},"
                       f"摄像头1角度：{angle_camera1},摄像头1角度是否符合：{angle_camera1_flag},"
                       f"摄像头2角度：{angle_camera2},摄像头2角度是否符合：{angle_camera2_flag}")
            file.flush()
            print(f"{ip}-{station}")


if __name__ == '__main__':
    resource_path = sys.argv[1]
    result_path = sys.argv[2]
    allStation(resource_path, result_path)
