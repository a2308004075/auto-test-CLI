from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.act.device_manage.main_air_conditioning.main_air_conditioning import MainAirConditioning

KeyMainAirConditioning = {
    "主控室空调故障：温度上限报警": HandlerKw.kw(MainAirConditioning.action_1),
    "主控室空调故障：温度上限报警恢复": HandlerKw.kw(MainAirConditioning.action_2),
    "主控室空调故障：温度下限报警": HandlerKw.kw(MainAirConditioning.action_3),
    "主控室空调故障：温度下限报警恢复": HandlerKw.kw(MainAirConditioning.action_4),
    "主控室空调故障：第一路空调开关机失败": HandlerKw.kw(MainAirConditioning.action_5),
    "主控室空调故障：第一路空调开关机失败恢复": HandlerKw.kw(MainAirConditioning.action_6),
    "自动模式时，当当前温度≤制冷停止温度且电流真实值＞0且运行状态=制冷": HandlerKw.kw(MainAirConditioning.action_7),
    "自动模式时，当当前温度≥制热停止温度且电流真实值＞0且运行状态=制热": HandlerKw.kw(MainAirConditioning.action_8),
}
