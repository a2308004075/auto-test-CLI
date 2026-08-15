from datetime import datetime
import pandas as pd

"""
手动连接-三代蓝牙数据整理
"""


# ===============Utils===============
def read_file(path):
    readLines = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            readLines.append(line.strip())
    return readLines


def fitter_keyword(keyword, readlines):
    filterList = []
    for line in readlines:
        if keyword in line:
            filterList.append(line.strip())
    return filterList


def strpTime(timeStr: str):
    """
    字符串类型时间转dateTime类型时间

    param timeStr：字符串类型时间

    return dateTime：datetime类型时间
    """
    if "." not in timeStr:
        timeStr = timeStr + ".000"
    dateTime = datetime.strptime(timeStr, "%Y-%m-%d %H:%M:%S.%f")
    return dateTime


def getTime(datagram):
    timeStr = datagram.split(" - ")[0]
    return timeStr


def getBody(datagram):
    body = datagram.split("b:")[1]
    return body


def FilterTime(startTimeStr, endTimeStr, filterList):
    timeBodyList = []
    startTime = strpTime(startTimeStr)
    endTimeStr = strpTime(endTimeStr)
    for datagram in filterList:
        timeStr = getTime(datagram)

        time = strpTime(timeStr)
        if startTime < time and time < endTimeStr:
            timeBodyList.append(datagram)
    return timeBodyList


def intervalTime(startDateTime, endDateTime):
    """
    计算时间间隔（秒）

    param startDateTime：datetime格式时间

    param endDateTime：datetime格式时间

    return intervalSeconds：时间间隔（s）
    """
    # intervalSeconds = (endDateTime - startDateTime).seconds
    intervalSeconds = -1
    if startDateTime and endDateTime:
        intervalSeconds = round(
            (endDateTime - startDateTime).seconds + ((endDateTime - startDateTime).microseconds) / 1000000, 3)
    return intervalSeconds


def list_remove(l, key):
    new_list = []
    for i in l:
        if i != key:
            new_list.append(i)
    return new_list


def list_save(l, key):
    new_list = []
    for i in l:
        if i == key:
            new_list.append(i)
    return new_list


def average(l: list):
    return round((sum(l) / len(l)), 3)


def in_custom_display(data):
    """
    站内信号强度评级
    """
    # 调整bins以覆盖所有区间
    bins = [-float('inf'), -60, -55, float('inf')]

    # 使用pd.cut将数据分到不同的区间
    categories = pd.cut(data, bins=bins, right=False, include_lowest=True)

    # 计算每个区间的数量
    counts = categories.value_counts().sort_index()

    # 计算每个区间的占比
    percentage = counts / len(data) * 100

    percentList = []
    for interval, count in counts.items():
        percent = percentage[interval]
        percentList.append(round(percent, 2))

    return percentList


def out_custom_display(data):
    """
    站外信号强度评级
    """
    # 使用pd.cut将数据分到不同的区间
    bins = [-float('inf'), -75, -65, float('inf')]
    categories = pd.cut(data, bins=bins, right=False, include_lowest=True)

    # 计算每个区间的数量
    counts = categories.value_counts().sort_index()

    # 计算每个区间的占比
    percentage = counts / len(data) * 100

    percentList = []
    for interval, count in counts.items():
        percent = percentage[interval]
        percentList.append(round(percent, 2))

    return percentList


# ===============蓝牙信息===============
# 下控蓝牙连接时间
def getControlConnectTime(readlines):
    controlConnectTimeList = []
    send0405 = fitter_keyword("[4, 2]", readlines)
    if send0405 == []:
        result = None
    else:
        for datagram in send0405:
            body = eval(datagram.split("b:")[1])
            if body[0] == 2 or body[0] == 1 or body[0] == 3:
                controlConnectTime = getTime(datagram)
                controlConnectTimeList.append(controlConnectTime)
        result = controlConnectTimeList[0]
    return result


# 下控蓝牙断开时间
def getControlDisconnectTime(readlines):
    controlDisconnectTimeList = []
    send0403 = fitter_keyword("[4, 3]", readlines)
    if send0403 == []:
        result = None
    else:
        for datagram in send0403:
            body = eval(datagram.split("b:")[1])
            if body[0] == 1:
                controlDisconnectTime = getTime(datagram)
                controlDisconnectTimeList.append(controlDisconnectTime)
        result = controlDisconnectTimeList[0]
    return result


# 连接成功时间
def getConnectSuccessTime(readlines):
    connectSuccessTimeList = []
    send0505 = fitter_keyword("[5, 5]", readlines)
    if send0505 == []:
        result = None
    else:
        for datagram in send0505:
            body = eval(datagram.split("b:")[1])
            if body[0] == 2:
                connectSuccessTime = getTime(datagram)
                connectSuccessTimeList.append(connectSuccessTime)
        result = connectSuccessTimeList[0]
    return result


# 断开成功时间
def getDisConnectSuccessTime(readlines):
    disConnectSuccessTimeList = []
    send050A = fitter_keyword("[5, 10]", readlines)
    if send050A == []:
        result = None
    else:
        for datagram in send050A:
            body = eval(datagram.split("b:")[1])
            if body[0] == 2:
                disConnectSuccessTime = getTime(datagram)
                disConnectSuccessTimeList.append(disConnectSuccessTime)
        result = disConnectSuccessTimeList[0]
    return result


# 获取蓝牙状态
def getBleStatusList(readlines):
    bleStatus = []
    send0502 = fitter_keyword("[5, 2]", readlines)
    for datagram in send0502:
        body = eval(datagram.split("b:")[1])
        bleStatus.append(body[0])
    return bleStatus


# 获取SBLE传递给VBLE的信息的信号强度
def getSBLEtoVBLEList(readlines):
    SBLEtoVBLEList = []
    send0502 = fitter_keyword("[5, 2]", readlines)
    for datagram in send0502:
        body = eval(datagram.split("b:")[1])
        SBLEtoVBLEList.append(body[1])
    return SBLEtoVBLEList


# 获取VBLE传递给SBLE的信息的信号强度
def getVBLEtoSBLEList(readlines):
    VBLEtoSBLEList = []
    send0508 = fitter_keyword("[5, 8]", readlines)
    for datagram in send0508:
        body = eval(datagram.split("b:")[1])
        VBLEtoSBLEList.append(body[6])
    return VBLEtoSBLEList


# ===============数据处理===============
def getData(readlines, resultlog):
    """
    获取单次连接数据
    :param readlines: 读取数据
    :return: 结果
    """
    controlConnectTime = getControlConnectTime(readlines)
    connectSuccessTime = getConnectSuccessTime(readlines)

    controlDisconnectTime = getControlDisconnectTime(readlines)
    disConnectSuccessTime = getDisConnectSuccessTime(readlines)

    if connectSuccessTime == None or disConnectSuccessTime == None:
        keepConnectTime = None
        BleStatusList = []
        SBLEtoVBLEList = []
        VBLEtoSBLEList = []
    else:
        connectSuccessDateTime = strpTime(connectSuccessTime)
        disConnectSuccessDateTime = strpTime(disConnectSuccessTime)
        controlDisconnectTimeDateTime = strpTime(controlDisconnectTime)

        keepConnectTime = intervalTime(connectSuccessDateTime, controlDisconnectTimeDateTime)
        keepConnectReadLine = FilterTime(connectSuccessTime, controlDisconnectTime, readlines)
        BleStatusList = getBleStatusList(keepConnectReadLine)
        SBLEtoVBLEList = list_remove(getSBLEtoVBLEList(keepConnectReadLine), 0)
        VBLEtoSBLEList = list_remove(getVBLEtoSBLEList(keepConnectReadLine), 0)

    # 输出结果
    with open(resultlog, 'a', encoding='utf-8') as f:
        f.write(f"下控蓝牙连接时间：{controlConnectTime}\r")
        f.write(f"蓝牙连接成功时间：{connectSuccessTime}\r")
        f.write(f"下控蓝牙断开时间：{controlDisconnectTime}\r")
        f.write(f"蓝牙断开成功时间：{disConnectSuccessTime}\r")
        f.write(f"保持连接时间：{keepConnectTime}s\r")

        print(f"下控蓝牙连接时间：{controlConnectTime}")
        print(f"蓝牙连接成功时间：{connectSuccessTime}")
        print(f"下控蓝牙断开时间：{controlDisconnectTime}")
        print(f"蓝牙断开成功时间：{disConnectSuccessTime}")
        print(f"保持连接时间：{keepConnectTime}s")
    result = [controlConnectTime, connectSuccessTime, controlDisconnectTime, disConnectSuccessTime, keepConnectTime,
              BleStatusList, SBLEtoVBLEList, VBLEtoSBLEList]
    return result


def handleData(startTimeStr, endTimeStr, readlines, resultlog, location):
    """
    单次连接数据
    :param startTimeStr:站控蓝牙连接接口调用时间
    :param endTimeStr:站控蓝牙断开接口调用时间
    :param readlines:读取数据
    :param location:站内，站外
    :return:结果
    """
    timeReadLines = FilterTime(startTimeStr, endTimeStr, readlines)
    controlConnectTime, connectSuccessTime, controlDisconnectTime, disConnectSuccessTime, keepConnectTime, BleStatusList, SBLEtoVBLEList, VBLEtoSBLEList = getData(
        timeReadLines, resultlog)

    # 连接成功耗时
    if connectSuccessTime == None:
        connectedConsumeTimes = None
    else:
        controlConnectDateTime = strpTime(controlConnectTime)
        connectSuccessDateTime = strpTime(connectSuccessTime)
        connectedConsumeTimes = intervalTime(controlConnectDateTime, connectSuccessDateTime)

    # 断开成功耗时
    if disConnectSuccessTime == None:
        disconnectedConsumeTimes = None
    else:
        controlDisconnectDateTime = strpTime(controlDisconnectTime)
        disConnectSuccessDateTime = strpTime(disConnectSuccessTime)
        disconnectedConsumeTimes = intervalTime(controlDisconnectDateTime, disConnectSuccessDateTime)

    # SBLE到VBLE蓝牙强度
    if SBLEtoVBLEList == []:
        maxValueSBLEtoVBLE = None
        minValueSBLEtoVBLE = None
        averageValueSBLEtoVBLE = None
        S2VpercentList = []
    else:
        maxValueSBLEtoVBLE = max(SBLEtoVBLEList)
        minValueSBLEtoVBLE = min(SBLEtoVBLEList)
        averageValueSBLEtoVBLE = average(SBLEtoVBLEList)
        if location == '站内':
            S2VpercentList = in_custom_display(SBLEtoVBLEList)
        elif location == '站外':
            S2VpercentList = out_custom_display(SBLEtoVBLEList)
        else:
            S2VpercentList = []

    # VBLE到SBLE蓝牙强度
    if VBLEtoSBLEList == []:
        maxValueVBLEtoSBLE = None
        minValueVBLEtoSBLE = None
        averageValueVBLEtoSBLE = None
        V2SpercentList = []
    else:
        maxValueVBLEtoSBLE = max(VBLEtoSBLEList)
        minValueVBLEtoSBLE = min(VBLEtoSBLEList)
        averageValueVBLEtoSBLE = average(VBLEtoSBLEList)
        if location == '站内':
            V2SpercentList = in_custom_display(VBLEtoSBLEList)
        elif location == '站外':
            V2SpercentList = out_custom_display(VBLEtoSBLEList)
        else:
            V2SpercentList = []

    # 保持连接率
    if BleStatusList == []:
        connectedRate = None
    else:
        BleStatus_1_List = list_save(BleStatusList, 1)
        connectedRate = len(BleStatus_1_List) / len(BleStatusList)

    # 输出结果
    with open(resultlog, 'a', encoding='utf-8') as f:
        f.write(f"连接成功耗时：{connectedConsumeTimes}s\r")
        f.write(f"断开成功耗时：{disconnectedConsumeTimes}s\r")
        f.write(f"保持连接率：{connectedRate * 100}%\r")
        f.write(f"S2V蓝牙强度最大值：{maxValueSBLEtoVBLE}\r")
        f.write(f"S2V蓝牙强度最小值：{minValueSBLEtoVBLE}\r")
        f.write(f"S2V蓝牙强度平均值：{round(averageValueSBLEtoVBLE)}\r")
        f.write(f"V2S蓝牙强度最大值：{maxValueVBLEtoSBLE}\r")
        f.write(f"V2S蓝牙强度最小值：{minValueVBLEtoSBLE}\r")
        f.write(f"V2S蓝牙强度平均值：{round(averageValueVBLEtoSBLE)}\r")

        print(f"连接成功耗时：{connectedConsumeTimes}s")
        print(f"断开成功耗时：{disconnectedConsumeTimes}s")
        print(f"保持连接率：{connectedRate * 100}%")
        print(f"S2V蓝牙强度最大值：{maxValueSBLEtoVBLE}")
        print(f"S2V蓝牙强度最小值：{minValueSBLEtoVBLE}")
        print(f"S2V蓝牙强度平均值：{round(averageValueSBLEtoVBLE)}")
        print(f"V2S蓝牙强度最大值：{maxValueVBLEtoSBLE}")
        print(f"V2S蓝牙强度最小值：{minValueVBLEtoSBLE}")
        print(f"V2S蓝牙强度平均值：{round(averageValueVBLEtoSBLE)}")

        if location == '站内':
            f.write(f"S2V蓝牙强度小于-60（差）占比：{S2VpercentList[0]}%\r")
            f.write(f"S2V蓝牙强度-60~-55（一般）占比：{S2VpercentList[1]}%\r")
            f.write(f"S2V蓝牙强度等于大于-55（优）占比：{S2VpercentList[2]}%\r")
            f.write(f"V2S蓝牙强度小于-60（差）占比：{V2SpercentList[0]}%\r")
            f.write(f"V2S蓝牙强度-60~-55（一般）占比：{V2SpercentList[1]}%\r")
            f.write(f"V2S蓝牙强度等于大于-55（优）占比：{V2SpercentList[2]}%\r\r")

            print(f"S2V蓝牙强度小于-60（差）占比：{S2VpercentList[0]}%")
            print(f"S2V蓝牙强度-60~-55（一般）占比：{S2VpercentList[1]}%")
            print(f"S2V蓝牙强度等于大于-55（优）占比：{S2VpercentList[2]}%")
            print(f"V2S蓝牙强度小于-60（差）占比：{V2SpercentList[0]}%")
            print(f"V2S蓝牙强度-60~-55（一般）占比：{V2SpercentList[1]}%")
            print(f"V2S蓝牙强度等于大于-55（优）占比：{V2SpercentList[2]}%")
            print()
        if location == '站外':
            f.write(f"S2V蓝牙强度小于-75（差）占比：{S2VpercentList[0]}%\r")
            f.write(f"S2V蓝牙强度-75~-65（一般）占比：{S2VpercentList[1]}%\r")
            f.write(f"S2V蓝牙强度等于大于-65（优）占比：{S2VpercentList[2]}%\r")
            f.write(f"V2S蓝牙强度小于-75（差）占比：{V2SpercentList[0]}%\r")
            f.write(f"V2S蓝牙强度-75~-65（一般）占比：{V2SpercentList[1]}%\r")
            f.write(f"V2S蓝牙强度等于大于-65（优）占比：{V2SpercentList[2]}%\r\r")

            print(f"S2V蓝牙强度小于-75（差）占比：{S2VpercentList[0]}%")
            print(f"S2V蓝牙强度-65~-75（一般）占比：{S2VpercentList[1]}%")
            print(f"S2V蓝牙强度等于大于-65（优）占比：{S2VpercentList[2]}%")
            print(f"V2S蓝牙强度小于-75（差）占比：{V2SpercentList[0]}%")
            print(f"V2S蓝牙强度-75~-65（一般）占比：{V2SpercentList[1]}%")
            print(f"V2S蓝牙强度等于大于-65（优）占比：{V2SpercentList[2]}%")
            print()

    result = [connectedConsumeTimes, disconnectedConsumeTimes, connectedRate, SBLEtoVBLEList, VBLEtoSBLEList, controlConnectTime]
    return result


def getAllData(starTimeStr_EndTimestr_List, filePath, resultlog, location):
    """
    数据汇总
    :param starTimeStr_EndTimestr_List:站控蓝牙连接接口调用时间，站控蓝牙断开接口调用时间
    :param filePath:日志路径
    """
    readlines = read_file(filePath)
    result_list = []
    all_connectedConsumeTimes = []
    all_disconnectedConsumeTimes = []
    all_connectedRate = []
    all_SBLEtoVBLEList = []
    all_VBLEtoSBLEList = []
    all_controlConnectTime = []

    for starTimeStr_endTimeStr in starTimeStr_EndTimestr_List:
        startTimeStr, endTimeStr = starTimeStr_endTimeStr
        result = handleData(startTimeStr, endTimeStr, readlines, resultlog, location)
        result_list.append(result)

    for result in result_list:
        all_connectedConsumeTimes.append(result[0])
        all_disconnectedConsumeTimes.append(result[1])
        all_connectedRate.append(result[2])
        all_SBLEtoVBLEList = all_SBLEtoVBLEList + result[3]
        all_VBLEtoSBLEList = all_VBLEtoSBLEList + result[4]
        all_controlConnectTime.append(result[5])

    # 连接成功耗时
    if all_connectedConsumeTimes == []:
        all_maxConnectedConsumeTimes = None
        all_minConnectedConsumeTimes = None
        all_averageConnectedConsumeTimes = None
    else:
        all_maxConnectedConsumeTimes = max(all_connectedConsumeTimes)
        all_minConnectedConsumeTimes = min(all_connectedConsumeTimes)
        all_averageConnectedConsumeTimes = average(all_connectedConsumeTimes)

    # 断开成功耗时
    if all_disconnectedConsumeTimes == []:
        all_maxDisconnectedConsumeTimes = None
        all_minDisconnectedConsumeTimes = None
        all_averageDisconnectedConsumeTimes = None
    else:
        all_maxDisconnectedConsumeTimes = max(all_disconnectedConsumeTimes)
        all_minDisconnectedConsumeTimes = min(all_disconnectedConsumeTimes)
        all_averageDisconnectedConsumeTimes = average(all_disconnectedConsumeTimes)

    # 保持连接率
    if all_connectedRate == []:
        all_maxConnectedRate = None
        all_minConnectedRate = None
    else:
        all_maxConnectedRate = max(all_connectedRate)
        all_minConnectedRate = min(all_connectedRate)

    # SBLE到VBLE蓝牙强度
    if all_SBLEtoVBLEList == []:
        all_maxValueSBLEtoVBLE = None
        all_minValueSBLEtoVBLE = None
        all_averageValueSBLEtoVBLE = None
        all_S2VpercentList = None
    else:
        all_maxValueSBLEtoVBLE = max(all_SBLEtoVBLEList)
        all_minValueSBLEtoVBLE = min(all_SBLEtoVBLEList)
        all_averageValueSBLEtoVBLE = average(all_SBLEtoVBLEList)
        if location == '站内':
            all_S2VpercentList = in_custom_display(all_SBLEtoVBLEList)
        elif location == '站外':
            all_S2VpercentList = out_custom_display(all_SBLEtoVBLEList)
        else:
            all_S2VpercentList = []

    # VBLE到SBLE蓝牙强度
    if all_VBLEtoSBLEList == []:
        all_maxValueVBLEtoSBLE = None
        all_minValueVBLEtoSBLE = None
        all_averageValueVBLEtoSBLE = None
        all_V2SpercentList = None
    else:
        all_maxValueVBLEtoSBLE = max(all_VBLEtoSBLEList)
        all_minValueVBLEtoSBLE = min(all_VBLEtoSBLEList)
        all_averageValueVBLEtoSBLE = average(all_VBLEtoSBLEList)
        if location == '站内':
            all_V2SpercentList = in_custom_display(all_VBLEtoSBLEList)
        elif location == '站外':
            all_V2SpercentList = out_custom_display(all_VBLEtoSBLEList)
        else:
            all_V2SpercentList = []

    with open(resultlog, 'a', encoding='utf-8') as f:
        f.write(f"#####{location}")
        f.write(f"数据时间：{all_controlConnectTime[0]}~{all_controlConnectTime[-1]}")
        f.write(f"连接成功耗时最大值：{all_maxConnectedConsumeTimes}s\r")
        f.write(f"连接成功耗时最小值：{all_minConnectedConsumeTimes}s\r")
        f.write(f"连接成功耗时平均值：{all_averageConnectedConsumeTimes}s\r")
        f.write(f"断开成功耗时最大值：{all_maxDisconnectedConsumeTimes}s\r")
        f.write(f"断开成功耗时最小值：{all_minDisconnectedConsumeTimes}s\r")
        f.write(f"断开成功耗时平均值：{all_averageDisconnectedConsumeTimes}s\r")
        f.write(f"保持连接率最大值：{all_maxConnectedRate * 100}%\r")
        f.write(f"保持连接率最小值：{all_minConnectedRate * 100}%\r")
        f.write(f"S2V蓝牙强度最大值：{all_maxValueSBLEtoVBLE}\r")
        f.write(f"S2V蓝牙强度最小值：{all_minValueSBLEtoVBLE}\r")
        f.write(f"S2V蓝牙强度平均值：{round(all_averageValueSBLEtoVBLE)}\r")
        f.write(f"V2S蓝牙强度最大值：{all_maxValueVBLEtoSBLE}\r")
        f.write(f"V2S蓝牙强度最小值：{all_minValueVBLEtoSBLE}\r")
        f.write(f"V2S蓝牙强度平均值：{round(all_averageValueVBLEtoSBLE)}\r")

        print(f"#####{location}")
        print(f"数据时间：{all_controlConnectTime[0]}~{all_controlConnectTime[-1]}")
        print(f"连接成功耗时最大值：{all_maxConnectedConsumeTimes}s")
        print(f"连接成功耗时最小值：{all_minConnectedConsumeTimes}s")
        print(f"连接成功耗时平均值：{all_averageConnectedConsumeTimes}s")
        print(f"断开成功耗时最大值：{all_maxDisconnectedConsumeTimes}s")
        print(f"断开成功耗时最小值：{all_minDisconnectedConsumeTimes}s")
        print(f"断开成功耗时平均值：{all_averageDisconnectedConsumeTimes}s")
        print(f"保持连接率最大值：{all_maxConnectedRate * 100}%")
        print(f"保持连接率最小值：{all_minConnectedRate * 100}%")
        print(f"S2V蓝牙强度最大值：{all_maxValueSBLEtoVBLE}")
        print(f"S2V蓝牙强度最小值：{all_minValueSBLEtoVBLE}")
        print(f"S2V蓝牙强度平均值：{round(all_averageValueSBLEtoVBLE)}")
        print(f"V2S蓝牙强度最大值：{all_maxValueVBLEtoSBLE}")
        print(f"V2S蓝牙强度最小值：{all_minValueVBLEtoSBLE}")
        print(f"V2S蓝牙强度平均值：{round(all_averageValueVBLEtoSBLE)}")
        if location == '站内':
            f.write(f"S2V蓝牙强度小于-60（差）占比：{all_S2VpercentList[0]}%\r")
            f.write(f"S2V蓝牙强度-60~-55（一般）占比：{all_S2VpercentList[1]}%\r")
            f.write(f"S2V蓝牙强度等于大于-55（优）占比：{all_S2VpercentList[2]}%\r")
            f.write(f"V2S蓝牙强度小于-60（差）占比：{all_V2SpercentList[0]}%\r")
            f.write(f"V2S蓝牙强度-60~-55（一般）占比：{all_V2SpercentList[1]}%\r")
            f.write(f"V2S蓝牙强度等于大于-55（优）占比：{all_V2SpercentList[2]}%\r\r")

            print(f"S2V蓝牙强度小于-60（差）占比：{all_S2VpercentList[0]}%")
            print(f"S2V蓝牙强度-60~-55（一般）占比：{all_S2VpercentList[1]}%")
            print(f"S2V蓝牙强度等于大于-55（优）占比：{all_S2VpercentList[2]}%")
            print(f"V2S蓝牙强度小于-60（差）占比：{all_V2SpercentList[0]}%")
            print(f"V2S蓝牙强度-60~-55（一般）占比：{all_V2SpercentList[1]}%")
            print(f"V2S蓝牙强度等于大于-55（优）占比：{all_V2SpercentList[2]}%")
        if location == '站外':
            f.write(f"S2V蓝牙强度小于-75（差）占比：{all_S2VpercentList[0]}%")
            f.write(f"S2V蓝牙强度-75~-65（一般）占比：{all_S2VpercentList[1]}%")
            f.write(f"S2V蓝牙强度等于大于-65（优）占比：{all_S2VpercentList[2]}%")
            f.write(f"V2S蓝牙强度小于-75（差）占比：{all_V2SpercentList[0]}%")
            f.write(f"V2S蓝牙强度-75~-65（一般）占比：{all_V2SpercentList[1]}%")
            f.write(f"V2S蓝牙强度等于大于-65（优）占比：{all_V2SpercentList[2]}%")

            print(f"S2V蓝牙强度小于-75（差）占比：{all_S2VpercentList[0]}%")
            print(f"S2V蓝牙强度-75~-65（一般）占比：{all_S2VpercentList[1]}%")
            print(f"S2V蓝牙强度等于大于-65（优）占比：{all_S2VpercentList[2]}%")
            print(f"V2S蓝牙强度小于-75（差）占比：{all_V2SpercentList[0]}%")
            print(f"V2S蓝牙强度-75~-65（一般）占比：{all_V2SpercentList[1]}%")
            print(f"V2S蓝牙强度等于大于-65（优）占比：{all_V2SpercentList[2]}%")


if __name__ == '__main__':
    """
    数据整理
    """
    starTimeStr_EndTimestr_List = [
        ["2026-07-09 16:19:56.279", "2026-07-09 16:23:42.980"],
        ["2026-07-09 16:23:42.980", "2026-07-09 16:26:12.043"],
        ["2026-07-09 16:26:12.043", "2026-07-09 16:26:33.215"],
        ["2026-07-09 16:26:33.215", "2026-07-09 16:29:29.703"],
        ["2026-07-09 16:29:29.703", "2026-07-09 16:31:48.136"],

    ]

    filePath = "datagram-docking-car-station-2026-07-09-2.log"
    resultlog = 'blueResult.log'
    location = '站内'
    getAllData(starTimeStr_EndTimestr_List, filePath, resultlog, location)
