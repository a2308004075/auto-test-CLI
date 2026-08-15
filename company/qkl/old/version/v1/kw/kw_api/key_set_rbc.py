from common.handlerKw.handlerKw import HandlerKw
from company.qkl.old.version.v1.dao.api.set_rbc import SetRbc

KeySetRbc = {
    "SetRbc：云端换电结果下发：闽H984EC5，换电类型": HandlerKw.kw(SetRbc.rbc_certification_notifyvincmd_2),  # 参数：['changeType']
    "SetRbc：云端换电结果下发：闽H984EC5，是否允许换电": HandlerKw.kw(SetRbc.rbc_certification_notifyvincmd_1),  # 参数：['ableToChange']
    "SetRbc：换电系统复位": HandlerKw.kw(SetRbc.rbc_stationcontrol_swapreset),
    "SetRbc：车辆到位信号：是否到位": HandlerKw.kw(SetRbc.rbc_preparation_putvehicleinplace),  # 参数：['inPlace']
}
