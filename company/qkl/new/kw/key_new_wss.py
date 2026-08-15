from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.common.wss.new_wss import NewWss

KeyNewWss = {
    "获取currentProcessData的wss消息": HandlerKw.kw(NewWss.current_process_data_wss),
    "获取fireMoveWarn的wss消息": HandlerKw.kw(NewWss.fire_move_warn_wss),
    "获取underBox的wss消息": HandlerKw.kw(NewWss.under_box_wss),
    "获取volume的wss消息": HandlerKw.kw(NewWss.volume_wss),
}
