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

# (Line 1) const character = PVariable();
character = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 2) const inMap = PVariable(); // ??????
inMap = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 3) const inConv = PVariable(); // ?????? ???
inConv = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 4) const isAlive = PVariable(); // ??????
isAlive = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 5) const posX = PVariable();
posX = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 6) const posY = PVariable();
posY = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 7) const currentSlot = PVariable();
currentSlot = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 9) const deathCave = PVariable();
deathCave = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 10) const onPotal = PVariable();
onPotal = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 12) const openedInven = PVariable();
openedInven = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 13) const _mouseX = PVariable();
_mouseX = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 14) const _mouseY = PVariable();
_mouseY = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 16) const level = PVariable();
level = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 17) const exp = PVariable();
exp = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 18) const gold = PVariable();
gold = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 19) const job = PVariable();
job = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 21) const playTimeHour = PVariable();
playTimeHour = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 22) const playTimeMin = PVariable();
playTimeMin = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 23) const playTimeSec = PVariable();
playTimeSec = _CGFW(lambda: [PVariable()], 1)[0]
