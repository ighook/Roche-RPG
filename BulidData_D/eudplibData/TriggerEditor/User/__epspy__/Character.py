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

# (Line 1) import System as sys;
import System as sys
# (Line 2) import User.Info as user;
from User import Info as user
# (Line 3) import User.Stats as stats;
from User import Stats as stats
# (Line 4) import Item.Manager as item;
from Item import Manager as item
# (Line 5) import Equip as equip;
import Equip as equip
# (Line 6) import StatusBar as status;
import StatusBar as status
# (Line 7) import Variable as v;
import Variable as v
# (Line 9) function NewCharacter() {
@EUDTracedFunc
def NewCharacter():
    # (Line 10) const cp = getcurpl();
    EUDTraceLog(10)
    cp = f_getcurpl()
    # (Line 11) setloc("temp", 322, 280);
    EUDTraceLog(11)
    f_setloc("temp", 322, 280)
    # (Line 12) bwrite(0x65FD00 + 18424 + v.unitNum[cp], 71); // ????????? ??????
    EUDTraceLog(12)
    f_bwrite(0x65FD00 + 18424 + v.unitNum[cp], 71)
    # (Line 13) bwrite(0x65FD00 + 14776 + cp, 130); // ?????? NONE
    EUDTraceLog(13)
    f_bwrite(0x65FD00 + 14776 + cp, 130)
    # (Line 14) if(sys.single == false) CenterView("temp");
    _t1 = EUDIf()
    EUDTraceLog(14)
    if _t1(sys.single == False):
        # (Line 15) user.character[cp] = sys.SetNextUnitEPD();
        EUDTraceLog(14)
        DoActions(CenterView("temp"))
    EUDEndIf()
    EUDTraceLog(15)
    _ARRW(user.character, cp) << (sys.SetNextUnitEPD())
    # (Line 16) CreateUnit(1, v.unitNum[cp], "temp", cp);
    # (Line 18) user.inMap[cp] = 1;
    EUDTraceLog(16)
    DoActions(CreateUnit(1, v.unitNum[cp], "temp", cp))
    EUDTraceLog(18)
    _ARRW(user.inMap, cp) << (1)
    # (Line 19) user.isAlive[cp] = 1;
    EUDTraceLog(19)
    _ARRW(user.isAlive, cp) << (1)
    # (Line 20) user.level[cp] = 1;
    EUDTraceLog(20)
    _ARRW(user.level, cp) << (1)
    # (Line 21) user.maxHP[cp] = v.defaultHP;
    EUDTraceLog(21)
    _ARRW(user.maxHP, cp) << (v.defaultHP)
    # (Line 22) user.maxMP[cp] = v.defaultMP;
    EUDTraceLog(22)
    _ARRW(user.maxMP, cp) << (v.defaultMP)
    # (Line 23) user.mp[cp] = v.defaultMP;
    EUDTraceLog(23)
    _ARRW(user.mp, cp) << (v.defaultMP)
    # (Line 24) user.physDmg[cp] = v.defaultDmg;
    EUDTraceLog(24)
    _ARRW(user.physDmg, cp) << (v.defaultDmg)
    # (Line 26) stats.SetHP();
    EUDTraceLog(26)
    stats.SetHP()
    # (Line 27) sys.Heal();
    EUDTraceLog(27)
    sys.Heal()
    # (Line 29) stats.RefreshExp();
    EUDTraceLog(29)
    stats.RefreshExp()
    # (Line 30) SetMemoryXEPD(user.character[cp] + 0x08F / 4, SetTo, user.level[cp] << 24, 0xFF000000);
    # (Line 32) item.AddItem(10000, 2, 1, 1, false);
    EUDTraceLog(30)
    DoActions(SetMemoryXEPD(user.character[cp] + 0x08F // 4, SetTo, _LSH(user.level[cp],24), 0xFF000000))
    EUDTraceLog(32)
    item.AddItem(10000, 2, 1, 1, False)
    # (Line 33) item.AddItem(10000, 3, 1, 1, false);
    EUDTraceLog(33)
    item.AddItem(10000, 3, 1, 1, False)
    # (Line 34) item.AddItem(10000, 1, 1, 1, false);
    EUDTraceLog(34)
    item.AddItem(10000, 1, 1, 1, False)
    # (Line 35) item.AddItem(10000, 1, 2, 2, false);
    EUDTraceLog(35)
    item.AddItem(10000, 1, 2, 2, False)
    # (Line 36) item.AddItem(10000, 1, 16, 3, false);
    EUDTraceLog(36)
    item.AddItem(10000, 1, 16, 3, False)
    # (Line 37) item.AddItem(10000, 1, 17, 4, false);
    EUDTraceLog(37)
    item.AddItem(10000, 1, 17, 4, False)
    # (Line 38) status.stats[cp] = status.USER_STATUS;
    EUDTraceLog(38)
    _ARRW(status.stats, cp) << (status.USER_STATUS)
    # (Line 39) user.posX[cp], user.posY[cp] = dwbreak(dwread_epd(user.character[cp] + 0x28 / 4))[[0,1]];
    EUDTraceLog(39)
    _SV([_ARRW(user.posX, cp), _ARRW(user.posY, cp)], [_SRET(f_dwbreak(f_dwread_epd(user.character[cp] + 0x28 // 4)), [0, 1])])
    # (Line 40) equip.EquipWeapon(1);
    EUDTraceLog(40)
    equip.EquipWeapon(1)
    # (Line 41) }
    # (Line 43) function LoadCharacter() {

@EUDTracedFunc
def LoadCharacter():
    # (Line 44) const cp = getcurpl();
    EUDTraceLog(44)
    cp = f_getcurpl()
    # (Line 45) }
