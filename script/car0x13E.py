import os
import gzip
from datetime import datetime


def strpTime(timeStr: str):
    dateTime = datetime.strptime(timeStr, "%Y-%m-%d %H:%M:%S.%f")
    return dateTime


def getConnectVehicleBle():
    resource_swap = '/logs/svc-swap-flow/all'
    for root, dirs, files in os.walk(resource_swap):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)
            if file_path.endswith('.gz'):
                with gzip.open(file_path, 'rt', encoding='utf-8') as file_a:
                    with open('result_swap.txt', 'a', encoding='utf-8') as file_b:
                        for line in file_a:
                            if '【站】蓝牙连接流程，存储流程标记：connectVehicleBle' in line:
                                file_b.write(line.split('[svc-swap-flow]')[0].strip() + '\n')
                            if '【站】设值界面步序：连接车辆蓝牙，数据：{"resultMsg":null,"status":2,"connectResult":1}' in line:
                                file_b.write(line.split('[svc-swap-flow]')[0].strip() + '\n')

            if file_path.endswith('.log'):
                with open(file_path, 'r', encoding='utf-8') as file_a:
                    with open('result_swap.txt', 'a', encoding='utf-8') as file_b:
                        for line in file_a:
                            if '【站】蓝牙连接流程，存储流程标记：connectVehicleBle' in line:
                                file_b.write(line.split('[svc-swap-flow]')[0].strip() + '\n')
                            if '【站】设值界面步序：连接车辆蓝牙，数据：{"resultMsg":null,"status":2,"connectResult":1}' in line:
                                file_b.write(line.split('[svc-swap-flow]')[0].strip() + '\n')


def get0x13E():
    resource_car = '/logs/docking-car-station/datagram'
    for root, dirs, files in os.walk(resource_car):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)
            if file_path.endswith('.gz'):
                with gzip.open(file_path, 'rt', encoding='utf-8') as file_a:
                    with open('result_car.txt', 'a', encoding='utf-8') as file_b:
                        for line in file_a:
                            if '[5, 86]' in line:
                                if '0, 0, 0, 0, 0, 1, 62' in line:
                                    file_b.write(line.split(' - R')[0].strip() + '\n')

            if file_path.endswith('.log'):
                with open(file_path, 'r', encoding='utf-8') as file_a:
                    with open('result_car.txt', 'a', encoding='utf-8') as file_b:
                        for line in file_a:
                            if '[5, 86]' in line:
                                if '0, 0, 0, 0, 0, 1, 62' in line:
                                    file_b.write(line.split(' - R')[0].strip() + '\n')


def handle():
    with open('result_swap.txt', 'r', encoding='utf-8') as file_swap:
        content_swap = file_swap.read().split("\n")
        content_swap = [t for t in content_swap if t]

    with open('result_car.txt', 'r', encoding='utf-8') as file_car:
        content_car = file_car.read().split("\n")
        content_car = [t for t in content_car if t]

    with open('result.txt', 'w', encoding='utf-8') as file:
        for car in content_car:
            car_strp = strpTime(car)
            for index in range(0, len(content_swap), 2):
                start = content_swap[index:index + 2][0]
                start_strp = strpTime(start)
                end = content_swap[index:index + 2][1]
                end_strp = strpTime(end)

                if (start_strp <= car_strp) and (car_strp <= end_strp):
                    file.write(f'start：{start}\r')
                    file.write(f'0x13E：{car}\r')
                    file.write(f'end：{end}\r\r')
                    file.flush()
                    print(f'start：{start}')
                    print(f'0x13E：{car}')
                    print(f'end：{end}\r\n')





if __name__ == '__main__':
    getConnectVehicleBle()
    get0x13E()
    handle()
