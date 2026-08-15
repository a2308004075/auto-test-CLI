from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.act.battery_manage.one_click_return.lock_unlock_platform_return import LockUnlockPlatformReturn

KeyLockUnlockPlatformReturn = {
    "加解锁平台回位：执行中": HandlerKw.kw(LockUnlockPlatformReturn.action_1),
    "加解锁平台回位：执行完毕": HandlerKw.kw(LockUnlockPlatformReturn.action_2),
    "加解锁平台回位：执行错误": HandlerKw.kw(LockUnlockPlatformReturn.action_3),
}
