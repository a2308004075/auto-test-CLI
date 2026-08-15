"""
十进制转二进制（字节）
"""


def int_to_bytes(num):
    # 将整数转换为8位的二进制字符串
    return [format(num >> i & 1, 'b') for i in range(7, -1, -1)]


# 示例
num = -104
bytes_seq = int_to_bytes(num)
print(bytes_seq)  # 输出: ['1', '0', '1', '0', '0', '0', '0', '0']
