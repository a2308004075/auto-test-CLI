# -*- coding: utf-8 -*-
"""eBus7.0 报文位定义(来源: eBus7.0_Protocol_MCAN-SBLE_V01.5.pdf, 34个报文/316条信号)

如何新增报文:
1. 在下方 messages 字典追加一条:
       "MsgID大写去前导0": (报文名, 发送方, 发送周期ms, [信号定义, ...])
2. 每条信号定义为7元组:
       (信号名, 中文含义, 起始位, 长度, Factor, Offset, 值表)
   - 起始位按协议口径: bit0 为数据段最低位(Intel格式@1+, Startbit 从0起)
   - 信号段须从 bit0 无缝铺满到 bit63(DLC=8), 无重叠无间隙
   - 物理值 = 原始值 * Factor + Offset(Factor=1 且 Offset=0 时不显示物理值)
   - 值表为 {原始值: "含义"} 字典或 None; 常用值表可复用下方 VL_ 前缀常量
3. MsgID 末字节随 SBMU 序号(0x4A~0x4D)变化的报文, key 只写前6位(如 "40141"),
   主脚本匹配时会先精确匹配、失败再去掉末字节降级匹配
"""

# 常用值表
VL_LVL3 = {0: "No Alarm", 1: "Level 1 Alarm", 2: "Level 2 Alarm", 3: "Level 3 Alarm"}
VL_FLT = {0: "No Alarm", 1: "Alarm"}
VL_ONOFF = {0: "Signal not defined", 1: "Offline", 2: "Online", 3: "Signal invalid"}
VL_DEACT = {0: "Signal not defined", 1: "Deactive", 2: "Active", 3: "Signal invalid"}
VL_OK = {0: "Signal not defined", 1: "Not OK", 2: "OK", 3: "Signal invalid"}
VL_OPEN = {0: "Open", 1: "Close"}
VL_RLYF = {0: "No Alarm", 1: "Stuck Close", 2: "Stuck Open", 3: "Invalid"}
VL_STS = {0: "默认", 1: "失败", 2: "成功"}
VL_FB = {0: "未收到", 1: "收到"}
VL_FRM = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6"}
VL_INV = {255: "invalid"}
VL_ASCII = {i: chr(i) for i in list(range(48, 58)) + list(range(65, 91))}

# 报文定义: MsgID(大写去前导0) → (报文名, 发送方, 发送周期ms, [信号定义...])
messages = {
    # S2P_Status 0x040141(4A~4D) SBLE 50ms
    "40141": ("S2P_Status", "SBLE", 50, [
        ("SBMUCRC", "SBMU状态报文的CRC", 0, 8, 1, 0, None),
        ("SBMUALIV", "SBMU生命信号,0~15循环", 8, 4, 1, 0, None),
        ("HVPwrOnStatus", "SBMU高压上电状态(软件驱动状态)", 12, 2, 1, 0, VL_ONOFF),
        ("HVPwrOffRuquest", "SBMU高压下电请求", 14, 2, 1, 0, VL_DEACT),
        ("LVPwrOffReady", "SBMU低压下电准备状态", 16, 2, 1, 0, VL_OK),
        ("SbmuAddress", "SBMU地址", 18, 4, 1, 0, None),
        ("ReqDCChrgMode", "DC充电控制电流请求模式", 22, 2, 1, 0, {0: "Not DC Charging", 1: "CC Charging", 2: "CV Charging"}),
        ("PackDispSOC", "高精度显示SOC", 24, 16, 0.002, 0, {120: "invalid"}),
        ("PackRealSOH", "真实SOH", 40, 8, 1, 0, {255: "Null"}),
        ("SysFltLvl", "故障等级", 48, 4, 1, 0, {0: "Normal", 1: "Level 1", 2: "Level 2", 3: "Level 3"}),
        ("MainAllowPwrOn", "主回路允许上高压", 52, 2, 1, 0, VL_OK),
        ("AuxAllowPwrOn", "辅件回路允许上高压", 54, 2, 1, 0, VL_OK),
        ("ReqDCChrgStop", "直流充电请求停止标志", 56, 1, 1, 0, {0: "No Request Charge Stop", 1: "Request Charge Stop"}),
        ("StsSysFltID", "BMS内部唯一识别故障码(故障列表)", 57, 7, 1, 0, None),
    ]),
    # S2P_ALARM1 0x040241(4A~4D) SBLE 100ms
    "40241": ("S2P_ALARM1", "SBLE", 100, [
        ("AL1CRC", "SBMU状态报文的CRC", 0, 8, 1, 0, None),
        ("AL1ALIV", "SBMU生命信号,0~15循环", 8, 4, 1, 0, None),
        ("AL1CellOverVolt", "单体过压报警", 12, 2, 1, 0, VL_LVL3),
        ("AL1CellUnderVolt", "单体欠压报警", 14, 2, 1, 0, VL_LVL3),
        ("AL1CellOverTemp", "单体过温报警", 16, 2, 1, 0, VL_LVL3),
        ("AL1CellUnderTemp", "单体低温报警", 18, 2, 1, 0, VL_LVL3),
        ("AL1PackOverVolt", "箱体过压报警(总电压)", 20, 2, 1, 0, VL_LVL3),
        ("AL1PackUnderVolt", "箱体欠压报警(总电压)", 22, 2, 1, 0, VL_LVL3),
        ("AL1ChrgOverCurrFlt", "充电过流报警", 24, 2, 1, 0, VL_LVL3),
        ("AL1BranDchrgOvrCurFlt", "支路放电过流报警", 26, 2, 1, 0, VL_LVL3),
        ("AL1PackDchrgOvrCurFlt", "Pack放电过流报警", 28, 2, 1, 0, VL_LVL3),
        ("AL1BranRechrgOvrCurFlt", "支路回充电流超限", 30, 2, 1, 0, VL_LVL3),
        ("AL1PackRechrgOvrCurFlt", "Pack回充电流超限", 32, 2, 1, 0, VL_LVL3),
        ("AL1ContBranReOvrCurFlt", "行车持续充电支路回充过流", 34, 2, 1, 0, VL_LVL3),
        ("AL1ContPackReOvrCurFlt", "行车持续充电Pack回充过流", 36, 2, 1, 0, VL_LVL3),
        ("AL1ContBranDisOvrCurFlt", "行车持续放电支路放电过流", 38, 2, 1, 0, VL_LVL3),
        ("AL1ContPackDisOvrCurFlt", "行车持续充电Pack放电过流", 40, 2, 1, 0, VL_LVL3),
        ("AL1PackOverSOC", "SOC过高报警", 42, 2, 1, 0, {0: "No Alarm", 1: "Alarm", 3: "Invalid Value"}),
        ("AL1PackUnderSOC", "SOC过低报警", 44, 2, 1, 0, VL_LVL3),
        ("AL1BranSumVoltOvrDiff", "单支路累加和压差过大(并联支路之间)", 46, 2, 1, 0, VL_LVL3),
        ("AL1IsoResLowFlt", "绝缘阻抗报警", 48, 2, 1, 0, VL_LVL3),
        ("AL1CellVoltOverDiff", "单体压差过大", 50, 2, 1, 0, VL_LVL3),
        ("AL1BranchSOCOverDiff", "SOC差异过大(并联支路之间)", 52, 2, 1, 0, VL_LVL3),
        ("AL1CellTempOverDiff", "单体温差过大", 54, 2, 1, 0, VL_LVL3),
        ("AL1RTCFlt", "实时时钟故障", 56, 1, 1, 0, VL_FLT),
        ("AL1InnerCommonFlt", "内部通信故障(电流报文丢失/菊花链通讯丢失/HVB报文丢失)", 57, 1, 1, 0, VL_FLT),
        ("AL1BalaCircuitFlt", "均衡电路故障", 58, 1, 1, 0, VL_FLT),
        ("AL1WaterCoolWarn", "水冷告警", 59, 1, 1, 0, VL_FLT),
        ("AL1CellVoltSampErr", "单体电压采样异常", 60, 1, 1, 0, VL_FLT),
        ("AL1CellTempSampErr", "电芯温度采样异常", 61, 1, 1, 0, VL_FLT),
        ("AL1CellSOCOverDiff", "单体SOC差异过大", 62, 2, 1, 0, VL_LVL3),
    ]),
    # S2P_ALARM2 0x040341(4A~4D) SBLE 100ms
    "40341": ("S2P_ALARM2", "SBLE", 100, [
        ("AL2CRC", "SBMU状态报文的CRC", 0, 8, 1, 0, None),
        ("AL2ALIV", "SBMU生命信号,0~15循环", 8, 4, 1, 0, None),
        ("AL2SampLineOpnFlg", "采样线开路报警", 12, 1, 1, 0, VL_FLT),
        ("AL2VoltOutOfRangeFlg", "电压超范围报警", 13, 1, 1, 0, VL_FLT),
        ("AL2SysNTCMinorFlt", "温度采样NTC轻微报警", 14, 1, 1, 0, VL_FLT),
        ("AL2SysNTCSeriousFlt", "温度采样NTC严重报警", 15, 1, 1, 0, VL_FLT),
        ("AL2DaisyChainComLost", "菊花链通讯丢失故障", 16, 1, 1, 0, VL_FLT),
        ("AL2PackSOCJumpFlt", "Pack SOC跳变故障", 17, 1, 1, 0, VL_FLT),
        ("AL2HeatFlmFlt", "加热回路异常故障", 18, 1, 1, 0, VL_FLT),
        ("AL2BranchMsdOffWarn", "支路断路故障", 19, 2, 1, 0, VL_FLT),
        ("AL2SysParaNotMatchFlt", "可充电储能系统不匹配故障", 21, 2, 1, 0, VL_FLT),
        ("AL2ChrgOvrDisCurrFlt", "充电时放电电流过大", 23, 2, 1, 0, VL_FLT),
        ("AL2ChrgOvrCurrLowTFlt", "总回路充电过流(低温CC状态)", 25, 2, 1, 0, VL_FLT),
        ("AL2ChrgOvrCurrNormTFlt", "总回路充电过流(非低温CC状态)", 27, 2, 1, 0, VL_FLT),
        ("AL2FireProbeFlt", "火警探测器内部故障", 29, 1, 1, 0, VL_FLT),
        ("AL2FireProbeComFlt", "火警探测器通信故障", 30, 1, 1, 0, VL_FLT),
        ("AL2CurrSensorFlt", "电流传感器内部故障", 31, 1, 1, 0, VL_FLT),
        ("AL2ACANComFlt", "ACAN通讯故障", 32, 1, 1, 0, VL_FLT),
        ("AL2CSUCommLostFlg", "电流传感器通讯丢失", 33, 1, 1, 0, VL_FLT),
        ("AL2HVBMsgTimeOut", "HVB通信故障", 34, 1, 1, 0, VL_FLT),
        ("AL2SCANLostFlg", "SCAN通信故障", 35, 1, 1, 0, VL_FLT),
        ("AL2BSPEOverTempFlt", "电池自保护极限过温故障", 36, 1, 1, 0, VL_FLT),
        ("AL2BSPEOverVoltFlt", "电池自保护极限过压故障", 37, 1, 1, 0, VL_FLT),
        ("AL2BSPEUnderVoltFlt", "电池自保护极限欠压故障", 38, 1, 1, 0, VL_FLT),
        ("AL2FireAlarmFlt", "火灾报警故障", 39, 1, 1, 0, VL_FLT),
        ("AL2BMUPwrFlt", "SBMU供电电压故障", 40, 1, 1, 0, VL_FLT),
        ("AL2HvilFlt", "高压互锁故障", 41, 1, 1, 0, VL_FLT),
        ("AL2BSPEAllFlt", "电池自保护极限故障", 42, 1, 1, 0, VL_FLT),
        ("AL2InnerHVOpnCircuitFlt", "内侧高压回路断路故障", 43, 1, 1, 0, VL_FLT),
        ("AL2CellOverDisChrgWarn", "电芯过放故障", 44, 2, 1, 0, VL_LVL3),
        ("AL2ZZTCutOffRelayFlg", "宇通断继电器标志", 46, 1, 1, 0, VL_FLT),
        ("AL2Reserved1", "预留位", 47, 17, 1, 0, None),
    ]),
    # S2P_RelayStatus 0x040641(4A~4D) SBLE 100ms
    "40641": ("S2P_RelayStatus", "SBLE", 100, [
        ("Branch1PosRlyStatus", "支路1正继电器状态", 0, 1, 1, 0, VL_OPEN),
        ("Branch1NegRlyStatus", "支路1负继电器状态", 1, 1, 1, 0, VL_OPEN),
        ("Branch2PosRlyStatus", "支路2正继电器状态", 2, 1, 1, 0, VL_OPEN),
        ("Branch2NegRlyStatus", "支路2负继电器状态", 3, 1, 1, 0, VL_OPEN),
        ("Branch3PosRlyStatus", "支路3正继电器状态", 4, 1, 1, 0, VL_OPEN),
        ("Branch3NegRlyStatus", "支路3负继电器状态", 5, 1, 1, 0, VL_OPEN),
        ("Branch4PosRlyStatus", "支路4正继电器状态", 6, 1, 1, 0, VL_OPEN),
        ("Branch4NegRlyStatus", "支路4负继电器状态", 7, 1, 1, 0, VL_OPEN),
        ("MainPosRlyStatus", "主正继电器状态", 8, 1, 1, 0, VL_OPEN),
        ("MainNegRlyStatus", "主负继电器状态", 9, 1, 1, 0, VL_OPEN),
        ("PreChrgRlyStatus", "预充继电器状态", 10, 1, 1, 0, VL_OPEN),
        ("HeatPosRlyStatus", "加热正继电器状态", 11, 1, 1, 0, VL_OPEN),
        ("HeatNegRlyStatus", "加热负继电器状态", 12, 1, 1, 0, VL_OPEN),
        ("RlyStsReserved1", "预留1", 13, 3, 1, 0, None),
        ("Branch1PosRlyFlt", "支路1正继电器故障", 16, 2, 1, 0, VL_RLYF),
        ("Branch1NegRlyFlt", "支路1负继电器故障", 18, 2, 1, 0, VL_RLYF),
        ("Branch2PosRlyFlt", "支路2正继电器故障", 20, 2, 1, 0, VL_RLYF),
        ("Branch2NegRlyFlt", "支路2负继电器故障", 22, 2, 1, 0, VL_RLYF),
        ("Branch3PosRlyFlt", "支路3正继电器故障", 24, 2, 1, 0, VL_RLYF),
        ("Branch3NegRlyFlt", "支路3负继电器故障", 26, 2, 1, 0, VL_RLYF),
        ("Branch4PosRlyFlt", "支路4正继电器故障", 28, 2, 1, 0, VL_RLYF),
        ("Branch4NegRlyFlt", "支路4负继电器故障", 30, 2, 1, 0, VL_RLYF),
        ("MainPosRlyFlt", "主正继电器故障", 32, 2, 1, 0, VL_RLYF),
        ("MainNegRlyFlt", "主负继电器故障", 34, 2, 1, 0, VL_RLYF),
        ("PreChrgPosRlyFlt", "预充继电器故障", 36, 2, 1, 0, VL_RLYF),
        ("HeatPosRlyFlt", "加热正继电器故障", 38, 2, 1, 0, VL_RLYF),
        ("HeatNegRlyFlt", "加热负继电器故障", 40, 2, 1, 0, VL_RLYF),
        ("Branch1PosRlyCoilFlt", "支路1正继电器线圈故障", 42, 1, 1, 0, VL_FLT),
        ("Branch1NegRlyCoilFlt", "支路1负继电器线圈故障", 43, 1, 1, 0, VL_FLT),
        ("Branch2PosRlyCoilFlt", "支路2正继电器线圈故障", 44, 1, 1, 0, VL_FLT),
        ("Branch2NegRlyCoilFlt", "支路2负继电器线圈故障", 45, 1, 1, 0, VL_FLT),
        ("Branch3PosRlyCoilFlt", "支路3正继电器线圈故障", 46, 1, 1, 0, VL_FLT),
        ("Branch3NegRlyCoilFlt", "支路3负继电器线圈故障", 47, 1, 1, 0, VL_FLT),
        ("Branch4PosRlyCoilFlt", "支路4正继电器线圈故障", 48, 1, 1, 0, VL_FLT),
        ("Branch4NegRlyCoilFlt", "支路4负继电器线圈故障", 49, 1, 1, 0, VL_FLT),
        ("MainPosRlyCoilFlt", "主正继电器线圈故障", 50, 1, 1, 0, VL_FLT),
        ("MainNegRlyCoilFlt", "主负继电器线圈故障", 51, 1, 1, 0, VL_FLT),
        ("PreChrgPosRlyCoilFlt", "预充继电器线圈故障", 52, 1, 1, 0, VL_FLT),
        ("HeatPosRlyCoilFlt", "加热正继电器线圈故障", 53, 1, 1, 0, VL_FLT),
        ("HeatNegRlyCoilFlt", "加热负继电器线圈故障", 54, 1, 1, 0, VL_FLT),
        ("RlyStsReserved2", "预留2", 55, 9, 1, 0, None),
    ]),
    # S2P_RunStatusInfo 0x040841(4A~4D) SBLE 50ms
    "40841": ("S2P_RunStatusInfo", "SBLE", 50, [
        ("PackSoc", "Pack真实SOC(高精度)", 0, 16, 0.002, 0, {120: "invalid"}),
        ("RunStatusInfo_Reserved1", "预留", 16, 16, 1, 0, None),
        ("RunStatusInfo_Reserved2", "预留", 32, 32, 1, 0, None),
    ]),
    # S2P_VehInfo1 0x0C05FF41 SBLE 500ms
    "C05FF41": ("S2P_VehInfo1", "SBLE", 500, [
        ("S2PVehInfo1CRC", "MBMU控制指令1的CRC", 0, 8, 1, 0, None),
        ("S2PVehInfo1ALIV", "MBMU控制指令1的生命信号,0~15循环", 8, 4, 1, 0, None),
        ("S2PVehInfo1_SBMUNo", "SBMU号", 12, 4, 1, 0, {0: "Invalid", 1: "SBMU1", 2: "SBMU2", 3: "SBMU3", 4: "SBMU4", 15: "All SBMU"}),
        ("S2PVehTotalOdometer", "车辆总里程信息", 16, 32, 0.1, 0, None),
        ("S2PVehStatus", "车速", 48, 8, 1, 0, None),
        ("S2PVehInfo1_Reserved", "预留", 56, 8, 1, 0, None),
    ]),
    # S2P_Resrved 0x0C06FF41 SBLE 500ms
    "C06FF41": ("S2P_Resrved", "SBLE", 500, [
        ("S2PResrved_Reserved1", "预留", 0, 32, 1, 0, None),
        ("S2PResrved_Reserved2", "预留", 32, 32, 1, 0, None),
    ]),
    # S2P_VehInfo2 0x0C01BE41 SBLE 500ms
    "C01BE41": ("S2P_VehInfo2", "SBLE", 500, [
        ("S2PVehInfo2ALIV", "MBMU控制指令1的生命信号,0~15循环", 0, 4, 1, 0, None),
        ("S2PBattSwappingAllw", "电池系统允许换电标志位(热失控故障不允许换电,其它可以)", 4, 2, 1, 0, {0: "不允许", 1: "允许"}),
        ("S2PSystemHVOnStatus", "电池系统高压状态", 6, 2, 1, 0, {0: "HV open", 1: "HV closed"}),
        ("S2PGearSts", "挂N挡状态", 8, 2, 1, 0, {0: "默认值", 1: "N档", 2: "非N档"}),
        ("S2PEPBWorkingSts", "驻车制动状态(车辆手刹/电子手刹状态)", 10, 2, 1, 0, {0: "默认值", 1: "未制动", 2: "制动"}),
        ("S2PBrakeSwitchSts", "制动器状态(车辆刹车踏板状态)", 12, 2, 1, 0, {0: "默认值", 1: "未制动", 2: "制动"}),
        ("S2PDoorSts", "车门开关状态", 14, 2, 1, 0, {0: "默认值", 1: "全部车门关闭", 2: "未关闭全部车门"}),
        ("S2PSteeringWheelAngle", "转向角角度", 16, 16, 0.1, -3000, None),
        ("S2PL2distance", "L2距离", 32, 32, 1, 0, None),
    ]),
    # S2P_SwapInfo1 0x0C02BE41 SBLE 1000ms
    "C02BE41": ("S2P_SwapInfo1", "SBLE", 1000, [
        ("S2PHVPwrOffReq_Feedback", "收到下高压请求", 0, 1, 1, 0, VL_FB),
        ("S2PSysHVOnStatus", "系统下高压结果", 1, 2, 1, 0, {0: "默认", 1: "HV closed", 2: "HV open"}),
        ("S2PBATLVPowDwnReq_Feedback", "收到电池低压下电请求", 3, 1, 1, 0, VL_FB),
        ("S2PBATLVPowDwnStatus", "电池低压下电结果", 4, 2, 1, 0, VL_STS),
        ("S2PSwapSelfCheckReq_Feedback", "收到自检请求", 6, 1, 1, 0, VL_FB),
        ("S2PSwapSelfCheckSts", "自检结果", 7, 2, 1, 0, VL_STS),
        ("S2PContrlVehHVONFlg_Feedback", "收到站控控制车辆上高压标志", 9, 1, 1, 0, VL_FB),
        ("S2PFltClearingReq_Feedback", "收到故障清除请求", 10, 1, 1, 0, VL_FB),
        ("S2PFltClearingSts", "故障清除结果", 11, 2, 1, 0, VL_STS),
        ("S2PWLDOpenReq_Feedback", "MBMU收到蓝牙请求断开", 13, 1, 1, 0, VL_FB),
        ("S2PSysSubInfoOutClrReq_Feedback", "收到站外系统小计信息清除请求", 14, 1, 1, 0, VL_FB),
        ("S2PSysSubInfoOutClrSts", "站外系统小计信息清除结果", 15, 2, 1, 0, VL_STS),
        ("S2PSwapingIndex_Result", "换电时系统编码结果", 17, 2, 1, 0, VL_STS),
        ("S2PSwapInfo1_Reserve1", "预留", 19, 13, 1, 0, None),
        ("S2PSwapInfo1_Reserve2", "预留", 32, 32, 1, 0, None),
    ]),
    # S2P_SwapInfo2 0x0C03BE41 SBLE 1000ms
    "C03BE41": ("S2P_SwapInfo2", "SBLE", 1000, [
        ("S2PHVOFFFailReason", "下高压失败原因ID", 0, 32, 1, 0, None),
        ("S2PSwapSelfChckFailReason", "自检失败原因ID", 32, 32, 1, 0, None),
    ]),
    # S2P_SwapInfo3 0x0C04BE41 SBLE 1000ms
    "C04BE41": ("S2P_SwapInfo3", "SBLE", 1000, [
        ("S2PSysSubTotalChrgTimeOutStat", "电池系统小计站外插枪充电次数", 0, 16, 1, 0, None),
        ("S2PSysAccuChrgTimeOutStation", "电池系统累计站外插枪充电次数", 16, 32, 1, 0, None),
        ("S2PSwapInfo3_Reserved", "预留", 48, 16, 1, 0, None),
    ]),
    # S2P_SwapInfo4 0x0C05BE41 SBLE 1000ms
    "C05BE41": ("S2P_SwapInfo4", "SBLE", 1000, [
        ("S2PBMSMostCriticalFltLvl", "电池系统最高故障等级", 0, 2, 1, 0, None),
        ("S2PBMSMostCriticalFltID", "电池系统最高故障等级ID", 2, 10, 1, 0, None),
        ("S2P_TroubleCode", "故障代码(具体故障码参考Sheet:U2P_ALARM_AL_Trouble_Code)", 12, 10, 1, 0, None),
        ("S2PBCU_ALIV", "BCU生命信号,0~15循环", 22, 4, 1, 0, None),
        ("S2PBlockingSystemStatus", "封堵系统状态", 26, 4, 1, 0, {0: "默认", 1: "1个封堵", 2: "2个封堵"}),
        ("S2PBlocking2Status", "封堵机构2状态", 30, 4, 1, 0, {0: "默认", 1: "关闭", 2: "打开"}),
        ("S2PBlocking3Status", "封堵机构3状态", 34, 4, 1, 0, {0: "默认", 1: "关闭", 2: "打开"}),
        ("S2PBlockSysTroubleCode", "封堵机构系统故障码", 38, 8, 1, 0, None),
        ("S2PBlock2SysFltLevel", "封堵机构2故障等级", 46, 2, 1, 0, {0: "无故障", 1: "一级故障", 2: "二级故障", 3: "三级故障"}),
        ("S2PBlock3SysFltLevel", "封堵机构3故障等级", 48, 2, 1, 0, {0: "无故障", 1: "一级故障", 2: "二级故障", 3: "三级故障"}),
        ("S2PBCUPwrVolt", "BCU供电电压", 50, 8, 0.2, 0, None),
        ("S2PBCUSelfCheckSts", "BCU硬件自检状态", 58, 4, 1, 0, None),
        ("S2PSwapBattySystInstNum", "换电电池系统安装个数", 62, 2, 1, 0, {0: "无效", 1: "1个", 2: "2个", 3: "3个"}),
    ]),
    # S2P_SwapInfo5 0x0C06BE41 SBLE 1000ms
    "C06BE41": ("S2P_SwapInfo5", "SBLE", 1000, [
        ("S2PMBMUSWVFrameIndex", "MBMU软件版本号报文的帧序号", 0, 8, 1, 0, VL_FRM),
        ("S2PMBMUSWVByteN", "MBMU软件版本号(共16字节)报文字节N(ASCII)", 8, 8, 1, 0, VL_INV),
        ("S2PMBMUSWVByteN1", "MBMU软件版本号(共16字节)报文字节N1(ASCII)", 16, 8, 1, 0, VL_INV),
        ("S2PMBMUSWVByteN2", "MBMU软件版本号(共16字节)报文字节N2(ASCII)", 24, 8, 1, 0, VL_INV),
        ("S2PMBMUSWVByteN3", "MBMU软件版本号(共16字节)报文字节N3(ASCII)", 32, 8, 1, 0, VL_INV),
        ("S2PMBMUSWVByteN4", "MBMU软件版本号(共16字节)报文字节N4(ASCII)", 40, 8, 1, 0, VL_INV),
        ("S2PMBMUSWVByteN5", "MBMU软件版本号(共16字节)报文字节N5(ASCII)", 48, 8, 1, 0, VL_INV),
        ("S2PMBMUSWVByteN6", "MBMU软件版本号(共16字节)报文字节N6(ASCII)", 56, 8, 1, 0, VL_INV),
    ]),
    # S2P_SwapInfo6 0x0C07BE41 SBLE 1000ms
    "C07BE41": ("S2P_SwapInfo6", "SBLE", 1000, [
        ("S2PMBMUHWVFrameIndex", "MBMU硬件版本号报文的帧序号", 0, 8, 1, 0, VL_FRM),
        ("S2PMBMUHWVByteN", "MBMU硬件版本号(共16字节)报文字节N(ASCII)", 8, 8, 1, 0, VL_INV),
        ("S2PMBMUHWVByteN1", "MBMU硬件版本号(共16字节)报文字节N1(ASCII)", 16, 8, 1, 0, VL_INV),
        ("S2PMBMUHWVByteN2", "MBMU硬件版本号(共16字节)报文字节N2(ASCII)", 24, 8, 1, 0, VL_INV),
        ("S2PMBMUHWVByteN3", "MBMU硬件版本号(共16字节)报文字节N3(ASCII)", 32, 8, 1, 0, VL_INV),
        ("S2PMBMUHWVByteN4", "MBMU硬件版本号(共16字节)报文字节N4(ASCII)", 40, 8, 1, 0, VL_INV),
        ("S2PMBMUHWVByteN5", "MBMU硬件版本号(共16字节)报文字节N5(ASCII)", 48, 8, 1, 0, VL_INV),
        ("S2PMBMUHWVByteN6", "MBMU硬件版本号(共16字节)报文字节N6(ASCII)", 56, 8, 1, 0, VL_INV),
    ]),
    # S2P_VINCode 0x0C08BE41 SBLE 1000ms
    "C08BE41": ("S2P_VINCode", "SBLE", 1000, [
        ("S2PVIN_FrameNo", "VIN帧序号", 0, 8, 1, 0, {1: "Frame1", 2: "Frame2", 3: "Frame3"}),
        ("S2PVIN_B1_8_15", "车辆VIN码1,8,15字符(ASCII码)", 8, 8, 1, 0, VL_ASCII),
        ("S2PVIN_B2_9_16", "车辆VIN码2,9,16字符(ASCII码)", 16, 8, 1, 0, VL_ASCII),
        ("S2PVIN_B3_10_17", "车辆VIN码3,10,17字符(ASCII码)", 24, 8, 1, 0, VL_ASCII),
        ("S2PVIN_B4_11", "车辆VIN码4,11字符(ASCII码)", 32, 8, 1, 0, VL_ASCII),
        ("S2PVIN_B5_12", "车辆VIN码5,12字符(ASCII码)", 40, 8, 1, 0, VL_ASCII),
        ("S2PVIN_B6_13", "车辆VIN码6,13字符(ASCII码)", 48, 8, 1, 0, VL_ASCII),
        ("S2PVIN_B7_14", "车辆VIN码7,14字符(ASCII码)", 56, 8, 1, 0, VL_ASCII),
    ]),
    # S2P_SwapInfo7 0x0C09BE41 SBLE 500ms
    "C09BE41": ("S2P_SwapInfo7", "SBLE", 500, [
        ("S2PWLDRuquest_Feedback", "收到蓝牙连接请求", 0, 1, 1, 0, VL_FB),
        ("S2PWLDRuquestStatus", "蓝牙连接请求执行结果", 1, 2, 1, 0, VL_STS),
        ("S2PWLDOpenRuquest_Feedback", "SBLE收到蓝牙断开请求", 3, 1, 1, 0, VL_FB),
        ("S2PWLDOpenRuquestStatus", "蓝牙断开请求执行结果", 4, 2, 1, 0, VL_STS),
        ("S2PWLDFailReason", "SBLE和VBLE建立连接执行失败原因", 6, 8, 1, 0, None),
        ("S2PWLDOpenFailReason", "SBLE和VBLE断开连接执行失败原因", 14, 8, 1, 0, None),
        ("S2PCommutSignInRuquest", "客户端请求通信登录", 22, 8, 1, 0, None),
        ("S2PSwapInfo7_Reserve1", "预留", 30, 18, 1, 0, None),
        ("S2PSwapInfo7_Reserve2", "预留", 48, 16, 1, 0, None),
    ]),
    # P2S_SwapInfo 0x0C0141EF PC 500ms
    "C0141EF": ("P2S_SwapInfo", "PC", 500, [
        ("P2SStionCtrler_AlIV", "站控生命信号,0~15循环", 0, 4, 1, 0, None),
        ("P2SSwapProcessSts", "换电进程状态", 4, 8, 1, 0, {
            0: "默认", 1: "车辆认证", 2: "车辆自由度调整", 3: "车辆举升",
            4: "1包拆卸完成", 5: "1包安装完成", 6: "2包拆卸完成", 7: "2包安装完成",
            8: "3包拆卸完成", 9: "3包安装完成", 10: "车辆自检 (车辆回位)", 11: "换电成功",
            12: "换电失败", 13: "换电暂停"}),
        ("P2SWLDRuquest", "请求连接", 12, 1, 1, 0, {0: "默认", 1: "已请求"}),
        ("P2SSwapInfo_Reserve2", "预留", 13, 2, 1, 0, None),
        ("P2SVehicleInPlaceSts", "车辆到位状态", 15, 1, 1, 0, {0: "车辆未停靠到指定位置", 1: "车辆已停靠到指定位置"}),
        ("P2SHVPwrOffRuquest", "请求下高压", 16, 1, 1, 0, {0: "默认", 1: "已请求"}),
        ("P2SBATLVPowDwnRuquest", "电池低压下电请求", 17, 1, 1, 0, {0: "默认", 1: "已请求"}),
        ("P2SInstallPackNum", "电池包安装个数", 18, 2, 1, 0, {0: "0", 1: "1", 2: "2", 3: "3"}),
        ("P2SInstallPack1Loc", "电池包1安装状态", 20, 2, 1, 0, {0: "未安装电池包", 1: "真包", 2: "假包"}),
        ("P2SInstallPack2Loc", "电池包2安装状态", 22, 2, 1, 0, {0: "未安装电池包", 1: "真包", 2: "假包"}),
        ("P2SInstallPack3Loc", "电池包3安装状态", 24, 2, 1, 0, {0: "未安装电池包", 1: "真包", 2: "假包"}),
        ("P2SSwapSelfCheckRuquest", "请求自检", 26, 1, 1, 0, {0: "默认", 1: "已请求"}),
        ("P2SContrlVehicleHVONFlg", "站控控制车辆上高压标志", 27, 2, 1, 0, {0: "默认", 1: "允许", 2: "不允许"}),
        ("P2SFltClearingRuquest", "请求故障清除", 29, 2, 1, 0, {0: "默认值", 1: "清除不存储NVM的故障", 2: "清除所有故障 (包含存储NVM和不存储NVM)"}),
        ("P2SWLDOpenRuquest", "请求断开", 31, 1, 1, 0, {0: "默认", 1: "已请求"}),
        ("P2SSubInfoOutClrRuquest", "请求站外小计信息清除", 32, 1, 1, 0, {0: "默认", 1: "已请求"}),
        ("P2SSwapInfo_Reserve1", "预留", 33, 31, 1, 0, None),
    ]),
    # P2S_SwapInfo1 0x0C0241EF PC 500ms
    "C0241EF": ("P2S_SwapInfo1", "PC", 500, [
        ("P2SCommutSignInRuqStat", "服务端应答登录请求", 0, 1, 1, 0, {0: "失败", 1: "成功"}),
        ("P2SCommutSignInFailReason", "登录失败的原因", 1, 8, 1, 0, None),
        ("P2SSwapInfo1_Reserve1", "预留", 9, 23, 1, 0, None),
        ("P2SSwapInfo1_Reserve2", "预留", 32, 32, 1, 0, None),
    ]),
    # S2P_VBLEMAC 0x0C0241BE SBLE 1000ms
    "C0241BE": ("S2P_VBLEMAC", "SBLE", 1000, [
        ("S2PVBLE_MAC_Byte1", "VBLE_MAC地址字节1", 0, 8, 1, 0, VL_INV),
        ("S2PVBLE_MAC_Byte2", "VBLE_MAC地址字节2", 8, 8, 1, 0, VL_INV),
        ("S2PVBLE_MAC_Byte3", "VBLE_MAC地址字节3", 16, 8, 1, 0, VL_INV),
        ("S2PVBLE_MAC_Byte4", "VBLE_MAC地址字节4", 24, 8, 1, 0, VL_INV),
        ("S2PVBLE_MAC_Byte5", "VBLE_MAC地址字节5", 32, 8, 1, 0, VL_INV),
        ("S2PVBLE_MAC_Byte6", "VBLE_MAC地址字节6", 40, 8, 1, 0, VL_INV),
        ("S2PVBLE_Resered", "预留", 48, 16, 1, 0, None),
    ]),
    # S2P_VBLESWVer 0x0C0341BE SBLE 1000ms
    "C0341BE": ("S2P_VBLESWVer", "SBLE", 1000, [
        ("S2PVBLESWVFrameIndex", "VBLE软件版本号报文的帧序号", 0, 8, 1, 0, VL_FRM),
        ("S2PVBLESWVByteN", "VBLE软件版本号(共16字节)报文字节N(ASCII)", 8, 8, 1, 0, VL_INV),
        ("S2PVBLESWVByteN1", "VBLE软件版本号(共16字节)报文字节N1(ASCII)", 16, 8, 1, 0, VL_INV),
        ("S2PVBLESWVByteN2", "VBLE软件版本号(共16字节)报文字节N2(ASCII)", 24, 8, 1, 0, VL_INV),
        ("S2PVBLESWVByteN3", "VBLE软件版本号(共16字节)报文字节N3(ASCII)", 32, 8, 1, 0, VL_INV),
        ("S2PVBLESWVByteN4", "VBLE软件版本号(共16字节)报文字节N4(ASCII)", 40, 8, 1, 0, VL_INV),
        ("S2PVBLESWVByteN5", "VBLE软件版本号(共16字节)报文字节N5(ASCII)", 48, 8, 1, 0, VL_INV),
        ("S2PVBLESWVByteN6", "VBLE软件版本号(共16字节)报文字节N6(ASCII)", 56, 8, 1, 0, VL_INV),
    ]),
    # S2P_VBLEHWVer 0x0C0441BE SBLE 1000ms
    "C0441BE": ("S2P_VBLEHWVer", "SBLE", 1000, [
        ("S2PVBLEHWVFrameIndex", "VBLE硬件版本号报文的帧序号", 0, 8, 1, 0, VL_FRM),
        ("S2PVBLEHWVByteN", "VBLE硬件版本号(共16字节)报文字节N(ASCII)", 8, 8, 1, 0, VL_INV),
        ("S2PVBLEHWVByteN1", "VBLE硬件版本号(共16字节)报文字节N1(ASCII)", 16, 8, 1, 0, VL_INV),
        ("S2PVBLEHWVByteN2", "VBLE硬件版本号(共16字节)报文字节N2(ASCII)", 24, 8, 1, 0, VL_INV),
        ("S2PVBLEHWVByteN3", "VBLE硬件版本号(共16字节)报文字节N3(ASCII)", 32, 8, 1, 0, VL_INV),
        ("S2PVBLEHWVByteN4", "VBLE硬件版本号(共16字节)报文字节N4(ASCII)", 40, 8, 1, 0, VL_INV),
        ("S2PVBLEHWVByteN5", "VBLE硬件版本号(共16字节)报文字节N5(ASCII)", 48, 8, 1, 0, VL_INV),
        ("S2PVBLEHWVByteN6", "VBLE硬件版本号(共16字节)报文字节N6(ASCII)", 56, 8, 1, 0, VL_INV),
    ]),
    # S2P_SBLEMAC 0x0C0641BE SBLE 1000ms
    "C0641BE": ("S2P_SBLEMAC", "SBLE", 1000, [
        ("S2PSBLE_MAC_Byte1", "SBLE_MAC地址字节1", 0, 8, 1, 0, VL_FRM),  # PDF原表值如此(疑为笔误)
        ("S2PSBLE_MAC_Byte2", "SBLE_MAC地址字节2", 8, 8, 1, 0, VL_INV),
        ("S2PSBLE_MAC_Byte3", "SBLE_MAC地址字节3", 16, 8, 1, 0, VL_INV),
        ("S2PSBLE_MAC_Byte4", "SBLE_MAC地址字节4", 24, 8, 1, 0, VL_INV),
        ("S2PSBLE_MAC_Byte5", "SBLE_MAC地址字节5", 32, 8, 1, 0, VL_INV),
        ("S2PSBLE_MAC_Byte6", "SBLE_MAC地址字节6", 40, 8, 1, 0, VL_INV),
        ("S2PSBLE_Resered", "预留", 48, 16, 1, 0, None),
    ]),
    # S2P_SBLESWVer 0x0C0741BE SBLE 1000ms
    "C0741BE": ("S2P_SBLESWVer", "SBLE", 1000, [
        ("S2PSBLESWVFrameIndex", "SBLE软件版本号报文的帧序号", 0, 8, 1, 0, VL_FRM),
        ("S2PSBLESWVByteN", "SBLE软件版本号(共16字节)报文字节N(ASCII)", 8, 8, 1, 0, VL_INV),
        ("S2PSBLESWVByteN1", "SBLE软件版本号(共16字节)报文字节N1(ASCII)", 16, 8, 1, 0, VL_INV),
        ("S2PSBLESWVByteN2", "SBLE软件版本号(共16字节)报文字节N2(ASCII)", 24, 8, 1, 0, VL_INV),
        ("S2PSBLESWVByteN3", "SBLE软件版本号(共16字节)报文字节N3(ASCII)", 32, 8, 1, 0, VL_INV),
        ("S2PSBLESWVByteN4", "SBLE软件版本号(共16字节)报文字节N4(ASCII)", 40, 8, 1, 0, VL_INV),
        ("S2PSBLESWVByteN5", "SBLE软件版本号(共16字节)报文字节N5(ASCII)", 48, 8, 1, 0, VL_INV),
        ("S2PSBLESWVByteN6", "SBLE软件版本号(共16字节)报文字节N6(ASCII)", 56, 8, 1, 0, VL_INV),
    ]),
    # S2P_SBLEHWVer 0x0C0841BE SBLE 1000ms
    "C0841BE": ("S2P_SBLEHWVer", "SBLE", 1000, [
        ("S2PSBLEHWVFrameIndex", "SBLE硬件版本号报文的帧序号", 0, 8, 1, 0, VL_FRM),
        ("S2PSBLEHWVByteN", "SBLE硬件版本号(共16字节)报文字节N(ASCII)", 8, 8, 1, 0, VL_INV),
        ("S2PSBLEHWVByteN1", "SBLE硬件版本号(共16字节)报文字节N1(ASCII)", 16, 8, 1, 0, VL_INV),
        ("S2PSBLEHWVByteN2", "SBLE硬件版本号(共16字节)报文字节N2(ASCII)", 24, 8, 1, 0, VL_INV),
        ("S2PSBLEHWVByteN3", "SBLE硬件版本号(共16字节)报文字节N3(ASCII)", 32, 8, 1, 0, VL_INV),
        ("S2PSBLEHWVByteN4", "SBLE硬件版本号(共16字节)报文字节N4(ASCII)", 40, 8, 1, 0, VL_INV),
        ("S2PSBLEHWVByteN5", "SBLE硬件版本号(共16字节)报文字节N5(ASCII)", 48, 8, 1, 0, VL_INV),
        ("S2PSBLEHWVByteN6", "SBLE硬件版本号(共16字节)报文字节N6(ASCII)", 56, 8, 1, 0, VL_INV),
    ]),
    # S2P_SBLESignalStre 0x0C0941BE SBLE 1000ms
    "C0941BE": ("S2P_SBLESignalStre", "SBLE", 1000, [
        ("S2P_SBLE_ALIV", "SBLE生命信号,0~15循环", 0, 4, 1, 0, None),
        ("S2P_SBLE_WLDSts", "蓝牙配对状态", 4, 2, 1, 0, {0: "未连接", 1: "连接"}),
        ("S2P_DataRecSucRate", "数据接收成功率", 6, 10, 1, 0, None),
        ("S2P_BMUDataRecNum", "接收BMU数据个数", 16, 16, 1, 0, None),
        ("S2P_UplinkBlueTSignalStre", "SBLE传递给VBLE的信息的信号强度", 32, 16, 0.1, -150, None),
        ("S2P_LowerBlueTSignalStre", "VBLE传递给SBLE的信息的信号强度", 48, 16, 0.1, -150, None),
    ]),
    # P2S_VBLEMAC 0x0C0341EF PC 1000ms
    "C0341EF": ("P2S_VBLEMAC", "PC", 1000, [
        ("P2SVBLE_MAC_Byte1", "VBLE_MAC地址字节1", 0, 8, 1, 0, VL_INV),
        ("P2SVBLE_MAC_Byte2", "VBLE_MAC地址字节2", 8, 8, 1, 0, VL_INV),
        ("P2SVBLE_MAC_Byte3", "VBLE_MAC地址字节3", 16, 8, 1, 0, VL_INV),
        ("P2SVBLE_MAC_Byte4", "VBLE_MAC地址字节4", 24, 8, 1, 0, VL_INV),
        ("P2SVBLE_MAC_Byte5", "VBLE_MAC地址字节5", 32, 8, 1, 0, VL_INV),
        ("P2SVBLE_MAC_Byte6", "VBLE_MAC地址字节6", 40, 8, 1, 0, VL_INV),
        ("P2SVBLE_Resered", "预留", 48, 16, 1, 0, VL_INV),
    ]),
    # S2P_BattEnergyInfo1 0x050141(4A~4D) SBLE 1000ms
    "50141": ("S2P_BattEnergyInfo1", "SBLE", 1000, [
        ("S2PSubTotalChgEngyOutStat", "小计站外插枪充电能量", 0, 24, 0.1, 0, None),
        ("S2PSubTotalReChgeEngyOutStat", "小计站外回充能量(动能回馈充电)", 24, 24, 0.1, 0, None),
        ("S2PSubTotalchgEngyInStat", "小计站内充电能量", 48, 16, 0.1, 0, None),
    ]),
    # S2P_BattEnergyInfo2 0x050241(4A~4D) SBLE 1000ms
    "50241": ("S2P_BattEnergyInfo2", "SBLE", 1000, [
        ("S2PSubTotalDischgEngyOutStat", "小计站外放电能量", 0, 24, 0.1, 0, None),
        ("S2PSubTotalDischgEngyInStat", "小计站内放电能量", 24, 16, 0.1, 0, None),
        ("S2PSubTotalBattOdometer", "小计电池包行驶里程", 40, 24, 0.1, 0, None),
    ]),
    # S2P_BattEnergyInfo3 0x050341(4A~4D) SBLE 1000ms
    "50341": ("S2P_BattEnergyInfo3", "SBLE", 1000, [
        ("S2PSysAccuChrgEngyOutStat", "系统站外插枪充电能量(累计)", 0, 32, 0.1, 0, None),
        ("S2PSysAccuBattOdometer", "电池包行驶里程(累计)", 32, 32, 0.1, 0, None),
    ]),
    # S2P_BattEnergyInfo4 0x050441(4A~4D) SBLE 1000ms
    "50441": ("S2P_BattEnergyInfo4", "SBLE", 1000, [
        ("S2PSysAccuDisChrgEngyInStat", "系统站内放电电能量(累计)", 0, 32, 0.1, 0, None),
        ("S2PSysAccuChrgEngyInStat", "系统站内充电能量(累计)", 32, 32, 0.1, 0, None),
    ]),
    # S2P_BattEnergyInfo5 0x050541(4A~4D) SBLE 1000ms
    "50541": ("S2P_BattEnergyInfo5", "SBLE", 1000, [
        ("S2PFult1SwapContorContErr", "快换连接器连接故障", 0, 1, 1, 0, VL_FLT),
        ("S2PFult1SwapConOverTemp", "快换连接器过温报警", 1, 2, 1, 0, {0: "Normal", 1: "Level 1-Light fault", 2: "Level 2-More severe fault", 3: "Level3-Most severe fault"}),
        ("S2PFult1SwapConPTCErr", "快换连接器PTC开路或短路故障", 3, 1, 1, 0, VL_FLT),
        ("S2PSOCAvailableFlg", "SOC不可信标志(≥10Cycle不满充置出)", 4, 1, 1, 0, VL_FLT),
        ("S2PCellFullDisChrgFlg", "满放标志位", 5, 1, 1, 0, VL_FLT),
        ("S2PBattEngyInfo5_Reserved1", "预留", 6, 26, 1, 0, None),
        ("S2PBattEngyInfo5_Reserved2", "预留", 32, 32, 1, 0, None),
    ]),
    # S2P_BattEnergyInfo6 0x050641(4A~4D) SBLE 1000ms
    "50641": ("S2P_BattEnergyInfo6", "SBLE", 1000, [
        ("S2PSysAccuReChrgEngyOutStat", "系统站外回充能量(累计)", 0, 32, 0.1, 0, None),
        ("S2PSysAccuDisChrgEngyOutStat", "系统站外放电能量(累计)", 32, 32, 0.1, 0, None),
    ]),
    # S2P_SysCode 0x050741(4A~4D) SBLE 500ms
    "50741": ("S2P_SysCode", "SBLE", 500, [
        ("S2PSNFrameNo", "电池编码信息帧序号", 0, 8, 1, 0, {1: "Frame1", 2: "Frame2", 3: "Frame3", 4: "Frame4"}),
        ("S2PSNSysCodeLength", "电池编码长度", 8, 8, 1, 0, None),
        ("S2PSNPackCodeB1", "电池编码(SN)字符1,7,13,19(ASCII)", 16, 8, 1, 0, VL_ASCII),
        ("S2PSNPackCodeB2", "电池编码(SN)字符2,8,14,20(ASCII)", 24, 8, 1, 0, VL_ASCII),
        ("S2PSNPackCodeB3", "电池编码(SN)字符3,9,15,21(ASCII)", 32, 8, 1, 0, VL_ASCII),
        ("S2PSNPackCodeB4", "电池编码(SN)字符4,10,16,22(ASCII)", 40, 8, 1, 0, VL_ASCII),
        ("S2PSNPackCodeB5", "电池编码(SN)字符5,11,17,23(ASCII)", 48, 8, 1, 0, VL_ASCII),
        ("S2PSNPackCodeB6", "电池编码(SN)字符6,12,18,24(ASCII)", 56, 8, 1, 0, VL_ASCII),
    ]),
    # S2P_SwapConTempInfo 0x050841(4A~4D) SBLE 1000ms
    "50841": ("S2P_SwapConTempInfo", "SBLE", 1000, [
        ("S2PSwapConPos1Temp", "换电连接器温度检测1(放电1正)", 0, 8, 1, -40, None),
        ("S2PSwapConNeg1Temp", "换电连接器温度检测2(放电1负)", 8, 8, 1, -40, None),
        ("S2PSwapConPos2Temp", "换电连接器温度检测3(放电2正、预留)", 16, 8, 1, -40, None),
        ("S2PSwapConNeg2Temp", "换电连接器温度检测4(放电2负、预留)", 24, 8, 1, -40, None),
        ("Reserved9", "预留", 32, 32, 10, 0, None),
    ]),
}
