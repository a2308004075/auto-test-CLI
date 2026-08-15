from common.handlerKw.handlerKw import HandlerKw
from company.qkl.old.common.wss.old_wss import OldWss

KeyOldWss = {
    "获取newWebSocket的wss消息": HandlerKw.kw(OldWss.manager_newWebSocket),
    "获取rbcWebSocket的wss消息": HandlerKw.kw(OldWss.rbc_webSocket),
    "获取webSocketOfManager的wss消息": HandlerKw.kw(OldWss.manager_webSocketOfManager),
}
