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

# (Line 1) import Inventory as inven;
import Inventory as inven
# (Line 2) import User.Info as user;
from User import Info as user
# (Line 3) import Variable as v;
import Variable as v
# (Line 4) import StatusBar as status;
import StatusBar as status
# (Line 5) import Item.Info.Weapon as weapon;
from Item.Info import Weapon as weapon
# (Line 6) import Equip as equip;
import Equip as equip
# (Line 7) import SCA.Data as data;
from SCA import Data as data
# (Line 8) import TriggerEditor.SCArchive as sca;
from TriggerEditor import SCArchive as sca
# (Line 13) const saveCoolDown = PVariable();
saveCoolDown = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 14) const saveTimer = PVariable();
saveTimer = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 15) const step = PVariable();
step = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 17) function SaveUserSlot();
# (Line 18) function SaveUserInven();
# (Line 19) function Save0Slot();
# (Line 21) function Save() {
@EUDTracedFunc
def Save():
    # (Line 22) const cp = getcurpl();
    EUDTraceLog(22)
    cp = f_getcurpl()
    # (Line 23) if(step[cp] != 0) return;
    _t1 = EUDIf()
    EUDTraceLog(23)
    if _t1(step[cp] == 0, neg=True):
        EUDTraceLog(23)
        EUDReturn()
        # (Line 24) if(sca.ConnectStatus() == 1) {
    EUDEndIf()
    _t2 = EUDIf()
    EUDTraceLog(24)
    if _t2(sca.ConnectStatus() == 1):
        # (Line 25) if(saveCoolDown[cp] == 0) {
        _t3 = EUDIf()
        EUDTraceLog(25)
        if _t3(saveCoolDown[cp] == 0):
            # (Line 26) SaveUserInven();
            EUDTraceLog(26)
            SaveUserInven()
            # (Line 30) sca.SaveData(user.currentSlot[cp]); // 현재 슬롯에 저장
            EUDTraceLog(30)
            sca.SaveData(user.currentSlot[cp])
            # (Line 31) status.stats[cp] = status.SAVE_START;
            EUDTraceLog(31)
            _ARRW(status.stats, cp) << (status.SAVE_START)
            # (Line 32) step[cp] = 1;
            EUDTraceLog(32)
            _ARRW(step, cp) << (1)
            # (Line 33) }
            # (Line 35) }
        EUDEndIf()
        # (Line 36) else status.stats[cp] = status.SCA_ERROR;
    if EUDElse()():
        EUDTraceLog(36)
        _ARRW(status.stats, cp) << (status.SCA_ERROR)
        # (Line 38) }
    EUDEndIf()
    # (Line 40) function SaveCheck() {

@EUDTracedFunc
def SaveCheck():
    # (Line 41) const cp = getcurpl();
    EUDTraceLog(41)
    cp = f_getcurpl()
    # (Line 42) if(saveCoolDown[cp] > 0) saveCoolDown[cp] -= 1;
    _t1 = EUDIf()
    EUDTraceLog(42)
    if _t1(saveCoolDown[cp] <= 0, neg=True):
        EUDTraceLog(42)
        _ARRW(saveCoolDown, cp).__isub__(1)
        # (Line 43) if(saveTimer[cp] > 0) saveTimer[cp] -= 1;
    EUDEndIf()
    _t2 = EUDIf()
    EUDTraceLog(43)
    if _t2(saveTimer[cp] <= 0, neg=True):
        EUDTraceLog(43)
        _ARRW(saveTimer, cp).__isub__(1)
        # (Line 44) if(step[cp] == 1) {
    EUDEndIf()
    _t3 = EUDIf()
    EUDTraceLog(44)
    if _t3(step[cp] == 1):
        # (Line 45) if(sca.GetLastMessage() == 6) {
        _t4 = EUDIf()
        EUDTraceLog(45)
        if _t4(sca.GetLastMessage() == 6):
            # (Line 46) sca.ResetLastMessage();
            EUDTraceLog(46)
            sca.ResetLastMessage()
            # (Line 47) step[cp] = 2;
            EUDTraceLog(47)
            _ARRW(step, cp) << (2)
            # (Line 48) saveTimer[cp] = 71;
            EUDTraceLog(48)
            _ARRW(saveTimer, cp) << (71)
            # (Line 49) }
            # (Line 50) }
        EUDEndIf()
        # (Line 51) else if(step[cp] == 2) {
    _t5 = EUDElseIf()
    EUDTraceLog(51)
    if _t5(step[cp] == 2):
        # (Line 52) if(saveTimer[cp] == 1) {
        _t6 = EUDIf()
        EUDTraceLog(52)
        if _t6(saveTimer[cp] == 1):
            # (Line 53) Save0Slot();
            EUDTraceLog(53)
            Save0Slot()
            # (Line 54) }
            # (Line 55) if(sca.GetLastMessage() == 6) {
        EUDEndIf()
        _t7 = EUDIf()
        EUDTraceLog(55)
        if _t7(sca.GetLastMessage() == 6):
            # (Line 56) sca.ResetLastMessage();
            EUDTraceLog(56)
            sca.ResetLastMessage()
            # (Line 57) status.stats[cp] = status.SAVE_END;
            EUDTraceLog(57)
            _ARRW(status.stats, cp) << (status.SAVE_END)
            # (Line 58) saveCoolDown[cp] = 71;
            EUDTraceLog(58)
            _ARRW(saveCoolDown, cp) << (71)
            # (Line 59) step[cp] = 0;
            EUDTraceLog(59)
            _ARRW(step, cp) << (0)
            # (Line 60) }
            # (Line 61) }
        EUDEndIf()
        # (Line 62) }
    EUDEndIf()
    # (Line 64) function SaveUserSlot() {

@EUDTracedFunc
def SaveUserSlot():
    # (Line 65) const cp = getcurpl();
    EUDTraceLog(65)
    cp = f_getcurpl()
    # (Line 66) const w = weapon.Weapon.cast(equip.equip[7 * cp + 0]);
    EUDTraceLog(66)
    w = weapon.Weapon.cast(equip.equip[7 * cp + 0])
    # (Line 67) var info = user.level[cp] * py_pow(10, 6) + user.playTimeHour[cp] * py_pow(10, 2) + user.playTimeMin[cp];
    EUDTraceLog(67)
    info = EUDVariable()
    info << (user.level[cp] * pow(10, 6) + user.playTimeHour[cp] * pow(10, 2) + user.playTimeMin[cp])
    # (Line 68) data.userSlot[cp * 5 + user.currentSlot[cp] - 1] = info;
    EUDTraceLog(68)
    _ARRW(data.userSlot, cp * 5 + user.currentSlot[cp] - 1) << (info)
    # (Line 69) data.level[cp] = user.level[cp];
    EUDTraceLog(69)
    _ARRW(data.level, cp) << (user.level[cp])
    # (Line 70) data.exp[cp] = user.exp[cp];
    EUDTraceLog(70)
    _ARRW(data.exp, cp) << (user.exp[cp])
    # (Line 71) data.gold[cp] = user.gold[cp];
    EUDTraceLog(71)
    _ARRW(data.gold, cp) << (user.gold[cp])
    # (Line 72) }
    # (Line 74) function SaveUserInven() {

@EUDTracedFunc
def SaveUserInven():
    # (Line 75) const cp = getcurpl();
    EUDTraceLog(75)
    cp = f_getcurpl()
    # (Line 76) const t = 24 * cp;
    EUDTraceLog(76)
    t = 24 * cp
    # (Line 77) for(var i = 0; i < 24; i++) {
    EUDTraceLog(77)
    i = EUDVariable()
    i << (0)
    _t1 = EUDWhile()
    EUDTraceLog(77)
    if _t1(i >= 24, neg=True):
        def _t2():
            EUDTraceLog(77)
            i.__iadd__(1)
        # (Line 78) const c = inven.Inven.cast(inven.inven[t + i]);
        EUDTraceLog(78)
        c = inven.Inven.cast(inven.inven[t + i])
        # (Line 79) if(c.type != 0) {
        _t3 = EUDIf()
        EUDTraceLog(79)
        if _t3(c.type == 0, neg=True):
            # (Line 80) var info = c.type * py_pow(10, 6) + c.index * py_pow(10, 3) + c.amount;
            EUDTraceLog(80)
            info = EUDVariable()
            info << (c.type * pow(10, 6) + c.index * pow(10, 3) + c.amount)
            # (Line 81) data.userInven[t + i] = info;
            EUDTraceLog(81)
            _ARRW(data.userInven, t + i) << (info)
            # (Line 82) }
            # (Line 83) }
        EUDEndIf()
        # (Line 84) }
        EUDSetContinuePoint()
        _t2()
    EUDEndWhile()
    # (Line 86) function Save0Slot() {

@EUDTracedFunc
def Save0Slot():
    # (Line 87) const cp = getcurpl();
    EUDTraceLog(87)
    cp = f_getcurpl()
    # (Line 88) SaveUserSlot();
    EUDTraceLog(88)
    SaveUserSlot()
    # (Line 91) var tempLv = data.level[cp];
    EUDTraceLog(91)
    tempLv = EUDVariable()
    tempLv << (data.level[cp])
    # (Line 92) data.level[cp] = 0;
    EUDTraceLog(92)
    _ARRW(data.level, cp) << (0)
    # (Line 93) var tempExp = data.exp[cp];
    EUDTraceLog(93)
    tempExp = EUDVariable()
    tempExp << (data.exp[cp])
    # (Line 94) data.exp[cp] = 0;
    EUDTraceLog(94)
    _ARRW(data.exp, cp) << (0)
    # (Line 96) for(var i = 0; i < 20; i++) data.userQuest[i] = 0;
    EUDTraceLog(96)
    i = EUDVariable()
    i << (0)
    _t1 = EUDWhile()
    EUDTraceLog(96)
    if _t1(i >= 20, neg=True):
        def _t2():
            EUDTraceLog(96)
            i.__iadd__(1)
        EUDTraceLog(96)
        _ARRW(data.userQuest, i) << (0)
        # (Line 97) for(var i = 0; i < 24; i++) data.userInven[i] = 0;
        EUDSetContinuePoint()
        _t2()
    EUDEndWhile()
    EUDTraceLog(97)
    i = EUDVariable()
    i << (0)
    _t3 = EUDWhile()
    EUDTraceLog(97)
    if _t3(i >= 24, neg=True):
        def _t4():
            EUDTraceLog(97)
            i.__iadd__(1)
        EUDTraceLog(97)
        _ARRW(data.userInven, i) << (0)
        # (Line 98) for(var i = 0; i < 2; i++) data.userSkillSlot[i] = 0;
        EUDSetContinuePoint()
        _t4()
    EUDEndWhile()
    EUDTraceLog(98)
    i = EUDVariable()
    i << (0)
    _t5 = EUDWhile()
    EUDTraceLog(98)
    if _t5(i >= 2, neg=True):
        def _t6():
            EUDTraceLog(98)
            i.__iadd__(1)
        EUDTraceLog(98)
        _ARRW(data.userSkillSlot, i) << (0)
        # (Line 99) for(var i = 0; i < 30; i++) data.userSkill[i] = 0;
        EUDSetContinuePoint()
        _t6()
    EUDEndWhile()
    EUDTraceLog(99)
    i = EUDVariable()
    i << (0)
    _t7 = EUDWhile()
    EUDTraceLog(99)
    if _t7(i >= 30, neg=True):
        def _t8():
            EUDTraceLog(99)
            i.__iadd__(1)
        EUDTraceLog(99)
        _ARRW(data.userSkill, i) << (0)
        # (Line 101) sca.SaveData(0);
        EUDSetContinuePoint()
        _t8()
    EUDEndWhile()
    EUDTraceLog(101)
    sca.SaveData(0)
    # (Line 104) data.level[cp] = tempLv;
    EUDTraceLog(104)
    _ARRW(data.level, cp) << (tempLv)
    # (Line 105) data.exp[cp] = tempExp;
    EUDTraceLog(105)
    _ARRW(data.exp, cp) << (tempExp)
    # (Line 106) }