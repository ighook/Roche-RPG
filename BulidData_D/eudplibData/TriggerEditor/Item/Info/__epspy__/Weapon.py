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

# (Line 1) object Weapon { var type; var index; var name; var name2; var lv; var phyDmg; var magicDmg; };
class Weapon(EUDStruct):
    # (Line 3) const slot = 100;
    _fields_ = [
        'type',
        'index',
        'name',
        'name2',
        'lv',
        'phyDmg',
        'magicDmg',
    ]

slot = _CGFW(lambda: [100], 1)[0]
# (Line 4) const weaponList = EUDArray(slot);
weaponList = _CGFW(lambda: [EUDArray(slot)], 1)[0]
# (Line 6) function SetItemInfo() {
@EUDTracedFunc
def SetItemInfo():
    # (Line 7) for(var i = 0; i < slot; i++) weaponList[i] = Weapon.alloc();
    EUDTraceLog(7)
    i = EUDVariable()
    i << (0)
    _t1 = EUDWhile()
    EUDTraceLog(7)
    if _t1(i >= slot, neg=True):
        def _t2():
            EUDTraceLog(7)
            i.__iadd__(1)
        EUDTraceLog(7)
        _ARRW(weaponList, i) << (Weapon.alloc())
        # (Line 8) const sword01 = Weapon.cast(weaponList[0]);
        EUDSetContinuePoint()
        _t2()
    EUDEndWhile()
    EUDTraceLog(8)
    sword01 = Weapon.cast(weaponList[0])
    # (Line 9) sword01.type = 2;
    EUDTraceLog(9)
    _ATTW(sword01, 'type') << (2)
    # (Line 10) sword01.index = 1;
    EUDTraceLog(10)
    _ATTW(sword01, 'index') << (1)
    # (Line 11) sword01.name = Db("\x04철 검");
    EUDTraceLog(11)
    _ATTW(sword01, 'name') << (Db("\x04철 검"))
    # (Line 12) sword01.name2 = EPD(Db(u2b("\x04철 검")));
    EUDTraceLog(12)
    _ATTW(sword01, 'name2') << (EPD(Db(u2b("\x04철 검"))))
    # (Line 13) sword01.lv = 1;
    EUDTraceLog(13)
    _ATTW(sword01, 'lv') << (1)
    # (Line 14) sword01.phyDmg = 9;
    EUDTraceLog(14)
    _ATTW(sword01, 'phyDmg') << (9)
    # (Line 15) const sword02 = Weapon.cast(weaponList[1]);
    EUDTraceLog(15)
    sword02 = Weapon.cast(weaponList[1])
    # (Line 16) sword02.type = 2;
    EUDTraceLog(16)
    _ATTW(sword02, 'type') << (2)
    # (Line 17) sword02.index = 2;
    EUDTraceLog(17)
    _ATTW(sword02, 'index') << (2)
    # (Line 18) sword02.name = Db("\x04강철 검");
    EUDTraceLog(18)
    _ATTW(sword02, 'name') << (Db("\x04강철 검"))
    # (Line 19) sword02.name2 = EPD(Db(u2b("\x04강철 검")));
    EUDTraceLog(19)
    _ATTW(sword02, 'name2') << (EPD(Db(u2b("\x04강철 검"))))
    # (Line 20) sword02.lv = 1;
    EUDTraceLog(20)
    _ATTW(sword02, 'lv') << (1)
    # (Line 21) sword02.phyDmg = 9;
    EUDTraceLog(21)
    _ATTW(sword02, 'phyDmg') << (9)
    # (Line 22) const sword03 = Weapon.cast(weaponList[2]);
    EUDTraceLog(22)
    sword03 = Weapon.cast(weaponList[2])
    # (Line 23) sword03.type = 2;
    EUDTraceLog(23)
    _ATTW(sword03, 'type') << (2)
    # (Line 24) sword03.index = 3;
    EUDTraceLog(24)
    _ATTW(sword03, 'index') << (3)
    # (Line 25) sword03.name = Db("\x04켈람");
    EUDTraceLog(25)
    _ATTW(sword03, 'name') << (Db("\x04켈람"))
    # (Line 26) sword03.name2 = EPD(Db(u2b("\x04켈람")));
    EUDTraceLog(26)
    _ATTW(sword03, 'name2') << (EPD(Db(u2b("\x04켈람"))))
    # (Line 27) sword03.lv = 7;
    EUDTraceLog(27)
    _ATTW(sword03, 'lv') << (7)
    # (Line 28) sword03.phyDmg = 9;
    EUDTraceLog(28)
    _ATTW(sword03, 'phyDmg') << (9)
    # (Line 29) const sword04 = Weapon.cast(weaponList[3]);
    EUDTraceLog(29)
    sword04 = Weapon.cast(weaponList[3])
    # (Line 30) sword04.type = 2;
    EUDTraceLog(30)
    _ATTW(sword04, 'type') << (2)
    # (Line 31) sword04.index = 4;
    EUDTraceLog(31)
    _ATTW(sword04, 'index') << (4)
    # (Line 32) sword04.name = Db("\x04[일반] 스파타");
    EUDTraceLog(32)
    _ATTW(sword04, 'name') << (Db("\x04[일반] 스파타"))
    # (Line 33) sword04.name2 = EPD(Db(u2b("\x04[일반] 스파타")));
    EUDTraceLog(33)
    _ATTW(sword04, 'name2') << (EPD(Db(u2b("\x04[일반] 스파타"))))
    # (Line 34) sword04.lv = 1;
    EUDTraceLog(34)
    _ATTW(sword04, 'lv') << (1)
    # (Line 35) sword04.phyDmg = 9;
    EUDTraceLog(35)
    _ATTW(sword04, 'phyDmg') << (9)
    # (Line 36) const sword05 = Weapon.cast(weaponList[4]);
    EUDTraceLog(36)
    sword05 = Weapon.cast(weaponList[4])
    # (Line 37) sword05.type = 2;
    EUDTraceLog(37)
    _ATTW(sword05, 'type') << (2)
    # (Line 38) sword05.index = 5;
    EUDTraceLog(38)
    _ATTW(sword05, 'index') << (5)
    # (Line 39) sword05.name = Db("\x04[일반] 반월검");
    EUDTraceLog(39)
    _ATTW(sword05, 'name') << (Db("\x04[일반] 반월검"))
    # (Line 40) sword05.name2 = EPD(Db(u2b("\x04[일반] 반월검")));
    EUDTraceLog(40)
    _ATTW(sword05, 'name2') << (EPD(Db(u2b("\x04[일반] 반월검"))))
    # (Line 41) sword05.lv = 1;
    EUDTraceLog(41)
    _ATTW(sword05, 'lv') << (1)
    # (Line 42) sword05.phyDmg = 9;
    EUDTraceLog(42)
    _ATTW(sword05, 'phyDmg') << (9)
    # (Line 43) const sword06 = Weapon.cast(weaponList[5]);
    EUDTraceLog(43)
    sword06 = Weapon.cast(weaponList[5])
    # (Line 44) sword06.type = 2;
    EUDTraceLog(44)
    _ATTW(sword06, 'type') << (2)
    # (Line 45) sword06.index = 6;
    EUDTraceLog(45)
    _ATTW(sword06, 'index') << (6)
    # (Line 46) sword06.name = Db("\x04[일반] 단혼검");
    EUDTraceLog(46)
    _ATTW(sword06, 'name') << (Db("\x04[일반] 단혼검"))
    # (Line 47) sword06.lv = 1;
    EUDTraceLog(47)
    _ATTW(sword06, 'lv') << (1)
    # (Line 48) sword06.phyDmg = 9;
    EUDTraceLog(48)
    _ATTW(sword06, 'phyDmg') << (9)
    # (Line 49) const sword07 = Weapon.cast(weaponList[6]);
    EUDTraceLog(49)
    sword07 = Weapon.cast(weaponList[6])
    # (Line 50) sword07.type = 2;
    EUDTraceLog(50)
    _ATTW(sword07, 'type') << (2)
    # (Line 51) sword07.index = 7;
    EUDTraceLog(51)
    _ATTW(sword07, 'index') << (7)
    # (Line 52) sword07.name = Db("\x04[일반] 켈람");
    EUDTraceLog(52)
    _ATTW(sword07, 'name') << (Db("\x04[일반] 켈람"))
    # (Line 53) sword07.lv = 1;
    EUDTraceLog(53)
    _ATTW(sword07, 'lv') << (1)
    # (Line 54) sword07.phyDmg = 9;
    EUDTraceLog(54)
    _ATTW(sword07, 'phyDmg') << (9)
    # (Line 55) const sword08 = Weapon.cast(weaponList[7]);
    EUDTraceLog(55)
    sword08 = Weapon.cast(weaponList[7])
    # (Line 56) sword08.type = 2;
    EUDTraceLog(56)
    _ATTW(sword08, 'type') << (2)
    # (Line 57) sword08.index = 8;
    EUDTraceLog(57)
    _ATTW(sword08, 'index') << (8)
    # (Line 58) sword08.name = Db("\x04[일반] 써큘러스");
    EUDTraceLog(58)
    _ATTW(sword08, 'name') << (Db("\x04[일반] 써큘러스"))
    # (Line 59) sword08.lv = 1;
    EUDTraceLog(59)
    _ATTW(sword08, 'lv') << (1)
    # (Line 60) sword08.phyDmg = 9;
    EUDTraceLog(60)
    _ATTW(sword08, 'phyDmg') << (9)
    # (Line 61) const sword09 = Weapon.cast(weaponList[8]);
    EUDTraceLog(61)
    sword09 = Weapon.cast(weaponList[8])
    # (Line 62) sword09.type = 2;
    EUDTraceLog(62)
    _ATTW(sword09, 'type') << (2)
    # (Line 63) sword09.index = 9;
    EUDTraceLog(63)
    _ATTW(sword09, 'index') << (9)
    # (Line 64) sword09.name = Db("\x04[일반] 샤크람");
    EUDTraceLog(64)
    _ATTW(sword09, 'name') << (Db("\x04[일반] 샤크람"))
    # (Line 65) sword09.lv = 1;
    EUDTraceLog(65)
    _ATTW(sword09, 'lv') << (1)
    # (Line 66) sword09.phyDmg = 9;
    EUDTraceLog(66)
    _ATTW(sword09, 'phyDmg') << (9)
    # (Line 67) const sword10 = Weapon.cast(weaponList[9]);
    EUDTraceLog(67)
    sword10 = Weapon.cast(weaponList[9])
    # (Line 68) sword10.type = 2;
    EUDTraceLog(68)
    _ATTW(sword10, 'type') << (2)
    # (Line 69) sword10.index = 10;
    EUDTraceLog(69)
    _ATTW(sword10, 'index') << (10)
    # (Line 70) sword10.name = Db("\x04[일반] 악령검");
    EUDTraceLog(70)
    _ATTW(sword10, 'name') << (Db("\x04[일반] 악령검"))
    # (Line 71) sword10.lv = 1;
    EUDTraceLog(71)
    _ATTW(sword10, 'lv') << (1)
    # (Line 72) sword10.phyDmg = 9;
    EUDTraceLog(72)
    _ATTW(sword10, 'phyDmg') << (9)
    # (Line 73) }
