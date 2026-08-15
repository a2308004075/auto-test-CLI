from common.http.httpRq import HttpRq
from common.http.httpMethod import HttpMethod


class ApiPlc:
    @staticmethod
    def _get_path(path):
        service = '/plc'
        return service + path

    @staticmethod
    def api_air_faultRest(data):
        """
        空调故障复位
        请求参数:
            slaveId: integer [可选]
        """
        path = f'/api/air/faultRest'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_air_getInfos(data):
        """
        获取空调信息
        """
        path = f'/api/air/getInfos'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_air_powerSwitch(data):
        """
        空调电源开关
        请求参数:
            on: boolean [可选]
            slaveId: integer [可选]
        """
        path = f'/api/air/powerSwitch'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_air_setParams(data):
        """
        设置空调参数
        请求参数:
            coolTemp: number [可选]
            coolTempDiff: number [可选]
            dehumidifyDiff: number [可选]
            dehumidifySwicth: boolean [可选]
            dehumidifyValue: number [可选]
            highHumidityAlarm: number [可选]
            highTempAlarm: number [可选]
            hotTemp: number [可选]
            hotTempDiff: number [可选]
            internalFanStatus: boolean [可选]
            lowTempAlarm: number [可选]
            slaveId: integer [可选]
        """
        path = f'/api/air/setParams'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_afterEquipmentCenteringReset(data):
        """
        设备归中后复位
        请求参数:
            backCenterAndLift: integer [可选] - 归中举升请求 0：默认值 1：请求归中举升
            controlTimeOut: integer [可选] - 下控超时时间 ms
            subType: string [可选] - 下控子类型
            timeOut: integer [可选] - 执行超时时间 ms
        """
        path = f'/api/control/afterEquipmentCenteringReset'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_allowDisassemblyBattery(data):
        """
        发送允许拆卸电池包指令
        请求参数:
            allowDisBattery: integer [可选] - 站控允许拆解电池 0:不允许 1:允许
            commandExpireTime: integer [可选]
            lastTimePackOneStatus: integer [可选] - 上次1号位电池包类别 0：默认值 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632 255-BMS数据有误
            lastTimePackTwoStatus: integer [可选] - 上次2号位电池包类别 0：默认值 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632 255-BMS数据有误
        """
        path = f'/api/control/allowDisassemblyBattery'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_allowReturnVehicle(data):
        """
        换电通道设备归位请求
        请求参数:
            subTypeEnum: string [可选] - 下控子类型枚举
            swapChannelBack: integer [可选] - 请求换电通道设备归位 0：默认值 1：请求归位
        """
        path = f'/api/control/allowReturnVehicle'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_allowVehicleEnter(data):
        """
        车辆驶入换电站请求
        请求参数:
            carModel: string [可选] - 车型代号
            sendReason: integer [可选] - 发送原因
            vehicleAccessStation: integer [可选] - 请求车辆驶入换电站 0：默认值 1：允许驶入
        """
        path = f'/api/control/allowVehicleEnter'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_allowVehicleLeave(data):
        """
        发送车辆允许驶离指令到PLC
        请求参数:
            subType: string [可选] - 下控子类型
            vehicleLeaveStationReason: integer [可选] - 请求车辆驶出换电站的原因 0：默认值 1：正常换电流程结束驶离 2：异常换电中断驶离
            vehicleLeaveStationReq: integer [可选] - 请求车辆驶出换电站 0：默认值 1：允许驶出
        """
        path = f'/api/control/allowVehicleLeave'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_api_control_plcCommandStart(data):
        """
        PLC命令启动
        请求参数:
            commandSubType: string [可选] - 下控子类型
            commandTypeVal: string [可选] - 下控类型数据 存储于缓存中
            pfk: string [可选] - 下控唯一标志
        """
        path = f'/api/control/api/control/plcCommandStart'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_backCenterAndLift(data):
        """
        归中、举升
        请求参数:
            backCenterAndLift: integer [可选] - 归中举升请求 0：默认值 1：请求归中举升
            controlTimeOut: integer [可选] - 下控超时时间 ms
            subType: string [可选] - 下控子类型
            timeOut: integer [可选] - 执行超时时间 ms
        """
        path = f'/api/control/backCenterAndLift'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_batteryMaintenance(data):
        """
        电池维护
        请求参数:
            moveInPositionNo: integer [可选] - 入仓仓位号 0：默认值 1~96：仓位号
            moveOutPositionNo: integer [可选] - 出仓仓位号 0：默认值 1~96：仓位号
            subType: string [可选] - 下控子类型
        """
        path = f'/api/control/batteryMaintenance'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_batteryMaintenanceComplete(data):
        """
        电池维护完成
        """
        path = f'/api/control/batteryMaintenanceComplete'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_batteryMaintenanceReset(data):
        """
        电池维护完成
        """
        path = f'/api/control/batteryMaintenanceReset'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_carModelInfoCache(data):
        """
        缓存车型信息
        请求参数:
            carModel: string [必填]
            carNo: string [必填]
        """
        path = f'/api/control/carModelInfoCache'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_clearBbsFault(data):
        """
        清除BBS故障
        请求参数:
            deviceNo: integer [可选] - 设备ID
            faultCode: string [可选] - 故障编码
            faultTypeEnum: string [可选] - 故障上报设备类型
            originFaultCode: string [可选] - 原始故障编码
        """
        path = f'/api/control/clearBbsFault'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_closeCircuitBreaker(data):
        """
        远程关闭断路器
        请求参数:
            circuitBreaker: integer [可选] - 远程关闭断路器 0:复位 1:关闭
        """
        path = f'/api/control/closeCircuitBreaker'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_closeOrder(data):
        """
        关闭订单
        请求参数:
            guardFlag: integer [可选] - 值守模式 1：无人看守 2：有人看守
        """
        path = f'/api/control/closeOrder'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_continueOperation(data):
        """
        暂停后重新继续
        请求参数:
            continueRequestReason: integer [可选] - 请求暂停后继续 0：默认值 1：由于车门不满足，PLC暂停后继续请求 2：由于非车门不满足，PLC暂停后继续请求
        """
        path = f'/api/control/continueOperation'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_controlBatteryOut(data):
        """
        一键出仓
        请求参数:
            batteryPackFlag: integer [可选] - 电池包状态 0：默认值 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632 255-BMS数据有误
            hasTakenBattery: integer [可选] - 请求电池出仓 0：默认值 1：请求电池出仓
            position: integer [可选] - 出仓仓位 0：默认值 1~96：仓位号
            subType: string [可选] - 下控子类型
        """
        path = f'/api/control/controlBatteryOut'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_controlBatteryOutReset(data):
        """
        一键出仓复位
        """
        path = f'/api/control/controlBatteryOutReset'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_controlBatteryReturn(data):
        """
        一键入仓
        请求参数:
            batteryPackFlag: integer [可选] - 电池包状态 0：默认值 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632 255-BMS数据有误
            hasTakenBattery: integer [可选] - 请求电池入仓 0：默认值 1：请求电池入仓
            position: integer [可选] - 入仓仓位 0：默认值 1~96：仓位号
            subType: string [可选] - 下控子类型
        """
        path = f'/api/control/controlBatteryReturn'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_controlBatteryReturnReset(data):
        """
        一键入仓复位
        """
        path = f'/api/control/controlBatteryReturnReset'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_controlExhaustFan(data):
        """
        排风扇控制
        请求参数:
            commandSubType: string [可选] - 下控子类型
            commandTypeVal: string [可选] - 下控类型数据 存储于缓存中
            fanControl: integer [可选] - 风扇控制 一代使用：0:关闭 1:开启
            fourExhaustFanControlAction: integer [可选] -  控制排风扇4动作 0：默认值 1：开启 2：关闭
            oneExhaustFanControlAction: integer [可选] -  控制排风扇1动作 0：默认值 1：开启 2：关闭
            pfk: string [可选] - 下控唯一标志
            subType: string [可选] - 下控子类型
            threeExhaustFanControlAction: integer [可选] -  控制排风扇3动作 0：默认值 1：开启 2：关闭
            twoExhaustFanControlAction: integer [可选] -  控制排风扇2动作 0：默认值 1：开启 2：关闭
        """
        path = f'/api/control/controlExhaustFan'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_controlLight(data):
        """
        灯光控制
        请求参数:
            commandSubType: string [可选] - 下控子类型
            commandTypeVal: string [可选] - 下控类型数据 存储于缓存中
            eightLightControlAction: integer [可选] -  控制照明8动作 0：默认值 1：开启 2：关闭
            fiveLightControlAction: integer [可选] -  控制照明5动作 0：默认值 1：开启 2：关闭
            fourLightControlAction: integer [可选] -  控制照明4动作 0：默认值 1：开启 2：关闭
            lightControlAction: integer [可选] - 照明控制动作 一代：0-关闭 1-开启
            lightControlAreaEnum: string [可选] - 照明控制枚举
            nineLightControlAction: integer [可选] -  控制照明9动作 0：默认值 1：开启 2：关闭
            oneLightControlAction: integer [可选] -  控制照明1动作 0：默认值 1：开启 2：关闭
            pfk: string [可选] - 下控唯一标志
            sevenLightControlAction: integer [可选] -  控制照明7动作 0：默认值 1：开启 2：关闭
            sixLightControlAction: integer [可选] -  控制照明6动作 0：默认值 1：开启 2：关闭
            subType: string [可选] - 下控子类型
            tenLightControlAction: integer [可选] -  控制照明10动作 0：默认值 1：开启 2：关闭
            threeLightControlAction: integer [可选] -  控制照明3动作 0：默认值 1：开启 2：关闭
            twoLightControlAction: integer [可选] -  控制照明2动作 0：默认值 1：开启 2：关闭
        """
        path = f'/api/control/controlLight'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_delCarModelInfoCache(data):
        """
        删除车型信息缓存
        """
        path = f'/api/control/delCarModelInfoCache'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_endSwap(data):
        """
        换电完成
        请求参数:
            endSwap: integer [可选] - 收到换电任务完成 当“PLC执行任务状态=12”，回复 1，当“PLC执行任务状态=1”，回复 0
        """
        path = f'/api/control/endSwap'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_equipmentSelfCheckReqDTO(data):
        """
        设备自检
        请求参数:
            controlTimeOut: integer [可选] - 下控超时时间 ms
            subType: string [可选] - 下控子类型
            timeOut: integer [可选] - 执行超时时间 ms
        """
        path = f'/api/control/equipmentSelfCheckReqDTO'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_exchangeBattery(data):
        """
        电池交换
        请求参数:
            moveInBatteryPackFlag: integer [可选] - 入仓电池包状态 0：默认值 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632 255-BMS数据有误
            moveInPositionNo: integer [可选] - 入仓仓位号 0：默认值 1~96：仓位号
            moveOutBatteryPackFlag: integer [可选] - 出仓电池包状态 0：默认值 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632 255-BMS数据有误
            moveOutPositionNo: integer [可选] - 出仓仓位号 0：默认值 1~96：仓位号
            subType: string [可选] - 下控子类型
        """
        path = f'/api/control/exchangeBattery'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_executeEliminateFault(data):
        """
        执行PLC故障清除命令
        请求参数:
            commandSubType: string [可选] - 下控子类型
            commandTypeVal: string [可选] - 下控类型数据 存储于缓存中
            pfk: string [可选] - 下控唯一标志
            subType: string [可选] - 下控子类型
        """
        path = f'/api/control/executeEliminateFault'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_fireBatteryEnter(data):
        """
        消防电池进入
        请求参数:
            batteryPackFlag: integer [可选] - 电池包状态 0：默认值 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632 255-BMS数据有误
            positionNo: integer [可选] - 仓位号
        """
        path = f'/api/control/fireBatteryEnter'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_fireBatteryOut(data):
        """
        消防电池出仓
        请求参数:
            batteryPackFlag: integer [可选] - 电池包状态 0：默认值 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632 255-BMS数据有误
            positionNo: integer [可选] - 仓位号
        """
        path = f'/api/control/fireBatteryOut'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_fireBatteryReturn(data):
        """
        消防电池入仓
        请求参数:
            batteryPackFlag: integer [可选] - 电池包状态 0：默认值 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632 255-BMS数据有误
            positionNo: integer [可选] - 仓位号
        """
        path = f'/api/control/fireBatteryReturn'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_fireOut(data):
        """
        消防出仓
        """
        path = f'/api/control/fireOut'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_fireReturn(data):
        """
        消防返回
        """
        path = f'/api/control/fireReturn'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_freedomDoneSync(data):
        """
        自由模式完成同步
        """
        path = f'/api/control/freedomDoneSync'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_initPlcEquip(data):
        """
        初始化PLC设备
        请求参数:
            guardFlag: integer [可选] - 值守模式 1：无人看守 2：有人看守
        """
        path = f'/api/control/initPlcEquip'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_initializationPlc(data):
        """
        PLC初始化
        """
        path = f'/api/control/initializationPlc'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_liftAndLowElectricalPlug(data):
        """
        升降低压电气插头
        请求参数:
            batteryPackFlag: integer [可选] - 电池包状态 0：默认值 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632 255-BMS数据有误
            positionNo: integer [可选] - 仓位号
        """
        path = f'/api/control/liftAndLowElectricalPlug'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_movedBatteryPosition(data):
        """
        电池移仓
        请求参数:
            batteryPackFlag: integer [可选] - 电池包状态 0：默认值 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632 255-BMS数据有误
            moveInPositionNo: integer [可选] - 入仓仓位号 0：默认值 1~96：仓位号
            moveOutPositionNo: integer [可选] - 出仓仓位号 0：默认值 1~96：仓位号
            subType: string [可选] - 下控子类型
        """
        path = f'/api/control/movedBatteryPosition'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_movedBatteryPositionReset(data):
        """
        电池移仓重置
        """
        path = f'/api/control/movedBatteryPositionReset'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_pauseOperation(data):
        """
        运动过程中暂停
        请求参数:
            pauseRequestReason: integer [可选] - 请求故障的原因 0：默认值 1：换电过程中自由度不满足导致暂停 2：站控检测到故障导致暂停 3：其他
        """
        path = f'/api/control/pauseOperation'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_plcRecipeDigestVerify(data):
        """
        PLC配方校验请求
        请求参数:
            carModel: string [可选] - 车型代号 8位
            carModelName: string [可选] - 车型代号名称
            carModelSource: integer [可选] - 车型配方来源 1:云端 2：无法获取
            vehicleModelRecipeDigest: string [可选] - 车型配方
        """
        path = f'/api/control/plcRecipeDigestVerify'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_rePickPackStatus(data):
        """
        重新取包状态
        请求参数:
            guardFlag: integer [可选] - 值守模式 1：无人看守 2：有人看守
            rePickPackStatus: integer [可选] - 重新选包状态值 0：默认值 1：选包成功 2：选包失败
        """
        path = f'/api/control/rePickPackStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_readBatteryCompartmentRecipeDigest(data):
        """
        读取电池仓配方详细信息
        请求参数:
            readBatteryCompartmentRecipeDigest: integer [可选] - 读取电池仓配方详细信息请求 0：默认值 1：请求读取
        """
        path = f'/api/control/readBatteryCompartmentRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_readRfid(data):
        """
        读取RFID
        请求参数:
            positionNo: integer [可选] - 仓位号
            type: string [可选] - 类型
        """
        path = f'/api/control/readRfid'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_readSwapBaseRecipeDigest(data):
        """
        读取换电通道基础配方详细信息
        请求参数:
            readSwapBaseRecipeDigest: integer [可选] - 读取换电通道基础配方详细信息请求 0：默认值 1：请求读取
        """
        path = f'/api/control/readSwapBaseRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_readSwapDeltaRecipeDigest(data):
        """
        读取换电通道Delta配方详细信息
        请求参数:
            carModel: string [可选] - 车型代号
            readSwapDeltaRecipeDigest: integer [可选] - 读取车型配方详细信息请求 0：默认值 1：请求读取
        """
        path = f'/api/control/readSwapDeltaRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_replyUpgrade(data):
        """
        回复升级
        """
        path = f'/api/control/replyUpgrade'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_repositionBattery(data):
        """
        电池重放
        请求参数:
            batteryPackFlag: integer [可选] - 电池包状态 0：默认值 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632 255-BMS数据有误
            repositionPositionNo: integer [可选] - 重放仓位号 0：默认值 1~96：仓位号
            subType: string [可选] - 下控子类型
        """
        path = f'/api/control/repositionBattery'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_resetPlcTask(data):
        """
        PLC复位操作接口（一代）
        请求参数:
            commandSubType: string [可选] - 下控子类型
            commandTypeVal: string [可选] - 下控类型数据 存储于缓存中
            pfk: string [可选] - 下控唯一标志
            resetPlcTaskEnum: string [可选] - 复位PLC相关任务状态点位枚举
        """
        path = f'/api/control/resetPlcTask'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_returnRecipeDigest(data):
        """
        返回配方摘要
        请求参数:
            plcPrescriptionType: integer [可选]
            result: integer [可选] - 接收结果 1：成功 2：失败
        """
        path = f'/api/control/returnRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_rgvDriveChannel(data):
        """
        RGV行驶至换电通道 (不带电池)
        请求参数:
            plcRgvControlTaskEnum: string [可选] - PLC右侧RGV入库下控枚举（一代使用）
            subType: string [可选] - 下控子类型
        """
        path = f'/api/control/rgvDriveChannel'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_rgvReturn(data):
        """
        RGV回位 (不带电池)
        请求参数:
            plcRgvControlTaskEnum: string [可选] - PLC右侧RGV出库下控枚举（一代使用）
            subType: string [可选] - 下控子类型
        """
        path = f'/api/control/rgvReturn'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_rgvReturnTake(data):
        """
        RGV回位 (带电池、一代)
        请求参数:
            plcRgvControlTaskEnum: string [可选] - PLC右侧RGV出库下控枚举（一代使用）
            subType: string [可选] - 下控子类型
        """
        path = f'/api/control/rgvReturnTake'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_scramOperation(data):
        """
        运动过程中急停
        """
        path = f'/api/control/scramOperation'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_startSwap(data):
        """
        同步换电电池信息+下发开始换电
        请求参数:
            carModel: string [可选] - 车型代码
            lastLock10RingsNum: number [可选] - 上次1号位电池包10号锁加锁圈数
            lastLock1RingsNum: number [可选] - 上次1号位电池包1号锁加锁圈数
            lastLock2RingsNum: number [可选] - 上次1号位电池包2号锁加锁圈数
            lastLock3RingsNum: number [可选] - 上次1号位电池包3号锁加锁圈数
            lastLock4RingsNum: number [可选] - 上次1号位电池包4号锁加锁圈数
            lastLock5RingsNum: number [可选] - 上次1号位电池包5号锁加锁圈数
            lastLock6RingsNum: number [可选] - 上次1号位电池包6号锁加锁圈数
            lastLock7RingsNum: number [可选] - 上次1号位电池包7号锁加锁圈数
            lastLock8RingsNum: number [可选] - 上次1号位电池包8号锁加锁圈数
            lastLock9RingsNum: number [可选] - 上次1号位电池包9号锁加锁圈数
            lastTimePackOneStatus: integer [可选] - 上次1号位电池包类别 0：默认值 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632 255-BMS数据有误
            lastTimePackTwoStatus: integer [可选] - 上次2号位电池包类别 0：默认值 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632 255-BMS数据有误
            packOneInWarehouseNo: integer [可选] - 一号入仓电池包仓位号
            packOneOutWarehouseNo: integer [可选] - 一号出仓电池包仓位号
            packTwoInWarehouseNo: integer [可选] - 二号入仓电池包仓位号
            packTwoOutWarehouseNo: integer [可选] - 二号出仓电池包仓位号
            sendType: integer [可选] - 发送原因 0：默认值 1：首次选包 2：重新选包
            thisTimePackOneStatus: integer [可选] - 本次1号位电池包类别 0：默认值 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632 255-BMS数据有误
            thisTimePackTwoStatus: integer [可选] - 本次2号位电池包类别 0：默认值 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632 255-BMS数据有误
        """
        path = f'/api/control/startSwap'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_stationAndCampInfo(data):
        """
        换电站及仓位信息数据请求
        请求参数:
            stationAndCampInfoReq: integer [可选] - 请求换电站及仓位信息数据 0：默认值 1：请求信息
        """
        path = f'/api/control/stationAndCampInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_stationAndCampInfoForeSync(data):
        """
        站点和仓位信息前置同步
        请求参数:
            campNo: integer [可选] - 1号位出仓电池包仓位号 0：默认值 1~96：仓位号
        """
        path = f'/api/control/stationAndCampInfoForeSync'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_stopFireMove(data):
        """
        停止消防移动
        请求参数:
            position: integer [可选]
        """
        path = f'/api/control/stopFireMove'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_stopReadRfid(data):
        """
        停止读取RFID
        """
        path = f'/api/control/stopReadRfid'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_switchSeasonMode(data):
        """
        季节模式控制
        请求参数:
            switchSeason: integer [可选] - 季节模式切换 0：夏季模式 1：冬季模式
        """
        path = f'/api/control/switchSeasonMode'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_syncFlowStatus(data):
        """
        同步流程状态
        请求参数:
            status: integer [可选] - 换电状态 0：默认值 1：开启 2：结束
            subType: string [可选] - 下控子类型
        """
        path = f'/api/control/syncFlowStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_syncStrategyInfo(data):
        """
        同步策略信息
        请求参数:
            language: integer [可选]
            rain: integer [可选]
            rollingStrategyEnable: integer [可选]
            snow: integer [可选]
        """
        path = f'/api/control/syncStrategyInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_syncSwapCampInfoAndSendRePickPackSuccess(data):
        """
        同步换电电池信息
        请求参数:
            carModel: string [可选] - 车型代码
            lastLock10RingsNum: number [可选] - 上次1号位电池包10号锁加锁圈数
            lastLock1RingsNum: number [可选] - 上次1号位电池包1号锁加锁圈数
            lastLock2RingsNum: number [可选] - 上次1号位电池包2号锁加锁圈数
            lastLock3RingsNum: number [可选] - 上次1号位电池包3号锁加锁圈数
            lastLock4RingsNum: number [可选] - 上次1号位电池包4号锁加锁圈数
            lastLock5RingsNum: number [可选] - 上次1号位电池包5号锁加锁圈数
            lastLock6RingsNum: number [可选] - 上次1号位电池包6号锁加锁圈数
            lastLock7RingsNum: number [可选] - 上次1号位电池包7号锁加锁圈数
            lastLock8RingsNum: number [可选] - 上次1号位电池包8号锁加锁圈数
            lastLock9RingsNum: number [可选] - 上次1号位电池包9号锁加锁圈数
            lastTimePackOneStatus: integer [可选] - 上次1号位电池包类别 0：默认值 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632 255-BMS数据有误
            lastTimePackTwoStatus: integer [可选] - 上次2号位电池包类别 0：默认值 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632 255-BMS数据有误
            packOneInWarehouseNo: integer [可选] - 一号入仓电池包仓位号
            packOneOutWarehouseNo: integer [可选] - 一号出仓电池包仓位号
            packTwoInWarehouseNo: integer [可选] - 二号入仓电池包仓位号
            packTwoOutWarehouseNo: integer [可选] - 二号出仓电池包仓位号
            sendType: integer [可选] - 发送原因 0：默认值 1：首次选包 2：重新选包
            thisTimePackOneStatus: integer [可选] - 本次1号位电池包类别 0：默认值 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632 255-BMS数据有误
            thisTimePackTwoStatus: integer [可选] - 本次2号位电池包类别 0：默认值 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632 255-BMS数据有误
        """
        path = f'/api/control/syncSwapCampInfoAndSendRePickPackSuccess'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_thermalRunawayBatteryChannel(data):
        """
        热失控电池包转移换电通道
        请求参数:
            fireMovedWarehousePositionNo: integer [可选] - 消防移仓仓位号 0：默认值 1-96: 仓位号
        """
        path = f'/api/control/thermalRunawayBatteryChannel'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_thermalRunawayBatterySandbox(data):
        """
        热失控电池包转移消防箱
        请求参数:
            barcode: string [可选]
            dataType: integer [可选]
            fireMovedWarehousePositionNo: integer [可选] - 消防移仓仓位号
            mac: string [可选]
            moveTestStatus: integer [可选]
            optUser: string [可选]
            optUserAccount: string [可选]
            packType: integer [可选] - 仓位类型
            subType: string [可选] - 下控子类型
        """
        path = f'/api/control/thermalRunawayBatterySandbox'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_touchScreenRestart(data):
        """
        触摸屏重启
        """
        path = f'/api/control/touchScreenRestart'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_writeBatteryCompartmentRecipeDigest(data):
        """
        写入电池仓配方详细信息
        请求参数:
            batteryCompartmentRecipeDigest: string [可选] - 电池仓配方
            cloudMsgId: integer [可选]
            writeBatteryCompartmentRecipeDigest: integer [可选] - 写入电池仓配方详细信息请求 0：默认值 1：请求写入
        """
        path = f'/api/control/writeBatteryCompartmentRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_writeStationModelRecipeDigest(data):
        """
        写入站点模型配方摘要
        请求参数:
            cloudMsgId: integer [可选]
            stationModelRecipeDigest: string [可选] - 站型配置配方
            writeStationModelRecipeDigest: integer [可选] - 写入站型配置详细信息请求 0：默认值 1：请求写入
        """
        path = f'/api/control/writeStationModelRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_writeStationParamRecipeDigest(data):
        """
        写入站点参数配方摘要
        请求参数:
            cloudMsgId: integer [可选]
            stationParamRecipeDigest: string [可选] - 站点参数配方 0：默认值 1：请求写入
            writeStationParamRecipeDigest: integer [可选] - 写入站点参数配方详细信息请求 0：默认值 1：请求写入
        """
        path = f'/api/control/writeStationParamRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_writeSwapBaseRecipeDigest(data):
        """
        写入换电通道基础配方详细信息
        请求参数:
            cloudMsgId: integer [可选]
            swapBaseRecipeDigest: string [可选] - 换电通道基础配方 0：默认值 1：请求写入
            writeSwapBaseRecipeDigest: integer [可选] - 写入换电通道基础配方详细信息请求 0：默认值 1：请求写入
        """
        path = f'/api/control/writeSwapBaseRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_writeSwapDeltaRecipeDigest(data):
        """
        写入换电通道Delta配方详细信息
        请求参数:
            carModel: string [可选] - 车型代号
            cloudMsgId: integer [可选]
            swapDeltaRecipeDigest: string [可选] - 车型配方
            writeSwapDeltaRecipeDigest: integer [可选] - 写入车型配方详细信息请求 0：默认值 1：请求写入
        """
        path = f'/api/control/writeSwapDeltaRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_control_writeVehicleModelRecipeDigest(data):
        """
        写入车辆模型配方摘要
        请求参数:
            carModel: string [可选] - 车型代号
            cloudMsgId: integer [可选]
            vehicleModelRecipeDigest: string [可选] - 车型配方
            writeVehicleModelRecipeDigest: integer [可选] - 写入车型配方详细信息请求 0：默认值 1：请求写入
        """
        path = f'/api/control/writeVehicleModelRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_curtain_faultRest(data):
        """
        风幕机故障复位
        请求参数:
            slaveId: integer [可选]
        """
        path = f'/api/curtain/faultRest'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_curtain_forcedHeating(data):
        """
        风幕机强制加热
        请求参数:
            on: boolean [可选]
            slaveId: integer [可选]
        """
        path = f'/api/curtain/forcedHeating'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_curtain_getInfos(data):
        """
        获取风幕机信息
        """
        path = f'/api/curtain/getInfos'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_curtain_powerSwitch(data):
        """
        风幕机电源开关
        请求参数:
            on: boolean [可选]
            slaveId: integer [可选]
        """
        path = f'/api/curtain/powerSwitch'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_curtain_selfCheck(data):
        """
        风幕机自检
        请求参数:
            on: boolean [可选]
            slaveId: integer [可选]
        """
        path = f'/api/curtain/selfCheck'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_curtain_setParams(data):
        """
        设置风幕机参数
        请求参数:
            heaterStartTemp: number [可选]
            heaterStopReturnDiffTemp: number [可选]
            slaveId: integer [可选]
            standbyfanStatus: number [可选]
        """
        path = f'/api/curtain/setParams'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_plcPeriodicData(data):
        """
        获取PLC周期数据
        """
        path = f'/api/equipment/plcPeriodicData'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_plcStatus(data):
        """
        获取PLC状态
        """
        path = f'/api/equipment/plcStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_fan_control(data):
        """
        风扇控制
        请求参数:
            commandSubType: string [可选] - 下控子类型
            commandTypeVal: string [可选] - 下控类型数据 存储于缓存中
            equipActionType: integer [可选] - 设备控制类型 0：默认值 1：开启 2：关闭
            fanCode: string [可选]
            pfk: string [可选] - 下控唯一标志
        """
        path = f'/api/fan/control'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_fan_status(data):
        """
        获取风扇状态
        """
        path = f'/api/fan/status'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_gate_control(data):
        """
        道闸控制
        请求参数:
            commandSubType: string [可选] - 下控子类型
            commandTypeVal: string [可选] - 下控类型数据 存储于缓存中
            gateControlAction: integer [可选] - 控制道闸动作 0：默认值 1：开启 2：关闭
            gateControlObject: integer [可选] - 控制道闸对象 0：默认值 1：入口道闸 2：出口道闸
            pfk: string [可选] - 下控唯一标志
        """
        path = f'/api/gate/control'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_gate_status(data):
        """
        道闸状态
        """
        path = f'/api/gate/status'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_info_getBatteryLockNum(data):
        """
        获取电池锁数量(一代)
        """
        path = f'/api/info/getBatteryLockNum'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_info_getBatteryLockStatus(data):
        """
        获取电池锁状态(一代)
        """
        path = f'/api/info/getBatteryLockStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_info_getBatteryPlaceStatus():
        """
        获取电池在位状态
        """
        path = f'/api/info/getBatteryPlaceStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'GET', None))

    @staticmethod
    def api_info_getCarInPlace():
        """
        获取车辆到位状态
        """
        path = f'/api/info/getCarInPlace'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'GET', None))

    @staticmethod
    def api_info_getCenteringStatus():
        """
        查询归中状态
        """
        path = f'/api/info/getCenteringStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'GET', None))

    @staticmethod
    def api_info_getCurrentFaultInfo(data):
        """
        获取当前故障信息
        请求参数:
            deviceNo: integer [可选] - 设备ID
            faultCode: string [可选] - 故障编码
            faultTypeEnum: string [可选] - 故障上报设备类型
            originFaultCode: string [可选] - 原始故障编码
        """
        path = f'/api/info/getCurrentFaultInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_info_getDeadheadTestInfo():
        """
        获取空载测试信息
        """
        path = f'/api/info/getDeadheadTestInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'GET', None))

    @staticmethod
    def api_info_getFireMoveProcess(data):
        """
        获取消防移动进程
        """
        path = f'/api/info/getFireMoveProcess'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_info_getFireSandBoxInfo(data):
        """
        获取消防沙箱信息
        """
        path = f'/api/info/getFireSandBoxInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_info_getLastTimeFireMoveCampNo():
        """
        获取上次消防移动仓位号
        """
        path = f'/api/info/getLastTimeFireMoveCampNo'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'GET', None))

    @staticmethod
    def api_info_getLockInfo():
        """
        查询锁信息
        """
        path = f'/api/info/getLockInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'GET', None))

    @staticmethod
    def api_info_getOrderId():
        """
        获取订单ID
        """
        path = f'/api/info/getOrderId'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'GET', None))

    @staticmethod
    def api_info_getPeripheralEquipmentStatus():
        """
        获取周边设备状态
        """
        path = f'/api/info/getPeripheralEquipmentStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'GET', None))

    @staticmethod
    def api_info_getPlcBasicInfo():
        """
        获取PLC基本信息
        """
        path = f'/api/info/getPlcBasicInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'GET', None))

    @staticmethod
    def api_info_getPlcBatteryNum(data):
        """
        获取PLC电池数量
        """
        path = f'/api/info/getPlcBatteryNum'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_info_getPlcFault(data):
        """
        查询PLC故障数据
        请求参数:
            faultCode: string [可选] - 故障码
            faultName: string [可选] - 故障名称
            faultNumber: string [可选] - 故障编号
            normalSignal: integer [可选] - 故障信号 0:正常信号 1:故障信号
        """
        path = f'/api/info/getPlcFault'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_info_getPlcLife():
        """
        获取PLC生命反馈帧
        """
        path = f'/api/info/getPlcLife'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'GET', None))

    @staticmethod
    def api_info_getPlcLocalSwapInfo():
        """
        获取PLC本地换电时信息反馈
        """
        path = f'/api/info/getPlcLocalSwapInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'GET', None))

    @staticmethod
    def api_info_getPlcStatusAreaInfo():
        """
        获取PLC状态信息数据
        """
        path = f'/api/info/getPlcStatusAreaInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'GET', None))

    @staticmethod
    def api_info_getPlcStatusFeedback():
        """
        获取PLC状态反馈
        """
        path = f'/api/info/getPlcStatusFeedback'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'GET', None))

    @staticmethod
    def api_info_getPlcSwapEquipmentStatus(data):
        """
        获取PLC换电设备状态(一代)
        """
        path = f'/api/info/getPlcSwapEquipmentStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_info_getPlcSwapStatus(data):
        """
        获取PLC换电状态(一代)
        """
        path = f'/api/info/getPlcSwapStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_info_getPlcWorkingMode():
        """
        获取PLC工作模式
        """
        path = f'/api/info/getPlcWorkingMode'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'GET', None))

    @staticmethod
    def api_info_getPositionChangeMdInfo():
        """
        获取仓位变化指令信息
        """
        path = f'/api/info/getPositionChangeMdInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'GET', None))

    @staticmethod
    def api_info_getRgvHasBattery():
        """
        获取RGV电池是否在位
        """
        path = f'/api/info/getRgvHasBattery'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'GET', None))

    @staticmethod
    def api_info_getSafetyEquipmentStatus():
        """
        获取安全设备状态
        """
        path = f'/api/info/getSafetyEquipmentStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'GET', None))

    @staticmethod
    def api_info_getStationType():
        """
        获取站点类型
        """
        path = f'/api/info/getStationType'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'GET', None))

    @staticmethod
    def api_info_getSwapEquipmentStatus():
        """
        获取换电设备状态
        """
        path = f'/api/info/getSwapEquipmentStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'GET', None))

    @staticmethod
    def api_info_queryPositionInfo(data):
        """
        查询仓位信息及状态
        请求参数:
            batteryPlaceStatus: integer [可选] - 仓位电池在位信息状态 0：电池不在位 1：电池在位
            electricPutterDownStatus: integer [可选] - (一代)仓位电插头下压状态信息 0：未下压到位 1：下压到位   表示双仓的右仓或者单仓
            electricPutterUpStatus: integer [可选] - (一代)仓位电插头抬起状态信息 0：未抬起到位 1：抬起到位  表示双仓的右仓或者单仓
            positionFaultStatus: integer [可选] - 仓位故障信息 0：无故障 1：故障
            positionList: array [可选] - 电池仓编号列表
        """
        path = f'/api/info/queryPositionInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_light_control(data):
        """
        灯光控制
        请求参数:
            commandSubType: string [可选] - 下控子类型
            commandTypeVal: string [可选] - 下控类型数据 存储于缓存中
            leftChargeCityLight: integer [可选]
            leftChargeUpsLight: integer [可选]
            logoLight: integer [可选]
            mainControlLight: integer [可选]
            pfk: string [可选] - 下控唯一标志
            rightChargeCityLight: integer [可选]
            rightChargeUpsLight: integer [可选]
            storageLight: integer [可选]
            swapCityLight: integer [可选]
            swapUpsLight: integer [可选]
        """
        path = f'/api/light/control'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_light_status(data):
        """
        获取灯光状态
        """
        path = f'/api/light/status'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_light_switchControl(data):
        """
        灯光开关控制
        请求参数:
            commandSubType: string [可选] - 下控子类型
            commandTypeVal: string [可选] - 下控类型数据 存储于缓存中
            equipActionType: integer [可选]
            lightCode: string [可选]
            pfk: string [可选] - 下控唯一标志
        """
        path = f'/api/light/switchControl'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_light_switchControls(data):
        """
        批量灯光开关控制
        请求参数:
            commandSubType: string [可选] - 下控子类型
            commandTypeVal: string [可选] - 下控类型数据 存储于缓存中
            equipActionType: integer [可选]
            lightCode: string [可选]
            pfk: string [可选] - 下控唯一标志
        """
        path = f'/api/light/switchControls'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_HeaterConfig(data):
        """
        加热器配置
        请求参数:
            slaveId: integer [可选] - 加热器编号
        """
        path = f'/api/mqtt/HeaterConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_closeAllFan(data):
        """
        关闭所有风扇
        """
        path = f'/api/mqtt/closeAllFan'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_controlAirCondition(data):
        """
        控制空调
        请求参数:
            airControlType: string [可选] - 空调下控类型 1-参数设置 2-制冷开机发射 3-制热开机发射 4-空调关机发射
            controlModel: integer [可选] - 控制模式 1：自动 0：远程
            electricSill: number [可选] - 电流门槛
            heat: integer [可选] - 制热发射
            id: string [可选] - ID
            lowerTemperatureAlarmValueFlag: integer [可选] - 温度下限报警值使能
            openCloseFlag: integer [可选] - 开关机失败报警使能
            refrigeration: integer [可选] - 制冷发射
            shutdown: integer [可选] - 关机发射
            temperature: integer [可选] - 温度
            temperatureDownAlarm: number [可选] - 温度下限报警值（℃）
            temperatureUpAlarm: number [可选] - 温度上限报警值（℃）
            upperTemperatureLimitAlarmValueFlag: integer [可选] - 温度上限报警使能
        """
        path = f'/api/mqtt/controlAirCondition'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_controlAmmeterSettingTimeZone(data):
        """
        控制电表时区设置
        请求参数:
            id: integer [可选] - ID
            num: integer [可选]
            timePeriodList: array [可选] - 时段
                        periodHour: integer [可选] - 开始时
                        periodMinute: integer [可选] - 开始分
                        periodTableNum: integer [可选] - 第N套时区序号
                        periodType: integer [可选] - 尖峰平谷
            timeZoneList: array [可选] - 时区
                        startDay: integer [可选] - 开始日
                        startMonth: integer [可选] - 开始月
                        zoneNum: integer [可选] - 时区序号
        """
        path = f'/api/mqtt/controlAmmeterSettingTimeZone'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_controlFan(data):
        """
        控制风扇
        请求参数:
            alarmReset: integer [可选] - 告警复位 0xFF00
            controlModel: integer [可选] - 控制模式 0-自动 1-手动 2-定时
            fanControlType: string [可选] - 风机下控类型 1-参数设置 2-远程开关空调 3-手动开启风扇 4-恢复出厂参数 5-告警复位
            fanStartSmallBoxTem: number [可选] - 风机开启最小柜内外温差
            fanStartTem: number [可选] - 风机开启温度
            fanStopBoxTemDifference: number [可选] - 风机停止柜内外温差回差值
            fanStopTem: number [可选] - 风机停止回差温度
            highAlarmTem: number [可选] - 高温告警温度值
            id: string [可选] - ID
            lowAlarmTem: number [可选] - 低温告警温度值
            manuallyStartFan: integer [可选] - 手动开启风扇 0xFF00 开 ON ; 0x0000 关 OFF
            remoteSwitchingAirConditioner: integer [可选] - 远程开关空调 0xFF00 开 ON ; 0x0000 关 OFF
            restoreDefaultParam: integer [可选] - 恢复出厂参数 0xFF00
            timerStartHour: integer [可选] - 定时开启间隔小时
            timerStartMin: integer [可选] - 定时开启工作时间分钟
        """
        path = f'/api/mqtt/controlFan'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_controlFire(data):
        """
        控制消防设备
        请求参数:
            autoModel: integer [可选] - 自动模式 0xFF00：自动模式有效 0x0000：默认状态
            delayTime: integer [可选] - 延时时间设置 0x0000~0x001E (0~30)
            fireControlType: string [可选] - 消防下控类型 1-复位 2-消报警音 3-自检 4-声光报警 5-手动模式 6-自动模式 7-延时时间设置 8-灭火器控制
            fireExtinguisherControl: integer [可选] - 灭火器控制 0xFF00：灭火器ON 0x0000：默认状态
            id: string [可选] - ID
            manualModel: integer [可选] - 手动模式 0xFF00：手动模式有效 0x0000：默认状态
            muteAlarmTone: integer [可选] - 消报警音 0xFF00：消报警音ON 0x0000：默认状态
            reset: integer [可选] - 复位 0xFF00：复位ON 0x0000：默认状态
            selfTest: integer [可选] - 自检 0xFF00：自检ON 0x0000：默认状态
            voiceAndLightAlarm: integer [可选] - 声光报警 0xFF00：声光报警ON 0x0000：默认状态
        """
        path = f'/api/mqtt/controlFire'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_controlHeater(data):
        """
        控制加热器
        请求参数:
            alarmReset: integer [可选] - 告警复位 0xFF00
            cabinetInsideHighTemperatureLimit: number [可选] - 高温警告温度值
            cabinetInsideLowTemperatureLimit: number [可选] - 低温警告温度值
            forcedHeating: integer [可选] - 强制制热 0xFF00 开 ON ; 0x0000 关 OFF
            heaterControlType: string [可选] - 加热器下控类型 1-参数设置 2-远程开关设备 3-强制制热 4-恢复出厂参数 5-告警复位
            heaterStartingTemperature: number [可选] - 制热启动温度
            heaterStopReturnDifferenceTemperature: number [可选] - 制热停止回差值
            id: string [可选] - ID
            remoteSwitchingEquipment: integer [可选] - 远程开关设备 0xFF00 开 ON ; 0x0000 关 OFF
            restoreDefaultParam: integer [可选] - 恢复出厂参数 0xFF00
        """
        path = f'/api/mqtt/controlHeater'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_controlTemperatureAndHumidity(data):
        """
        控制温湿度
        请求参数:
            humidityDownAlarm: number [可选] - 湿度下限报警值（%RH）
            humidityDownAlarmEnable: integer [可选] - 湿度下限报警使能
            humidityUpAlarm: number [可选] - 湿度上限报警值（%RH）
            humidityUpAlarmEnable: integer [可选] - 湿度上限使能
            id: string [可选] - ID
            temperatureDownAlarm: number [可选] - 温度下限报警值（℃）
            temperatureDownAlarmEnable: integer [可选] - 温度下限使能
            temperatureUpAlarm: number [可选] - 温度上限报警值（℃）
            temperatureUpAlarmEnable: integer [可选] - 温度上限报警使能
        """
        path = f'/api/mqtt/controlTemperatureAndHumidity'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_disConnect(data):
        """
        断开MQTT连接
        """
        path = f'/api/mqtt/disConnect'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_electricConfig(data):
        """
        电气配置
        请求参数:
            electricOne: number [可选]
            electricTwo: number [可选]
            reportDay: integer [可选]
            slaveId: integer [可选]
            voltageOne: number [可选]
            voltageTwo: number [可选]
            way: integer [可选]
        """
        path = f'/api/mqtt/electricConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_electricMeterTypeConfig(data):
        """
        电表类型配置
        请求参数:
            amcType: integer [可选] - 电表类型
            name: string [可选] - 电表名称
            slaveId: integer [可选] - 电表编号
        """
        path = f'/api/mqtt/electricMeterTypeConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_getAir(data):
        """
        获取空调状态
        """
        path = f'/api/mqtt/getAir'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_getAmmeterSetting(data):
        """
        获取电表设置
        """
        path = f'/api/mqtt/getAmmeterSetting'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_getConnectedInfo(data):
        """
        获取MQTT连接信息
        """
        path = f'/api/mqtt/getConnectedInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_getElectricMeter(data):
        """
        获取电表数据
        """
        path = f'/api/mqtt/getElectricMeter'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_getFan(data):
        """
        获取风扇状态
        """
        path = f'/api/mqtt/getFan'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_getFanById(data):
        """
        根据ID获取风扇状态
        请求参数:
            id: integer [可选] - ID
        """
        path = f'/api/mqtt/getFanById'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_getFire(data):
        """
        获取消防状态
        """
        path = f'/api/mqtt/getFire'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_getHeater(data):
        """
        获取加热器状态
        """
        path = f'/api/mqtt/getHeater'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_getTemperatureAndHumidity(data):
        """
        获取温湿度数据
        """
        path = f'/api/mqtt/getTemperatureAndHumidity'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_getUps(data):
        """
        获取UPS状态
        """
        path = f'/api/mqtt/getUps'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_isConnected(data):
        """
        检查MQTT连接状态
        """
        path = f'/api/mqtt/isConnected'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_openAllFan(data):
        """
        打开所有风扇
        """
        path = f'/api/mqtt/openAllFan'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_openAllFanEquip(data):
        """
        打开所有风扇设备
        """
        path = f'/api/mqtt/openAllFanEquip'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_mqtt_reConnect(data):
        """
        重新连接MQTT
        """
        path = f'/api/mqtt/reConnect'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_newRfid_connect(data):
        """
        连接设备
        """
        path = f'/api/newRfid/connect'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_newRfid_disconnect(data):
        """
        断开设备
        """
        path = f'/api/newRfid/disconnect'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_newRfid_read(data):
        """
        读数据
        请求参数:
            commandSubType: string [可选] - 下控子类型
            commandTypeVal: string [可选] - 下控类型数据 存储于缓存中
            pfk: string [可选] - 下控唯一标志
            readPower: integer [可选]
        """
        path = f'/api/newRfid/read'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_newRfid_write(data):
        """
        写入数据
        请求参数:
            data: string [必填] - 写入数据
            epcId: string [可选] - epc标签
        """
        path = f'/api/newRfid/write'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_modbus_getAllPlcHoldingRegisterData(data):
        """
        获取所有PLC保持寄存器数据
        请求参数:
            point: integer [可选] - 一帧是16个bit位，这个值就是第几个bit位
            realCode: integer [可选] - 真实点位，如系协议里面是 40001，则这个值是 1
            value: integer [可选] - 第几个bit位的值
        """
        path = f'/api/plc/modbus/getAllPlcHoldingRegisterData'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_modbus_setPlcHoldingRegisterData(data):
        """
        设置PLC保持寄存器数据
        请求参数:
            point: integer [可选] - 一帧是16个bit位，这个值就是第几个bit位
            realCode: integer [可选] - 真实点位，如系协议里面是 40001，则这个值是 1
            value: integer [可选] - 第几个bit位的值
        """
        path = f'/api/plc/modbus/setPlcHoldingRegisterData'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plcEquip_start(data):
        """
        启动PLC设备
        请求参数:
            commandSubType: string [可选] - 下控子类型
            commandTypeVal: string [可选] - 下控类型数据 存储于缓存中
            pfk: string [可选] - 下控唯一标志
        """
        path = f'/api/plcEquip/start'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plcEquip_warningReset(data):
        """
        告警复位
        请求参数:
            commandSubType: string [可选] - 下控子类型
            commandTypeVal: string [可选] - 下控类型数据 存储于缓存中
            pfk: string [可选] - 下控唯一标志
        """
        path = f'/api/plcEquip/warningReset'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_rfid_readEpc(data):
        """
        读取EPC
        请求参数:
        """
        path = f'/api/rfid/readEpc'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_rfid_stopReadEpc(data):
        """
        停止读取EPC
        """
        path = f'/api/rfid/stopReadEpc'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_rollingDoor_control(data):
        """
        卷帘门控制
        请求参数:
            commandSubType: string [可选] - 下控子类型
            commandTypeVal: string [可选] - 下控类型数据 存储于缓存中
            curtainDoorControlAction: integer [可选] -  控制卷帘门动作 0：默认值 1：开启 2：关闭
            curtainDoorControlObject: integer [可选] -  控制卷帘门对象 0：默认值 1：入口卷帘门 2：出口卷帘门
            pfk: string [可选] - 下控唯一标志
        """
        path = f'/api/rollingDoor/control'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_rollingDoor_status(data):
        """
        卷帘门状态
        """
        path = f'/api/rollingDoor/status'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_sync_syncCarStatusInfo(data):
        """
        同步车辆状态信息
        请求参数:
            autohold: integer [可选]
            bonnet: integer [可选]
            btConnectState: integer [可选] - 车站蓝牙连接状态 1：已连接 2：未连接
            carDoor: integer [可选] - 车门开关状态 1：全部车门关闭 2：未关闭全部车门
            carModel: string [可选] - 车型代号
            carNo: string [可选] - 车牌
            enableSwapFlag: integer [可选] - 车辆允许换电标志位 1：不允许 2：允许
            footBrake: integer [可选] - 制动器状态 1：非制动 2：制动
            gear: integer [可选] - 挂N挡状态 1：N挡 2：非N挡
            handBrake: integer [可选] - 驻车制动状态 1：非制动 2：制动
            leftFrontDoor: integer [可选]
            leftRearDoor: integer [可选]
            lvStatus: integer [可选] - 下低压状态 0：默认 1：下电 2：上电
            mainHvState: integer [可选] - 包内主回路高压状态 255：默认值
            mainNegCnctrYn: integer [可选] - 是否有继电器粘连故障 1：有 2：无
            packType: integer [可选] - 电池包类型
            rightFrontDoor: integer [可选]
            rightRearDoor: integer [可选]
            trunk: integer [可选]
            turnAngle: integer [可选] - 转向角角度
            waitFlag: integer [可选]
            waitNum: integer [可选]
        """
        path = f'/api/sync/syncCarStatusInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_sync_syncIntrusionState(data):
        """
        同步绊线入侵状态
        请求参数:
            entranceIntrusionStatus: integer [可选]
            exitIntrusionStatus: integer [可选]
        """
        path = f'/api/sync/syncIntrusionState'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_sync_syncLoginInfo(data):
        """
        同步登录信息
        请求参数:
            account: string [可选]
            appStatus: integer [可选]
            loginStatus: integer [可选]
            roleCodes: array [可选]
            stationGuardStatus: integer [可选]
            username: string [可选]
        """
        path = f'/api/sync/syncLoginInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_sync_syncMechanicalLockStatus(data):
        """
        同步机械锁状态
        请求参数:
            batteryPacksNum: integer [可选] - 电池包个数
            locksNumOnBattery: integer [可选] - 每个电池包所包含的电池锁个数
            packOneLockFourStatus: integer [可选] - 1号电池包，4号锁状态，二代：0-默认值 1-上锁 2-解锁； 一代：0-未锁 1-已锁
            packOneLockOneStatus: integer [可选] - 1号电池包，1号锁状态，二代：0-默认值 1-上锁 2-解锁； 一代：0-未锁 1-已锁
            packOneLockThreeStatus: integer [可选] - 1号电池包，3号锁状态，二代：0-默认值 1-上锁 2-解锁； 一代：0-未锁 1-已锁
            packOneLockTwoStatus: integer [可选] - 1号电池包，2号锁状态，二代：0-默认值 1-上锁 2-解锁； 一代：0-未锁 1-已锁
            packTwoLockFourStatus: integer [可选] - 2号电池包，4号锁状态，二代：0-默认值 1-上锁 2-解锁； 一代：0-未锁 1-已锁
            packTwoLockOneStatus: integer [可选] - 2号电池包，1号锁状态，二代：0-默认值 1-上锁 2-解锁； 一代：0-未锁 1-已锁
            packTwoLockThreeStatus: integer [可选] - 2号电池包，3号锁状态，二代：0-默认值 1-上锁 2-解锁； 一代：0-未锁 1-已锁
            packTwoLockTwoStatus: integer [可选] - 2号电池包，2号锁状态，二代：0-默认值 1-上锁 2-解锁； 一代：0-未锁 1-已锁
        """
        path = f'/api/sync/syncMechanicalLockStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_sync_syncOrderId(data):
        """
        同步订单ID
        请求参数:
            orderId: string [可选]
        """
        path = f'/api/sync/syncOrderId'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_sync_syncPositionDisableStatus(data):
        """
        同步仓位禁用状态
        请求参数:
        """
        path = f'/api/sync/syncPositionDisableStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_sync_syncSn(data):
        """
        同步序列号
        请求参数:
            sn: string [可选]
        """
        path = f'/api/sync/syncSn'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_sync_syncStationInfo(data):
        """
        同步站点信息
        请求参数:
            stationName: string [可选] - 站点名称
        """
        path = f'/api/sync/syncStationInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_sync_syncVersionInfo(data):
        """
        同步版本信息
        请求参数:
            stationVersion: string [可选] - 站控版本
        """
        path = f'/api/sync/syncVersionInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_test_rfid_resp(data):
        """
        RFID响应测试接口
        请求参数:
        """
        path = f'/api/test/rfid/resp'
        return HttpRq.req(*HttpMethod.http_info(ApiPlc._get_path(path), 'POST', data))
