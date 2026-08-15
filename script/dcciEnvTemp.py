import json
import os
import codecs
import sys
import gzip


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

    def read_gz_files(self, directory):
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


read = Read()


def getEnvTemp(channelId, chargerNo, resourceFile):
    # dcciReadLines = read.read_files(resourceFile)
    dcciReadLines = read.read_gz_files(resourceFile)
    envTempList = []

    with open("result.txt", "w", encoding="utf-8") as file:
        for dcci in dcciReadLines:
            if f"channelId:{channelId}, chargerNo:{chargerNo}, gunNo:0, msgId:4551" in dcci:
                dataTime = dcci.split("- decode")[0].strip()
                envTemp = json.loads(dcci.split("body:")[1].strip())["envTemp"]
                file.write(f"{dataTime},{envTemp}\r")
                envTempList.append(f"{dataTime},{envTemp}")


if __name__ == '__main__':
    channelId = 1
    chargerNo = 1
    resourceFile = sys.argv[1]
    getEnvTemp(channelId, chargerNo, resourceFile)
