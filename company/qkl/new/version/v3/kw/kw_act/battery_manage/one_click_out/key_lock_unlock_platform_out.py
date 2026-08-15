from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.act.battery_manage.one_click_out.lock_unlock_platform_out import LockUnlockPlatformOut

KeyLockUnlockPlatformOut = {
    "加解锁平台上升：执行中": HandlerKw.kw(LockUnlockPlatformOut.action_1),
    "加解锁平台回位：执行完毕": HandlerKw.kw(LockUnlockPlatformOut.action_2),
    "加解锁平台回位：执行错误": HandlerKw.kw(LockUnlockPlatformOut.action_3),
}
