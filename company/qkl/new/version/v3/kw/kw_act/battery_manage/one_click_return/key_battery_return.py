from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.act.battery_manage.one_click_return.battery_return import BatteryReturn

KeyBatteryReturn = {
    "电池一键入仓：执行中": HandlerKw.kw(BatteryReturn.action_1),
    "电池一键入仓：执行完毕": HandlerKw.kw(BatteryReturn.action_2),
    "电池一键入仓：执行错误": HandlerKw.kw(BatteryReturn.action_3),
}
