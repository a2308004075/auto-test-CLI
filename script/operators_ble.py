from datetime import datetime
import pandas as pd


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
    return round((sum(l) / len(l)), 2)


def in_custom_display(data):
    """
    站内信号强度评级
    """
    # 调整bins以覆盖所有区间
    bins = [-float('inf'), -60, -55, float('inf')]

    # 使用pd.cut将数据分到不同的区间
    categories = pd.cut(data, bins)

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
    # 调整bins以覆盖所有区间
    bins = [-float('inf'), -75, -70, float('inf')]

    # 使用pd.cut将数据分到不同的区间
    categories = pd.cut(data, bins)

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


def get_data(starTime, connectSuccessTime, intoTime, endtime, readlines):
    statusline = FilterTime(connectSuccessTime, endtime, readlines)
    bleStatusList = getBleStatusList(statusline)
    BleStatus_1_List = list_save(bleStatusList, 1)
    connectedRate = len(BleStatus_1_List) / len(bleStatusList)
    print(f'保持连接率：{connectedRate}')

    if strpTime(starTime) != strpTime(intoTime):
        outline = FilterTime(starTime, intoTime, readlines)
        outs2vList = list_remove(getSBLEtoVBLEList(outline), 0)
        outv2sList = list_remove(getVBLEtoSBLEList(outline), 0)
        outAverageS2v = average(outs2vList)
        outAverageV2S = average(outv2sList)
        print(f"站外S2V蓝牙强度平均值：{outAverageS2v}")
        print(f"站外V2S蓝牙强度平均值：{outAverageV2S}")

    intoline = FilterTime(intoTime, endtime, readlines)
    intos2vList = list_remove(getSBLEtoVBLEList(intoline), 0)
    intov2sList = list_remove(getVBLEtoSBLEList(intoline), 0)
    intoAverageS2v = average(intos2vList)
    intoAverageV2S = average(intov2sList)
    print(f"站内S2V蓝牙强度平均值：{intoAverageS2v}")
    print(f"站内V2S蓝牙强度平均值：{intoAverageV2S}")


if __name__ == '__main__':
    readlines = read_file(r'datagram-docking-car-station.log')
    starTime = '2026-06-01 16:37:39.275'
    connectSuccessTime = '2026-06-01 16:37:42.761'
    intoTime = '2026-06-01 16:37:54.455'
    endtime = '2026-06-01 16:40:02.364'
    get_data(starTime, connectSuccessTime, intoTime, endtime, readlines)
