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
# (Line 2) import User.Info as user;
from User import Info as user
# (Line 5) var X0 = 0;
X0 = EUDCreateVariables(1)
_IGVA([X0], lambda: [0])
# (Line 6) const X1 = EUDArray(11);
X1 = _CGFW(lambda: [EUDArray(11)], 1)[0]
# (Line 7) const X2 = EUDArray(10);
X2 = _CGFW(lambda: [EUDArray(10)], 1)[0]
# (Line 8) const X3 = EUDArray(10);
X3 = _CGFW(lambda: [EUDArray(10)], 1)[0]
# (Line 9) const X4 = PVariable();
X4 = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 10) const X5 = PVariable();
X5 = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 12) const Trap1 = PVariable(); //변조확인
Trap1 = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 16) function Init(){
@EUDTracedFunc
def Init():
    # (Line 17) for(var i = 1 ; i < 11 ; i++){
    EUDTraceLog(17)
    i = EUDVariable()
    i << (1)
    _t1 = EUDWhile()
    EUDTraceLog(17)
    if _t1(i >= 11, neg=True):
        def _t2():
            EUDTraceLog(17)
            i.__iadd__(1)
        # (Line 18) const RandX = dwrand() % (32768) + 16348;
        EUDTraceLog(18)
        RandX = f_dwrand() % (32768) + 16348
        # (Line 19) X1[i] = RandX;
        EUDTraceLog(19)
        _ARRW(X1, i) << (RandX)
        # (Line 20) }
        # (Line 21) X1[0] = 0;
        EUDSetContinuePoint()
        _t2()
    EUDEndWhile()
    EUDTraceLog(21)
    _ARRW(X1, 0) << (0)
    # (Line 22) }
    # (Line 24) function BeforeExec(){ //클래식 트리거 실행전 처리

@EUDTracedFunc
def BeforeExec():
    # (Line 25) const XX = X1[X0];
    EUDTraceLog(25)
    XX = X1[X0]
    # (Line 26) foreach(cp : EUDLoopPlayer()){
    for cp in EUDLoopPlayer():
        # (Line 28) if (X2[cp] != XX + maskread_epd(EPD(0x57F0F0) + cp, 0xFFFFFFFF)) {
        _t1 = EUDIf()
        EUDTraceLog(28)
        if _t1(X2[cp] == XX + f_maskread_epd(EPD(0x57F0F0) + cp, 0xFFFFFFFF), neg=True):
            # (Line 29) Trap1[cp] = 1;
            EUDTraceLog(29)
            _ARRW(Trap1, cp) << (1)
            # (Line 30) }
            # (Line 31) if (X3[cp] != XX + maskread_epd(EPD(0x57F120) + cp, 0xFFFFFFFF)) {
        EUDEndIf()
        _t2 = EUDIf()
        EUDTraceLog(31)
        if _t2(X3[cp] == XX + f_maskread_epd(EPD(0x57F120) + cp, 0xFFFFFFFF), neg=True):
            # (Line 32) Trap1[cp] = 2;
            EUDTraceLog(32)
            _ARRW(Trap1, cp) << (2)
            # (Line 33) }
            # (Line 34) if (X4[cp] != XX + user.level[cp]) {
        EUDEndIf()
        _t3 = EUDIf()
        EUDTraceLog(34)
        if _t3(X4[cp] == XX + user.level[cp], neg=True):
            # (Line 35) Trap1[cp] = 4;
            EUDTraceLog(35)
            _ARRW(Trap1, cp) << (4)
            # (Line 36) }
            # (Line 37) if (X5[cp] != XX + user.exp[cp]) {
        EUDEndIf()
        _t4 = EUDIf()
        EUDTraceLog(37)
        if _t4(X5[cp] == XX + user.exp[cp], neg=True):
            # (Line 38) Trap1[cp] = 8;
            EUDTraceLog(38)
            _ARRW(Trap1, cp) << (8)
            # (Line 39) }
            # (Line 41) }
        EUDEndIf()
        # (Line 42) }

    # (Line 44) function AfterExec() {

@EUDTracedFunc
def AfterExec():
    # (Line 45) X0 += 1;
    EUDTraceLog(45)
    X0.__iadd__(1)
    # (Line 46) if (X0 > 11){
    _t1 = EUDIf()
    EUDTraceLog(46)
    if _t1(X0 <= 11, neg=True):
        # (Line 47) X0 = 1;
        EUDTraceLog(47)
        X0 << (1)
        # (Line 48) }
        # (Line 49) const XX = X1[X0];
    EUDEndIf()
    EUDTraceLog(49)
    XX = X1[X0]
    # (Line 50) foreach(cp : EUDLoopPlayer()){
    for cp in EUDLoopPlayer():
        # (Line 53) X4[cp] = XX + user.level[cp];
        EUDTraceLog(53)
        _ARRW(X4, cp) << (XX + user.level[cp])
        # (Line 54) X5[cp] = XX + user.exp[cp];
        EUDTraceLog(54)
        _ARRW(X5, cp) << (XX + user.exp[cp])
        # (Line 55) }
        # (Line 56) }