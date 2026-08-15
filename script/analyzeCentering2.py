import json


def read(resource):
    readLines = []
    with open(resource, 'r', encoding='utf-8') as file:
        for line in file:
            readLines.append(line.strip())
    return readLines


def handleData(resource, result):
    readLines = read(resource)
    with open(result, "w", encoding="utf-8") as file:
        for line in readLines:
            if "工控机" in line:
                print(line)
                name = line.split("-")[0]
                file.write(f"\r站名：{name},")
            elif "code" in line:
                json_data = line.split("}", 1)[1].split("%", 1)[0]
                # 解析JSON数据
                data = json.loads(json_data)
                # 提取角度
                try:

                    angle_camera1 = data['step2_camera1']['data'][0]['angle']
                    if angle_camera1 > 40 and angle_camera1 < 50:
                        angle_camera1_flag = "符合"

                    elif angle_camera1 > 130 and angle_camera1 < 140:
                        angle_camera1_flag = "符合"
                    else:
                        angle_camera1_flag = "不符合"
                except:
                    angle_camera1_flag = "空"
                    angle_camera1 = "空"
                file.write(f"摄像头1角度：{angle_camera1},是否符合：{angle_camera1_flag},")

                try:
                    angle_camera2 = data['step3_camera2']['data'][0]['angle']
                    if angle_camera2 > 40 and angle_camera2 < 50:
                        angle_camera2_flag = "符合"
                    elif angle_camera2 > 130 and angle_camera2 < 140:
                        angle_camera2_flag = "符合"
                    else:
                        angle_camera2_flag = "不符合"
                except:
                    angle_camera2_flag = "空"
                    angle_camera2 = "空"
                file.write(f"摄像头2角度：{angle_camera2},是否符合：{angle_camera2_flag},")
            elif "【车辆朝向识别】摄像头[1]" in line:
                direction1 = line.split("摄像头[1]")[1].split("%", 1)[0].split(",result")[0].strip()
                file.write(f"摄像头1车辆朝向：{direction1},")
            elif "【车辆朝向识别】摄像头[2]" in line:
                direction2 = line.split("摄像头[2]")[1].split("%", 1)[0].split(",result")[0].strip()
                file.write(f"摄像头2车辆朝向：{direction2},")


if __name__ == '__main__':
    resource = "上海云南北京吉林.log"
    result = "上海云南北京吉林result.log"
    handleData(resource, result)
