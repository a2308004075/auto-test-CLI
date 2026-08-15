import time
from common.handlerKw.runKw import RunKw
from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.version.v3.kw.kw_act.swap_manage.swap_flow.key_swap_flow import KeySwapFlow


class TestSwapFlow:
    @staticmethod
    @KwDecorator('初始化车辆状态')
    def test_init_car():
        RunKw.act_run(KeySwapFlow, '初始化车辆状态', 1)  # 1-25_LFP,2-20_LFP

    @staticmethod
    @KwDecorator('初始化PLC')
    def test_init_plc():
        RunKw.act_run(KeySwapFlow, '初始化PLC')

    @staticmethod
    @KwDecorator('抓拍车牌')
    def test_swap_cameraSendCarNo():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '抓拍车牌', '闽DDE5917')

    @staticmethod
    @KwDecorator('云端认证：允许抬杆')
    def test_swap_cloudReceiveCloudValid_ableToChangeTrue():
        # 测试步骤
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '云端认证', '闽DDE5917', '4', True)  # 4-25#LFP,5-20#LFP
        # 测试校验

    @staticmethod
    @KwDecorator('云端认证：不允许抬杆')
    def test_swap_cloudReceiveCloudValid_ableToChangeFalse():
        # 测试步骤
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '云端认证', '闽DDE5917', '4', False)  # 4-25#LFP,5-20#LFP
        # 测试校验

    @staticmethod
    @KwDecorator('云端认证：允许抬杆、用户租赁的电池包类别不符合规则')
    def test_swap_cloudReceiveCloudValid_packType():
        # 测试步骤
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '云端认证', '闽DDE5917', '57', True)  # 4-25#LFP,5-20#LFP
        # 测试校验

    @staticmethod
    @KwDecorator('云端认证：允许抬杆、用户租赁的电池包类别不符合规则')
    def test_swap_plcRecipeDigestVerify():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, 'PLC配方校验：通过', '闽DDE5917', '4')  # 4-25#LFP,5-20#LFP

    @staticmethod
    @KwDecorator('驶入换电通道至PLC：通过')
    def test_swap_plcAllowVehicleEnter():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '驶入换电通道至PLC：通过', '闽DDE5917', '4')  # 4-25#LFP,5-20#LFP

    @staticmethod
    @KwDecorator('【云->站】车辆停稳应答：通过')
    def test_swap_cloudCarStoppedResp():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '【云->站】车辆停稳应答：通过', '闽DDE5917', '4')  # 4-25#LFP,5-20#LFP

    @staticmethod
    @KwDecorator('同步仓位信息至PLC')
    def test_swap_plcSwapCampInfo():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '同步仓位信息至PLC', '闽DDE5917', '4')  # 4-25#LFP,5-20#LFP

    @staticmethod
    @KwDecorator('【云->站】云端发送开始换电：允许换电')
    def test_swap_cloudStartSwap():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '【云->站】云端发送开始换电：允许换电', '闽DDE5917', '4')  # 4-25#LFP,5-20#LFP

    @staticmethod
    @KwDecorator('归中举升：通过')
    def test_swap_plcBackCenterAndLift():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '归中举升：通过', '闽DDE5917', '4')  # 4-25#LFP,5-20#LFP

    @staticmethod
    @KwDecorator('拆装电池包：通过')
    def test_swap_plcAllowDisassemblyBattery():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '拆装电池包：通过', '闽DDE5917', '4')  # 4-25#LFP,5-20#LFP

    @staticmethod
    @KwDecorator('设备归位：通过')
    def test_swap_plcAllowReturnVehicle():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '设备归位：通过', '闽DDE5917', '4')  # 4-25#LFP,5-20#LFP

    @staticmethod
    @KwDecorator('车辆驶离：通过')
    def test_swap_plcAllowVehicleLeave():
        """
        车辆驶离通过，一次换电成功
        """
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '车辆驶离：通过', '闽DDE5917', '4')  # 4-25#LFP,5-20#LFP

    @staticmethod
    @KwDecorator('换电出仓清站外小计：未响应')
    def test_SubInfoOutClrSts_0():
        """
        电池出仓，换电出仓清站外小计：未响应
        """
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '换电出仓清站外小计：未响应', '闽DDE5917', '4')  # 4-25#LFP,5-20#LFP

    @staticmethod
    @KwDecorator('换电出仓清站外小计：失败')
    def test_SubInfoOutClrSts_1():
        """
        电池出仓，换电出仓清站外小计：失败
        """
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '换电出仓清站外小计：失败', '闽DDE5917', '4')  # 4-25#LFP,5-20#LFP

    @staticmethod
    @KwDecorator('换电出仓清站外小计：成功')
    def test_SubInfoOutClrSts_2():
        """
        电池出仓，换电出仓清站外小计：成功
        """
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        RunKw.act_run(KeySwapFlow, '换电出仓清站外小计：成功', '闽DDE5917', '4')  # 4-25#LFP,5-20#LFP

    @staticmethod
    @KwDecorator('换电入仓清站内小计：未响应')
    def test_SubInfoInClrSts_0():
        """
        换电完成，换电入仓清站内小计：未响应
        """
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '换电入仓清站内小计：未响应', '闽DDE5917', '4')  # 4-25#LFP,5-20#LFP

    @staticmethod
    @KwDecorator('换电入仓清站内小计：失败')
    def test_SubInfoInClrSts_1():
        """
        换电完成，换电入仓清站内小计：失败
        """
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '换电入仓清站内小计：失败', '闽DDE5917', '4')  # 4-25#LFP,5-20#LFP

    @staticmethod
    @KwDecorator('换电入仓清站内小计：成功')
    def test_SubInfoInClrSts_2():
        """
        换电完成，换电入仓清站内小计：成功
        """
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '换电入仓清站内小计：成功', '闽DDE5917', '4')  # 4-25#LFP,5-20#LFP

    @staticmethod
    @KwDecorator('车机信息不全，车辆停稳失')
    def test_swap_cloudCarStoppedResp_delCarInfo():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '车机信息不全，车辆停稳失败', 'v3_10B_command', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('车机信息不发【电池包SN】【车上电池真实SOC】【总里程信息】，车辆停稳失败')
    def test_swap_cloudCarStoppedResp_delAllCarInfo():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '车机信息不发【电池包SN】【车上电池真实SOC】【总里程信息】，车辆停稳失败', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('车机信息不全，10s内获取车辆停稳成功')
    def test_swap_cloudCarStoppedResp_delCarInfo_10s():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '车机信息不全，10s内获取车辆停稳成功', 'v3_244_command', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('离线换电，车机信息不全，车辆停稳失败')
    def test_swap_cloudCarStoppedResp_offCloud_DelCarInfo_false():
        RunKw.act_run(KeySwapFlow, '离线换电，车机信息不全，车辆停稳失败', 'v3_244_command')

    @staticmethod
    @KwDecorator('离线换电，车机信息不全，车辆停稳成功')
    def test_swap_cloudCarStoppedResp_offCloud_DelCarInfo():
        RunKw.act_run(KeySwapFlow, '离线换电，车机信息不全，车辆停稳成功', 'v3_244_command', '4')

    @staticmethod
    @KwDecorator('车机未发0x105，换电继续')
    def test_swap_closeAndDisableHVContactorBefor_carInfo():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)

        RunKw.act_run(KeySwapFlow, '车机未发0x105，换电继续', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('MBMU最高故障等级2、6、7、8')
    def test_swap_closeAndDisableHVContactor_supremeErrorLevelOfBattSys():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, 'MBMU最高故障等级2、6、7、8', '闽DDE5917', '4', 1, 8)

    @staticmethod
    @KwDecorator('PLC暂停，PLC超时未响应【归中举升请求】2：执行成功')
    def test_swap_plcBackCenterAndLift_stop():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, 'PLC暂停，PLC超时未响应【归中举升请求】2：执行成功', '闽DDE5917', '4', 4)

    @staticmethod
    @KwDecorator('PLC暂停，PLC超时未响应【拆装电池包】2：执行成功')
    def test_swap_plcAllowDisassemblyBattery_stop():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, 'PLC暂停，PLC超时未响应【拆装电池包】2：执行成功', '闽DDE5917', '4', 3)

    @staticmethod
    @KwDecorator('PLC暂停，PLC超时未响应【设备归位】2：执行成功')
    def test_swap_plcAllowReturnVehicle_stop():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, 'PLC暂停，PLC超时未响应【设备归位】2：执行成功', '闽DDE5917', '4', 4)

    @staticmethod
    @KwDecorator('PLC暂停，PLC超时未响应【车辆驶离】2：执行成功')
    def test_swap_plcAllowVehicleLeave_stop():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, 'PLC暂停，PLC超时未响应【车辆驶离】2：执行成功', '闽DDE5917', '4', 4)

    @staticmethod
    @KwDecorator('车机信息不全，10s内获收到车机信息，拆装电池包成功')
    def test_swap_plcAllowDisassemblyBattery_DelCarInfo_10s():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '车机信息不全，10s内获收到车机信息，拆装电池包成功', 'v3_13A_command', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('车机信息不全，拆安装包失败')
    def test_swap_plcAllowDisassemblyBattery_DelCarInfo_false():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '车机信息不全，拆安装包失败', 'v3_13A_command', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('车辆驶入到位前，顶部雷达状态，车辆左V槽在位信号不状态，车辆右V槽在位信号状态')
    def test_swap_VehicleEnterBefor_SwapEquipmentStatus():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '车辆驶入到位前，顶部雷达状态，车辆左V槽在位信号不状态，车辆右V槽在位信号状态', '闽DDE5917', '4', 2, 2, 2)

    @staticmethod
    @KwDecorator('车辆驶入到位后，站控下控PLC归中举升前，顶部雷达状态，车辆左V槽在位信号不状态，车辆右V槽在位信号状态')
    def test_swap_VehicleEnterAfter_plcBackCenterAndLiftBefor_SwapEquipmentStatus():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '车辆驶入到位后，站控下控PLC归中举升前，顶部雷达状态，车辆左V槽在位信号不状态，车辆右V槽在位信号状态', '闽DDE5917', '4',
                          2,
                          1, 2)

    @staticmethod
    @KwDecorator('PLC归中举升后，站控下控PLC归中举升后，顶部雷达状态，车辆左V槽在位信号不状态，车辆右V槽在位信号状态')
    def test_swap_plcBackCenterAndLiftAfter_SwapEquipmentStatus():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, 'PLC归中举升后，站控下控PLC归中举升后，顶部雷达状态，车辆左V槽在位信号不状态，车辆右V槽在位信号状态', '闽DDE5917', '4',
                          2, 2, 2)

    @staticmethod
    @KwDecorator('无人值守，PLC归中举升失败，自复位，设备归位超时未响应执行中')
    def test_swap_plcBackCenterAndLift_selfReset_plcAllowReturnVehicle_timeout1():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '无人值守，PLC归中举升失败，自复位，设备归位超时未响应执行中', '闽DDE5917', '4', 254)

    @staticmethod
    @KwDecorator('无人值守，PLC归中举升失败，自复位，设备归位超时未响应执行完成')
    def test_swap_plcBackCenterAndLift_selfReset_plcAllowReturnVehicle_timeout2():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '无人值守，PLC归中举升失败，自复位，设备归位超时未响应执行完成', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('无人值守，PLC归中举升失败，自复位，自检（最严重故障码，高压互锁状态）')
    def test_swap_plcBackCenterAndLift_selfReset_selfCheck_bmsmostCriticalFltID_hvil1State():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '无人值守，PLC归中举升失败，自复位，自检（最严重故障码，高压互锁状态）', '闽DDE5917', '4', 2, 0)

    @staticmethod
    @KwDecorator('无人值守，PLC归中举升失败，自复位，自检，车机停发129')
    def test_swap_plcBackCenterAndLift_selfReset_selfCheck_delV129():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '无人值守，PLC归中举升失败，自复位，自检，车机停发129', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('拆装电池包：执行中')
    def test_swap_plcAllowDisassemblyBattery_ing():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '拆装电池包：执行中', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('自检（最严重故障码，高压互锁状态）')
    def test_swap_selfCheck_bmsmostCriticalFltID_hvil1State():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '自检（最严重故障码，高压互锁状态）', '闽DDE5917', '4', 0, 2)

    @staticmethod
    @KwDecorator('自检，车机停发129')
    def test_swap_selfCheck_delV129():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '自检，车机停发129', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('自检，第二阶段12F心跳不变')
    def test_swap_selfCheck_heartNormal12F():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '自检，第二阶段12F心跳不变', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('自检，前两次满足自检条件，第三次不满足自检条件')
    def test_swap_selfCheck_heartNormal12F_110():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '自检，前两次满足自检条件，第三次不满足自检条件', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('自检，前两次不满足自检条件，第三次满足自检条件')
    def test_swap_selfCheck_heartNormal12F_001():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '自检，前两次不满足自检条件，第三次满足自检条件', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('自检，前两次不满足自检条件，第三次不满足满足自检条件')
    def test_swap_selfCheck_heartNormal12F_000():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '自检，前两次不满足自检条件，第三次不满足满足自检条件', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('自检，第一次满足自检条件，第二次不满足自检条件，第三次满足自检条件')
    def test_swap_selfCheck_heartNormal12F_101():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '自检，第一次满足自检条件，第二次不满足自检条件，第三次满足自检条件', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('自复位，自检，前两次满足自检条件，第三次不满足自检条件')
    def test_swap_selfReset_selfCheck_heartNormal12F_110():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '自复位，自检，前两次满足自检条件，第三次不满足自检条件', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('自复位，自检，前两次不满足自检条件，第三次满足自检条件')
    def test_swap_selfReset_selfCheck_heartNormal12F_001():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '自复位，自检，前两次不满足自检条件，第三次满足自检条件', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('自复位，自检，前两次不满足自检条件，第三次不满足满足自检条件')
    def test_swap_selfReset_selfCheck_heartNormal12F_000():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '自复位，自检，前两次不满足自检条件，第三次不满足满足自检条件', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('自复位，自检，第一次满足自检条件，第二次不满足自检条件，第三次满足自检条件')
    def test_swap_selfReset_selfCheck_heartNormal12F_101():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '自复位，自检，第一次满足自检条件，第二次不满足自检条件，第三次满足自检条件', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('车辆信息校验，缺少车辆电池SN')
    def test_swap_plcAllowVehicleLeave_delCarInfo_SN():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '车辆信息校验，缺少车辆电池SN', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('车辆信息校验，缺少VBLE MAC')
    def test_swap_plcAllowVehicleLeave_delCarInfo_MAC():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '车辆信息校验，缺少VBLE MAC', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('车辆信息校验，缺少packType')
    def test_swap_plcAllowVehicleLeave_delCarInfo_packType():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '车辆信息校验，缺少packType', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('车辆信息校验，缺少车辆电池SN、VBLE MAC、packType')
    def test_swap_plcAllowVehicleLeave_delCarInfo():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '车辆信息校验，缺少车辆电池SN、VBLE MAC、packType', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('车辆驶离条件判断，开合门未关到位')
    def test_swap_plcAllowVehicleLeave_openingClosingDoor():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '车辆驶离条件判断，开合门未关到位', '闽DDE5917', '4', 0)

    @staticmethod
    @KwDecorator('换电入仓，启动充电')
    def test_batteryIn_startCharge():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '换电入仓，启动充电', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('车机停发13A，进行换电')
    def test_swap_delCarInfo_13A():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '车机停发13A，进行换电', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('不同电池包，进行换电')
    def test_swap_packType():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '不同电池包，进行换电', '闽DDE5917', '5', 2)

    @staticmethod
    @KwDecorator('自由度监测阶段，方向盘')
    def test_swap_carFreedom_steeringTurnAngle():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '自由度监测阶段，方向盘', '闽DDE5917', '4', 91)

    @staticmethod
    @KwDecorator('归中举升中，方向角不满足')
    def test_swap_plcBackCenterAndLift_carFreedom_steeringTurnAngle():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(4)
        RunKw.act_run(KeySwapFlow, '归中举升中，方向角不满足', '闽DDE5917', '4', 4)

    @staticmethod
    @KwDecorator('站内有车，进行换电')
    def test_swap_have_car():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(2)
        RunKw.act_run(KeySwapFlow, '站内有车，进行换电', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('PLC超时未响应【车辆驶入换电站且到位请求】执行中，换电通道顶部雷达')
    def test_swap_plcAllowVehicleEntering_timeout():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(2)
        RunKw.act_run(KeySwapFlow, 'PLC超时未响应【车辆驶入换电站且到位请求】执行中，换电通道顶部雷达', '闽DDE5917', '4', 0, 2, 2)

    @staticmethod
    @KwDecorator('PLC超时未响应【车辆驶入换电站且到位请求】执行结果，换电通道顶部雷达')
    def test_swap_plcAllowVehicleEntered_timeout():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(2)
        RunKw.act_run(KeySwapFlow, 'PLC超时未响应【车辆驶入换电站且到位请求】执行结果，换电通道顶部雷达', '闽DDE5917', '4', 2, 2, 2)

    @staticmethod
    @KwDecorator('自由度超时，车机MBMU生命信号未发')
    def test_swap_delCarFreedom():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(2)
        RunKw.act_run(KeySwapFlow, '自由度超时，车机MBMU生命信号未发', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('车辆未驶入')
    def test_swap_VehicleEnter():
        TestSwapFlow.test_init_car()  # 初始化车辆状态
        TestSwapFlow.test_init_plc()  # 初始化PLC
        time.sleep(2)
        RunKw.act_run(KeySwapFlow, '车辆未驶入', '闽DDE5917', '4')

    @staticmethod
    @KwDecorator('车辆蓝牙连接成功')
    def test_connect_ble_success():
        """
        车辆蓝牙连接成功
        """
        RunKw.act_run(KeySwapFlow, '车辆蓝牙连接成功')

    @staticmethod
    @KwDecorator('车辆蓝牙断开成功')
    def test_disconnect_ble_success():
        """
        车辆蓝牙断开成功
        """
        RunKw.act_run(KeySwapFlow, '车辆蓝牙断开成功')

    @staticmethod
    @KwDecorator('驶入换电通道至PLC：执行中')
    def test_swap_plcAllowVehicleEntering():
        """
        驶入换电通道至PLC：执行中
        """
        RunKw.act_run(KeySwapFlow, '驶入换电通道至PLC：执行中', '闽DDE5917', '4')  # 4-25#LFP,5-20#LFP
