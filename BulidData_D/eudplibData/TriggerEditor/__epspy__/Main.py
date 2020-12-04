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

# (Line 1) import TriggerEditor.SCArchive as sca;
from TriggerEditor import SCArchive as sca
# (Line 2) import System as sys;
import System as sys
# (Line 3) import Variable as v;
import Variable as v
# (Line 4) import Screen as screen;
import Screen as screen
# (Line 5) import Opening as opening;
import Opening as opening
# (Line 6) import User.Info as user;
from User import Info as user
# (Line 7) import Potal as potal;
import Potal as potal
# (Line 8) import Inventory as inven;
import Inventory as inven
# (Line 9) import Equip as equip;
import Equip as equip
# (Line 10) import Box as box;
import Box as box
# (Line 11) import StatusBar as status;
import StatusBar as status
# (Line 12) import Monster.Spawn as spawn;
from Monster import Spawn as spawn
# (Line 13) import Monster.Kill as kill;
from Monster import Kill as kill
# (Line 14) import timeline as tL;
import timeline as tL
# (Line 15) import TriggerEditor.BGMPlayer as bgm;
from TriggerEditor import BGMPlayer as bgm
# (Line 16) import Crack as crack;
import Crack as crack
# (Line 17) import User.ClickedUnit as unit;
from User import ClickedUnit as unit
# (Line 18) import KeyDetect as key;
import KeyDetect as key
# (Line 19) import ChatDetect as chat;
import ChatDetect as chat
# (Line 20) import Cheat as cheat;
import Cheat as cheat
# (Line 21) import NPC.Guard as guard;
from NPC import Guard as guard
# (Line 22) import SCA.Data as data;
from SCA import Data as data
# (Line 23) import SCA.Slot as slot;
from SCA import Slot as slot
# (Line 24) import SCA.Save as save;
from SCA import Save as save
# (Line 25) import SCA.MemoryCrystal as memory;
from SCA import MemoryCrystal as memory
# (Line 26) import User.Character as char;
from User import Character as char
# (Line 27) import MSQCVariable;
import MSQCVariable
# (Line 29) const wideCheck = PVariable();
wideCheck = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 31) function MoveCivilian();
# (Line 33) function onPluginStart() {
@EUDTracedFunc
def onPluginStart():
    # (Line 34) randomize();
    EUDTraceLog(34)
    f_randomize()
    # (Line 35) sca.Init();
    EUDTraceLog(35)
    sca.Init()
    # (Line 36) sys.Init();
    EUDTraceLog(36)
    sys.Init()
    # (Line 37) sca.SetUseDefaultMessage(0);
    EUDTraceLog(37)
    sca.SetUseDefaultMessage(0)
    # (Line 39) EUDRegisterObjectToNamespace("KeyD", v.KeyD);
    EUDTraceLog(39)
    EUDRegisterObjectToNamespace("KeyD", v.KeyD)
    # (Line 40) EUDRegisterObjectToNamespace("KeyF", v.KeyF);
    EUDTraceLog(40)
    EUDRegisterObjectToNamespace("KeyF", v.KeyF)
    # (Line 41) EUDRegisterObjectToNamespace("KeyG", v.KeyG);
    EUDTraceLog(41)
    EUDRegisterObjectToNamespace("KeyG", v.KeyG)
    # (Line 42) EUDRegisterObjectToNamespace("KeyH", v.KeyH);
    EUDTraceLog(42)
    EUDRegisterObjectToNamespace("KeyH", v.KeyH)
    # (Line 47) bgm.loadSound();
    EUDTraceLog(47)
    bgm.f_loadSound()
    # (Line 63) foreach (cp : EUDLoopPlayer()) {
    for cp in EUDLoopPlayer():
        # (Line 64) setcurpl(cp);
        EUDTraceLog(64)
        f_setcurpl(cp)
        # (Line 65) bgm.SetBGM(0);
        EUDTraceLog(65)
        bgm.SetBGM(0)
        # (Line 67) status.stats[cp] = status.USER_STATUS;
        EUDTraceLog(67)
        _ARRW(status.stats, cp) << (status.USER_STATUS)
        # (Line 68) if(sys.single == false) screen.WideCheck();
        _t1 = EUDIf()
        EUDTraceLog(68)
        if _t1(sys.single == False):
            EUDTraceLog(68)
            screen.WideCheck()
            # (Line 69) char.NewCharacter();
        EUDEndIf()
        EUDTraceLog(69)
        char.NewCharacter()
        # (Line 70) }
        # (Line 74) }

    # (Line 76) function beforeTriggerExec() {

@EUDTracedFunc
def beforeTriggerExec():
    # (Line 77) sca.Exec();
    EUDTraceLog(77)
    sca.Exec()
    # (Line 80) sys.AllyCheck();
    EUDTraceLog(80)
    sys.AllyCheck()
    # (Line 81) foreach (cp : EUDLoopPlayer()) {
    for cp in EUDLoopPlayer():
        # (Line 82) setcurpl(cp);
        EUDTraceLog(82)
        f_setcurpl(cp)
        # (Line 83) bgm.Play();
        EUDTraceLog(83)
        bgm.Play()
        # (Line 84) sys.GetDeath();
        EUDTraceLog(84)
        sys.GetDeath()
        # (Line 85) sys.GetMousePos();
        EUDTraceLog(85)
        sys.GetMousePos()
        # (Line 86) cheat.Cheat();
        EUDTraceLog(86)
        cheat.Cheat()
        # (Line 88) if(user.isAlive[cp] == 1) {
        _t1 = EUDIf()
        EUDTraceLog(88)
        if _t1(user.isAlive[cp] == 1):
            # (Line 89) user.posX[cp], user.posY[cp] = dwbreak(dwread_epd(user.character[cp] + 0x28 / 4))[[0,1]];
            EUDTraceLog(89)
            _SV([_ARRW(user.posX, cp), _ARRW(user.posY, cp)], [_SRET(f_dwbreak(f_dwread_epd(user.character[cp] + 0x28 // 4)), [0, 1])])
            # (Line 90) }
            # (Line 97) if(user.isAlive[cp] == 1) {
        EUDEndIf()
        _t2 = EUDIf()
        EUDTraceLog(97)
        if _t2(user.isAlive[cp] == 1):
            # (Line 98) if(MemoryXEPD(user.character[cp] + 0x4D / 4, Exactly, 3 << 8, 0xFF00)) {
            _t3 = EUDIf()
            EUDTraceLog(98)
            if _t3(MemoryXEPD(user.character[cp] + 0x4D // 4, Exactly, _LSH(3,8), 0xFF00)):
                # (Line 99) SetMemoryXEPD(user.character[cp] + 0x4D / 4, SetTo, 107 << 8 , 0xFF00);
                # (Line 100) }
                EUDTraceLog(99)
                DoActions(SetMemoryXEPD(user.character[cp] + 0x4D // 4, SetTo, _LSH(107,8), 0xFF00))
                # (Line 101) }
            EUDEndIf()
            # (Line 103) guard.Guard();
        EUDEndIf()
        EUDTraceLog(103)
        guard.Guard()
        # (Line 105) status.StatusBar(); // 상태바
        EUDTraceLog(105)
        status.StatusBar()
        # (Line 106) screen.LightCheck(); // 밝기 조절
        EUDTraceLog(106)
        screen.LightCheck()
        # (Line 107) potal.PotalCheck(); // 포탈 이동
        EUDTraceLog(107)
        potal.PotalCheck()
        # (Line 108) sys.PlayerLoc(); // 플레이어 로케이션
        EUDTraceLog(108)
        sys.PlayerLoc()
        # (Line 109) sys.ExpCheck(); // 경험치 변동 체크
        EUDTraceLog(109)
        sys.ExpCheck()
        # (Line 110) kill.KillCheck(); // 플레이어 킬 체크
        EUDTraceLog(110)
        kill.KillCheck()
        # (Line 112) inven.Inventory(); // 인벤토리
        EUDTraceLog(112)
        inven.Inventory()
        # (Line 113) equip.Equip(); // 장비
        EUDTraceLog(113)
        equip.Equip()
        # (Line 116) memory.MemoryCrystal(); // 저장 크리스탈
        EUDTraceLog(116)
        memory.MemoryCrystal()
        # (Line 117) save.SaveCheck(); // 저장
        EUDTraceLog(117)
        save.SaveCheck()
        # (Line 119) key.KeyDetect(cp);
        EUDTraceLog(119)
        key.KeyDetect(cp)
        # (Line 120) chat.ChatDetect(cp);
        EUDTraceLog(120)
        chat.ChatDetect(cp)
        # (Line 121) screen.WideCheckExec();
        EUDTraceLog(121)
        screen.WideCheckExec()
        # (Line 124) }
        # (Line 125) unit.clickedUnit();

    EUDTraceLog(125)
    unit.f_clickedUnit()
    # (Line 136) SetMemory(0x5124F0, SetTo, 28);
    # (Line 137) }
    EUDTraceLog(136)
    DoActions(SetMemory(0x5124F0, SetTo, 28))
    # (Line 139) function afterTriggerExec() {

@EUDTracedFunc
def afterTriggerExec():
    # (Line 141) foreach (cp : EUDLoopPlayer()) {
    for cp in EUDLoopPlayer():
        # (Line 142) setcurpl(cp);
        EUDTraceLog(142)
        f_setcurpl(cp)
        # (Line 144) }
        # (Line 145) }
