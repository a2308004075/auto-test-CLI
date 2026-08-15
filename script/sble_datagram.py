"""
解析SBLE报文
"""


def decimal2ascii(hexlist):
    """
    十进制转ASCII
    """
    hex_string = ''.join(f'{value}' for value in hexlist)
    byte_data = bytes.fromhex(hex_string)
    ascii_string = byte_data.decode('ascii')
    print(ascii_string)


def hex2ascii(decimallist):
    """
    十六进制转ASCII
    """
    hex_string = ''.join(f'{value:02x}' for value in decimallist)
    byte_data = bytes.fromhex(hex_string)
    ascii_string = byte_data.decode('ascii')
    print(ascii_string)


if __name__ == '__main__':
    decimallist = [86, 66, 84, 72, 87, 51, 48, 49]
    hex2ascii(decimallist)