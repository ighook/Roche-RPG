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
# (Line 2) import SCA.Save as save;
from SCA import Save as save
# (Line 3) import Screen as screen;
import Screen as screen
# (Line 4) import System as sys;
import System as sys
# (Line 6) function KeyDetect(cp) {
@EUDTracedFunc
def KeyDetect(cp):
    # (Line 7) if(v.key[cp] == 0) return;
    _t1 = EUDIf()
    EUDTraceLog(7)
    if _t1(v.key[cp] == 0):
        EUDTraceLog(7)
        EUDReturn()
        # (Line 8) else if(v.key[cp] == v.KeySave) save.Save(); // F12 ?????? ??????
    _t2 = EUDElseIf()
    EUDTraceLog(8)
    if _t2(v.key[cp] == v.KeySave):
        EUDTraceLog(8)
        save.Save()
        # (Line 9) else if(sys.single == false && v.key[cp] == v.KeyWideCheck) screen.WideCheck(); // ALT ????????? ??????
    _t3 = EUDElseIf()
    EUDTraceLog(9)
    if _t3(EUDSCAnd()(sys.single == False)(v.key[cp] == v.KeyWideCheck)()):
        EUDTraceLog(9)
        screen.WideCheck()
        # (Line 11) if(v.numberKey[cp] == 0) return;
    EUDEndIf()
    _t4 = EUDIf()
    EUDTraceLog(11)
    if _t4(v.numberKey[cp] == 0):
        EUDTraceLog(11)
        EUDReturn()
        # (Line 12) else {
    if EUDElse()():
        # (Line 13) v.s.print("\x05", v.numberKey[cp], "??? ??????");
        EUDTraceLog(13)
        v.s.print("\x05", v.numberKey[cp], "??? ??????")
        # (Line 14) }
        # (Line 15) }
    EUDEndIf()
