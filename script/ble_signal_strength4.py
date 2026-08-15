import os
import codecs
import pandas as pd
from datetime import datetime

"""
自动换电-三代蓝牙数据整理
"""


class HandleTime:
    """
    时间处理
    """

    def strpTime(self, timeStr: str):
        """
        字符串类型时间转dateTime类型时间
        param timeStr（str）：字符串类型时间
        return dateTime（datetime）：datetime类型时间
        """
        if "." not in timeStr:
            timeStr = timeStr + ".000"
        dateTime = datetime.strptime(timeStr, "%Y-%m-%d %H:%M:%S.%f")
        return dateTime

    def intervalTime(self, startDateTime, endDateTime):
        """
        计算时间间隔（秒）
        param startDateTime（datetime）：datetime格式时间
        param endDateTime（datetime）：datetime格式时间
        return intervalSeconds（）：时间间隔（s）
        """
        intervalSeconds = -1
        if startDateTime and endDateTime:
            intervalSeconds = round(
                (endDateTime - startDateTime).seconds + ((endDateTime - startDateTime).microseconds) / 1000000, 3)
        return intervalSeconds


handleTime = HandleTime()


class Read:
    """
    读取文件
    """

    def read_files(self, directory):
        """
        读取指定目录下所有文件的内容，并将每一行的内容存储在一个列表中。
        param directory (str): 文件夹路径
        return readLines（list）: 包含所有文件内容行的列表
        """
        readLines = []

        # 遍历目录及其子目录中的所有文件
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                print(file_path)
                try:
                    # 尝试以 UTF-8 编码打开文件
                    with codecs.open(file_path, 'r', encoding='utf-8') as file:
                        for line in file:
                            readLines.append(line.strip())
                except UnicodeDecodeError:
                    # 如果 UTF-8 编码失败，尝试以其他编码打开文件
                    try:
                        with codecs.open(file_path, 'r', encoding='gbk') as file:
                            for line in file:
                                readLines.append(line.strip())
                    except UnicodeDecodeError:
                        # 如果其他编码也失败，打印错误信息并跳过该文件
                        print(f"Failed to decode file {file_path} with UTF-8 and GBK encoding.")
                        continue
        return readLines

    def read_file(self, filepath):
        """
        读取指定文件内容
        param filepath (str): 文件路径
        return readLines（list）: 包含所有文件内容行的列表
        """
        readLines = []

        try:
            # 尝试以 UTF-8 编码打开文件
            with codecs.open(filepath, 'r', encoding='utf-8') as file:
                for line in file:
                    # 逐行读取文件内容，并移除行尾的空白字符（如换行符）
                    readLines.append(line.strip())
        except UnicodeDecodeError:
            # 如果 UTF-8 编码失败，捕获异常并尝试以其他编码打开文件
            try:
                with codecs.open(filepath, 'r', encoding='gbk') as file:
                    for line in file:
                        # 逐行读取文件内容，并移除行尾的空白字符（如换行符）
                        readLines.append(line.strip())
            except UnicodeDecodeError:
                # 如果其他编码也失败，打印错误信息并返回空列表
                print(f"Failed to decode file {filepath} with UTF-8 and GBK encoding.")
                return []
        return readLines

    def fitter_keyword(self, keyword, readLines):
        """
        通过关键字过滤内容
        param keyword (str): 关键字
        param readLines (str): 要筛选的行
        return filterLines（list）: 包含关键字的行
        """
        filterLines = []
        for readline in readLines:
            if keyword in readline:
                filterLines.append(readline.strip())
        return filterLines

    def getOrderDateTime(self, filepath):
        orderList = self.read_file(filepath)
        orderDateTimeList = []
        for order in orderList:
            orderDateTimeList.append(handleTime.strpTime(order))
        return orderDateTimeList


read = Read()


class Arithmetic:
    """
    计算
    """

    def average(self, bleStrengthList: list):
        """
        取平均数
        param bleStrengthList（list）：蓝牙强度
        return averageBleStrength（float）：平均蓝牙强度
        """
        averageValue = round(sum(bleStrengthList) / len(bleStrengthList), 3)
        return averageValue

    def averageStrength(self, bleStrengthList: list):
        """
        取平均数
        param bleStrengthList（list）：蓝牙强度
        return averageBleStrength（float）：平均蓝牙强度
        """
        averageBleStrength = int(sum(bleStrengthList) / len(bleStrengthList))
        return averageBleStrength

    def mostNum(self, bleStrengthList: list):
        """
        取众数
        param bleStrengthList（list）：蓝牙强度
        return mostNum（float）：蓝牙强度的众数
        """
        mostNumBleStrength = max(set(bleStrengthList), key=bleStrengthList.count)
        return mostNumBleStrength

    def in_custom_display(self, data):
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

    def out_custom_display(self, data):
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


arithmetic = Arithmetic()


class HandleDatagram:
    """
    处理datagram日志
    """

    def getTime(self, datagram):
        """
        取时间
        param datagram（str）：datagram日志行
        return timeStr（str）：时间
        """
        timeStr = handleTime.strpTime(datagram.split(" - ")[0])
        return timeStr

    def getBody(self, datagram):
        """
        取body
        param datagram（str）：datagram日志行
        return body（list）：body
        """
        body = []
        if 'body:' in datagram:
            body = eval(datagram.split("body:")[1])
        if 'b:' in datagram:
            body = eval(datagram.split("b:")[1])
        return body

    def list_remove(self, datagrams, key):
        new_list = []
        for datagram in datagrams:
            if datagram != key:
                new_list.append(datagram)
        return new_list

    def list_save(self, datagrams, key):
        new_list = []
        for datagram in datagrams:
            if datagram == key:
                new_list.append(datagram)
        return new_list

    def FilterTime(self, startDateTime, endDateTime, filterList):
        timeBodyList = []
        for datagram in filterList:
            if startDateTime <= datagram[0] and datagram[0] <= endDateTime:
                timeBodyList.append(datagram)
        return timeBodyList


handleDatagram = HandleDatagram()


class SBLE:
    """
    SBLE协议
    """

    def getsble0402(self, readlines):
        """
        下控蓝牙连接402
        """
        sble0402List = []
        sble0402 = read.fitter_keyword("[4, 2]", readlines)
        for datagram in sble0402:
            time = handleDatagram.getTime(datagram)
            body = handleDatagram.getBody(datagram)[0:1]
            if body[0] == 2:
                sble0402List.append([time, body])
        return sble0402List

    def getsble0403(self, readlines):
        """
        下控蓝牙断开403
        """
        sble0403List = []
        sble0403 = read.fitter_keyword("[4, 3]", readlines)
        for datagram in sble0403:
            time = handleDatagram.getTime(datagram)
            body = handleDatagram.getBody(datagram)[0:1]
            if body[0] == 1:
                sble0403List.append([time, body])
        return sble0403List

    def getsble0505(self, readlines):
        """
        蓝牙连接成功505
        """
        sble0505List = []
        sble0505 = read.fitter_keyword("[5, 5]", readlines)
        for datagram in sble0505:
            time = handleDatagram.getTime(datagram)
            body = handleDatagram.getBody(datagram)[0:1]
            if body[0] == 2:
                sble0505List.append([time, body])
        return sble0505List

    def getsble0510(self, readlines):
        """
        蓝牙断开时间50A
        """
        sble0510List = []
        sble0510 = read.fitter_keyword("[5, 10]", readlines)
        for datagram in sble0510:
            time = handleDatagram.getTime(datagram)
            body = handleDatagram.getBody(datagram)[0:1]
            if body[0] == 2:
                sble0510List.append([time, body])
        return sble0510List

    def getsble0502(self, readlines):
        """
        SBLE和VBLE蓝牙连接状态
        SBLE传递给VBLE的信息的信号强度
        """
        sble0502List = []
        sble0502 = read.fitter_keyword("[5, 2]", readlines)
        for datagram in sble0502:
            time = handleDatagram.getTime(datagram)
            body = handleDatagram.getBody(datagram)[:2]
            sble0502List.append([time, body])
        return sble0502List

    def getsble0508(self, readlines):
        """
        VBLE传递给SBLE的信息的信号强度
        """
        sble0508List = []
        sble0508 = read.fitter_keyword("[5, 8]", readlines)
        for datagram in sble0508:
            time = handleDatagram.getTime(datagram)
            body = handleDatagram.getBody(datagram)[6:7]
            sble0508List.append([time, body])
        return sble0508List

    def getBleStatus(self, sble0502List):
        BleStatusList = []
        for sble0502 in sble0502List:
            BleStatusList.append(sble0502[1][0])
        return BleStatusList

    def getSBLEtoVBLE(self, sble0502List):
        SBLEtoVBLEList = []
        for sble0502 in sble0502List:
            SBLEtoVBLEList.append(sble0502[1][1])
        return SBLEtoVBLEList

    def getVBLEtoSBLEList(self, sble0508List):
        VBLEtoSBLEList = []
        for sble0508 in sble0508List:
            VBLEtoSBLEList.append(sble0508[1][0])
        return VBLEtoSBLEList


sble = SBLE()


class HandleDate:

    def getData(self, sbleLogPath, stepTimePath, resultFile):
        stepTimeList = sorted(read.read_file(stepTimePath))
        sbleReadLines = read.read_files(sbleLogPath)
        sble0502List = sorted(sble.getsble0502(sbleReadLines), key=lambda x: x[0])
        sble0508List = sorted(sble.getsble0508(sbleReadLines), key=lambda x: x[0])
        result_list = []
        with open(resultFile, "w", encoding="utf-8") as file:
            count = 0
            for stepTime in stepTimeList:
                step = stepTime.split(",")
                controlConnectTime = handleTime.strpTime(step[0])  # 下控蓝牙连接时间
                connectSuccessTime = handleTime.strpTime(step[1])  # 蓝牙连接成功时间
                connectedConsumeTimes = handleTime.intervalTime(controlConnectTime, connectSuccessTime)  # 连接成功耗时
                controlDisconnectTime = handleTime.strpTime(step[5])  # 下控蓝牙断开时间
                disConnectSuccessTime = handleTime.strpTime(step[6])  # 断开成功时间
                disconnectedConsumeTimes = handleTime.intervalTime(controlDisconnectTime, disConnectSuccessTime)  # 断开成功耗时
                keepConnectTime = handleTime.intervalTime(connectSuccessTime, disConnectSuccessTime)  # 保持连接时间
                print(f"下控蓝牙连接时间：{controlConnectTime}")
                print(f"蓝牙连接成功时间：{connectSuccessTime}")
                print(f"连接成功耗时：{connectedConsumeTimes}s")
                print(f"下控蓝牙断开时间：{controlDisconnectTime}")
                print(f"断开成功时间：{disConnectSuccessTime}")
                print(f"断开成功耗时：{disconnectedConsumeTimes}s")
                print(f"保持连接时间：{keepConnectTime}s")
                file.write(f"下控蓝牙连接时间：{controlConnectTime}\r")
                file.write(f"蓝牙连接成功时间：{connectSuccessTime}\r")
                file.write(f"连接成功耗时：{connectedConsumeTimes}s\r")
                file.write(f"下控蓝牙断开时间：{controlDisconnectTime}\r")
                file.write(f"断开成功时间：{disConnectSuccessTime}\r")
                file.write(f"断开成功耗时：{disconnectedConsumeTimes}s\r")
                file.write(f"保持连接时间：{keepConnectTime}s\r")

                # 站外
                vehiclePositionTime = handleTime.strpTime(step[2])  # 入口道闸触发
                print(f"入口道闸触发时间：{vehiclePositionTime}")
                file.write(f"入口道闸触发时间：{vehiclePositionTime}\r")
                # 蓝牙连接成功-入口道闸触发
                outsideSBLE0502bodyList = handleDatagram.FilterTime(connectSuccessTime, vehiclePositionTime, sble0502List)
                outsideSBLE0508bodyList = handleDatagram.FilterTime(connectSuccessTime, vehiclePositionTime, sble0508List)
                outsideBleStatusList = sble.getBleStatus(outsideSBLE0502bodyList)
                outsideSBLEtoVBLEList = handleDatagram.list_remove(sble.getSBLEtoVBLE(outsideSBLE0502bodyList), 0)
                outsideVBLEtoSBLEList = handleDatagram.list_remove(sble.getSBLEtoVBLE(sble.getVBLEtoSBLEList(outsideSBLE0508bodyList)), 0)

                # 站外S2V强度
                maxOutsideSBLEtoVBLE = max(outsideSBLEtoVBLEList)
                minOutsideSBLEtoVBLE = min(outsideSBLEtoVBLEList)
                averageOutsideSBLEtoVBLE = arithmetic.averageStrength(outsideSBLEtoVBLEList)
                mostOutsideSBLEtoVBLE = arithmetic.mostNum(outsideSBLEtoVBLEList)
                out_S2VpercentList = arithmetic.out_custom_display(outsideSBLEtoVBLEList)
                print(f"S2V蓝牙强度最大值：{maxOutsideSBLEtoVBLE}")
                print(f"S2V蓝牙强度最小值：{minOutsideSBLEtoVBLE}")
                print(f"S2V蓝牙强度平均值：{averageOutsideSBLEtoVBLE}")
                print(f"S2V蓝牙强度众数值：{mostOutsideSBLEtoVBLE}")
                print(f"S2V蓝牙强度小于-75（差）占比：{out_S2VpercentList[0]}%")
                print(f"S2V蓝牙强度-75~-70（一般）占比：{out_S2VpercentList[1]}%")
                print(f"S2V蓝牙强度大于-70（优）占比：{out_S2VpercentList[2]}%")
                file.write(f"S2V蓝牙强度最大值：{maxOutsideSBLEtoVBLE}\r")
                file.write(f"S2V蓝牙强度最小值：{minOutsideSBLEtoVBLE}\r")
                file.write(f"S2V蓝牙强度平均值：{averageOutsideSBLEtoVBLE}\r")
                file.write(f"S2V蓝牙强度众数值：{mostOutsideSBLEtoVBLE}\r")
                file.write(f"S2V蓝牙强度小于-75（差）占比：{out_S2VpercentList[0]}%\r")
                file.write(f"S2V蓝牙强度-75~-70（一般）占比：{out_S2VpercentList[1]}%\r")
                file.write(f"S2V蓝牙强度大于-70（优）占比：{out_S2VpercentList[2]}%\r")

                # 站外V2S强度
                maxOutsideVBLEtoSBLE = max(outsideVBLEtoSBLEList)
                minOutsideVBLEtoSBLE = min(outsideVBLEtoSBLEList)
                averageOutsideVBLEtoSBLE = arithmetic.averageStrength(outsideVBLEtoSBLEList)
                mostOutsideVBLEtoSBLE = arithmetic.mostNum(outsideVBLEtoSBLEList)
                out_V2SpercentList = arithmetic.out_custom_display(outsideVBLEtoSBLEList)
                print(f"V2S蓝牙强度最大值：{maxOutsideVBLEtoSBLE}")
                print(f"V2S蓝牙强度最小值：{minOutsideVBLEtoSBLE}")
                print(f"V2S蓝牙强度平均值：{averageOutsideVBLEtoSBLE}")
                print(f"V2S蓝牙强度众数值：{mostOutsideVBLEtoSBLE}")
                print(f"V2S蓝牙强度小于-75（差）占比：{out_V2SpercentList[0]}%")
                print(f"V2S蓝牙强度-75~-70（一般）占比：{out_V2SpercentList[1]}%")
                print(f"V2S蓝牙强度大于-70（优）占比：{out_V2SpercentList[2]}%")
                file.write(f"V2S蓝牙强度最大值：{maxOutsideVBLEtoSBLE}\r")
                file.write(f"V2S蓝牙强度最小值：{minOutsideVBLEtoSBLE}\r")
                file.write(f"V2S蓝牙强度平均值：{averageOutsideVBLEtoSBLE}\r")
                file.write(f"V2S蓝牙强度众数值：{mostOutsideVBLEtoSBLE}\r")
                file.write(f"V2S蓝牙强度小于-75（差）占比：{out_V2SpercentList[0]}%\r")
                file.write(f"V2S蓝牙强度-75~-70（一般）占比：{out_V2SpercentList[1]}%\r")
                file.write(f"V2S蓝牙强度大于-70（优）占比：{out_V2SpercentList[2]}%\r")

                # 站外保持连接率
                outsideBleStatusList_new = handleDatagram.list_save(outsideBleStatusList, 1)
                outsideConnectedRate = len(outsideBleStatusList_new) / len(outsideBleStatusList) * 100
                print(f"保持连接率：{outsideConnectedRate}%")
                file.write(f"保持连接率：{outsideConnectedRate}%\r")

                # 站内
                plcLiftTime = handleTime.strpTime(step[3])  # 归中举升请求时间
                plcRecoverTime = handleTime.strpTime(step[4])  # 设备归位时间
                print(f"归中举升请求时间：{plcLiftTime}")
                print(f"设备归位时间：{plcRecoverTime}")
                file.write(f"归中举升请求时间：{plcLiftTime}\r")
                file.write(f"设备归位时间：{plcRecoverTime}\r")

                # 归中举升-设备归位
                insideSBLE0502bodyList = handleDatagram.FilterTime(plcLiftTime, plcRecoverTime, sble0502List)
                insideSBLE0508bodyList = handleDatagram.FilterTime(plcLiftTime, plcRecoverTime, sble0508List)
                insideBleStatusList = sble.getBleStatus(insideSBLE0502bodyList)
                insideSBLEtoVBLEList = sble.getSBLEtoVBLE(insideSBLE0502bodyList)
                insideVBLEtoSBLEList = sble.getVBLEtoSBLEList(insideSBLE0508bodyList)

                # 站内S2V强度
                maxInsideSBLEtoVBLE = max(insideSBLEtoVBLEList)
                minInsideSBLEtoVBLE = min(insideSBLEtoVBLEList)
                averageInsideSBLEtoVBLE = arithmetic.averageStrength(insideSBLEtoVBLEList)
                mostInsideSBLEtoVBLE = arithmetic.mostNum(insideSBLEtoVBLEList)
                in_S2VpercentList = arithmetic.in_custom_display(insideSBLEtoVBLEList)
                print(f"S2V蓝牙强度最大值：{maxInsideSBLEtoVBLE}")
                print(f"S2V蓝牙强度最小值：{minInsideSBLEtoVBLE}")
                print(f"S2V蓝牙强度平均值：{averageInsideSBLEtoVBLE}")
                print(f"S2V蓝牙强度众数值：{mostInsideSBLEtoVBLE}")
                print(f"S2V蓝牙强度小于-60（差）占比：{in_S2VpercentList[0]}%")
                print(f"S2V蓝牙强度-60~-55（一般）占比：{in_S2VpercentList[1]}%")
                print(f"S2V蓝牙强度大于-55（优）占比：{in_S2VpercentList[2]}%")
                file.write(f"S2V蓝牙强度最大值：{maxInsideSBLEtoVBLE}\r")
                file.write(f"S2V蓝牙强度最小值：{minInsideSBLEtoVBLE}\r")
                file.write(f"S2V蓝牙强度平均值：{averageInsideSBLEtoVBLE}\r")
                file.write(f"S2V蓝牙强度众数值：{mostInsideSBLEtoVBLE}\r")
                file.write(f"S2V蓝牙强度小于-60（差）占比：{in_S2VpercentList[0]}%\r")
                file.write(f"S2V蓝牙强度-60~-55（一般）占比：{in_S2VpercentList[1]}%\r")
                file.write(f"S2V蓝牙强度大于-55（优）占比：{in_S2VpercentList[2]}%\r")

                # 站内V2S强度
                maxInsideVBLEtoSBLE = max(insideVBLEtoSBLEList)
                minInsideVBLEtoSBLE = min(insideVBLEtoSBLEList)
                averageInsideVBLEtoSBLE = arithmetic.averageStrength(insideVBLEtoSBLEList)
                mostInsideVBLEtoSBLE = arithmetic.mostNum(insideVBLEtoSBLEList)
                in_V2SpercentList = arithmetic.in_custom_display(insideVBLEtoSBLEList)
                print(f"V2S蓝牙强度最大值：{maxInsideVBLEtoSBLE}")
                print(f"V2S蓝牙强度最小值：{minInsideVBLEtoSBLE}")
                print(f"V2S蓝牙强度平均值：{averageInsideVBLEtoSBLE}")
                print(f"V2S蓝牙强度众数值：{mostInsideVBLEtoSBLE}")
                print(f"V2S蓝牙强度小于-60（差）占比：{in_V2SpercentList[0]}%")
                print(f"V2S蓝牙强度-60~-55（一般）占比：{in_V2SpercentList[1]}%")
                print(f"V2S蓝牙强度大于-55（优）占比：{in_V2SpercentList[2]}%")
                file.write(f"V2S蓝牙强度最大值：{maxInsideVBLEtoSBLE}\r")
                file.write(f"V2S蓝牙强度最小值：{minInsideVBLEtoSBLE}\r")
                file.write(f"V2S蓝牙强度平均值：{averageInsideVBLEtoSBLE}\r")
                file.write(f"V2S蓝牙强度众数值：{mostInsideVBLEtoSBLE}\r")
                file.write(f"V2S蓝牙强度小于-60（差）占比：{in_V2SpercentList[0]}%\r")
                file.write(f"V2S蓝牙强度-60~-55（一般）占比：{in_V2SpercentList[1]}%\r")
                file.write(f"V2S蓝牙强度大于-55（优）占比：{in_V2SpercentList[2]}%\r")

                # 站内保持连接率
                insideBleStatusList_new = handleDatagram.list_save(insideBleStatusList, 1)
                insideConnectedRate = len(insideBleStatusList_new) / len(insideBleStatusList) * 100  # 保持连接率
                print(f"保持连接率：{insideConnectedRate}%")
                file.write(f"保持连接率：{insideConnectedRate}%\r")

                result = [connectedConsumeTimes, disconnectedConsumeTimes,
                          outsideSBLEtoVBLEList, outsideVBLEtoSBLEList, outsideConnectedRate,
                          insideSBLEtoVBLEList, insideVBLEtoSBLEList, insideConnectedRate, controlConnectTime]
                result_list.append(result)
                count = count + 1
                file.write(f"{count}\r\r")
                print(count)

        return result_list

    def getAllData(self, sbleLogPath, stepTimePath, resultFile):
        result_list = self.getData(sbleLogPath, stepTimePath, resultFile)
        all_connectedConsumeTimes = []
        all_disconnectedConsumeTimes = []
        all_outsideSBLEtoVBLEList = []
        all_outsideVBLEtoSBLEList = []
        all_outsideConnectedRate = []
        all_insideSBLEtoVBLEList = []
        all_insideVBLEtoSBLEList = []
        all_insideConnectedRate = []
        all_controlConnectTime = []

        for result in result_list:
            all_connectedConsumeTimes.append(result[0])
            all_disconnectedConsumeTimes.append(result[1])
            all_outsideSBLEtoVBLEList = all_outsideSBLEtoVBLEList + result[2]
            all_outsideVBLEtoSBLEList = all_outsideVBLEtoSBLEList + result[3]
            all_outsideConnectedRate.append(result[4])
            all_insideSBLEtoVBLEList = all_insideSBLEtoVBLEList + result[5]
            all_insideVBLEtoSBLEList = all_insideVBLEtoSBLEList + result[6]
            all_insideConnectedRate.append(result[7])
            all_controlConnectTime.append(result[8])

        with open(resultFile, "w", encoding="utf-8") as file:
            file.write(f"######统计\r")
            print(f"######统计")

            max_all_connectedConsumeTimes = max(all_connectedConsumeTimes)
            min_all_connectedConsumeTimes = min(all_connectedConsumeTimes)
            avg_all_connectedConsumeTimes = arithmetic.averageStrength(all_connectedConsumeTimes)
            mode_all_connectedConsumeTimes = arithmetic.mostNum(all_connectedConsumeTimes)
            print(f"数据时间：{all_controlConnectTime[0]}~{all_controlConnectTime[-1]}")
            print(f"连接成功耗时最大值：{max_all_connectedConsumeTimes}s")
            print(f"连接成功耗时最小值：{min_all_connectedConsumeTimes}s")
            print(f"连接成功耗时平均值：{avg_all_connectedConsumeTimes}s")
            print(f"连接成功耗时众数值：{mode_all_connectedConsumeTimes}s")
            file.write(f"数据时间：{all_controlConnectTime[0]}~{all_controlConnectTime[-1]}\r")
            file.write(f"连接成功耗时最大值：{max_all_connectedConsumeTimes}s\r")
            file.write(f"连接成功耗时最小值：{min_all_connectedConsumeTimes}s\r")
            file.write(f"连接成功耗时平均值：{avg_all_connectedConsumeTimes}s\r")
            file.write(f"连接成功耗时众数值：{mode_all_connectedConsumeTimes}s\r")

            max_all_disconnectedConsumeTimes = max(all_disconnectedConsumeTimes)
            min_all_disconnectedConsumeTimes = min(all_disconnectedConsumeTimes)
            avg_all_disconnectedConsumeTimes = arithmetic.averageStrength(all_disconnectedConsumeTimes)
            mode_all_disconnectedConsumeTimes = arithmetic.mostNum(all_disconnectedConsumeTimes)
            print(f"断开成功耗时最大值：{max_all_disconnectedConsumeTimes}s")
            print(f"断开成功耗时最小值：{min_all_disconnectedConsumeTimes}s")
            print(f"断开成功耗时平均值：{avg_all_disconnectedConsumeTimes}s")
            print(f"断开成功耗时众数值：{mode_all_disconnectedConsumeTimes}s")
            file.write(f"断开成功耗时最大值：{max_all_disconnectedConsumeTimes}s\r")
            file.write(f"断开成功耗时最小值：{min_all_disconnectedConsumeTimes}s\r")
            file.write(f"断开成功耗时平均值：{avg_all_disconnectedConsumeTimes}s\r")
            file.write(f"断开成功耗时众数值：{mode_all_disconnectedConsumeTimes}s\r")

            print(f"#####站外：蓝牙连接成功-入口道闸触发")
            file.write(f"#####站外：蓝牙连接成功-入口道闸触发\r")
            max_all_outsideSBLEtoVBLEList = max(all_outsideSBLEtoVBLEList)
            min_all_outsideSBLEtoVBLEList = min(all_outsideSBLEtoVBLEList)
            avg_all_outsideSBLEtoVBLEList = arithmetic.averageStrength(all_outsideSBLEtoVBLEList)
            mode_all_outsideSBLEtoVBLEList = arithmetic.mostNum(all_outsideSBLEtoVBLEList)
            all_out_S2VpercentList = arithmetic.out_custom_display(all_outsideSBLEtoVBLEList)
            print(f"S2V蓝牙强度最大值：{max_all_outsideSBLEtoVBLEList}")
            print(f"S2V蓝牙强度最小值：{min_all_outsideSBLEtoVBLEList}")
            print(f"S2V蓝牙强度平均值：{avg_all_outsideSBLEtoVBLEList}")
            print(f"S2V蓝牙强度众数值：{mode_all_outsideSBLEtoVBLEList}")
            print(f"S2V蓝牙强度小于-75（差）占比：{all_out_S2VpercentList[0]}%")
            print(f"S2V蓝牙强度-75~-70（一般）占比：{all_out_S2VpercentList[1]}%")
            print(f"S2V蓝牙强度大于-70（优）占比：{all_out_S2VpercentList[2]}%")
            file.write(f"S2V蓝牙强度最大值：{max_all_outsideSBLEtoVBLEList}\r")
            file.write(f"S2V蓝牙强度最小值：{min_all_outsideSBLEtoVBLEList}\r")
            file.write(f"S2V蓝牙强度平均值：{avg_all_outsideSBLEtoVBLEList}\r")
            file.write(f"S2V蓝牙强度众数值：{mode_all_outsideSBLEtoVBLEList}\r")
            file.write(f"S2V蓝牙强度小于-75（差）占比：{all_out_S2VpercentList[0]}%\r")
            file.write(f"S2V蓝牙强度-75~-70（一般）占比：{all_out_S2VpercentList[1]}%\r")
            file.write(f"S2V蓝牙强度大于-70（优）占比：{all_out_S2VpercentList[2]}%\r")

            max_all_outsideVBLEtoSBLEList = max(all_outsideVBLEtoSBLEList)
            min_all_outsideVBLEtoSBLEList = min(all_outsideVBLEtoSBLEList)
            avg_all_outsideVBLEtoSBLEList = arithmetic.averageStrength(all_outsideVBLEtoSBLEList)
            mode_all_outsideVBLEtoSBLEList = arithmetic.mostNum(all_outsideVBLEtoSBLEList)
            all_out_V2SpercentList = arithmetic.out_custom_display(all_outsideVBLEtoSBLEList)
            print(f"V2S蓝牙强度最大值：{max_all_outsideVBLEtoSBLEList}")
            print(f"V2S蓝牙强度最小值：{min_all_outsideVBLEtoSBLEList}")
            print(f"V2S蓝牙强度平均值：{avg_all_outsideVBLEtoSBLEList}")
            print(f"V2S蓝牙强度众数值：{mode_all_outsideVBLEtoSBLEList}")
            print(f"V2S蓝牙强度小于-75（差）占比：{all_out_V2SpercentList[0]}%")
            print(f"V2S蓝牙强度-75~-70（一般）占比：{all_out_V2SpercentList[1]}%")
            print(f"V2S蓝牙强度大于-70（优）占比：{all_out_V2SpercentList[2]}%")
            file.write(f"V2S蓝牙强度最大值：{max_all_outsideVBLEtoSBLEList}\r")
            file.write(f"V2S蓝牙强度最小值：{min_all_outsideVBLEtoSBLEList}\r")
            file.write(f"V2S蓝牙强度平均值：{avg_all_outsideVBLEtoSBLEList}\r")
            file.write(f"V2S蓝牙强度众数值：{mode_all_outsideVBLEtoSBLEList}\r")
            file.write(f"V2S蓝牙强度小于-75（差）占比：{all_out_V2SpercentList[0]}%\r")
            file.write(f"V2S蓝牙强度-75~-70（一般）占比：{all_out_V2SpercentList[1]}%\r")
            file.write(f"V2S蓝牙强度大于-70（优）占比：{all_out_V2SpercentList[2]}%\r")

            max_all_outsideConnectedRate = max(all_outsideConnectedRate)
            min_all_outsideConnectedRate = min(all_outsideConnectedRate)
            avg_all_outsideConnectedRate = arithmetic.averageStrength(all_outsideConnectedRate)
            mode_all_outsideConnectedRate = arithmetic.mostNum(all_outsideConnectedRate)
            print(f"保持连接率最大值：{max_all_outsideConnectedRate}%")
            print(f"保持连接率最小值：{min_all_outsideConnectedRate}%")
            print(f"保持连接率平均值：{avg_all_outsideConnectedRate}%")
            print(f"保持连接率众数值：{mode_all_outsideConnectedRate}%")
            file.write(f"保持连接率最大值：{max_all_outsideConnectedRate}%\r")
            file.write(f"保持连接率最小值：{min_all_outsideConnectedRate}%\r")
            file.write(f"保持连接率平均值：{avg_all_outsideConnectedRate}%\r")
            file.write(f"保持连接率众数值：{mode_all_outsideConnectedRate}%\r")

            print(f"站内：归中举升-设备归位")
            file.write(f"#####站内：归中举升-设备归位\r")
            max_all_insideSBLEtoVBLEList = max(all_insideSBLEtoVBLEList)
            min_all_insideSBLEtoVBLEList = min(all_insideSBLEtoVBLEList)
            avg_all_insideSBLEtoVBLEList = arithmetic.averageStrength(all_insideSBLEtoVBLEList)
            mode_all_insideSBLEtoVBLEList = arithmetic.mostNum(all_insideSBLEtoVBLEList)
            all_in_S2VpercentList = arithmetic.in_custom_display(all_insideSBLEtoVBLEList)
            print(f"S2V蓝牙强度最大值：{max_all_insideSBLEtoVBLEList}")
            print(f"S2V蓝牙强度最小值：{min_all_insideSBLEtoVBLEList}")
            print(f"S2V蓝牙强度平均值：{avg_all_insideSBLEtoVBLEList}")
            print(f"S2V蓝牙强度众数值：{mode_all_insideSBLEtoVBLEList}")
            print(f"S2V蓝牙强度小于-60（差）占比：{all_in_S2VpercentList[0]}%")
            print(f"S2V蓝牙强度-60~-55（一般）占比：{all_in_S2VpercentList[1]}%")
            print(f"S2V蓝牙强度大于-55（优）占比：{all_in_S2VpercentList[2]}%")
            file.write(f"S2V蓝牙强度最大值：{max_all_insideSBLEtoVBLEList}\r")
            file.write(f"S2V蓝牙强度最小值：{min_all_insideSBLEtoVBLEList}\r")
            file.write(f"S2V蓝牙强度平均值：{avg_all_insideSBLEtoVBLEList}\r")
            file.write(f"S2V蓝牙强度众数值：{mode_all_insideSBLEtoVBLEList}\r")
            file.write(f"S2V蓝牙强度小于-60（差）占比：{all_in_S2VpercentList[0]}%\r")
            file.write(f"S2V蓝牙强度-60~-55（一般）占比：{all_in_S2VpercentList[1]}%\r")
            file.write(f"S2V蓝牙强度大于-55（优）占比：{all_in_S2VpercentList[2]}%\r")

            max_all_insideVBLEtoSBLEList = max(all_insideVBLEtoSBLEList)
            min_all_insideVBLEtoSBLEList = min(all_insideVBLEtoSBLEList)
            avg_all_insideVBLEtoSBLEList = arithmetic.averageStrength(all_insideVBLEtoSBLEList)
            mode_all_insideVBLEtoSBLEList = arithmetic.mostNum(all_insideVBLEtoSBLEList)
            all_in_V2SpercentList = arithmetic.in_custom_display(all_insideVBLEtoSBLEList)
            print(f"V2S蓝牙强度最大值：{max_all_insideVBLEtoSBLEList}")
            print(f"V2S蓝牙强度最小值：{min_all_insideVBLEtoSBLEList}")
            print(f"V2S蓝牙强度平均值：{avg_all_insideVBLEtoSBLEList}")
            print(f"V2S蓝牙强度众数值：{mode_all_insideVBLEtoSBLEList}")
            print(f"V2S蓝牙强度小于-60（差）占比：{all_in_V2SpercentList[0]}%")
            print(f"V2S蓝牙强度-60~-55（一般）占比：{all_in_V2SpercentList[1]}%")
            print(f"V2S蓝牙强度大于-55（优）占比：{all_in_V2SpercentList[2]}%")
            file.write(f"V2S蓝牙强度最大值：{max_all_insideVBLEtoSBLEList}\r")
            file.write(f"V2S蓝牙强度最小值：{min_all_insideVBLEtoSBLEList}\r")
            file.write(f"V2S蓝牙强度平均值：{avg_all_insideVBLEtoSBLEList}\r")
            file.write(f"V2S蓝牙强度众数值：{mode_all_insideVBLEtoSBLEList}\r")
            file.write(f"V2S蓝牙强度小于-60（差）占比：{all_in_V2SpercentList[0]}%\r")
            file.write(f"V2S蓝牙强度-60~-55（一般）占比：{all_in_V2SpercentList[1]}%\r")
            file.write(f"V2S蓝牙强度大于-55（优）占比：{all_in_V2SpercentList[2]}%\r")

            max_all_insideConnectedRate = max(all_insideConnectedRate)
            min_all_insideConnectedRate = min(all_insideConnectedRate)
            avg_all_insideConnectedRate = arithmetic.averageStrength(all_insideConnectedRate)
            mode_all_insideConnectedRate = arithmetic.mostNum(all_insideConnectedRate)
            print(f"保持连接率最大值：{max_all_insideConnectedRate}%")
            print(f"保持连接率最小值：{min_all_insideConnectedRate}%")
            print(f"保持连接率平均值：{avg_all_insideConnectedRate}%")
            print(f"保持连接率众数值：{mode_all_insideConnectedRate}%")
            file.write(f"保持连接率最大值：{max_all_insideConnectedRate}%\r")
            file.write(f"保持连接率最小值：{min_all_insideConnectedRate}%\r")
            file.write(f"保持连接率平均值：{avg_all_insideConnectedRate}%\r")
            file.write(f"保持连接率众数值：{mode_all_insideConnectedRate}%\r")


if __name__ == '__main__':
    handleDate = HandleDate()
    # 步骤2
    handleDate.getData(sbleLogPath="car", stepTimePath="stepTime.txt", resultFile="resultFile.txt")
