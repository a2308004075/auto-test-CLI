from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.act.battery_manage.one_click_out.battery_out import BatteryOut

KeyBatteryOut = {
    "电池一键出仓：执行中": HandlerKw.kw(BatteryOut.action_1),
    "电池一键出仓：执行完毕": HandlerKw.kw(BatteryOut.action_2),
    "电池一键出仓：执行错误": HandlerKw.kw(BatteryOut.action_3),
}
