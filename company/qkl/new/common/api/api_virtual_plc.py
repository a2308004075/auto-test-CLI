from common.http.httpRq import HttpRq
from common.http.httpMethod import HttpMethod


class ApiVirtualPlc:
    @staticmethod
    def _get_path(path):
        service = '/virtual-plc'
        return service + path

    @staticmethod
    def algorith_api_charge_queryChargeEstimateTime(data):
        """
        通过Tmax、Tmin、起充SOC、结束SOC获取充至结束SOC的时间
        请求参数:
            endSoc: number [可选]
            startSoc: number [可选]
            tmax: number [可选]
            tmin: number [可选]
        """
        path = f'/algorith/api/charge/queryChargeEstimateTime'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_schedule_getPlcScheduleList(data):
        """
        查询PLC模拟器定时任务
        请求参数:
            jobName: string [可选] - 任务名称
            scheduleBelongs: string [可选] - 任务所属
        """
        path = f'/api/plc/schedule/getPlcScheduleList'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_getAllPlcHoldingRegisterData(data):
        """
        获取PLC全部或单个寄存器缓存数据
        请求参数:
            point: integer [可选] - 一帧是16个bit位，这个值就是第几个bit位
            realCode: integer [可选] - 真实点位，如系协议里面是 40001，则这个值是 1
            value: integer [可选] - 第几个bit位的值，值只有0或1
        """
        path = f'/api/plc/virtual/modbus/getAllPlcHoldingRegisterData'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_initPlcSwapPoint(data):
        """
        初始化PLC 远程、自动、等待任务、电池在位、仓位故障信息、电推杆为下压、道闸、卷帘门
        """
        path = f'/api/plc/virtual/modbus/initPlcSwapPoint'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_resetPlcGateAndRollingDoor(data):
        """
        复位道闸、卷帘门状态
        """
        path = f'/api/plc/virtual/modbus/resetPlcGateAndRollingDoor'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setAllowDisassemblyBattery(data):
        """
        设置PLC待拆解电池状态
        """
        path = f'/api/plc/virtual/modbus/setAllowDisassemblyBattery'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setBackCenter(data):
        """
        设置PLC车辆归中
        请求参数:
            result: integer [可选] - 1:成功 0：失败
        """
        path = f'/api/plc/virtual/modbus/setBackCenter'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setCloseOrder(data):
        """
        设置PLC终止订单
        请求参数:
            closeOrder: integer [可选] - 关闭订单
        """
        path = f'/api/plc/virtual/modbus/setCloseOrder'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setElectricPutterUp(data):
        """
        设置PLC抬电插头状态
        请求参数:
            faultCampNoOne: integer [可选] - 错误仓位号1
            faultCampNoTwo: integer [可选] - 错误仓位号2
            putterOne: integer [可选] - 1:正常 0：异常
            putterTwo: integer [可选] - 1:正常 0：异常
        """
        path = f'/api/plc/virtual/modbus/setElectricPutterUp'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setInitEquip(data):
        """
        设置PLC设备初始化
        请求参数:
            result: integer [可选] - 1:成功 0：失败
        """
        path = f'/api/plc/virtual/modbus/setInitEquip'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setInitEquipResult(data):
        """
        设置PLC设备结果初始化
        请求参数:
            result: integer [可选] - 19:执行成功 20：执行失败
        """
        path = f'/api/plc/virtual/modbus/setInitEquipResult'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setPlcAutoModel(data):
        """
        设置PLC自动模式
        """
        path = f'/api/plc/virtual/modbus/setPlcAutoModel'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setPlcCampExecute(data):
        """
        设置PLC仓位操作反馈
        请求参数:
            value: integer [可选] - 仓位反馈状态值  1：等待任务 3：一键入仓转出 13：一键入仓转入 4：一键出仓转出 14：一键出仓转入 5:电池维护转出 15：电池维护转入 6：库内转移转出 16：库内转移转入
        """
        path = f'/api/plc/virtual/modbus/setPlcCampExecute'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setPlcCarHasLeftSignal(data):
        """
        设置PLC车辆回位状态
        """
        path = f'/api/plc/virtual/modbus/setPlcCarHasLeftSignal'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setPlcCarReturnVHasCarSignal(data):
        """
        设置PLC车辆驶离状态
        """
        path = f'/api/plc/virtual/modbus/setPlcCarReturnVHasCarSignal'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setPlcCurtainDoorControl(data):
        """
        设置PLC卷帘门控制状态
        请求参数:
            curtainDoorControlAction: integer [可选] -  控制卷帘门动作 0：默认值 1：开启 2：关闭
            curtainDoorControlObject: integer [可选] -  控制卷帘门对象 0：默认值 1：入口卷帘门 2：出口卷帘门
        """
        path = f'/api/plc/virtual/modbus/setPlcCurtainDoorControl'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setPlcElectricPushControl(data):
        """
        设置PLC电推杆控制状态
        请求参数:
            electricPushControlAction: integer [可选] -  电插头控制动作 1：抬起 2：下压
            position: array [可选] - 仓位号
        """
        path = f'/api/plc/virtual/modbus/setPlcElectricPushControl'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setPlcGateControl(data):
        """
        设置PLC道闸控制状态
        请求参数:
            gateControlAction: integer [可选] - 控制道闸动作 0：默认值 1：开启 2：关闭
            gateControlObject: integer [可选] - 控制道闸对象 0：默认值 1：入口道闸 2：出口道闸
        """
        path = f'/api/plc/virtual/modbus/setPlcGateControl'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setPlcHoldingRegisterData(data):
        """
        设置PLC单个寄存器缓存数据
        请求参数:
            point: integer [可选] - 一帧是16个bit位，这个值就是第几个bit位
            realCode: integer [可选] - 真实点位，如系协议里面是 40001，则这个值是 1
            value: integer [可选] - 第几个bit位的值，值只有0或1
        """
        path = f'/api/plc/virtual/modbus/setPlcHoldingRegisterData'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setPlcHoldingRegisterData0and1(data):
        """
        设置单个点位的所有值为1或0
        请求参数:
            realCodes: array [可选] - 真实点位，如系协议里面是 40001，则这个值是 1
            type: integer [可选] - 0-初始化为0，1-初始化为1
        """
        path = f'/api/plc/virtual/modbus/setPlcHoldingRegisterData0and1'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setPlcHoldingRegisterDataList(data):
        """
        设置PLC单个寄存器缓存数据
        请求参数:
            point: integer [可选] - 一帧是16个bit位，这个值就是第几个bit位
            realCode: integer [可选] - 真实点位，如系协议里面是 40001，则这个值是 1
            value: integer [可选] - 第几个bit位的值，值只有0或1
        """
        path = f'/api/plc/virtual/modbus/setPlcHoldingRegisterDataList'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setPlcLocalModel(data):
        """
        设置PLC本地模式
        """
        path = f'/api/plc/virtual/modbus/setPlcLocalModel'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setPlcManualModel(data):
        """
        设置PLC手动模式
        """
        path = f'/api/plc/virtual/modbus/setPlcManualModel'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setPlcMechanicalLock(data):
        """
        设置PLC机械锁状态
        请求参数:
            packOneLockFourStatus: integer [可选] - 第一块电池机械锁止状态4  0-未锁 1-已锁
            packOneLockOneStatus: integer [可选] - 第一块电池机械锁止状态1  0-未锁 1-已锁
            packOneLockThreeStatus: integer [可选] - 第一块电池机械锁止状态3  0-未锁 1-已锁
            packOneLockTwoStatus: integer [可选] - 第一块电池机械锁止状态2  0-未锁 1-已锁
            packTwoLockFourStatus: integer [可选] - 第二块电池机械锁止状态4  0-未锁 1-已锁
            packTwoLockOneStatus: integer [可选] - 第二块电池机械锁止状态1  0-未锁 1-已锁
            packTwoLockThreeStatus: integer [可选] - 第二块电池机械锁止状态3  0-未锁 1-已锁
            packTwoLockTwoStatus: integer [可选] - 第二块电池机械锁止状态2  0-未锁 1-已锁
        """
        path = f'/api/plc/virtual/modbus/setPlcMechanicalLock'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setPlcPause(data):
        """
        设置PLC暂停命令反馈状态
        """
        path = f'/api/plc/virtual/modbus/setPlcPause'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setPlcPerformingTaskStatusExecute(data):
        """
        设置PLC状态为执行任务状态
        """
        path = f'/api/plc/virtual/modbus/setPlcPerformingTaskStatusExecute'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setPlcPerformingTaskStatusWait(data):
        """
        设置PLC状态为等待任务状态
        """
        path = f'/api/plc/virtual/modbus/setPlcPerformingTaskStatusWait'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setPlcRemoteModel(data):
        """
        设置PLC远程模式
        """
        path = f'/api/plc/virtual/modbus/setPlcRemoteModel'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setPlcSwapStepWorkingOrder(data):
        """
        设置PLC换电流程状态（拆卸电池步序，每2s切换步序）
        """
        path = f'/api/plc/virtual/modbus/setPlcSwapStepWorkingOrder'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setPlcSwapWorkingOrder(data):
        """
        设置PLC换电流程状态
        请求参数:
            workingOrder: integer [可选] - 5：正在拆解第一块电池
      6：正在拆解第二块电池
      7：拆解第一块电池成功
      8：拆解第二块电池成功
      9：拆解第一块电池失败
      10：拆解第二块电池失败
      15：正在安装第一块电池
      16：正在安装第二块电池
      17：安装第一块电池成功
      18：安装第二块电池成功
      19：安装第一块电池失败
      20：安装第二块电池失败
      25：换电完成
        """
        path = f'/api/plc/virtual/modbus/setPlcSwapWorkingOrder'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setPlcVHasCarSignal(data):
        """
        设置PLC车辆为到位状态
        """
        path = f'/api/plc/virtual/modbus/setPlcVHasCarSignal'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setPositionFault(data):
        """
        设置仓位故障状态
        请求参数:
            position: array [可选] - 仓位号
            status: integer [可选] - 0-正常 1-存在故障
        """
        path = f'/api/plc/virtual/modbus/setPositionFault'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setPositionInPlace(data):
        """
        设置仓位电池在位或者不在位状态
        请求参数:
            position: array [可选] - 仓位号
            status: integer [可选] - 0-不在位 1-在位
        """
        path = f'/api/plc/virtual/modbus/setPositionInPlace'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setRePickPackStatus(data):
        """
        设置PLC重新选包状态
        请求参数:
            rePickPackStatus: integer [可选] - 1:收到40197=1反馈 2：收到40197=2反馈
        """
        path = f'/api/plc/virtual/modbus/setRePickPackStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setStartPlc(data):
        """
        设置PLC启动命令反馈状态
        """
        path = f'/api/plc/virtual/modbus/setStartPlc'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plc_virtual_modbus_setTotalPlcHoldingRegisterData(data):
        """
        设置PLC单个寄存器
        请求参数:
            realCode: integer [可选] - 真实点位，如系协议里面是 40001，则这个值是 1
            value: integer [可选] - 值
        """
        path = f'/api/plc/virtual/modbus/setTotalPlcHoldingRegisterData'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_plcReq_uninstallPackLocation(data):
        """
        拆卸电池位置变化
        请求参数:
            uninstallPackLocationChange: integer [可选] - 亏电电池包回仓 0：默认值 1：车底位开始往缓存位 2：缓存升降到缓存位后
        """
        path = f'/api/plcReq/uninstallPackLocation'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_allowDisassemblyBattery(data):
        """
        allowDisassemblyBattery
        请求参数:
            contactDisplacementPackingMeasurement: number [可选] - 接触式位移装包测量值
            contactDisplacementUnpackingMeasurement: number [可选] - 接触式位移拆包测量值
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            leftAndRightPackingPerspectives: number [可选] - 左右装包需求角度
            leftAndRightUnpackingPerspectives: number [可选] - 左右拆包需求角度
            lockInfoList: array [可选]
                        enterUnlockExtraNum: integer [可选] - 入仓电池包号锁解锁次数
                        enterUnlockMaxTorque: number [可选] - 入仓电池包号锁最大解锁扭矩
                        enterUnlockRecognizeNum: number [可选] - 入仓电池包解锁认帽圈数
                        enterUnlockRingNum: number [可选] - 入仓电池包号锁解锁圈数
                        lockNo: integer [可选]
                        outLockMaxTorque: number [可选] - 出仓电池包号锁最大加锁扭矩
                        outLockRingNum: number [可选] - 出仓电池包号锁加锁圈数
                        ringsNum: number [可选]
            onePackFourLockNum: integer [可选] - 一号包，四号锁的上锁次数 0：默认值 1~4：执行次数 9：错误值
            onePackOneLockNum: integer [可选] - 一号包，一号锁的上锁次数 0：默认值 1~4：执行次数 9：错误值
            onePackThreeLockNum: integer [可选] - 一号包，三号锁的上锁次数 0：默认值 1~4：执行次数 9：错误值
            onePackTwoLockNum: integer [可选] - 一号包，二号锁的上锁次数 0：默认值 1~4：执行次数 9：错误值
            packingOfLeftFrontHighReachAxle: number [可选] - 左前探高轴拆包测量值
            packingOfLeftRearHighReachAxle: number [可选] - 左后探高轴装包测量值
            packingOfRightFrontHighReachAxle: number [可选] - 右前探高轴装包测量值
            packingOfRightRearHighReachAxle: number [可选] - 右后探高轴装包测量值
            packingOffsetValueInXDirection: number [可选] - X向装包偏移值
            packingPositionOfScissorLiftShaft: number [可选] - 剪叉升降轴装包位置
            preAndPostPackingPerspectives: number [可选] - 前后装包需求角度
            preAndPostUnpackingPerspectives: number [可选] - 前后拆包需求角度
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
            twoPackFourLockNum: integer [可选] - 二号包，四号锁的上锁次数 0：默认值 1~4：执行次数 9：错误值
            twoPackOneLockNum: integer [可选] - 二号包，一号锁的上锁次数 0：默认值 1~4：执行次数 9：错误值
            twoPackThreeLockNum: integer [可选] - 二号包，三号锁的上锁次数 0：默认值 1~4：执行次数 9：错误值
            twoPackTwoLockNum: integer [可选] - 二号包，二号锁的上锁次数 0：默认值 1~4：执行次数 9：错误值
            unpackingOfLeftFrontHighReachAxle: number [可选] - 左前探高轴拆包测量值
            unpackingOfLeftRearHighReachAxle: number [可选] - 左后探高轴拆包测量值
            unpackingOfRightFrontHighReachAxle: number [可选] - 右前探高轴拆包测量值
            unpackingOfRightRearHighReachAxle: number [可选] - 右后探高轴拆包测量值
            unpackingOffsetValueInXDirection: number [可选] - X向拆包偏移值
            unpackingPositionOfScissorLiftShaft: number [可选] - 剪叉升降轴拆包位置
        """
        path = f'/api/swap/plc/virtual/allowDisassemblyBattery'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_allowReturnVehicle(data):
        """
        allowReturnVehicle
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/swap/plc/virtual/allowReturnVehicle'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_allowVehicleEnter(data):
        """
        allowVehicleEnter
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/swap/plc/virtual/allowVehicleEnter'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_allowVehicleLeave(data):
        """
        allowVehicleLeave
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/swap/plc/virtual/allowVehicleLeave'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_continueOperation(data):
        """
        continueOperation
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/swap/plc/virtual/continueOperation'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_controlBatteryOut(data):
        """
        controlBatteryOut
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/swap/plc/virtual/controlBatteryOut'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_controlBatteryReturn(data):
        """
        controlBatteryReturn
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/swap/plc/virtual/controlBatteryReturn'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_controlGate(data):
        """
        controlGate
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/swap/plc/virtual/controlGate'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_exchangeBattery(data):
        """
        exchangeBattery
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/swap/plc/virtual/exchangeBattery'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_getAlarmPositionFaults(data):
        """
        getAlarmPositionFaults
        请求参数:
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            faultCodeDesc: array [可选] - 故障描述 故障总数量填了多少个，则这个集合数组里面就要填几个值
            faultCodeList: array [可选] - 故障码集合 故障总数量填了多少个，则这个集合数组里面就要填几个值
            faultTotalNum: integer [可选] - 故障总数量 0：无故障 65535：当前发生的故障数
        """
        path = f'/api/swap/plc/virtual/getAlarmPositionFaults'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_getPlcCommunicationVersion(data):
        """
        getPlcCommunicationVersion
        请求参数:
            aversion: integer [可选]
            bversion: integer [可选]
            cversion: integer [可选]
            dversion: integer [可选]
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            maxVersion: integer [可选] - 大版本号 十进制解析，0~255
            minVersion: integer [可选] - 小版本号 十进制解析，0~255
        """
        path = f'/api/swap/plc/virtual/getPlcCommunicationVersion'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_getPlcStatusFeedBack(data):
        """
        getPlcStatusFeedBack
        请求参数:
            electricChannelPlcStatus: integer [可选] - 换电时PLC状态 0：默认值 (非换电时发送) 1：车辆归中 2：开始举升 11：rgv开始拆第一个电池包 12：rgv拆卸第一个电池包成功 13：第一块电池包回堆垛机上 18：rgv开始安装第一块电池包 19：rgv安装第一块电池包成功 21：rgv开始拆第二个电池包 22：rgv拆卸第二个电池包成功 23：第二块电池包回堆垛机上 28：rgv开始安装第二块电池包 29：rgv安装第二块电池包成功 31 - 39 同 21 - 29，以此类推，第三块电池包 40：rgv开始行走，回仓 41：举升平台开始下降 42：举升平台下降到位 43：换电结束 备注：获取PLC是否空闲和非换电时发送 0，获取步序发 1
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            plcGeneralStatus: integer [可选] - PLC的任务状态 0：默认值 1：自动换电 2：入仓 (RGV带电池进仓) 3：出仓 (RGV带电池驶出) 4：移仓 5：调仓 6：重放 7：RGV空载驶出 8：RGV空载驶入 9：消防转移至消防箱 10：消防转移至通道 20：设备位置初始化中 21：空闲1（换电通道空闲，垛机忙）22：空闲2（换电通道空闲，垛机空闲） 23：RGV带电池驶出完成 27：RGV空载驶出完成 99：其他
        """
        path = f'/api/swap/plc/virtual/getPlcStatusFeedBack'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_getPlcWorkingMode(data):
        """
        getPlcWorkingMode
        请求参数:
            affectNextSwapReason: string [可选] - 影响下次换电原因
            attendedSafetyAlarmStatus: integer [可选] - 安全类报警状态（仅适用有人值守）
            batteryDetectionAlarmStatus: integer [可选] - 电池检测报警状态
            communicationType: integer [可选] - 通讯类型 0：默认值 1：远程 2：本地 注：0代表保持上一刻设置，站控初始化时收到0默认为本地模式
            controlMode: integer [可选] - 控制方式 0：默认值 1：自动 2：手动 注：0代表保持上一刻设置，站控初始化时收到0默认为手动模式
            debugStatus: integer [可选] - 0：默认值 1：正常模式 (非调试模式) 2：调试模式
            electricStep: integer [可选] - 换电步序
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            faultStatus: integer [可选] - 故障状态 0：默认值 1：正常 (非故障状态) 2：严重故障 (不能执行任务)
            motionModuleStatus: integer [可选] - 运动模组状态
            pauseStatus: integer [可选] - 暂停状态 0：默认值 1：正常(非暂停状态) 2：暂停
            scapegoatDetectionAlarmStatus: integer [可选] - 替罪羊检测报警状态
            scramStatus: integer [可选] - 急停状态 0：默认值 1：正常(非急停状态) 2：急停
            servoAlarmStatus: integer [可选] - 伺服类报警状态
            stackerStep: integer [可选] - 堆垛机步序
            unattendedSafetyAlarmStatus: integer [可选] - 安全类报警状态（仅适用无人值守）
            upgradeStatus: integer [可选] - 升级状态
        """
        path = f'/api/swap/plc/virtual/getPlcWorkingMode'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_getPositionChangeMdInfo(data):
        """
        getPositionChangeMdInfo
        请求参数:
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            positionChangeAction: integer [可选] - 变化动作 0：默认值 1：由在位变成不在位 2：由不在位变成在位 备注：当该字段值为2时会发送最后入仓时间
            positionChangeNumber: integer [可选] - 变化的仓位编号 0：默认值 1~96：变化仓位
        """
        path = f'/api/swap/plc/virtual/getPositionChangeMdInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_getPositionInfo(data):
        """
        getPositionInfo
        请求参数:
            batteryPlaceStatus: integer [可选] - 电池在位信息状态 0：不存在该仓位或电池不在位 1：电池在位
            electricPutterStatus: integer [可选] - 电推杆状态信息 0：其他 1：下压到位
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            positionDisableStatus: integer [可选] - 仓位禁用信息 0：无禁用 1：禁用
            positionFaultStatus: integer [可选] - 仓位故障信息 0：无故障 1：故障
            positionForeignStatus: integer [可选] - 仓位异物信息 0：无异物 1：异物
            positionNo: integer [可选] - 仓位号 1-96 (如需初始化某个仓位需要填写，否则初始化全部仓位信息)
        """
        path = f'/api/swap/plc/virtual/getPositionInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_getPositionSummaryInfo(data):
        """
        getPositionSummaryInfo
        请求参数:
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            positionsBatteryNum: integer [可选] - 仓位在位电池总数量 0-96
            positionsTotalNum: integer [可选] - 仓位总数量 1-96
        """
        path = f'/api/swap/plc/virtual/getPositionSummaryInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_getRgvHasBattery(data):
        """
        getRgvHasBattery
        请求参数:
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            manual: integer [可选] - HMI是否人工介入 0：默认值 1：是
            rgvHasBattery: integer [可选] - RGV上是否有电池反馈 0：默认值 1：有电池 2：无电池
        """
        path = f'/api/swap/plc/virtual/getRgvHasBattery'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_getStationBaseInfo(data):
        """
        getStationBaseInfo
        请求参数:
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            hardwareVersion: string [可选] - 硬件版本 案例：C000000000000000000
            softwareVersion: string [可选] - 软件版本 案例：V1.0.0
        """
        path = f'/api/swap/plc/virtual/getStationBaseInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_getSwapEquipmentStatus(data):
        """
        getSwapEquipmentStatus
        请求参数:
            addLockSuccessStatus: integer [可选] - 加锁成功标志 0：默认值 1：是 2：否
            channelTopRadarStatus: integer [可选] - 通道顶部雷达状态 0：默认值 1：在位 2：不在位
            chargeCampSafetyDoorStatus: integer [可选] - 充电仓侧安全门状态 0：默认值 1：关到位 2：开到位
            containerSafetyDoorStatus: integer [可选] - 集装箱侧安全门状态 0：默认值 1：关到位 2：开到位
            entranceRadarStatus: integer [可选] - 入口雷达状态 0：默认值 1：触发 2：未触发
            entranceRoadStatus: integer [可选] - 入口道闸状态 0：默认值 1：开闸 2：闭闸
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            exitRadarStatus: integer [可选] - 出口雷达状态 0：默认值 1：触发 2：未触发
            exitRoadStatus: integer [可选] - 出口道闸状态 0：默认值 1：开闸 2：闭闸
            leftVSlotPositionSignal: integer [可选] - 车辆左V槽在位信号 0：默认值 1：在位 2：不在位
            mainControlSafetyDoorStatus: integer [可选] - 主控室侧安全门状态 0：默认值 1：关到位 2：开到位
            openingClosingDoorStatus: integer [可选] - 开合门状态 0：默认值 1：关到位 2：开到位 3：关到安全状态
            passagewaySafetyDoor1: integer [可选] - 通道安全门1（靠近出口）状态
            passagewaySafetyDoor2: integer [可选] - 通道安全门2（靠近入口）状态
            rgvHeatingMode: integer [可选] - RGV加热模式 0：默认值 1：加热 2：不加热
            rightVSlotPositionSignal: integer [可选] - 车辆右V槽在位信号 0：默认值 1：在位 2：不在位
            vehiclePositionStatus: integer [可选] - 车辆位置状态 0：默认值 1：车辆到位，允许调整自由度 2：换电站内有车辆，但车辆未到位 3：换电站内无车辆
        """
        path = f'/api/swap/plc/virtual/getSwapEquipmentStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_initializationPlc(data):
        """
        initializationPlc
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/swap/plc/virtual/initializationPlc'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_movedBatteryPosition(data):
        """
        movedBatteryPosition
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/swap/plc/virtual/movedBatteryPosition'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_pauseOperation(data):
        """
        pauseOperation
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/swap/plc/virtual/pauseOperation'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_plcRecipeDigestVerify(data):
        """
        plcRecipeDigestVerify
        请求参数:
            batteryCompartmentRecipeDigest: string [可选] - 电池仓内配方的消息摘要值
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
            swapBaseRecipeDigest: string [可选] - 换电时基础配方的消息摘要值
            swapDeltaRecipeDigest: string [可选] - 换电时Delta配方的消息摘要值
        """
        path = f'/api/swap/plc/virtual/plcRecipeDigestVerify'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_readBatteryCompartmentRecipeDigest(data):
        """
        readBatteryCompartmentRecipeDigest
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            readBatteryCompartmentRecipeDigest: string [可选] - 电池仓配方
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/swap/plc/virtual/readBatteryCompartmentRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_readSwapBaseRecipeDigest(data):
        """
        readSwapBaseRecipeDigest
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            readSwapBaseRecipeDigest: string [可选] - 换电通道基础配方
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/swap/plc/virtual/readSwapBaseRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_readSwapDeltaRecipeDigest(data):
        """
        readSwapDeltaRecipeDigest
        请求参数:
            carModel: string [可选] - 车型代号
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            readSwapDeltaRecipeDigest: string [可选] - 换电通道Delta配方
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/swap/plc/virtual/readSwapDeltaRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_repositionBattery(data):
        """
        repositionBattery
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/swap/plc/virtual/repositionBattery'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_scramOperation(data):
        """
        scramOperation
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/swap/plc/virtual/scramOperation'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_startSwap(data):
        """
        startSwap
        请求参数:
            failCamp1: integer [可选]
            failCamp2: integer [可选]
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/swap/plc/virtual/startSwap'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_thermalRunawayBatterySandbox(data):
        """
        thermalRunawayBatterySandbox
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/swap/plc/virtual/thermalRunawayBatterySandbox'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_writeBatteryCompartmentRecipeDigest(data):
        """
        writeBatteryCompartmentRecipeDigest
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/swap/plc/virtual/writeBatteryCompartmentRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_writeSwapBaseRecipeDigest(data):
        """
        writeSwapBaseRecipeDigest
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/swap/plc/virtual/writeSwapBaseRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_swap_plc_virtual_writeSwapDeltaRecipeDigest(data):
        """
        writeSwapDeltaRecipeDigest
        请求参数:
            carModel: string [可选] - 车型代号
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/swap/plc/virtual/writeSwapDeltaRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_afterEquipmentCenteringReset(data):
        """
        PLC设备后归中复位0032
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/afterEquipmentCenteringReset'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_allowDisassemblyBattery(data):
        """
        发送允许拆卸电池包指令0004
        请求参数:
            contactDisplacementPackingMeasurement: number [可选] - 接触式位移装包测量值
            contactDisplacementUnpackingMeasurement: number [可选] - 接触式位移拆包测量值
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            leftAndRightPackingPerspectives: number [可选] - 左右装包需求角度
            leftAndRightUnpackingPerspectives: number [可选] - 左右拆包需求角度
            lockInfoList: array [可选]
                        enterUnlockExtraNum: integer [可选] - 入仓电池包号锁解锁次数
                        enterUnlockMaxTorque: number [可选] - 入仓电池包号锁最大解锁扭矩
                        enterUnlockRecognizeNum: number [可选] - 入仓电池包解锁认帽圈数
                        enterUnlockRingNum: number [可选] - 入仓电池包号锁解锁圈数
                        lockNo: integer [可选]
                        outLockMaxTorque: number [可选] - 出仓电池包号锁最大加锁扭矩
                        outLockRingNum: number [可选] - 出仓电池包号锁加锁圈数
                        ringsNum: number [可选]
            onePackFourLockNum: integer [可选] - 一号包，四号锁的上锁次数 0：默认值 1~4：执行次数 9：错误值
            onePackOneLockNum: integer [可选] - 一号包，一号锁的上锁次数 0：默认值 1~4：执行次数 9：错误值
            onePackThreeLockNum: integer [可选] - 一号包，三号锁的上锁次数 0：默认值 1~4：执行次数 9：错误值
            onePackTwoLockNum: integer [可选] - 一号包，二号锁的上锁次数 0：默认值 1~4：执行次数 9：错误值
            packingOfLeftFrontHighReachAxle: number [可选] - 左前探高轴拆包测量值
            packingOfLeftRearHighReachAxle: number [可选] - 左后探高轴装包测量值
            packingOfRightFrontHighReachAxle: number [可选] - 右前探高轴装包测量值
            packingOfRightRearHighReachAxle: number [可选] - 右后探高轴装包测量值
            packingOffsetValueInXDirection: number [可选] - X向装包偏移值
            packingPositionOfScissorLiftShaft: number [可选] - 剪叉升降轴装包位置
            preAndPostPackingPerspectives: number [可选] - 前后装包需求角度
            preAndPostUnpackingPerspectives: number [可选] - 前后拆包需求角度
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
            twoPackFourLockNum: integer [可选] - 二号包，四号锁的上锁次数 0：默认值 1~4：执行次数 9：错误值
            twoPackOneLockNum: integer [可选] - 二号包，一号锁的上锁次数 0：默认值 1~4：执行次数 9：错误值
            twoPackThreeLockNum: integer [可选] - 二号包，三号锁的上锁次数 0：默认值 1~4：执行次数 9：错误值
            twoPackTwoLockNum: integer [可选] - 二号包，二号锁的上锁次数 0：默认值 1~4：执行次数 9：错误值
            unpackingOfLeftFrontHighReachAxle: number [可选] - 左前探高轴拆包测量值
            unpackingOfLeftRearHighReachAxle: number [可选] - 左后探高轴拆包测量值
            unpackingOfRightFrontHighReachAxle: number [可选] - 右前探高轴拆包测量值
            unpackingOfRightRearHighReachAxle: number [可选] - 右后探高轴拆包测量值
            unpackingOffsetValueInXDirection: number [可选] - X向拆包偏移值
            unpackingPositionOfScissorLiftShaft: number [可选] - 剪叉升降轴拆包位置
        """
        path = f'/api/virtual/feign/allowDisassemblyBattery'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_allowReturnVehicle(data):
        """
        允许车辆回位指令
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/allowReturnVehicle'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_allowVehicleEnter(data):
        """
        发送允许驶入换电通道至PLC
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/allowVehicleEnter'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_allowVehicleLeave(data):
        """
        发送车辆允许驶离指令到PLC
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/allowVehicleLeave'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_api_virtual_feign_plcLogin(data):
        """
        PLC登录
        """
        path = f'/api/virtual/feign/api/virtual/feign/plcLogin'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_backCenterAndLift(data):
        """
        发送归中举升指令
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/backCenterAndLift'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_continueOperation(data):
        """
        暂停后重新继续
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/continueOperation'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_controlBatteryOut(data):
        """
        一键出仓
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/controlBatteryOut'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_controlBatteryReturn(data):
        """
        一键入仓
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/controlBatteryReturn'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_controlCurtainDoor(data):
        """
        卷帘门控制
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/controlCurtainDoor'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_controlExhaustFan(data):
        """
        排风扇控制
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/controlExhaustFan'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_controlGate(data):
        """
        道闸控制
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/controlGate'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_controlLight(data):
        """
        照明控制
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/controlLight'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_controlMqttPower(data):
        """
        MQTT网关断电、通电控制
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/controlMqttPower'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_controlPlcHeat(data):
        """
        PLC加热模式控制
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/controlPlcHeat'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_controlSblePower(data):
        """
        SBLE (站端通信模块) 通电、断电控制
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/controlSblePower'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_controlVoiceLight(data):
        """
        声光报警控制
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/controlVoiceLight'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_controlZhouPowered(data):
        """
        周立功断电、通电控制
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/controlZhouPowered'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_deadheadTestInfo(data):
        """
        厂内空跑测试0219
        请求参数:
            currentNum: integer [可选] - 当前次数
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            settingNum: integer [可选] - 设定次数
        """
        path = f'/api/virtual/feign/deadheadTestInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_electricMeter(data):
        """
        PLC请求电表信息0510
        """
        path = f'/api/virtual/feign/electricMeter'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_equipmentSelfCheck(data):
        """
        PLC设备自检002C
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/equipmentSelfCheck'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_exchangeBattery(data):
        """
        电池交换
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/exchangeBattery'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_executeEliminateFault(data):
        """
        执行PLC故障清除命令
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/executeEliminateFault'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_fireBatteryOut(data):
        """
        电池出仓（消防机构）
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/fireBatteryOut'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_fireBatteryReturn(data):
        """
        电池入仓（消防机构）
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/fireBatteryReturn'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_fireOut(data):
        """
        消防机构驶出
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/fireOut'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_fireReturn(data):
        """
        消防机构驶入
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/fireReturn'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_getAlarmPositionFaults(data):
        """
        设置PLC故障信息
        请求参数:
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            faultCodeDesc: array [可选] - 故障描述 故障总数量填了多少个，则这个集合数组里面就要填几个值
            faultCodeList: array [可选] - 故障码集合 故障总数量填了多少个，则这个集合数组里面就要填几个值
            faultTotalNum: integer [可选] - 故障总数量 0：无故障 65535：当前发生的故障数
        """
        path = f'/api/virtual/feign/getAlarmPositionFaults'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_getBatteryPlaceStatus(data):
        """
        设置电池在位状态
        请求参数:
            cacheLiftInPlace: integer [可选] - 缓存升降台是否有电池包
            cachePlaceHasBattery: integer [可选] - 缓存位是否有电池包 0：默认值 1：缓存位有电池包 2：缓存位无电池包
            cacheTranslationInPlace: integer [可选] - 缓存平移机构在位信号
            electricChannelHasThermalRunawayBattery: integer [可选] - 换电通道是否有热失控电池包
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            fireTranslationMechanismInPlace: integer [可选] - 消防平移机构在位信号
            rgvHasBattery: integer [可选] - RGV是否有电池包 0：默认值 1：RGV有电池包 2：RGV无电池包
            sandboxHasThermalRunawayBattery: integer [可选] - 沙箱是否有热失控电池包
            stackerHasBattery: integer [可选] - 堆垛机是否有电池包 0：默认值 1：堆垛机有电池包 2：堆垛机无电池包
        """
        path = f'/api/virtual/feign/getBatteryPlaceStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_getCenteringStatus(data):
        """
        设置归中状态
        请求参数:
            centeringStatus: integer [可选] - 归中状态 0：默认值 1：归中夹紧进行中 2：归中夹紧完成 3：归中松开进行中 4：归中松开完成
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
        """
        path = f'/api/virtual/feign/getCenteringStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_getCurrentMagIdControlData(data):
        """
        设置PLC对应协议帧自动回复数据
        请求参数:
            msgCommandId: string [可选] - 需要查询下控数据的命令ID，组合规则：0001 代表 协议的 0x00 0x01，必填
        """
        path = f'/api/virtual/feign/getCurrentMagIdControlData'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_getDataLog(data):
        """
        日志0216/2017/0218/0511/0512/0513/0514/0515
        请求参数:
            step: integer [可选] - 协议号 16:0216 17:0217 18:0218 11：0511 12：0512 13：0513 14：0514 15：0515
        """
        path = f'/api/virtual/feign/getDataLog'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_getLiftAndDownHeight(data):
        """
        设置举升/下降高度数据
        请求参数:
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            installCarLiftingHeight: number [可选] - 装包车辆举升高度
            lockBatteryDescentHeight: number [可选] - 加锁电池包下降高度
            lockBatteryLiftingHeight: number [可选] - 加锁电池包举升高度
            unInstallCarLiftingHeight: number [可选] - 拆包车辆举升高度
            unlockBatteryDescentHeight: number [可选] - 解锁电池包下降高度
            unlockBatteryLiftingHeight: number [可选] - 解锁电池包举升高度
        """
        path = f'/api/virtual/feign/getLiftAndDownHeight'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_getLockAndUnlockData(data):
        """
        设置快换锁加解锁数据
        请求参数:
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            lockingDataList: array [可选] - 快换锁加锁数据
                        lockNo: integer [可选] - 锁序号
                        lockTorque: number [可选] - 加锁扭矩
                        lockTurns: number [可选] - 加锁圈数
                        recognizeSpeed: number [可选] - 加锁认帽旋转速度
                        recognizeTorque: number [可选] - 加锁认帽扭矩
                        unLockResetTorque: number [可选] - 解锁复位扭矩
                        unLockTurns: number [可选] - 解锁复位圈数
            unlockingDataList: array [可选] - 快换锁解锁数据
                        lockNo: integer [可选] - 锁序号
                        lockResetTorque: number [可选] - 加锁复位扭矩
                        lockResetTurns: number [可选] - 加锁复位圈数
                        unLockRecognizeSpeed: number [可选] - 解锁认帽旋转速度
                        unLockRecognizeTorque: number [可选] - 解锁认帽扭矩
                        unLockTorque: number [可选] - 解锁扭矩
                        unLockTurns: number [可选] - 解锁圈数
                        unlockNum: integer [可选] - 快换锁解锁次数
        """
        path = f'/api/virtual/feign/getLockAndUnlockData'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_getLockSensorStatus(data):
        """
        设置加解锁传感器数据
        请求参数:
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            sensorStatus1: integer [可选] - 传感器1状态  0-未感应 1-感应到
            sensorStatus2: integer [可选] - 传感器2状态  0-未感应 1-感应到
            sensorStatus3: integer [可选] - 传感器3状态  0-未感应 1-感应到
            sensorStatus4: integer [可选] - 传感器4状态  0-未感应 1-感应到
        """
        path = f'/api/virtual/feign/getLockSensorStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_getNewBatteryLockStatus(data):
        """
        设置新包机械锁状态
        请求参数:
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            thisLock10LockStatus: integer [可选] - 同上
            thisLock1LockStatus: integer [可选] - 本次1号位电池包1号锁锁状态 0：默认值 1：解锁认帽中 2：解锁认帽完成 3：解锁认帽失败 4：解锁中 5：解锁完成 6：解锁失败 7：加锁复位中 8：加锁复位完成 9：加锁复位失败 11：加锁认帽中 12：加锁认帽完成 13：加锁认帽失败 14：解锁复位中 15：解锁复位完成 16：解锁复位失败 17：加锁中 18：加锁完成 19：加锁失败
            thisLock2LockStatus: integer [可选] - 同上
            thisLock3LockStatus: integer [可选] - 同上
            thisLock4LockStatus: integer [可选] - 同上
            thisLock5LockStatus: integer [可选] - 同上
            thisLock6LockStatus: integer [可选] - 同上
            thisLock7LockStatus: integer [可选] - 同上
            thisLock8LockStatus: integer [可选] - 同上
            thisLock9LockStatus: integer [可选] - 同上
        """
        path = f'/api/virtual/feign/getNewBatteryLockStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_getOldBatteryLockStatus(data):
        """
        设置旧包机械锁状态
        请求参数:
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            thisLock10LockStatus: integer [可选] - 同上
            thisLock1LockStatus: integer [可选] - 本次1号位电池包1号锁锁状态 0：默认值 1：解锁认帽中 2：解锁认帽完成 3：解锁认帽失败 4：解锁中 5：解锁完成 6：解锁失败 7：加锁复位中 8：加锁复位完成 9：加锁复位失败 11：加锁认帽中 12：加锁认帽完成 13：加锁认帽失败 14：解锁复位中 15：解锁复位完成 16：解锁复位失败 17：加锁中 18：加锁完成 19：加锁失败
            thisLock2LockStatus: integer [可选] - 同上
            thisLock3LockStatus: integer [可选] - 同上
            thisLock4LockStatus: integer [可选] - 同上
            thisLock5LockStatus: integer [可选] - 同上
            thisLock6LockStatus: integer [可选] - 同上
            thisLock7LockStatus: integer [可选] - 同上
            thisLock8LockStatus: integer [可选] - 同上
            thisLock9LockStatus: integer [可选] - 同上
        """
        path = f'/api/virtual/feign/getOldBatteryLockStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_getPeripheralEquipmentStatus(data):
        """
        0207周边设备状态
        请求参数:
            chargerOutageAndEnergizeStatus: integer [可选] - 充电机总闸断电、通电状态 0：默认值 1：通电 2：断电
            entranceShutterDoorStatus: integer [可选] - 入口卷帘门状态 0：默认值 1：开启 2：关闭
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            exhaustFanFiveStatus: integer [可选] - 排风扇5状态 0：默认值 1：开启 2：关闭
            exhaustFanFourStatus: integer [可选] - 排风扇4状态 0：默认值 1：开启 2：关闭
            exhaustFanOneStatus: integer [可选] - 排风扇1状态 0：默认值 1：开启 2：关闭
            exhaustFanSixStatus: integer [可选] - 排风扇6状态 0：默认值 1：开启 2：关闭
            exhaustFanThreeStatus: integer [可选] - 排风扇3状态 0：默认值 1：开启 2：关闭
            exhaustFanTwoStatus: integer [可选] - 排风扇2状态 0：默认值 1：开启 2：关闭
            exitShutterDoorStatus: integer [可选] - 出口卷帘门状态 0：默认值 1：开启 2：关闭
            lightEightStatus: integer [可选] - 照明8状态 0：默认值 1：开启 2：关闭
            lightFiveStatus: integer [可选] - 照明5状态（电池仓UPS照明） 0：默认值 1：开启 2：关闭
            lightFourStatus: integer [可选] - 照明4状态（电池仓市电照明） 0：默认值 1：开启 2：关闭
            lightNineStatus: integer [可选] - 照明9状态 0：默认值 1：开启 2：关闭
            lightOneStatus: integer [可选] - 照明1状态（主控室UPS照明） 0：默认值 1：开启 2：关闭
            lightSevenStatus: integer [可选] - 照明7状态（站外饰品灯） 0：默认值 1：开启 2：关闭
            lightSixStatus: integer [可选] - 照明6状态（站外LOGO灯） 0：默认值 1：开启 2：关闭
            lightTenStatus: integer [可选] - 照明10状态 0：默认值 1：开启 2：关闭
            lightThreeStatus: integer [可选] - 照明3状态（换电通道UPS照明） 0：默认值 1：开启 2：关闭
            lightTwoStatus: integer [可选] - 照明2状态（换电通道市电照明） 0：默认值 1：开启 2：关闭
            liquidLevelStatus1: integer [可选] - 液位传感器1状态
            liquidLevelStatus2: integer [可选] - 液位传感器2状态
            liquidLevelStatus3: integer [可选] - 液位传感器3状态
            mqttStatus: integer [可选] - MQTT网关通道、断电状态 0：默认值 1：通电 2：断电
            pumpStatus: integer [可选] - 水泵状态
            sbleStatus: integer [可选] - SBLE (站端通信模块) 通电、断电状态 0：默认值 1：通电 2：断电
            stationOutageAndEnergizeStatus: integer [可选] - 换电站总闸断电、通电状态 0：默认值 1：通电 2：断电
            voiceLightStatus: integer [可选] - 声光报警状态 0：默认值 1：开启 2：关闭
            zhouPowerStatus: integer [可选] - 周立功断电、通电状态 0：默认值 1：通电 2：断电
        """
        path = f'/api/virtual/feign/getPeripheralEquipmentStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_getPlcCommunicationVersion(data):
        """
        设置PLC使用通信协议版本
        请求参数:
            aversion: integer [可选]
            bversion: integer [可选]
            cversion: integer [可选]
            dversion: integer [可选]
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            maxVersion: integer [可选] - 大版本号 十进制解析，0~255
            minVersion: integer [可选] - 小版本号 十进制解析，0~255
        """
        path = f'/api/virtual/feign/getPlcCommunicationVersion'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_getPlcLocalSwapInfo(data):
        """
        设置PLC本地换电时信息反馈
        请求参数:
            carCode: string [可选] - 车型代码
            electricChannelOnePackInPositionNum: integer [可选] - 换电时一号入仓电池包仓位号
            electricChannelOnePackOutPositionNum: integer [可选] - 换电时一号出仓电池包仓位号
            electricChannelTwoPackInPositionNum: integer [可选] - 换电时二号入仓电池包仓位号
            electricChannelTwoPackOutPositionNum: integer [可选] - 换电时二号出仓电池包仓位号
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            reserve: integer [可选] - 预留位 0：默认值
            startLocalCharging: integer [可选] - 本地换电标志 0：默认值 1：未进行本地换电 2：正在进行本地换电
        """
        path = f'/api/virtual/feign/getPlcLocalSwapInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_getPlcStatusFeedBack(data):
        """
        设置PLC任务状态和步序（0204）
        请求参数:
            electricChannelPlcStatus: integer [可选] - 换电时PLC状态 0：默认值 (非换电时发送) 1：车辆归中 2：开始举升 11：rgv开始拆第一个电池包 12：rgv拆卸第一个电池包成功 13：第一块电池包回堆垛机上 18：rgv开始安装第一块电池包 19：rgv安装第一块电池包成功 21：rgv开始拆第二个电池包 22：rgv拆卸第二个电池包成功 23：第二块电池包回堆垛机上 28：rgv开始安装第二块电池包 29：rgv安装第二块电池包成功 31 - 39 同 21 - 29，以此类推，第三块电池包 40：rgv开始行走，回仓 41：举升平台开始下降 42：举升平台下降到位 43：换电结束 备注：获取PLC是否空闲和非换电时发送 0，获取步序发 1
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            plcGeneralStatus: integer [可选] - PLC的任务状态 0：默认值 1：自动换电 2：入仓 (RGV带电池进仓) 3：出仓 (RGV带电池驶出) 4：移仓 5：调仓 6：重放 7：RGV空载驶出 8：RGV空载驶入 9：消防转移至消防箱 10：消防转移至通道 20：设备位置初始化中 21：空闲1（换电通道空闲，垛机忙）22：空闲2（换电通道空闲，垛机空闲） 23：RGV带电池驶出完成 27：RGV空载驶出完成 99：其他
        """
        path = f'/api/virtual/feign/getPlcStatusFeedBack'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_getPlcWorkingMode(data):
        """
        设置PLC工作模式0205
        请求参数:
            affectNextSwapReason: string [可选] - 影响下次换电原因
            attendedSafetyAlarmStatus: integer [可选] - 安全类报警状态（仅适用有人值守）
            batteryDetectionAlarmStatus: integer [可选] - 电池检测报警状态
            communicationType: integer [可选] - 通讯类型 0：默认值 1：远程 2：本地 注：0代表保持上一刻设置，站控初始化时收到0默认为本地模式
            controlMode: integer [可选] - 控制方式 0：默认值 1：自动 2：手动 注：0代表保持上一刻设置，站控初始化时收到0默认为手动模式
            debugStatus: integer [可选] - 0：默认值 1：正常模式 (非调试模式) 2：调试模式
            electricStep: integer [可选] - 换电步序
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            faultStatus: integer [可选] - 故障状态 0：默认值 1：正常 (非故障状态) 2：严重故障 (不能执行任务)
            motionModuleStatus: integer [可选] - 运动模组状态
            pauseStatus: integer [可选] - 暂停状态 0：默认值 1：正常(非暂停状态) 2：暂停
            scapegoatDetectionAlarmStatus: integer [可选] - 替罪羊检测报警状态
            scramStatus: integer [可选] - 急停状态 0：默认值 1：正常(非急停状态) 2：急停
            servoAlarmStatus: integer [可选] - 伺服类报警状态
            stackerStep: integer [可选] - 堆垛机步序
            unattendedSafetyAlarmStatus: integer [可选] - 安全类报警状态（仅适用无人值守）
            upgradeStatus: integer [可选] - 升级状态
        """
        path = f'/api/virtual/feign/getPlcWorkingMode'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_getPositionChangeMdInfo(data):
        """
        设置仓位指令变化信息
        请求参数:
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            positionChangeAction: integer [可选] - 变化动作 0：默认值 1：由在位变成不在位 2：由不在位变成在位 备注：当该字段值为2时会发送最后入仓时间
            positionChangeNumber: integer [可选] - 变化的仓位编号 0：默认值 1~96：变化仓位
        """
        path = f'/api/virtual/feign/getPositionChangeMdInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_getPositionInfo(data):
        """
        设置仓位信息0303 0302
        请求参数:
            batteryPlaceStatus: integer [可选] - 电池在位信息状态 0：不存在该仓位或电池不在位 1：电池在位
            electricPutterStatus: integer [可选] - 电推杆状态信息 0：其他 1：下压到位
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            positionDisableStatus: integer [可选] - 仓位禁用信息 0：无禁用 1：禁用
            positionFaultStatus: integer [可选] - 仓位故障信息 0：无故障 1：故障
            positionForeignStatus: integer [可选] - 仓位异物信息 0：无异物 1：异物
            positionNo: integer [可选] - 仓位号 1-96 (如需初始化某个仓位需要填写，否则初始化全部仓位信息)
        """
        path = f'/api/virtual/feign/getPositionInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_getPositionSummaryInfo(data):
        """
        设置仓位总体信息0301
        请求参数:
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            positionsBatteryNum: integer [可选] - 仓位在位电池总数量 0-96
            positionsTotalNum: integer [可选] - 仓位总数量 1-96
        """
        path = f'/api/virtual/feign/getPositionSummaryInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_getRgvHasBattery(data):
        """
        HMI操作0503
        请求参数:
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            manual: integer [可选] - HMI是否人工介入 0：默认值 1：是
            rgvHasBattery: integer [可选] - RGV上是否有电池反馈 0：默认值 1：有电池 2：无电池
        """
        path = f'/api/virtual/feign/getRgvHasBattery'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_getSafetyEquipmentStatus(data):
        """
        0207周边设备状态
        请求参数:
            electricChannelHasThermalRunawayBattery: integer [可选] - 换电通道是否有热失控电池包 0：默认值 1：满仓 2：空仓
            electricChannelSmokeState: integer [可选] - 换电通道烟感状态 0：默认值 1：报警 2：正常
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            sandboxHasThermalRunawayBattery: integer [可选] - 沙箱是否有热失控电池包 0：默认值 1：满仓 2：空仓
            sandboxSmokeState: integer [可选] - 沙箱烟感状态 0：默认值 1：报警 2：正常
            stationSmokeState: integer [可选] - 站控监控室烟感状态 0：默认值 1：报警 2：正常
        """
        path = f'/api/virtual/feign/getSafetyEquipmentStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_getStationBaseInfo(data):
        """
        设置站基本信息0215
        请求参数:
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            hardwareVersion: string [可选] - 硬件版本 案例：C000000000000000000
            softwareVersion: string [可选] - 软件版本 案例：V1.0.0
        """
        path = f'/api/virtual/feign/getStationBaseInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_getStepAndDataLog(data):
        """
        日志0212/0213
        请求参数:
        """
        path = f'/api/virtual/feign/getStepAndDataLog'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_getSwapEquipmentStatus(data):
        """
        0206换电设备状态
        请求参数:
            addLockSuccessStatus: integer [可选] - 加锁成功标志 0：默认值 1：是 2：否
            channelTopRadarStatus: integer [可选] - 通道顶部雷达状态 0：默认值 1：在位 2：不在位
            chargeCampSafetyDoorStatus: integer [可选] - 充电仓侧安全门状态 0：默认值 1：关到位 2：开到位
            containerSafetyDoorStatus: integer [可选] - 集装箱侧安全门状态 0：默认值 1：关到位 2：开到位
            entranceRadarStatus: integer [可选] - 入口雷达状态 0：默认值 1：触发 2：未触发
            entranceRoadStatus: integer [可选] - 入口道闸状态 0：默认值 1：开闸 2：闭闸
            executeCount: integer [可选] - 定时任务执行次数 0 表示一直按协议任务周期执行，大于0 则表示按协议任务周期间隔执行几次后停止
            exitRadarStatus: integer [可选] - 出口雷达状态 0：默认值 1：触发 2：未触发
            exitRoadStatus: integer [可选] - 出口道闸状态 0：默认值 1：开闸 2：闭闸
            leftVSlotPositionSignal: integer [可选] - 车辆左V槽在位信号 0：默认值 1：在位 2：不在位
            mainControlSafetyDoorStatus: integer [可选] - 主控室侧安全门状态 0：默认值 1：关到位 2：开到位
            openingClosingDoorStatus: integer [可选] - 开合门状态 0：默认值 1：关到位 2：开到位 3：关到安全状态
            passagewaySafetyDoor1: integer [可选] - 通道安全门1（靠近出口）状态
            passagewaySafetyDoor2: integer [可选] - 通道安全门2（靠近入口）状态
            rgvHeatingMode: integer [可选] - RGV加热模式 0：默认值 1：加热 2：不加热
            rightVSlotPositionSignal: integer [可选] - 车辆右V槽在位信号 0：默认值 1：在位 2：不在位
            vehiclePositionStatus: integer [可选] - 车辆位置状态 0：默认值 1：车辆到位，允许调整自由度 2：换电站内有车辆，但车辆未到位 3：换电站内无车辆
        """
        path = f'/api/virtual/feign/getSwapEquipmentStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_initPlcInfo(data):
        """
        初始化PLC换电相关数据
        """
        path = f'/api/virtual/feign/initPlcInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_initializationPlc(data):
        """
        PLC初始化
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/initializationPlc'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_keyonControl(data):
        """
        唤醒源控制 050E
        请求参数:
            enterPosition: integer [可选]
            keyonReq: integer [可选]
        """
        path = f'/api/virtual/feign/keyonControl'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_liftAndLowElectricalPlug(data):
        """
        PLC抬起并下压电插头002E
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/liftAndLowElectricalPlug'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_lockBatteryData(data):
        """
        发送电池锁数据050D
        请求参数:
            carModel: string [可选] - 车辆型号
            carNo: string [可选] - 车牌号
            contactDisplacementPackingMeasurement: number [可选] - 接触式位移装包测量值
            contactDisplacementUnpackingMeasurement: number [可选] - 接触式位移拆包测量值
            leftAndRightPackingPerspectives: number [可选] - 左右装包需求角度
            leftAndRightUnpackingPerspectives: number [可选] - 左右拆包需求角度
            lockInfoList: array [可选]
                        enterUnlockExtraNum: integer [可选] - 入仓电池包号锁解锁次数
                        enterUnlockMaxTorque: number [可选] - 入仓电池包号锁最大解锁扭矩
                        enterUnlockRecognizeNum: number [可选] - 入仓电池包解锁认帽圈数
                        enterUnlockRingNum: number [可选] - 入仓电池包号锁解锁圈数
                        lockNo: integer [可选]
                        outLockMaxTorque: number [可选] - 出仓电池包号锁最大加锁扭矩
                        outLockRingNum: number [可选] - 出仓电池包号锁加锁圈数
                        ringsNum: number [可选]
            packingOfLeftFrontHighReachAxle: number [可选] - 左前探高轴拆包测量值
            packingOfLeftRearHighReachAxle: number [可选] - 左后探高轴装包测量值
            packingOfRightFrontHighReachAxle: number [可选] - 右前探高轴装包测量值
            packingOfRightRearHighReachAxle: number [可选] - 右后探高轴装包测量值
            packingOffsetValueInXDirection: number [可选] - X向装包偏移值
            packingPositionOfScissorLiftShaft: number [可选] - 剪叉升降轴装包位置
            preAndPostPackingPerspectives: number [可选] - 前后装包需求角度
            preAndPostUnpackingPerspectives: number [可选] - 前后拆包需求角度
            sn: string [可选] - sn
            unpackingOfLeftFrontHighReachAxle: number [可选] - 左前探高轴拆包测量值
            unpackingOfLeftRearHighReachAxle: number [可选] - 左后探高轴拆包测量值
            unpackingOfRightFrontHighReachAxle: number [可选] - 右前探高轴拆包测量值
            unpackingOfRightRearHighReachAxle: number [可选] - 右后探高轴拆包测量值
            unpackingOffsetValueInXDirection: number [可选] - X向拆包偏移值
            unpackingPositionOfScissorLiftShaft: number [可选] - 剪叉升降轴拆包位置
        """
        path = f'/api/virtual/feign/lockBatteryData'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_movedBatteryPosition(data):
        """
        电池移仓
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/movedBatteryPosition'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_pauseOperation(data):
        """
        运动过程中暂停
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/pauseOperation'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_plcRecipeDigestVerify(data):
        """
        PLC配方校验请求
        请求参数:
            batteryCompartmentRecipeDigest: string [可选] - 电池仓内配方的消息摘要值
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
            swapBaseRecipeDigest: string [可选] - 换电时基础配方的消息摘要值
            swapDeltaRecipeDigest: string [可选] - 换电时Delta配方的消息摘要值
        """
        path = f'/api/virtual/feign/plcRecipeDigestVerify'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_readBatteryCompartmentRecipeDigest(data):
        """
        读取电池仓配方详细信息
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            readBatteryCompartmentRecipeDigest: string [可选] - 电池仓配方
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/readBatteryCompartmentRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_readSwapBaseRecipeDigest(data):
        """
        读取换电通道基础配方详细信息
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            readSwapBaseRecipeDigest: string [可选] - 换电通道基础配方
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/readSwapBaseRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_readSwapDeltaRecipeDigest(data):
        """
        读取换电通道Delta配方详细信息
        请求参数:
            carModel: string [可选] - 车型代号
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            readSwapDeltaRecipeDigest: string [可选] - 换电通道Delta配方
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/readSwapDeltaRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_reportBatteryRecipeDigest(data):
        """
        配方请求0504
        请求参数:
            account: string [可选]
            request: integer [可选]
            username: string [可选]
        """
        path = f'/api/virtual/feign/reportBatteryRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_reportChannelRecipeDigest(data):
        """
        配方请求0505
        请求参数:
            account: string [可选]
            request: integer [可选]
            username: string [可选]
        """
        path = f'/api/virtual/feign/reportChannelRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_reportStationModelRecipeDigest(data):
        """
        上报站型配置
        请求参数:
            carModel: string [可选]
            data: array [可选]
                        desc: string [可选]
                        name: string [可选]
                        value: integer [可选]
            plcPrescription: string [可选]
        """
        path = f'/api/virtual/feign/reportStationModelRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_reportStationParamInfo(data):
        """
        站点参数上报050B
        请求参数:
            iterationVersion: integer [可选] - 迭代版本 0：默认值 1：V3.0 2：V3.1 3：V3.2
            sizeVersion: integer [可选] - 尺寸版本 0：默认值 1：Pro 2：Max 3：Miix
            structuralType: integer [可选] - 结构类型 0：默认值 1：单仓-左工位（SL） 2：单仓-右工位（SR） 
            tempAdaptation: integer [可选] - 尺寸版本 0：默认值 1：常温 2：低温 
        """
        path = f'/api/virtual/feign/reportStationParamInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_reportStationParamRecipeDigest(data):
        """
        上报站点参数
        请求参数:
            carModel: string [可选]
            data: array [可选]
                        desc: string [可选]
                        name: string [可选]
                        value: integer [可选]
            plcPrescription: string [可选]
        """
        path = f'/api/virtual/feign/reportStationParamRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_reportStationTypeAndCampInfo(data):
        """
        站型仓位信息上报050A
        请求参数:
            campCompatibleList: array [可选] - 时代电池兼容
                        lfp20SupportFlag: integer [可选] - 仓位支持LFP_20_01_L标志 0-不支持 1-支持
                        lfp25SupportFlag: integer [可选] - 仓位支持LFP_25_01_L标志 0-不支持 1-支持
                        lfp3501lSupportFlag: integer [可选] - 仓位支持LFP_35_01_L标志 0-不支持 1-支持
                        positionNo: integer [可选] - 仓位号 1-32 (如需初始化某个仓位需要填写，否则初始化全部仓位信息)
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            positionList: array [可选]
                        batteryFrameStatus: integer [可选] - 电池架位置信息 0：位于靠近换电通道的电池架 1：位于远离换电通道的电池架
                        batteryLibraryStatus: integer [可选] - 电池库位置信息 0：位于A侧电池库 1：位于B侧电池库
                        batteryPlaceStatus: integer [可选] - 电池在位信息状态 0：不存在该仓位或电池不在位 1：电池在位
                        highVoltageConfigStatus: integer [可选] - 高压配置状态 0：不存在高压 1：存在高压
                        positionBatteryRack: integer [可选] - 仓位电池架号(仓位不存在时默认发0) 表征1-15号电池架，最大值15
                        positionNo: integer [可选] - 仓位号 1-82 (如需初始化某个仓位需要填写，否则初始化全部仓位信息)
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
            rockA4: integer [可选] - 电池架A 25兼容 1：兼容 0：不兼容
            rockA5: integer [可选] - 电池架A 20兼容 1：兼容 0：不兼容
            rockA6: integer [可选] - 电池架A 35兼容 1：兼容 0：不兼容
            rockB4: integer [可选] - 电池架B 25兼容 1：兼容 0：不兼容
            rockB5: integer [可选] - 电池架B 20兼容 1：兼容 0：不兼容
            rockB6: integer [可选] - 电池架B 35兼容 1：兼容 0：不兼容
            rockC4: integer [可选] - 电池架C 25兼容 1：兼容 0：不兼容
            rockC5: integer [可选] - 电池架C 20兼容 1：兼容 0：不兼容
            rockC6: integer [可选] - 电池架C 35兼容 1：兼容 0：不兼容
            rockD4: integer [可选] - 电池架D 25兼容 1：兼容 0：不兼容
            rockD5: integer [可选] - 电池架D 20兼容 1：兼容 0：不兼容
            rockD6: integer [可选] - 电池架D 35兼容 1：兼容 0：不兼容
            stationType: integer [可选] - 换电站类型 11：一代V1.0.0乘用车标准 12：一代V2.0.0乘用车标准 21：二代V1.0.0乘用车标准 22：二代V2.0.0乘用车标准 23：二代V2.0.0乘用车小型 24：二代V2.0.0乘用车大型 25：二代V2.0.0轻卡标准站 31：三代V3.0.0乘用车Pro站 32：三代V3.0.0乘用车Pro MAX站 33：三代V3.0.0乘用车Lite站
        """
        path = f'/api/virtual/feign/reportStationTypeAndCampInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_reportVehicleModelRecipeDigest(data):
        """
        上报车型配方0509
        请求参数:
            carModel: string [可选]
            data: array [可选]
                        desc: string [可选]
                        name: string [可选]
                        value: integer [可选]
            plcPrescription: string [可选]
        """
        path = f'/api/virtual/feign/reportVehicleModelRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_reportVehicleRecipeDigest(data):
        """
        配方请求0506
        请求参数:
            account: string [可选]
            request: integer [可选]
            username: string [可选]
        """
        path = f'/api/virtual/feign/reportVehicleRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_reportVideo(data):
        """
        语音推送 050C
        请求参数:
            videoCode: integer [可选]
        """
        path = f'/api/virtual/feign/reportVideo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_repositionBattery(data):
        """
        电池重放
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/repositionBattery'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_rgvDriveChannel(data):
        """
        RGV行驶至换电通道 (不带电池)
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/rgvDriveChannel'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_rgvReturn(data):
        """
        RGV回位 (不带电池)
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/rgvReturn'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_scramOperation(data):
        """
        运动过程中急停
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/scramOperation'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_startSwap(data):
        """
        发送执行换电任务指令
        请求参数:
            failCamp1: integer [可选]
            failCamp2: integer [可选]
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/startSwap'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_stationAndCampInfoForeSync(data):
        """
        换电电池及仓位信息预同步
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/stationAndCampInfoForeSync'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_swapAndPositionInfo(data):
        """
        同步和初始化仓位信息
        请求参数:
            campCompatibleList: array [可选] - 时代电池兼容
                        lfp20SupportFlag: integer [可选] - 仓位支持LFP_20_01_L标志 0-不支持 1-支持
                        lfp25SupportFlag: integer [可选] - 仓位支持LFP_25_01_L标志 0-不支持 1-支持
                        lfp3501lSupportFlag: integer [可选] - 仓位支持LFP_35_01_L标志 0-不支持 1-支持
                        positionNo: integer [可选] - 仓位号 1-32 (如需初始化某个仓位需要填写，否则初始化全部仓位信息)
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            positionList: array [可选]
                        batteryFrameStatus: integer [可选] - 电池架位置信息 0：位于靠近换电通道的电池架 1：位于远离换电通道的电池架
                        batteryLibraryStatus: integer [可选] - 电池库位置信息 0：位于A侧电池库 1：位于B侧电池库
                        batteryPlaceStatus: integer [可选] - 电池在位信息状态 0：不存在该仓位或电池不在位 1：电池在位
                        highVoltageConfigStatus: integer [可选] - 高压配置状态 0：不存在高压 1：存在高压
                        positionBatteryRack: integer [可选] - 仓位电池架号(仓位不存在时默认发0) 表征1-15号电池架，最大值15
                        positionNo: integer [可选] - 仓位号 1-82 (如需初始化某个仓位需要填写，否则初始化全部仓位信息)
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
            rockA4: integer [可选] - 电池架A 25兼容 1：兼容 0：不兼容
            rockA5: integer [可选] - 电池架A 20兼容 1：兼容 0：不兼容
            rockA6: integer [可选] - 电池架A 35兼容 1：兼容 0：不兼容
            rockB4: integer [可选] - 电池架B 25兼容 1：兼容 0：不兼容
            rockB5: integer [可选] - 电池架B 20兼容 1：兼容 0：不兼容
            rockB6: integer [可选] - 电池架B 35兼容 1：兼容 0：不兼容
            rockC4: integer [可选] - 电池架C 25兼容 1：兼容 0：不兼容
            rockC5: integer [可选] - 电池架C 20兼容 1：兼容 0：不兼容
            rockC6: integer [可选] - 电池架C 35兼容 1：兼容 0：不兼容
            rockD4: integer [可选] - 电池架D 25兼容 1：兼容 0：不兼容
            rockD5: integer [可选] - 电池架D 20兼容 1：兼容 0：不兼容
            rockD6: integer [可选] - 电池架D 35兼容 1：兼容 0：不兼容
            stationType: integer [可选] - 换电站类型 11：一代V1.0.0乘用车标准 12：一代V2.0.0乘用车标准 21：二代V1.0.0乘用车标准 22：二代V2.0.0乘用车标准 23：二代V2.0.0乘用车小型 24：二代V2.0.0乘用车大型 25：二代V2.0.0轻卡标准站 31：三代V3.0.0乘用车Pro站 32：三代V3.0.0乘用车Pro MAX站 33：三代V3.0.0乘用车Lite站
        """
        path = f'/api/virtual/feign/swapAndPositionInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_thermalRunawayBatteryChannel(data):
        """
        消防移仓至换电通道
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/thermalRunawayBatteryChannel'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_thermalRunawayBatterySandbox(data):
        """
        消防移仓
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/thermalRunawayBatterySandbox'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_touchScreenRestart(data):
        """
        plc触摸屏重启0035
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/touchScreenRestart'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_upgrade(data):
        """
        PLC软件升级
        请求参数:
            upgrade: integer [可选]
        """
        path = f'/api/virtual/feign/upgrade'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_writeBatteryCompartmentRecipeDigest(data):
        """
        写入电池仓配方详细信息 3代2F
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/writeBatteryCompartmentRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_writeSwapBaseRecipeDigest(data):
        """
        写入换电通道基础配方详细信息 3代30
        请求参数:
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/writeSwapBaseRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def api_virtual_feign_writeSwapDeltaRecipeDigest(data):
        """
        写入换电通道Delta配方详细信息 3代31
        请求参数:
            carModel: string [可选] - 车型代号
            faultReason: integer [可选] - 错误信息 见协议
            faultReasonDetail: string [可选] - 错误原因 见协议
            result: integer [可选] - 执行结果 1-执行中 2-执行完毕 3-执行错误，支持重新选包 4-执行错误，不支持重新选包
        """
        path = f'/api/virtual/feign/writeSwapDeltaRecipeDigest'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def cloud_evogoMerchant_operation_external_vehicleInfo_getRdbFault(data):
        """
        获取rdb信息
        """
        path = f'/cloud/evogoMerchant/operation/external/vehicleInfo/getRdbFault'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def cloud_evogoMerchant_operation_external_vehicleInfo_getSwapInfoByCarNo(data):
        """
        通过车牌号获取半自动换电信息
        """
        path = f'/cloud/evogoMerchant/operation/external/vehicleInfo/getSwapInfoByCarNo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def modbusVirtual_getCoinsData():
        """
        查询线圈数据
        请求参数:
            port: integer [可选] - port
            slaveId: integer [可选] - 从机id
        """
        path = f'/modbusVirtual/getCoinsData'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'GET', None))

    @staticmethod
    def modbusVirtual_getHoldingRegistersData():
        """
        查询保持寄存器值数据
        请求参数:
            port: integer [可选] - port
            slaveId: integer [可选] - 从机id
        """
        path = f'/modbusVirtual/getHoldingRegistersData'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'GET', None))

    @staticmethod
    def modbusVirtual_getInputRegistersData():
        """
        查询输入寄存器值数据
        请求参数:
            port: integer [可选] - port
            slaveId: integer [可选] - 从机id
        """
        path = f'/modbusVirtual/getInputRegistersData'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'GET', None))

    @staticmethod
    def modbusVirtual_getModbusServers():
        """
        查询mobdbus服务信息列表
        """
        path = f'/modbusVirtual/getModbusServers'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'GET', None))

    @staticmethod
    def modbusVirtual_getReadDiscreteInputsData():
        """
        查询离散量值数据
        请求参数:
            port: integer [可选] - port
            slaveId: integer [可选] - 从机id
        """
        path = f'/modbusVirtual/getReadDiscreteInputsData'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'GET', None))

    @staticmethod
    def modbusVirtual_initReadHoldingRegisters(data):
        """
        初始化保持寄存器值(PLC)
        """
        path = f'/modbusVirtual/initReadHoldingRegisters'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def modbusVirtual_updateReadCoils(data):
        """
        更新线圈值
        请求参数:
            id: integer [可选] - 地址
            port: integer [可选] - port
            slaveId: integer [可选] - 从机id
            value: integer [可选] - 值
        """
        path = f'/modbusVirtual/updateReadCoils'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def modbusVirtual_updateReadDiscreteInputs(data):
        """
        更新离散量值
        请求参数:
            id: integer [可选] - 地址
            port: integer [可选] - port
            slaveId: integer [可选] - 从机id
            value: integer [可选] - 值
        """
        path = f'/modbusVirtual/updateReadDiscreteInputs'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def modbusVirtual_updateReadHoldingRegisters(data):
        """
        更新保持寄存器值
        请求参数:
            ashortValue: integer [可选]
            id: integer [可选] - 地址
            port: integer [可选] - port
            slaveId: integer [可选] - 从机id
            value: integer [可选] - 值
        """
        path = f'/modbusVirtual/updateReadHoldingRegisters'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def modbusVirtual_updateReadInputRegisters(data):
        """
        更新输入寄存器值
        请求参数:
            id: integer [可选] - 地址
            port: integer [可选] - port
            slaveId: integer [可选] - 从机id
            value: integer [可选] - 值
        """
        path = f'/modbusVirtual/updateReadInputRegisters'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))
