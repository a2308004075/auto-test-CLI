class HandlerDataType:
    @staticmethod
    def float_to_2shorts(value: float):
        """
        将float拆分成2个short值
        """
        # 说明：如果要设置【吸收有功电能(用户用电量)】为21，
        # electricMeter_value(21)输出结果s0_signed=16808，s1_signed=0，
        # 【吸收有功电能(用户用电量)】地址：0xE302、0xE303
        # 0xE302转十进制=58114，则ID为58114，value为16808
        # 0xE303转十进制=58115，则ID为58115，value为0

        # 1. 将浮点数转换为整数位表示
        # Python中使用struct包来处理float到int的转换
        bits = struct.unpack('>I', struct.pack('>f', value))[0]
        # print(f"{value} 的位表示: 0x{bits:08X} (十进制: {bits})")

        # 2. 提取4个字节
        b0 = (bits >> 24) & 0xFF
        b1 = (bits >> 16) & 0xFF
        b2 = (bits >> 8) & 0xFF
        b3 = bits & 0xFF

        # 3. 计算short值
        # Python中没有原生short类型，使用int并限制在16位范围内
        s0 = ((b0 << 8) | b1) & 0xFFFF
        s1 = ((b2 << 8) | b3) & 0xFFFF

        # 转换为有符号short（如果最高位为1，则为负数）
        s0_signed = s0 if s0 < 0x8000 else s0 - 0x10000
        s1_signed = s1 if s1 < 0x8000 else s1 - 0x10000

        return s0_signed, s1_signed

    @staticmethod
    def uint16_to_2shorts(value: int):
        """
        将uint16拆分成2个short值
        """
        assert 0 <= value <= 0xFFFF
        high_byte = (value >> 8) & 0xFF  # 保持正数 0~255
        low_byte = value & 0xFF
        # 转为有符号 short（其实就是正数，因为 < 0x8000）
        return high_byte, low_byte

    @staticmethod
    def uint16_to_short(value: int) -> int:
        """
        将uint16拆分成1个short值
        """
        value &= 0xFFFF
        hi_byte = (value >> 8) & 0xFF
        lo_byte = value & 0xFF
        short_val = (hi_byte << 8) | lo_byte
        # 处理符号
        if short_val >= 0x8000:
            short_val -= 0x10000
        return short_val

    @staticmethod
    def uint32_to_2shorts(value: int):
        """
        将uint32拆分成2个short值
        """
        # 确保输入是32位无符号范围
        value &= 0xFFFFFFFF

        # 提取高16位和低16位
        high = (value >> 16) & 0xFFFF
        low = value & 0xFFFF

        # 转换为有符号short（与原有逻辑一致）
        high_signed = high if high < 0x8000 else high - 0x10000
        low_signed = low if low < 0x8000 else low - 0x10000

        return high_signed, low_signed
