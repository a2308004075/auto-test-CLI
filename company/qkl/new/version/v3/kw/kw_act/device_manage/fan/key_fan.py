from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.act.device_manage.fan.fan import Fan

KeyFan = {
    "命令编码01，风机": HandlerKw.kw(Fan.action_1),  # 参数：['slaveId', 'id', 'value']
    "命令编码02，风机": HandlerKw.kw(Fan.action_2),  # 参数：['slaveId', 'id', 'value']
    "命令编码03，风机": HandlerKw.kw(Fan.action_3),  # 参数：['slaveId', 'id', 'value']
    "命令编码04，风机": HandlerKw.kw(Fan.action_4),  # 参数：['slaveId', 'id', 'value']
}
