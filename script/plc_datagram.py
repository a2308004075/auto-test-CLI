"""
解析PLC报文
"""

datagram = [68, 1, 0, 1, 2, 4, 0, 14, 1, 12, 0, 0, 0, 0]
print(f"长度：{len(datagram)}")
print(f"报文头：{datagram[0:8]}")
print(f"报文长度：{datagram[7]}")

if len(datagram) == datagram[7]:
    datagram_body = datagram[8:]
    for i in range(len(datagram_body)):
        print(f"位置:{i}值：{datagram_body[i]}")
else:
    print("长度错误")


