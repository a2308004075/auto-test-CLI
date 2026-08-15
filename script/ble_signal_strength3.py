import os
import codecs
import gzip
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

    def date2str(self, date):
        return date.strftime("%Y-%m-%d %H:%M:%S.%f")


handleTime = HandleTime()


class Read:
    """
    读取文件
    """

    def read_files(self, directory):
        readLines = []
        # 遍历目录中的所有文件
        for filename in os.listdir(directory):
            # 检查文件是否以 .gz 结尾
            if filename.endswith('.gz'):
                file_path = os.path.join(directory, filename)
                # 打开并读取.gz文件
                with gzip.open(file_path, 'rt', encoding='utf-8') as f:
                    for line in f:
                        readLines.append(line.strip())
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

    def getOrderDateTime(self, orderList):
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
            if startDateTime < datagram[0] and datagram[0] < endDateTime:
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


class PLC:

    def getplcencode0001(self, readlines):
        """
        车辆驶入换电站且到位请求
        """
        encode0001List = []
        encode0006 = read.fitter_keyword("encode", read.fitter_keyword("[0, 1]", readlines))
        for datagram in encode0006:
            time = handleDatagram.getTime(datagram)
            body = handleDatagram.getBody(datagram)[9:10]
            encode0001List.append([time, body])
        return encode0001List

    def getplcencode0003(self, readlines):
        """
        归中举升请求
        """
        encode0003List = []
        encode0003 = read.fitter_keyword("encode", read.fitter_keyword("[0, 3]", readlines))
        for datagram in encode0003:
            time = handleDatagram.getTime(datagram)
            body = handleDatagram.getBody(datagram)[8:9]
            encode0003List.append([time, body])
        return encode0003List

    def getplcencode0005(self, readlines):
        """
        换电通道设备归位请求
        """
        encode0005List = []
        encode0005 = read.fitter_keyword("encode", read.fitter_keyword("[0, 5]", readlines))
        for datagram in encode0005:
            time = handleDatagram.getTime(datagram)
            body = handleDatagram.getBody(datagram)[8:9]
            encode0005List.append([time, body])
        return encode0005List

    def getplcencode0006(self, readlines):
        """
        车辆驶出换电站请求
        """
        encode0006List = []
        encode0006 = read.fitter_keyword("encode", read.fitter_keyword("[0, 6]", readlines))
        for datagram in encode0006:
            time = handleDatagram.getTime(datagram)
            body = handleDatagram.getBody(datagram)[8:9]
            encode0006List.append([time, body])
        return encode0006List

    def getplc0206(self, readlines):
        """
        换电设备状态
        """
        plc0206List = []
        plc0206 = read.fitter_keyword("[2, 6]", readlines)
        for datagram in plc0206:
            time = handleDatagram.getTime(datagram)
            body = handleDatagram.getBody(datagram)[8:]
            plc0206List.append([time, body])
        return plc0206List

    def getEntranceRoadStatus(self, plc0206List):
        """
        入口道闸开启
        """
        entranceRoadStatusList = []
        for p0206 in plc0206List:
            entranceRoadStatus = p0206[1][2:3][0]
            if entranceRoadStatus == 1:
                entranceRoadStatusList.append(p0206)
        return entranceRoadStatusList

    def getEntranceRadarStatus(self, plc0206List):
        """
        入口雷达信号触发
        """
        entranceRadarStatusList = []
        for p0206 in plc0206List:
            entranceRadarStatus = p0206[1][0:1][0]
            if entranceRadarStatus == 1:
                entranceRadarStatusList.append(p0206)
        return entranceRadarStatusList

    def getVehiclePositionStatus1(self, plc0206List):
        """
        1=车辆到位，允许调整自由度
        """
        vehiclePositionStatusList = []
        for p0206 in plc0206List:
            vehiclePositionStatus = p0206[1][7:8][0]
            if vehiclePositionStatus == 1:
                vehiclePositionStatusList.append(p0206)
        return vehiclePositionStatusList


plc = PLC()


class HandleDate:
    def getStepTime(self, sbleLogPath, plcLogPath, orderList, stepTimePath):
        orderDateTimeList = sorted(read.getOrderDateTime(orderList))
        sbleReadLines = read.read_files(sbleLogPath)
        plcReadLines = read.read_files(plcLogPath)
        sble0402List = sorted(sble.getsble0402(sbleReadLines), key=lambda x: x[0])
        sble0403List = sorted(sble.getsble0403(sbleReadLines), key=lambda x: x[0])

        sble0505List = sorted(sble.getsble0505(sbleReadLines), key=lambda x: x[0])

        sble0510List = sorted(sble.getsble0510(sbleReadLines), key=lambda x: x[0])

        encode0003List = sorted(plc.getplcencode0003(plcReadLines), key=lambda x: x[0])
        encode0005List = sorted(plc.getplcencode0005(plcReadLines), key=lambda x: x[0])

        entranceRoadStatusList = sorted(plc.getEntranceRoadStatus(plc.getplc0206(plcReadLines)), key=lambda x: x[0])

        with open(stepTimePath, "a", encoding="utf-8") as file:
            for orderDateTime in orderDateTimeList:
                for sble0402 in sble0402List:
                    controlConnectDateTime = sble0402[0]  # 下控蓝牙连接时间
                    if orderDateTime <= controlConnectDateTime:
                        print(orderDateTime)
                        for sble0505 in sble0505List:
                            connectSuccessDateTime = sble0505[0]  # 蓝牙连接成功时间
                            if controlConnectDateTime <= connectSuccessDateTime:
                                for entranceRoadStatus in entranceRoadStatusList:
                                    entranceRoadDateTime = entranceRoadStatus[0]  # 入口道闸开启
                                    if connectSuccessDateTime <= entranceRoadDateTime:
                                        for encode0003 in encode0003List:
                                            plcLiftDateTime = encode0003[0]  # 归中举升请求时间
                                            if entranceRoadDateTime <= plcLiftDateTime:
                                                for encode0005 in encode0005List:
                                                    plcRecoverDateTime = encode0005[0]  # 设备归位时间
                                                    if plcLiftDateTime <= plcRecoverDateTime:
                                                        for sble0403 in sble0403List:
                                                            controlDisconnectDateTime = sble0403[0]  # 下控蓝牙断开时间
                                                            if plcRecoverDateTime <= controlDisconnectDateTime:
                                                                for sble0510 in sble0510List:
                                                                    disConnectSuccessDateTime = sble0510[0]  # 断开成功时间
                                                                    if controlDisconnectDateTime <= disConnectSuccessDateTime:
                                                                        controlConnectTime = handleTime.date2str(controlConnectDateTime)
                                                                        connectSuccessTime = handleTime.date2str(connectSuccessDateTime)
                                                                        entranceRoadTime = handleTime.date2str(entranceRoadDateTime)
                                                                        plcLiftTime = handleTime.date2str(plcLiftDateTime)
                                                                        plcRecoverTime = handleTime.date2str(plcRecoverDateTime)
                                                                        controlDisconnectTime = handleTime.date2str(controlDisconnectDateTime)
                                                                        disConnectSuccessTime = handleTime.date2str(disConnectSuccessDateTime)
                                                                        file.write(controlConnectTime + "," + connectSuccessTime + "," +
                                                                                   entranceRoadTime + "," + plcLiftTime + "," + plcRecoverTime + "," +
                                                                                   controlDisconnectTime + "," + disConnectSuccessTime + '\r')

                                                                        break
                                                                break
                                                        break
                                                break
                                        break
                                break
                        break

    def all(self, orderPath):
        orderList = read.read_file(orderPath)
        orderList = [datetime.strptime(ts, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S") for ts in orderList]
        sorted_time_strings = [ts.strftime("%Y-%m-%d") for ts in sorted([datetime.strptime(ts, "%Y-%m-%d") for ts in set(order.split(" ")[0] for order in orderList)])]
        for day in sorted_time_strings:
            order_path = datetime.strptime(day, '%Y-%m-%d').strftime('%Y-%m-%d')
            sbleLogPath = f"/logs/docking-car-station/datagram/{order_path}"
            plcLogPath = f"/logs/docking-plc/datagram/{order_path}"
            orderTime = [date for date in orderList if date.startswith(day)]
            handleDate.getStepTime(sbleLogPath, plcLogPath, orderTime, "stepTime.txt")


handleDate = HandleDate()

if __name__ == '__main__':
    # 步骤1
    handleDate.all("order.txt")
