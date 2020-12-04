## NOTE: THIS FILE IS GENERATED BY EPSCRIPT! DO NOT MODITY
from eudplib import *

def _IGVA(vList, exprListGen):
    def _():
        exprList = exprListGen()
        SetVariables(vList, exprList)
    EUDOnStart(_)

def _CGFW(exprf, retn):
    rets = [ExprProxy(None) for _ in range(retn)]
    def _():
        vals = exprf()
        for ret, val in zip(rets, vals):
            ret._value = val
    EUDOnStart(_)
    return rets

def _ARR(items):
    k = EUDArray(len(items))
    for i, item in enumerate(items):
        k[i] = item
    return k

def _VARR(items):
    k = EUDVArray(len(items))()
    for i, item in enumerate(items):
        k[i] = item
    return k

def _SRET(v, klist):
    return List2Assignable([v[k] for k in klist])

def _SV(dL, sL):
    [d << s for d, s in zip(FlattenList(dL), FlattenList(sL))]

class _ATTW:
    def __init__(self, obj, attrName):
        self.obj = obj
        self.attrName = attrName

    def __lshift__(self, r):
        setattr(self.obj, self.attrName, r)

    def __iadd__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov + v)

    def __isub__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov - v)

    def __imul__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov * v)

    def __ifloordiv__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov // v)

    def __iand__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov & v)

    def __ior__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov | v)

    def __ixor__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov ^ v)

class _ARRW:
    def __init__(self, obj, index):
        self.obj = obj
        self.index = index

    def __lshift__(self, r):
        self.obj[self.index] = r

    def __iadd__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov + v

    def __isub__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov - v

    def __imul__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov * v

    def __ifloordiv__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov // v

    def __iand__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov & v

    def __ior__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov | v

    def __ixor__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov ^ v

def _L2V(l):
    ret = EUDVariable()
    if EUDIf()(l):
        ret << 1
    if EUDElse()():
        ret << 0
    EUDEndIf()
    return ret

def _MVAR(vs):
    return List2Assignable([
        v.makeL() if IsEUDVariable(v) else EUDVariable() << v
        for v in FlattenList(vs)])

def _LSH(l, r):
    if IsEUDVariable(l):  return f_bitlshift(l, r)
    else: return l << r

## NOTE: THIS FILE IS GENERATED BY EPSCRIPT! DO NOT MODITY

# (Line 1) import Variable as v;
import Variable as v
# (Line 2) import System as sys;
import System as sys
# (Line 3) import User.StatusBar as statusBar;
from User import StatusBar as statusBar
# (Line 4) import User.Character as char;
from User import Character as char
# (Line 5) import User.Inventory as inven;
from User import Inventory as inven
# (Line 6) import NPC.NPC as npc;
from NPC import NPC as npc
# (Line 7) import NPC.Guard as guard;
from NPC import Guard as guard
# (Line 8) import Item.Manager as item;
from Item import Manager as item
# (Line 9) import Screen as screen;
import Screen as screen
# (Line 10) import TriggerEditor.SCArchive as sca;
from TriggerEditor import SCArchive as sca
# (Line 12) function onPluginStart() {
@EUDFunc
def onPluginStart():
    # (Line 16) sys.SetPColor(7, 0);    // 플레이어 7 색 변경
    sys.SetPColor(7, 0)
    # (Line 17) sys.SetPColor(8, 196);  // 플레이어 8 색 변경
    sys.SetPColor(8, 196)
    # (Line 18) sys.RegisterMSQC();     // MSQC 변수
    sys.RegisterMSQC()
    # (Line 19) sys.SinglePlayCheck();  // 싱글플레이 체크
    sys.SinglePlayCheck()
    # (Line 20) sys.SetAlly();          // 동맹 설정
    sys.SetAlly()
    # (Line 21) npc.CreateNPC();        // NPC 유닛 생성
    npc.CreateNPC()
    # (Line 22) item.SetItemInfo();     // 아이템 정보 입력
    item.SetItemInfo()
    # (Line 24) foreach (cp : EUDLoopPlayer()) {
    for cp in EUDLoopPlayer():
        # (Line 25) setcurpl(cp);
        f_setcurpl(cp)
        # (Line 26) inven.ResetInven(); // 인벤토리 초기화
        inven.ResetInven()
        # (Line 27) sys.SetName(); // 유닛 이름 변경
        sys.SetName()
        # (Line 28) screen.light[cp] = 31; // 밝기 최대로 변경
        _ARRW(screen.light, cp) << (31)
        # (Line 29) statusBar.stats[cp] = statusBar.USER_STATUS; // 상태바 기본값으로 설정
        _ARRW(statusBar.stats, cp) << (statusBar.USER_STATUS)
        # (Line 30) char.NewCharacter(); // 캐릭터 생성 (임시)
        char.NewCharacter()
        # (Line 33) item.AddItem(10000, 1, 1, 10, true);
        item.AddItem(10000, 1, 1, 10, True)
        # (Line 34) item.AddItem(10000, 1, 2, 10, true);
        item.AddItem(10000, 1, 2, 10, True)
        # (Line 35) }
        # (Line 36) }

    # (Line 38) function beforeTriggerExec() {

@EUDFunc
def beforeTriggerExec():
    # (Line 39) sca.Exec();
    sca.Exec()
    # (Line 40) foreach (cp : EUDLoopPlayer()) {
    for cp in EUDLoopPlayer():
        # (Line 41) setcurpl(cp);
        f_setcurpl(cp)
        # (Line 42) sys.GetMousePos(); // 마우스 좌표
        sys.GetMousePos()
        # (Line 43) statusBar.StatusBar(); // 상태바
        statusBar.StatusBar()
        # (Line 44) sys.SetPlayerLoc(); // 플레이어 로케이션
        sys.SetPlayerLoc()
        # (Line 45) if(v.KeyALT[cp] == 1 && v.singlePlay == 0) screen.WideCheckStart(); // ALT키 와이드 체크
        if EUDIf()(EUDSCAnd()(v.KeyALT[cp] == 1)(v.singlePlay == 0)()):
            screen.WideCheckStart()
            # (Line 47) inven.Inventory(); // 인벤토리
        EUDEndIf()
        inven.Inventory()
        # (Line 48) guard.Guard(); // 경비병
        guard.Guard()
        # (Line 53) screen.WideCheckExec(); // 와이드 체크
        screen.WideCheckExec()
        # (Line 54) screen.LightCheck(); // 밝기 체크
        screen.LightCheck()
        # (Line 55) sys.AllyCheck(); // 동맹 체크
        sys.AllyCheck()
        # (Line 56) }
        # (Line 57) SetMemoryEPD(EPD(0x5124F0), SetTo, 28);

    # (Line 58) }
    DoActions(SetMemoryEPD(EPD(0x5124F0), SetTo, 28))
    # (Line 60) function afterTriggerExec() {

@EUDFunc
def afterTriggerExec():
    # (Line 62) }
    pass