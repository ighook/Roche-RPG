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
# (Line 3) import NPC.NPC as npc;
from NPC import NPC as npc
# (Line 4) import User.Info as user;
from User import Info as user
# (Line 5) import Screen as screen;
import Screen as screen
# (Line 7) const color = PVariable();
color = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 8) const mousePosition = PVariable();
mousePosition = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 9) var text = Db("");
text = EUDCreateVariables(1)
_IGVA([text], lambda: [Db("")])
# (Line 11) function OpenConv();
# (Line 12) function CloseConv();
# (Line 14) function Guard() {
@EUDTracedFunc
def Guard():
    # (Line 15) const cp = getcurpl();
    EUDTraceLog(15)
    cp = f_getcurpl()
    # (Line 16) if(v.key[cp] == 1) {
    _t1 = EUDIf()
    EUDTraceLog(16)
    if _t1(v.key[cp] == 1):
        # (Line 17) if(user.inMap[cp] == 1) {
        _t2 = EUDIf()
        EUDTraceLog(17)
        if _t2(user.inMap[cp] == 1):
            # (Line 18) if(sys.EPDBring(v.locNum[cp], npc.Guard[0]) || sys.EPDBring(v.locNum[cp], npc.Guard[1])) {
            _t3 = EUDIf()
            EUDTraceLog(18)
            if _t3(EUDSCOr()(sys.EPDBring(v.locNum[cp], npc.Guard[0]))(sys.EPDBring(v.locNum[cp], npc.Guard[1]))()):
                # (Line 19) if(user.inConv[cp] == 0) OpenConv();
                _t4 = EUDIf()
                EUDTraceLog(19)
                if _t4(user.inConv[cp] == 0):
                    EUDTraceLog(19)
                    OpenConv()
                    # (Line 20) else CloseConv();
                if EUDElse()():
                    EUDTraceLog(20)
                    CloseConv()
                    # (Line 21) }
                EUDEndIf()
                # (Line 22) }
            EUDEndIf()
            # (Line 23) }
        EUDEndIf()
        # (Line 25) if(user.inConv[cp] == 1) {
    EUDEndIf()
    _t5 = EUDIf()
    EUDTraceLog(25)
    if _t5(user.inConv[cp] == 1):
        # (Line 26) sys.Stop();
        EUDTraceLog(26)
        sys.Stop()
        # (Line 27) var x = 0;
        EUDTraceLog(27)
        x = EUDVariable()
        x << (0)
        # (Line 28) if(v.screenMode[cp] == 1) x = 106;
        _t6 = EUDIf()
        EUDTraceLog(28)
        if _t6(v.screenMode[cp] == 1):
            EUDTraceLog(28)
            x << (106)
            # (Line 29) if(v.textRefresh[cp] == 1) {
        EUDEndIf()
        _t7 = EUDIf()
        EUDTraceLog(29)
        if _t7(v.textRefresh[cp] == 1):
            # (Line 30) v.textRefresh[cp] = 0;
            EUDTraceLog(30)
            _ARRW(v.textRefresh, cp) << (0)
            # (Line 31) v.display.insert(0);
            EUDTraceLog(31)
            v.display.insert(0)
            # (Line 32) v.display.append("\x13──────────────────\n");
            EUDTraceLog(32)
            v.display.append("\x13──────────────────\n")
            # (Line 33) v.display.append("\x13\x1c[ 경비병 ]\n");
            EUDTraceLog(33)
            v.display.append("\x13\x1c[ 경비병 ]\n")
            # (Line 34) v.display.append(ptr2s(text));
            EUDTraceLog(34)
            v.display.append(ptr2s(text))
            # (Line 35) v.display.append("\x13──────────────────\n");
            EUDTraceLog(35)
            v.display.append("\x13──────────────────\n")
            # (Line 36) v.display.append("\x13", ptr2s(color[cp]), "( C ) \x17대화 끝내기");
            EUDTraceLog(36)
            v.display.append("\x13", ptr2s(color[cp]), "( C ) \x17대화 끝내기")
            # (Line 37) }
            # (Line 38) v.display.DisplayAt(0);
        EUDEndIf()
        EUDTraceLog(38)
        v.display.DisplayAt(0)
        # (Line 39) if(IsUserCP()) {
        _t8 = EUDIf()
        EUDTraceLog(39)
        if _t8(IsUserCP()):
            # (Line 40) if(v._mouseY[cp] >= 176 && v._mouseY[cp] <= 190) {
            _t9 = EUDIf()
            EUDTraceLog(40)
            if _t9(EUDSCAnd()(v._mouseY[cp] >= 176)(v._mouseY[cp] <= 190)()):
                # (Line 41) if(v._mouseX[cp] >= 277 + x && v._mouseX[cp] <= 363 + x) {
                _t10 = EUDIf()
                EUDTraceLog(41)
                if _t10(EUDSCAnd()(v._mouseX[cp] >= 277 + x)(v._mouseX[cp] <= 363 + x)()):
                    # (Line 42) if(mousePosition[cp] != 1) {
                    _t11 = EUDIf()
                    EUDTraceLog(42)
                    if _t11(mousePosition[cp] == 1, neg=True):
                        # (Line 43) mousePosition[cp] = 1;
                        EUDTraceLog(43)
                        _ARRW(mousePosition, cp) << (1)
                        # (Line 44) color[cp] = Db("\x04");
                        EUDTraceLog(44)
                        _ARRW(color, cp) << (Db("\x04"))
                        # (Line 45) v.textRefresh[cp] = 1;
                        EUDTraceLog(45)
                        _ARRW(v.textRefresh, cp) << (1)
                        # (Line 46) }
                        # (Line 47) }
                    EUDEndIf()
                    # (Line 48) }
                EUDEndIf()
                # (Line 49) else if(mousePosition[cp] == 1) {
            _t12 = EUDElseIf()
            EUDTraceLog(49)
            if _t12(mousePosition[cp] == 1):
                # (Line 50) mousePosition[cp] = 0;
                EUDTraceLog(50)
                _ARRW(mousePosition, cp) << (0)
                # (Line 51) color[cp] = Db("\x05");
                EUDTraceLog(51)
                _ARRW(color, cp) << (Db("\x05"))
                # (Line 52) v.textRefresh[cp] = 1;
                EUDTraceLog(52)
                _ARRW(v.textRefresh, cp) << (1)
                # (Line 53) }
                # (Line 54) }
            EUDEndIf()
            # (Line 55) if(v.mouse[cp] == v.KeyC) {
        EUDEndIf()
        _t13 = EUDIf()
        EUDTraceLog(55)
        if _t13(v.mouse[cp] == v.KeyC):
            # (Line 56) if(v.mouseY[cp] >= 176 && v.mouseY[cp] <= 190) {
            _t14 = EUDIf()
            EUDTraceLog(56)
            if _t14(EUDSCAnd()(v.mouseY[cp] >= 176)(v.mouseY[cp] <= 190)()):
                # (Line 57) if(v.mouseX[cp] >= 277 + x && v.mouseX[cp] <= 363 + x) {
                _t15 = EUDIf()
                EUDTraceLog(57)
                if _t15(EUDSCAnd()(v.mouseX[cp] >= 277 + x)(v.mouseX[cp] <= 363 + x)()):
                    # (Line 58) PlayWAV("staredit\\wav\\click2.ogg");
                    # (Line 59) CloseConv();
                    EUDTraceLog(58)
                    DoActions(PlayWAV("staredit\\wav\\click2.ogg"))
                    EUDTraceLog(59)
                    CloseConv()
                    # (Line 60) }
                    # (Line 61) }
                EUDEndIf()
                # (Line 62) }
            EUDEndIf()
            # (Line 63) }
        EUDEndIf()
        # (Line 64) }
    EUDEndIf()
    # (Line 66) function OpenConv() {

@EUDTracedFunc
def OpenConv():
    # (Line 67) const cp = getcurpl();
    EUDTraceLog(67)
    cp = f_getcurpl()
    # (Line 68) user.inConv[cp] = 1;
    EUDTraceLog(68)
    _ARRW(user.inConv, cp) << (1)
    # (Line 69) v.textRefresh[cp] = 1;
    EUDTraceLog(69)
    _ARRW(v.textRefresh, cp) << (1)
    # (Line 70) color[cp] = Db("\x05");
    EUDTraceLog(70)
    _ARRW(color, cp) << (Db("\x05"))
    # (Line 71) mousePosition[cp] = 0;
    EUDTraceLog(71)
    _ARRW(mousePosition, cp) << (0)
    # (Line 72) screen.light[cp] = 25;
    EUDTraceLog(72)
    _ARRW(screen.light, cp) << (25)
    # (Line 73) if(IsUserCP()) {
    _t1 = EUDIf()
    EUDTraceLog(73)
    if _t1(IsUserCP()):
        # (Line 74) var ran = dwrand() % 5;
        EUDTraceLog(74)
        ran = EUDVariable()
        ran << (f_dwrand() % 5)
        # (Line 75) if(ran == 0) text = Db("\x13\x04무슨 일입니까?\n");
        _t2 = EUDIf()
        EUDTraceLog(75)
        if _t2(ran == 0):
            EUDTraceLog(75)
            text << (Db("\x13\x04무슨 일입니까?\n"))
            # (Line 76) else if(ran == 1) text = Db("\x13\x04밖은 위험하니 조심하십시오\n");
        _t3 = EUDElseIf()
        EUDTraceLog(76)
        if _t3(ran == 1):
            EUDTraceLog(76)
            text << (Db("\x13\x04밖은 위험하니 조심하십시오\n"))
            # (Line 77) else if(ran == 2) text = Db("\x13\x04자신을 보호하기 위해선 좋은 장비는 필수입니다\n");
        _t4 = EUDElseIf()
        EUDTraceLog(77)
        if _t4(ran == 2):
            EUDTraceLog(77)
            text << (Db("\x13\x04자신을 보호하기 위해선 좋은 장비는 필수입니다\n"))
            # (Line 78) else if(ran == 3) text = Db("\x13\x04주민들을 보호하기 위하여 열심히 경계중입니다\n");
        _t5 = EUDElseIf()
        EUDTraceLog(78)
        if _t5(ran == 3):
            EUDTraceLog(78)
            text << (Db("\x13\x04주민들을 보호하기 위하여 열심히 경계중입니다\n"))
            # (Line 79) else if(ran == 4) text = Db("\x13\x04이 마을에 별일이 없었으면 좋겠군요\n");
        _t6 = EUDElseIf()
        EUDTraceLog(79)
        if _t6(ran == 4):
            EUDTraceLog(79)
            text << (Db("\x13\x04이 마을에 별일이 없었으면 좋겠군요\n"))
            # (Line 80) }
        EUDEndIf()
        # (Line 81) }
    EUDEndIf()
    # (Line 83) function CloseConv() {

@EUDTracedFunc
def CloseConv():
    # (Line 84) const cp = getcurpl();
    EUDTraceLog(84)
    cp = f_getcurpl()
    # (Line 85) user.inConv[cp] = 0;
    EUDTraceLog(85)
    _ARRW(user.inConv, cp) << (0)
    # (Line 86) sys.TextClear();
    EUDTraceLog(86)
    sys.TextClear()
    # (Line 87) screen.light[cp] = 31;
    EUDTraceLog(87)
    _ARRW(screen.light, cp) << (31)
    # (Line 88) }
