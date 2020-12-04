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
# (Line 3) import System as sys;
import System as sys
# (Line 4) import SCA.Data as data;
from SCA import Data as data
# (Line 5) import Opening as opening;
import Opening as opening
# (Line 6) import Potal as potal;
import Potal as potal
# (Line 7) import Screen as screen;
import Screen as screen
# (Line 9) const color = EUDArray(6);
color = _CGFW(lambda: [EUDArray(6)], 1)[0]
# (Line 10) const mousePosition = PVariable();
mousePosition = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 11) const selectedSlot = PVariable();
selectedSlot = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 12) const hour = EUDArray(5 * 8);
hour = _CGFW(lambda: [EUDArray(5 * 8)], 1)[0]
# (Line 14) function Close();
# (Line 16) function New() {
@EUDTracedFunc
def New():
    # (Line 17) const cp = getcurpl();
    EUDTraceLog(17)
    cp = f_getcurpl()
    # (Line 18) if(user.openedSlot[cp] == 1) {
    _t1 = EUDIf()
    EUDTraceLog(18)
    if _t1(user.openedSlot[cp] == 1):
        # (Line 19) if(v.textRefresh[cp] == 1) {
        _t2 = EUDIf()
        EUDTraceLog(19)
        if _t2(v.textRefresh[cp] == 1):
            # (Line 20) v.textRefresh[cp] = 0;
            EUDTraceLog(20)
            _ARRW(v.textRefresh, cp) << (0)
            # (Line 21) v.display.insert(0);
            EUDTraceLog(21)
            v.display.insert(0)
            # (Line 22) v.display.append("\n\x13\x04=============================\n");
            EUDTraceLog(22)
            v.display.append("\n\x13\x04=============================\n")
            # (Line 23) v.display.append("\x13", ptr2s(color[0]), "Lv.", user.slotLevel[5 * cp + 0], "     플레이 시간 : ", hour[5 * cp + 0], " h\n");
            EUDTraceLog(23)
            v.display.append("\x13", ptr2s(color[0]), "Lv.", user.slotLevel[5 * cp + 0], "     플레이 시간 : ", hour[5 * cp + 0], " h\n")
            # (Line 24) v.display.append("\x13", ptr2s(color[1]), "Lv.", user.slotLevel[5 * cp + 1], "     플레이 시간 : ", hour[5 * cp + 1], " h\n");
            EUDTraceLog(24)
            v.display.append("\x13", ptr2s(color[1]), "Lv.", user.slotLevel[5 * cp + 1], "     플레이 시간 : ", hour[5 * cp + 1], " h\n")
            # (Line 25) v.display.append("\x13", ptr2s(color[2]), "Lv.", user.slotLevel[5 * cp + 2], "     플레이 시간 : ", hour[5 * cp + 2], " h\n");
            EUDTraceLog(25)
            v.display.append("\x13", ptr2s(color[2]), "Lv.", user.slotLevel[5 * cp + 2], "     플레이 시간 : ", hour[5 * cp + 2], " h\n")
            # (Line 26) v.display.append("\x13", ptr2s(color[3]), "Lv.", user.slotLevel[5 * cp + 3], "     플레이 시간 : ", hour[5 * cp + 3], " h\n");
            EUDTraceLog(26)
            v.display.append("\x13", ptr2s(color[3]), "Lv.", user.slotLevel[5 * cp + 3], "     플레이 시간 : ", hour[5 * cp + 3], " h\n")
            # (Line 27) v.display.append("\x13", ptr2s(color[4]), "Lv.", user.slotLevel[5 * cp + 4], "     플레이 시간 : ", hour[5 * cp + 4], " h\n");
            EUDTraceLog(27)
            v.display.append("\x13", ptr2s(color[4]), "Lv.", user.slotLevel[5 * cp + 4], "     플레이 시간 : ", hour[5 * cp + 4], " h\n")
            # (Line 28) v.display.append("\x13\x04=============================\n");
            EUDTraceLog(28)
            v.display.append("\x13\x04=============================\n")
            # (Line 29) v.display.append("\x13", ptr2s(color[5]), "새로하기");
            EUDTraceLog(29)
            v.display.append("\x13", ptr2s(color[5]), "새로하기")
            # (Line 30) }
            # (Line 32) v.display.DisplayAt(0);
        EUDEndIf()
        EUDTraceLog(32)
        v.display.DisplayAt(0)
        # (Line 33) sys.Stop();
        EUDTraceLog(33)
        sys.Stop()
        # (Line 35) if(IsUserCP()) {
        _t3 = EUDIf()
        EUDTraceLog(35)
        if _t3(IsUserCP()):
            # (Line 36) if(v._mouseY[cp] < 160 || v._mouseY[cp] > 222) {
            _t4 = EUDIf()
            EUDTraceLog(36)
            if _t4(EUDSCOr()(v._mouseY[cp] >= 160, neg=True)(v._mouseY[cp] <= 222, neg=True)()):
                # (Line 37) mousePosition[cp] = 0;
                EUDTraceLog(37)
                _ARRW(mousePosition, cp) << (0)
                # (Line 38) v.textRefresh[cp] = 1;
                EUDTraceLog(38)
                _ARRW(v.textRefresh, cp) << (1)
                # (Line 39) }
                # (Line 41) if(v._mouseY[cp] >= 144 && v._mouseY[cp] <= 158) {
            EUDEndIf()
            _t5 = EUDIf()
            EUDTraceLog(41)
            if _t5(EUDSCAnd()(v._mouseY[cp] >= 144)(v._mouseY[cp] <= 158)()):
                # (Line 42) if(selectedSlot[cp] != 1) {
                _t6 = EUDIf()
                EUDTraceLog(42)
                if _t6(selectedSlot[cp] == 1, neg=True):
                    # (Line 43) if(strcmp(color[0], Db("\x05")) == 0) {
                    _t7 = EUDIf()
                    EUDTraceLog(43)
                    if _t7(f_strcmp(color[0], Db("\x05")) == 0):
                        # (Line 44) color[0] = Db("\x04");
                        EUDTraceLog(44)
                        _ARRW(color, 0) << (Db("\x04"))
                        # (Line 45) v.textRefresh[cp] = 1;
                        EUDTraceLog(45)
                        _ARRW(v.textRefresh, cp) << (1)
                        # (Line 46) }
                        # (Line 47) }
                    EUDEndIf()
                    # (Line 48) }
                EUDEndIf()
                # (Line 49) else if(selectedSlot[cp] != 1 && strcmp(color[0], Db("\x05")) != 0)  {
            _t8 = EUDElseIf()
            EUDTraceLog(49)
            if _t8(EUDSCAnd()(selectedSlot[cp] == 1, neg=True)(f_strcmp(color[0], Db("\x05")) == 0, neg=True)()):
                # (Line 50) color[0] = Db("\x05");
                EUDTraceLog(50)
                _ARRW(color, 0) << (Db("\x05"))
                # (Line 51) v.textRefresh[cp] = 1;
                EUDTraceLog(51)
                _ARRW(v.textRefresh, cp) << (1)
                # (Line 52) }
                # (Line 54) if(v._mouseY[cp] >= 160 && v._mouseY[cp] <= 174) {
            EUDEndIf()
            _t9 = EUDIf()
            EUDTraceLog(54)
            if _t9(EUDSCAnd()(v._mouseY[cp] >= 160)(v._mouseY[cp] <= 174)()):
                # (Line 55) if(selectedSlot[cp] != 2) {
                _t10 = EUDIf()
                EUDTraceLog(55)
                if _t10(selectedSlot[cp] == 2, neg=True):
                    # (Line 56) if(strcmp(color[1], Db("\x05")) == 0) {
                    _t11 = EUDIf()
                    EUDTraceLog(56)
                    if _t11(f_strcmp(color[1], Db("\x05")) == 0):
                        # (Line 57) color[1] = Db("\x04");
                        EUDTraceLog(57)
                        _ARRW(color, 1) << (Db("\x04"))
                        # (Line 58) v.textRefresh[cp] = 1;
                        EUDTraceLog(58)
                        _ARRW(v.textRefresh, cp) << (1)
                        # (Line 59) }
                        # (Line 60) }
                    EUDEndIf()
                    # (Line 61) }
                EUDEndIf()
                # (Line 62) else if(selectedSlot[cp] != 2 && strcmp(color[1], Db("\x05")) != 0)  {
            _t12 = EUDElseIf()
            EUDTraceLog(62)
            if _t12(EUDSCAnd()(selectedSlot[cp] == 2, neg=True)(f_strcmp(color[1], Db("\x05")) == 0, neg=True)()):
                # (Line 63) color[1] = Db("\x05");
                EUDTraceLog(63)
                _ARRW(color, 1) << (Db("\x05"))
                # (Line 64) v.textRefresh[cp] = 1;
                EUDTraceLog(64)
                _ARRW(v.textRefresh, cp) << (1)
                # (Line 65) }
                # (Line 67) if(v._mouseY[cp] >= 176 && v._mouseY[cp] <= 190) {
            EUDEndIf()
            _t13 = EUDIf()
            EUDTraceLog(67)
            if _t13(EUDSCAnd()(v._mouseY[cp] >= 176)(v._mouseY[cp] <= 190)()):
                # (Line 68) if(selectedSlot[cp] != 3) {
                _t14 = EUDIf()
                EUDTraceLog(68)
                if _t14(selectedSlot[cp] == 3, neg=True):
                    # (Line 69) if(strcmp(color[2], Db("\x05")) == 0) {
                    _t15 = EUDIf()
                    EUDTraceLog(69)
                    if _t15(f_strcmp(color[2], Db("\x05")) == 0):
                        # (Line 70) color[2] = Db("\x04");
                        EUDTraceLog(70)
                        _ARRW(color, 2) << (Db("\x04"))
                        # (Line 71) v.textRefresh[cp] = 1;
                        EUDTraceLog(71)
                        _ARRW(v.textRefresh, cp) << (1)
                        # (Line 72) }
                        # (Line 73) }
                    EUDEndIf()
                    # (Line 74) }
                EUDEndIf()
                # (Line 75) else if(selectedSlot[cp] != 3 && strcmp(color[2], Db("\x05")) != 0) {
            _t16 = EUDElseIf()
            EUDTraceLog(75)
            if _t16(EUDSCAnd()(selectedSlot[cp] == 3, neg=True)(f_strcmp(color[2], Db("\x05")) == 0, neg=True)()):
                # (Line 76) color[2] = Db("\x05");
                EUDTraceLog(76)
                _ARRW(color, 2) << (Db("\x05"))
                # (Line 77) v.textRefresh[cp] = 1;
                EUDTraceLog(77)
                _ARRW(v.textRefresh, cp) << (1)
                # (Line 78) }
                # (Line 80) if(v._mouseY[cp] >= 192 && v._mouseY[cp] <= 206) {
            EUDEndIf()
            _t17 = EUDIf()
            EUDTraceLog(80)
            if _t17(EUDSCAnd()(v._mouseY[cp] >= 192)(v._mouseY[cp] <= 206)()):
                # (Line 81) if(selectedSlot[cp] != 4) {
                _t18 = EUDIf()
                EUDTraceLog(81)
                if _t18(selectedSlot[cp] == 4, neg=True):
                    # (Line 82) if(strcmp(color[3], Db("\x05")) == 0) {
                    _t19 = EUDIf()
                    EUDTraceLog(82)
                    if _t19(f_strcmp(color[3], Db("\x05")) == 0):
                        # (Line 83) color[3] = Db("\x04");
                        EUDTraceLog(83)
                        _ARRW(color, 3) << (Db("\x04"))
                        # (Line 84) v.textRefresh[cp] = 1;
                        EUDTraceLog(84)
                        _ARRW(v.textRefresh, cp) << (1)
                        # (Line 85) }
                        # (Line 86) }
                    EUDEndIf()
                    # (Line 87) }
                EUDEndIf()
                # (Line 88) else if(selectedSlot[cp] != 4 && strcmp(color[3], Db("\x05")) != 0) {
            _t20 = EUDElseIf()
            EUDTraceLog(88)
            if _t20(EUDSCAnd()(selectedSlot[cp] == 4, neg=True)(f_strcmp(color[3], Db("\x05")) == 0, neg=True)()):
                # (Line 89) color[3] = Db("\x05");
                EUDTraceLog(89)
                _ARRW(color, 3) << (Db("\x05"))
                # (Line 90) v.textRefresh[cp] = 1;
                EUDTraceLog(90)
                _ARRW(v.textRefresh, cp) << (1)
                # (Line 91) }
                # (Line 93) if(v._mouseY[cp] >= 208 && v._mouseY[cp] <= 222) {
            EUDEndIf()
            _t21 = EUDIf()
            EUDTraceLog(93)
            if _t21(EUDSCAnd()(v._mouseY[cp] >= 208)(v._mouseY[cp] <= 222)()):
                # (Line 94) if(selectedSlot[cp] != 5) {
                _t22 = EUDIf()
                EUDTraceLog(94)
                if _t22(selectedSlot[cp] == 5, neg=True):
                    # (Line 95) if(strcmp(color[4], Db("\x05")) == 0) {
                    _t23 = EUDIf()
                    EUDTraceLog(95)
                    if _t23(f_strcmp(color[4], Db("\x05")) == 0):
                        # (Line 96) color[4] = Db("\x04");
                        EUDTraceLog(96)
                        _ARRW(color, 4) << (Db("\x04"))
                        # (Line 97) v.textRefresh[cp] = 1;
                        EUDTraceLog(97)
                        _ARRW(v.textRefresh, cp) << (1)
                        # (Line 98) }
                        # (Line 99) }
                    EUDEndIf()
                    # (Line 100) }
                EUDEndIf()
                # (Line 101) else if(selectedSlot[cp] != 5 && strcmp(color[4], Db("\x05")) != 0) {
            _t24 = EUDElseIf()
            EUDTraceLog(101)
            if _t24(EUDSCAnd()(selectedSlot[cp] == 5, neg=True)(f_strcmp(color[4], Db("\x05")) == 0, neg=True)()):
                # (Line 102) color[4] = Db("\x05");
                EUDTraceLog(102)
                _ARRW(color, 4) << (Db("\x05"))
                # (Line 103) v.textRefresh[cp] = 1;
                EUDTraceLog(103)
                _ARRW(v.textRefresh, cp) << (1)
                # (Line 104) }
                # (Line 105) }
            EUDEndIf()
            # (Line 107) if(user.deathSCV[cp] == 1) {
        EUDEndIf()
        _t25 = EUDIf()
        EUDTraceLog(107)
        if _t25(user.deathSCV[cp] == 1):
            # (Line 108) if(sys.clickedLine(2)) {
            _t26 = EUDIf()
            EUDTraceLog(108)
            if _t26(sys.f_clickedLine(2)):
                # (Line 109) PlayWAV("staredit/wav/click2.ogg");
                # (Line 110) selectedSlot[cp] = 1;
                EUDTraceLog(109)
                DoActions(PlayWAV("staredit/wav/click2.ogg"))
                EUDTraceLog(110)
                _ARRW(selectedSlot, cp) << (1)
                # (Line 111) if(IsUserCP()) {
                _t27 = EUDIf()
                EUDTraceLog(111)
                if _t27(IsUserCP()):
                    # (Line 112) color[0] = Db("\x1f");
                    EUDTraceLog(112)
                    _ARRW(color, 0) << (Db("\x1f"))
                    # (Line 113) v.textRefresh[cp] = 1;
                    EUDTraceLog(113)
                    _ARRW(v.textRefresh, cp) << (1)
                    # (Line 114) }
                    # (Line 115) }
                EUDEndIf()
                # (Line 116) else if(sys.clickedLine(3)) {
            _t28 = EUDElseIf()
            EUDTraceLog(116)
            if _t28(sys.f_clickedLine(3)):
                # (Line 117) PlayWAV("staredit/wav/click2.ogg");
                # (Line 118) selectedSlot[cp] = 2;
                EUDTraceLog(117)
                DoActions(PlayWAV("staredit/wav/click2.ogg"))
                EUDTraceLog(118)
                _ARRW(selectedSlot, cp) << (2)
                # (Line 119) if(IsUserCP()) {
                _t29 = EUDIf()
                EUDTraceLog(119)
                if _t29(IsUserCP()):
                    # (Line 120) color[1] = Db("\x1f");
                    EUDTraceLog(120)
                    _ARRW(color, 1) << (Db("\x1f"))
                    # (Line 121) v.textRefresh[cp] = 1;
                    EUDTraceLog(121)
                    _ARRW(v.textRefresh, cp) << (1)
                    # (Line 122) }
                    # (Line 123) }
                EUDEndIf()
                # (Line 124) else if(sys.clickedLine(4)) {
            _t30 = EUDElseIf()
            EUDTraceLog(124)
            if _t30(sys.f_clickedLine(4)):
                # (Line 125) PlayWAV("staredit/wav/click2.ogg");
                # (Line 126) selectedSlot[cp] = 3;
                EUDTraceLog(125)
                DoActions(PlayWAV("staredit/wav/click2.ogg"))
                EUDTraceLog(126)
                _ARRW(selectedSlot, cp) << (3)
                # (Line 127) if(IsUserCP()) {
                _t31 = EUDIf()
                EUDTraceLog(127)
                if _t31(IsUserCP()):
                    # (Line 128) color[2] = Db("\x1f");
                    EUDTraceLog(128)
                    _ARRW(color, 2) << (Db("\x1f"))
                    # (Line 129) v.textRefresh[cp] = 1;
                    EUDTraceLog(129)
                    _ARRW(v.textRefresh, cp) << (1)
                    # (Line 130) }
                    # (Line 131) }
                EUDEndIf()
                # (Line 132) else if(sys.clickedLine(5)) {
            _t32 = EUDElseIf()
            EUDTraceLog(132)
            if _t32(sys.f_clickedLine(5)):
                # (Line 133) PlayWAV("staredit/wav/click2.ogg");
                # (Line 134) selectedSlot[cp] = 4;
                EUDTraceLog(133)
                DoActions(PlayWAV("staredit/wav/click2.ogg"))
                EUDTraceLog(134)
                _ARRW(selectedSlot, cp) << (4)
                # (Line 135) if(IsUserCP()) {
                _t33 = EUDIf()
                EUDTraceLog(135)
                if _t33(IsUserCP()):
                    # (Line 136) color[3] = Db("\x1f");
                    EUDTraceLog(136)
                    _ARRW(color, 3) << (Db("\x1f"))
                    # (Line 137) v.textRefresh[cp] = 1;
                    EUDTraceLog(137)
                    _ARRW(v.textRefresh, cp) << (1)
                    # (Line 138) }
                    # (Line 139) }
                EUDEndIf()
                # (Line 140) else if(sys.clickedLine(6)) {
            _t34 = EUDElseIf()
            EUDTraceLog(140)
            if _t34(sys.f_clickedLine(6)):
                # (Line 141) PlayWAV("staredit/wav/click2.ogg");
                # (Line 142) selectedSlot[cp] = 5;
                EUDTraceLog(141)
                DoActions(PlayWAV("staredit/wav/click2.ogg"))
                EUDTraceLog(142)
                _ARRW(selectedSlot, cp) << (5)
                # (Line 143) if(IsUserCP()) {
                _t35 = EUDIf()
                EUDTraceLog(143)
                if _t35(IsUserCP()):
                    # (Line 144) color[4] = Db("\x1f");
                    EUDTraceLog(144)
                    _ARRW(color, 4) << (Db("\x1f"))
                    # (Line 145) v.textRefresh[cp] = 1;
                    EUDTraceLog(145)
                    _ARRW(v.textRefresh, cp) << (1)
                    # (Line 146) }
                    # (Line 147) }
                EUDEndIf()
                # (Line 148) else if(sys.clickedLine(8) && selectedSlot[cp] != 0) {
            _t36 = EUDElseIf()
            EUDTraceLog(148)
            if _t36(EUDSCAnd()(sys.f_clickedLine(8))(selectedSlot[cp] == 0, neg=True)()):
                # (Line 149) opening.step[cp] = 6;
                EUDTraceLog(149)
                _ARRW(opening.step, cp) << (6)
                # (Line 150) screen.SetLight(25);
                EUDTraceLog(150)
                screen.SetLight(25)
                # (Line 151) potal.Move(potal.potal[0], potal.potal[1], 2);
                EUDTraceLog(151)
                potal.Move(potal.potal[0], potal.potal[1], 2)
                # (Line 152) Close();
                EUDTraceLog(152)
                Close()
                # (Line 153) }
                # (Line 154) }
            EUDEndIf()
            # (Line 155) }
        EUDEndIf()
        # (Line 156) }
    EUDEndIf()
    # (Line 158) function Open() {

@EUDTracedFunc
def Open():
    # (Line 159) const cp = getcurpl();
    EUDTraceLog(159)
    cp = f_getcurpl()
    # (Line 160) user.openedSlot[cp] = 1;
    EUDTraceLog(160)
    _ARRW(user.openedSlot, cp) << (1)
    # (Line 161) selectedSlot[cp] = 1;
    EUDTraceLog(161)
    _ARRW(selectedSlot, cp) << (1)
    # (Line 162) mousePosition[cp] = 0;
    EUDTraceLog(162)
    _ARRW(mousePosition, cp) << (0)
    # (Line 163) v.textRefresh[cp] = 1;
    EUDTraceLog(163)
    _ARRW(v.textRefresh, cp) << (1)
    # (Line 164) if(IsUserCP()) {
    _t1 = EUDIf()
    EUDTraceLog(164)
    if _t1(IsUserCP()):
        # (Line 165) color[0] = Db("\x1f");
        EUDTraceLog(165)
        _ARRW(color, 0) << (Db("\x1f"))
        # (Line 166) for(var i = 1; i < 6; i++)
        EUDTraceLog(166)
        i = EUDVariable()
        i << (1)
        _t2 = EUDWhile()
        EUDTraceLog(166)
        if _t2(i >= 6, neg=True):
            def _t3():
                EUDTraceLog(166)
                i.__iadd__(1)
            # (Line 167) color[i] = Db("\x05");
            EUDTraceLog(167)
            _ARRW(color, i) << (Db("\x05"))
            # (Line 168) }
            EUDSetContinuePoint()
            _t3()
        EUDEndWhile()
        # (Line 169) }
    EUDEndIf()
    # (Line 171) function Close() {

@EUDTracedFunc
def Close():
    # (Line 172) const cp = getcurpl();
    EUDTraceLog(172)
    cp = f_getcurpl()
    # (Line 173) user.openedSlot[cp] = 0;
    EUDTraceLog(173)
    _ARRW(user.openedSlot, cp) << (0)
    # (Line 174) sys.TextClear();
    EUDTraceLog(174)
    sys.TextClear()
    # (Line 175) }