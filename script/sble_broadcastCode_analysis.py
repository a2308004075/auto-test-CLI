"""
SBLE广播解析
"""


def hex_to_dec(hex_num):
    dec_num = int(hex_num, 16)
    return dec_num


def get_ip_info(broadcast_code):
    return broadcast_code[-40:]


def get_ipv4(dec_num):
    ip = -(dec_num - 255)
    return ip


def get_port(dec_num):
    port = -(dec_num - 65535)
    return port


def get_local_ip(broadcast_code):
    ip_info = get_ip_info(broadcast_code)
    hex_num_1 = ip_info[0:2]
    dec_num_1 = hex_to_dec(hex_num_1)
    ip_1 = get_ipv4(dec_num_1)
    hex_num_2 = ip_info[2:4]
    dec_num_2 = hex_to_dec(hex_num_2)
    ip_2 = get_ipv4(dec_num_2)
    hex_num_3 = ip_info[4:6]
    dec_num_3 = hex_to_dec(hex_num_3)
    ip_3 = get_ipv4(dec_num_3)
    hex_num_4 = ip_info[6:8]
    dec_num_4 = hex_to_dec(hex_num_4)
    ip_4 = get_ipv4(dec_num_4)
    local_ip = f"{ip_1}.{ip_2}.{ip_3}.{ip_4}"
    return local_ip


def get_gateway(broadcast_code):
    ip_info = get_ip_info(broadcast_code)
    hex_num_1 = ip_info[8:10]
    dec_num_1 = hex_to_dec(hex_num_1)
    ip_1 = get_ipv4(dec_num_1)
    hex_num_2 = ip_info[10:12]
    dec_num_2 = hex_to_dec(hex_num_2)
    ip_2 = get_ipv4(dec_num_2)
    hex_num_3 = ip_info[12:14]
    dec_num_3 = hex_to_dec(hex_num_3)
    ip_3 = get_ipv4(dec_num_3)
    hex_num_4 = ip_info[14:16]
    dec_num_4 = hex_to_dec(hex_num_4)
    ip_4 = get_ipv4(dec_num_4)
    gateway = f"{ip_1}.{ip_2}.{ip_3}.{ip_4}"
    return gateway


def get_subnet_mask(broadcast_code):
    ip_info = get_ip_info(broadcast_code)
    hex_num_1 = ip_info[16:18]
    dec_num_1 = hex_to_dec(hex_num_1)
    ip_1 = get_ipv4(dec_num_1)
    hex_num_2 = ip_info[18:20]
    dec_num_2 = hex_to_dec(hex_num_2)
    ip_2 = get_ipv4(dec_num_2)
    hex_num_3 = ip_info[20:22]
    dec_num_3 = hex_to_dec(hex_num_3)
    ip_3 = get_ipv4(dec_num_3)
    hex_num_4 = ip_info[22:24]
    dec_num_4 = hex_to_dec(hex_num_4)
    ip_4 = get_ipv4(dec_num_4)
    subnet_mask = f"{ip_1}.{ip_2}.{ip_3}.{ip_4}"
    return subnet_mask


def get_local_port(broadcast_code):
    ip_info = get_ip_info(broadcast_code)
    hex_num_1 = ip_info[24:26]
    hex_num_2 = ip_info[26:28]
    hex = f"{hex_num_2}{hex_num_1}"
    dec_num = hex_to_dec(hex)
    local_port = get_port(dec_num)
    return local_port


def get_server_ip(broadcast_code):
    ip_info = get_ip_info(broadcast_code)
    hex_num_1 = ip_info[28:30]
    dec_num_1 = hex_to_dec(hex_num_1)
    ip_1 = get_ipv4(dec_num_1)
    hex_num_2 = ip_info[30:32]
    dec_num_2 = hex_to_dec(hex_num_2)
    ip_2 = get_ipv4(dec_num_2)
    hex_num_3 = ip_info[32:34]
    dec_num_3 = hex_to_dec(hex_num_3)
    ip_3 = get_ipv4(dec_num_3)
    hex_num_4 = ip_info[34:36]
    dec_num_4 = hex_to_dec(hex_num_4)
    ip_4 = get_ipv4(dec_num_4)
    server_ip = f"{ip_1}.{ip_2}.{ip_3}.{ip_4}"
    return server_ip


def get_server_port(broadcast_code):
    ip_info = get_ip_info(broadcast_code)
    hex_num_1 = ip_info[36:38]
    hex_num_2 = ip_info[38:40]
    hex = f"{hex_num_2}{hex_num_1}"
    dec_num = hex_to_dec(hex)
    server_port = get_port(dec_num)
    return server_port


def get_network_info(broadcast_code):
    broadcast_code = get_ip_info(broadcast_code)
    local_ip = get_local_ip(broadcast_code)
    gateway = get_gateway(broadcast_code)
    local_port = get_local_port(broadcast_code)
    subnet_mask = get_subnet_mask(broadcast_code)
    server_ip = get_server_ip(broadcast_code)
    server_port = get_server_port(broadcast_code)
    network_info = f"""local_ip：{local_ip}
local_gateway：{gateway}
subnet_mask：{subnet_mask}
local_port：{local_port}
server_ip：{server_ip}
server_port：{server_port}
"""
    print(network_info)


if __name__ == '__main__':
    broadcast_code = "0x0201061107E01C4B5E1EEBA15CEEF45EBA0001FF01050853424C4517FF484853FFE1EB53FFE1FE000000FF8FE853FFF5EDECD8"
    get_network_info(broadcast_code)
