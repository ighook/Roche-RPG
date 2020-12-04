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
# (Line 2) import Screen as screen;
import Screen as screen
# (Line 3) import System as sys;
import System as sys
# (Line 4) import Variable as v;
import Variable as v
# (Line 5) import Item.Manager as item;
from Item import Manager as item
# (Line 6) import Inventory as inven;
import Inventory as inven
# (Line 7) import User.Info as user;
from User import Info as user
# (Line 8) import User.Stats as stats;
from User import Stats as stats
# (Line 9) import User.Character as char;
from User import Character as char
# (Line 10) import Equip as equip;
import Equip as equip
# (Line 11) import Potal as potal;
import Potal as potal
# (Line 12) import StatusBar as status;
import StatusBar as status
# (Line 13) import Box as box;
import Box as box
# (Line 14) import SCA.Load as load;
from SCA import Load as load
# (Line 15) import SCA.Data as data;
from SCA import Data as data
# (Line 16) import SCA.Slot as slot;
from SCA import Slot as slot
# (Line 18) const elapsedTime = PVariable();
elapsedTime = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 19) const step = PVariable();
step = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 20) const selectedSlot = PVariable();
selectedSlot = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 21) const selectNewSlot = PVariable();
selectNewSlot = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 22) const Message = PVariable();
Message = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 23) const helpPage = PVariable();
helpPage = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 24) const color = EUDArray(5);
color = _CGFW(lambda: [EUDArray(5)], 1)[0]
# (Line 25) const mousePosition = PVariable();
mousePosition = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 26) const btn1 = Db("\x07새로하기");
btn1 = _CGFW(lambda: [Db("\x07새로하기")], 1)[0]
# (Line 27) const btn2 = Db("\x0F불러오기");
btn2 = _CGFW(lambda: [Db("\x0F불러오기")], 1)[0]
# (Line 29) function GameStart();
# (Line 31) function Opening() {
@EUDTracedFunc
def Opening():
    # (Line 32) const cp = getcurpl();
    EUDTraceLog(32)
    cp = f_getcurpl()
    # (Line 33) if(step[cp] == 0) {
    _t1 = EUDIf()
    EUDTraceLog(33)
    if _t1(step[cp] == 0):
        # (Line 34) if(elapsedTime[cp] == 0) {
        _t2 = EUDIf()
        EUDTraceLog(34)
        if _t2(elapsedTime[cp] == 0):
            # (Line 35) if(IsUserCP()) {
            _t3 = EUDIf()
            EUDTraceLog(35)
            if _t3(IsUserCP()):
                # (Line 36) screen.light[cp] = 0;
                EUDTraceLog(36)
                _ARRW(screen.light, cp) << (0)
                # (Line 37) SetMemoryEPD(EPD(0x657A9C), SetTo, 0);
                # (Line 38) }
                EUDTraceLog(37)
                DoActions(SetMemoryEPD(EPD(0x657A9C), SetTo, 0))
                # (Line 40) }
            EUDEndIf()
            # (Line 41) else if(elapsedTime[cp] == 1) {
        _t4 = EUDElseIf()
        EUDTraceLog(41)
        if _t4(elapsedTime[cp] == 1):
            # (Line 42) screen.SetLight(0);
            EUDTraceLog(42)
            screen.SetLight(0)
            # (Line 43) }
            # (Line 44) else if(elapsedTime[cp] == 2) {
        _t5 = EUDElseIf()
        EUDTraceLog(44)
        if _t5(elapsedTime[cp] == 2):
            # (Line 45) elapsedTime[cp] += 1;
            EUDTraceLog(45)
            _ARRW(elapsedTime, cp).__iadd__(1)
            # (Line 46) status.stats[cp] = status.SCA_WAIT;
            EUDTraceLog(46)
            _ARRW(status.stats, cp) << (status.SCA_WAIT)
            # (Line 47) step[cp] = 1;
            EUDTraceLog(47)
            _ARRW(step, cp) << (1)
            # (Line 48) helpPage[cp] = 1;
            EUDTraceLog(48)
            _ARRW(helpPage, cp) << (1)
            # (Line 49) if(sys.single == false) screen.WideCheck();
            _t6 = EUDIf()
            EUDTraceLog(49)
            if _t6(sys.single == False):
                EUDTraceLog(49)
                screen.WideCheck()
                # (Line 50) user.inConv[cp] = 1;
            EUDEndIf()
            EUDTraceLog(50)
            _ARRW(user.inConv, cp) << (1)
            # (Line 51) v.textRefresh[cp] = 1;
            EUDTraceLog(51)
            _ARRW(v.textRefresh, cp) << (1)
            # (Line 52) }
            # (Line 53) elapsedTime[cp] += 1;
        EUDEndIf()
        EUDTraceLog(53)
        _ARRW(elapsedTime, cp).__iadd__(1)
        # (Line 54) }
        # (Line 56) if(step[cp] == 1) {
    EUDEndIf()
    _t7 = EUDIf()
    EUDTraceLog(56)
    if _t7(step[cp] == 1):
        # (Line 57) sys.Stop();
        EUDTraceLog(57)
        sys.Stop()
        # (Line 58) if(sca.ConnectStatus() == 0) {
        _t8 = EUDIf()
        EUDTraceLog(58)
        if _t8(sca.ConnectStatus() == 0):
            # (Line 59) if(v.textRefresh[cp] == 1) {
            _t9 = EUDIf()
            EUDTraceLog(59)
            if _t9(v.textRefresh[cp] == 1):
                # (Line 60) v.textRefresh[cp] = 0;
                EUDTraceLog(60)
                _ARRW(v.textRefresh, cp) << (0)
                # (Line 61) v.display.insert(0);
                EUDTraceLog(61)
                v.display.insert(0)
                # (Line 62) if(helpPage[cp] == 1) {
                _t10 = EUDIf()
                EUDTraceLog(62)
                if _t10(helpPage[cp] == 1):
                    # (Line 63) v.display.append("\x13\x07다운로드 링크\n");
                    EUDTraceLog(63)
                    v.display.append("\x13\x07다운로드 링크\n")
                    # (Line 64) v.display.append("\x13\x04www.scarchive.kr\n\n");
                    EUDTraceLog(64)
                    v.display.append("\x13\x04www.scarchive.kr\n\n")
                    # (Line 65) }
                    # (Line 66) else if(helpPage[cp] == 2) {
                _t11 = EUDElseIf()
                EUDTraceLog(66)
                if _t11(helpPage[cp] == 2):
                    # (Line 67) v.display.append("\x13\x07주의 사항\n");
                    EUDTraceLog(67)
                    v.display.append("\x13\x07주의 사항\n")
                    # (Line 68) v.display.append("\x13\x04스타크래프트를 32비트로 설정해 주세요\n\n");
                    EUDTraceLog(68)
                    v.display.append("\x13\x04스타크래프트를 32비트로 설정해 주세요\n\n")
                    # (Line 69) }
                    # (Line 70) v.display.append("\x13\x15■ \x1e이전    \x15■ \x1e다음\n");
                EUDEndIf()
                EUDTraceLog(70)
                v.display.append("\x13\x15■ \x1e이전    \x15■ \x1e다음\n")
                # (Line 71) v.display.append("\x13\x05이전 또는 다음을 마우스로 클릭 해주세요\n");
                EUDTraceLog(71)
                v.display.append("\x13\x05이전 또는 다음을 마우스로 클릭 해주세요\n")
                # (Line 72) }
                # (Line 73) v.display.DisplayAt(0);
            EUDEndIf()
            EUDTraceLog(73)
            v.display.DisplayAt(0)
            # (Line 74) if(v.mouse[cp] == 1) {
            _t12 = EUDIf()
            EUDTraceLog(74)
            if _t12(v.mouse[cp] == 1):
                # (Line 75) if(sys.clickedLine(3)) {
                _t13 = EUDIf()
                EUDTraceLog(75)
                if _t13(sys.f_clickedLine(3)):
                    # (Line 76) var x = 0;
                    EUDTraceLog(76)
                    x = EUDVariable()
                    x << (0)
                    # (Line 77) if(v.screenMode[cp] == 2) x += 107;
                    _t14 = EUDIf()
                    EUDTraceLog(77)
                    if _t14(v.screenMode[cp] == 2):
                        EUDTraceLog(77)
                        x.__iadd__(107)
                        # (Line 78) if(v.mouseX[cp] >= 277 + x && v.mouseX[cp] <= 324 + x) {
                    EUDEndIf()
                    _t15 = EUDIf()
                    EUDTraceLog(78)
                    if _t15(EUDSCAnd()(v.mouseX[cp] >= 277 + x)(v.mouseX[cp] <= 324 + x)()):
                        # (Line 79) PlayWAV("staredit\\wav\\click2.ogg");
                        # (Line 80) v.s.printAt(3, "\x13\x15■ \x0e이전    \x15■ \x1e다음");
                        EUDTraceLog(79)
                        DoActions(PlayWAV("staredit\\wav\\click2.ogg"))
                        EUDTraceLog(80)
                        v.s.printAt(3, "\x13\x15■ \x0e이전    \x15■ \x1e다음")
                        # (Line 81) if(helpPage[cp] == 2) helpPage[cp] = 1;
                        _t16 = EUDIf()
                        EUDTraceLog(81)
                        if _t16(helpPage[cp] == 2):
                            EUDTraceLog(81)
                            _ARRW(helpPage, cp) << (1)
                            # (Line 82) v.textRefresh[cp] = 1;
                        EUDEndIf()
                        EUDTraceLog(82)
                        _ARRW(v.textRefresh, cp) << (1)
                        # (Line 83) }
                        # (Line 84) else if(v.mouseX[cp] >= 328 + x && v.mouseX[cp] <= 364 + x) {
                    _t17 = EUDElseIf()
                    EUDTraceLog(84)
                    if _t17(EUDSCAnd()(v.mouseX[cp] >= 328 + x)(v.mouseX[cp] <= 364 + x)()):
                        # (Line 85) PlayWAV("staredit\\wav\\click2.ogg");
                        # (Line 86) v.s.printAt(3, "\x13\x15■ \x1e이전    \x15■ \x0e다음");
                        EUDTraceLog(85)
                        DoActions(PlayWAV("staredit\\wav\\click2.ogg"))
                        EUDTraceLog(86)
                        v.s.printAt(3, "\x13\x15■ \x1e이전    \x15■ \x0e다음")
                        # (Line 87) if(helpPage[cp] == 1) helpPage[cp] = 2;
                        _t18 = EUDIf()
                        EUDTraceLog(87)
                        if _t18(helpPage[cp] == 1):
                            EUDTraceLog(87)
                            _ARRW(helpPage, cp) << (2)
                            # (Line 88) v.textRefresh[cp] = 1;
                        EUDEndIf()
                        EUDTraceLog(88)
                        _ARRW(v.textRefresh, cp) << (1)
                        # (Line 89) }
                        # (Line 90) }
                    EUDEndIf()
                    # (Line 91) }
                EUDEndIf()
                # (Line 92) if(v.chat[cp] == 2) {
            EUDEndIf()
            _t19 = EUDIf()
            EUDTraceLog(92)
            if _t19(v.chat[cp] == 2):
                # (Line 93) sys.TextClear();
                EUDTraceLog(93)
                sys.TextClear()
                # (Line 94) user.currentSlot[cp] = 1;
                EUDTraceLog(94)
                _ARRW(user.currentSlot, cp) << (1)
                # (Line 95) char.NewCharacter();
                EUDTraceLog(95)
                char.NewCharacter()
                # (Line 96) step[cp] = 2;
                EUDTraceLog(96)
                _ARRW(step, cp) << (2)
                # (Line 97) v.started[cp] = 1;
                EUDTraceLog(97)
                _ARRW(v.started, cp) << (1)
                # (Line 98) user.inConv[cp] = 0;
                EUDTraceLog(98)
                _ARRW(user.inConv, cp) << (0)
                # (Line 99) screen.SetLight(31);
                EUDTraceLog(99)
                screen.SetLight(31)
                # (Line 100) }
                # (Line 101) }
            EUDEndIf()
            # (Line 102) else if(sca.ConnectStatus() == 1) {
        _t20 = EUDElseIf()
        EUDTraceLog(102)
        if _t20(sca.ConnectStatus() == 1):
            # (Line 104) sys.TextClear();
            EUDTraceLog(104)
            sys.TextClear()
            # (Line 105) sca.LoadGlobalData();
            EUDTraceLog(105)
            sca.LoadGlobalData()
            # (Line 106) status.stats[cp] = status.LOAD_GLOBAL;
            EUDTraceLog(106)
            _ARRW(status.stats, cp) << (status.LOAD_GLOBAL)
            # (Line 107) step[cp] = 2;
            EUDTraceLog(107)
            _ARRW(step, cp) << (2)
            # (Line 108) }
            # (Line 109) }
        EUDEndIf()
        # (Line 110) else if(step[cp] == 2) {
    _t21 = EUDElseIf()
    EUDTraceLog(110)
    if _t21(step[cp] == 2):
        # (Line 111) if(sca.GetLastMessage() == 4) {
        _t22 = EUDIf()
        EUDTraceLog(111)
        if _t22(sca.GetLastMessage() == 4):
            # (Line 112) sca.ResetLastMessage();
            EUDTraceLog(112)
            sca.ResetLastMessage()
            # (Line 113) status.stats[cp] = 0;
            EUDTraceLog(113)
            _ARRW(status.stats, cp) << (0)
            # (Line 114) if(v.version != sca.GlobalData[0]) {
            _t23 = EUDIf()
            EUDTraceLog(114)
            if _t23(v.version == sca.GlobalData[0], neg=True):
                # (Line 115) v.s.print("\x08최신 버전이 아닙니다");
                EUDTraceLog(115)
                v.s.print("\x08최신 버전이 아닙니다")
                # (Line 116) }
                # (Line 117) else {
            if EUDElse()():
                # (Line 118) v.s.print("\x07최신 버전입니다");
                EUDTraceLog(118)
                v.s.print("\x07최신 버전입니다")
                # (Line 119) }
                # (Line 120) step[cp] = 3;
            EUDEndIf()
            EUDTraceLog(120)
            _ARRW(step, cp) << (3)
            # (Line 121) }
            # (Line 122) }
        EUDEndIf()
        # (Line 123) else if(step[cp] == 3) {
    _t24 = EUDElseIf()
    EUDTraceLog(123)
    if _t24(step[cp] == 3):
        # (Line 124) if(sca.ConnectStatus() == 1) {
        _t25 = EUDIf()
        EUDTraceLog(124)
        if _t25(sca.ConnectStatus() == 1):
            # (Line 125) sca.LoadData(0);
            EUDTraceLog(125)
            sca.LoadData(0)
            # (Line 126) status.stats[cp] = status.LOADING;
            EUDTraceLog(126)
            _ARRW(status.stats, cp) << (status.LOADING)
            # (Line 127) if(IsUserCP()) {
            _t26 = EUDIf()
            EUDTraceLog(127)
            if _t26(IsUserCP()):
                # (Line 128) for(var i = 0; i < 5; i++) color[i] = Db("\x05");
                EUDTraceLog(128)
                i = EUDVariable()
                i << (0)
                _t27 = EUDWhile()
                EUDTraceLog(128)
                if _t27(i >= 5, neg=True):
                    def _t28():
                        EUDTraceLog(128)
                        i.__iadd__(1)
                    EUDTraceLog(128)
                    _ARRW(color, i) << (Db("\x05"))
                    # (Line 129) }
                    EUDSetContinuePoint()
                    _t28()
                EUDEndWhile()
                # (Line 130) step[cp] = 4;
            EUDEndIf()
            EUDTraceLog(130)
            _ARRW(step, cp) << (4)
            # (Line 131) }
            # (Line 132) }
        EUDEndIf()
        # (Line 133) else if(step[cp] == 4) {
    _t29 = EUDElseIf()
    EUDTraceLog(133)
    if _t29(step[cp] == 4):
        # (Line 134) if(sca.GetLastMessage() == 4) {
        _t30 = EUDIf()
        EUDTraceLog(134)
        if _t30(sca.GetLastMessage() == 4):
            # (Line 135) sca.ResetLastMessage();
            EUDTraceLog(135)
            sca.ResetLastMessage()
            # (Line 136) status.stats[cp] = 1;
            EUDTraceLog(136)
            _ARRW(status.stats, cp) << (1)
            # (Line 137) load.LoadSlot();
            EUDTraceLog(137)
            load.LoadSlot()
            # (Line 138) v.textRefresh[cp] = 1;
            EUDTraceLog(138)
            _ARRW(v.textRefresh, cp) << (1)
            # (Line 139) step[cp] = 5;
            EUDTraceLog(139)
            _ARRW(step, cp) << (5)
            # (Line 140) }
            # (Line 141) }
        EUDEndIf()
        # (Line 142) else if(step[cp] == 5) {
    _t31 = EUDElseIf()
    EUDTraceLog(142)
    if _t31(step[cp] == 5):
        # (Line 143) if(v.textRefresh[cp] == 1) {
        _t32 = EUDIf()
        EUDTraceLog(143)
        if _t32(v.textRefresh[cp] == 1):
            # (Line 144) v.textRefresh[cp] = 0;
            EUDTraceLog(144)
            _ARRW(v.textRefresh, cp) << (0)
            # (Line 145) v.display.insert(0);
            EUDTraceLog(145)
            v.display.insert(0)
            # (Line 146) v.display.append("\n\x13\x04================\n");
            EUDTraceLog(146)
            v.display.append("\n\x13\x04================\n")
            # (Line 147) v.display.append("\x13", ptr2s(color[0]), "Lv.", user.slotLevel[5 * cp + 0], "  장착중인 무기 : -\n");
            EUDTraceLog(147)
            v.display.append("\x13", ptr2s(color[0]), "Lv.", user.slotLevel[5 * cp + 0], "  장착중인 무기 : -\n")
            # (Line 148) v.display.append("\x13", ptr2s(color[1]), "Lv.", user.slotLevel[5 * cp + 1], "  장착중인 무기 : -\n");
            EUDTraceLog(148)
            v.display.append("\x13", ptr2s(color[1]), "Lv.", user.slotLevel[5 * cp + 1], "  장착중인 무기 : -\n")
            # (Line 149) v.display.append("\x13", ptr2s(color[2]), "Lv.", user.slotLevel[5 * cp + 2], "  장착중인 무기 : -\n");
            EUDTraceLog(149)
            v.display.append("\x13", ptr2s(color[2]), "Lv.", user.slotLevel[5 * cp + 2], "  장착중인 무기 : -\n")
            # (Line 150) v.display.append("\x13", ptr2s(color[3]), "Lv.", user.slotLevel[5 * cp + 3], "  장착중인 무기 : -\n");
            EUDTraceLog(150)
            v.display.append("\x13", ptr2s(color[3]), "Lv.", user.slotLevel[5 * cp + 3], "  장착중인 무기 : -\n")
            # (Line 151) v.display.append("\x13", ptr2s(color[4]), "Lv.", user.slotLevel[5 * cp + 4], "  장착중인 무기 : -\n");
            EUDTraceLog(151)
            v.display.append("\x13", ptr2s(color[4]), "Lv.", user.slotLevel[5 * cp + 4], "  장착중인 무기 : -\n")
            # (Line 152) v.display.append("\x13\x04================\n");
            EUDTraceLog(152)
            v.display.append("\x13\x04================\n")
            # (Line 153) v.display.append("\x13", ptr2s(btn1), "  ", ptr2s(btn2));
            EUDTraceLog(153)
            v.display.append("\x13", ptr2s(btn1), "  ", ptr2s(btn2))
            # (Line 154) }
            # (Line 155) v.display.DisplayAt(0);
        EUDEndIf()
        EUDTraceLog(155)
        v.display.DisplayAt(0)
        # (Line 156) if(IsUserCP()) {
        _t33 = EUDIf()
        EUDTraceLog(156)
        if _t33(IsUserCP()):
            # (Line 157) if(v._mouseY[cp] < 144 || v._mouseY[cp] > 222) {
            _t34 = EUDIf()
            EUDTraceLog(157)
            if _t34(EUDSCOr()(v._mouseY[cp] >= 144, neg=True)(v._mouseY[cp] <= 222, neg=True)()):
                # (Line 158) if(mousePosition[cp] != 0) {
                _t35 = EUDIf()
                EUDTraceLog(158)
                if _t35(mousePosition[cp] == 0, neg=True):
                    # (Line 159) mousePosition[cp] = 0;
                    EUDTraceLog(159)
                    _ARRW(mousePosition, cp) << (0)
                    # (Line 160) for(var i = 0; i < 5; i++) {
                    EUDTraceLog(160)
                    i = EUDVariable()
                    i << (0)
                    _t36 = EUDWhile()
                    EUDTraceLog(160)
                    if _t36(i >= 5, neg=True):
                        def _t37():
                            EUDTraceLog(160)
                            i.__iadd__(1)
                        # (Line 161) if(selectedSlot[cp] != i + 1) color[i] = Db("\x05");
                        _t38 = EUDIf()
                        EUDTraceLog(161)
                        if _t38(selectedSlot[cp] == i + 1, neg=True):
                            EUDTraceLog(161)
                            _ARRW(color, i) << (Db("\x05"))
                            # (Line 162) }
                        EUDEndIf()
                        # (Line 163) v.textRefresh[cp] = 1;
                        EUDSetContinuePoint()
                        _t37()
                    EUDEndWhile()
                    EUDTraceLog(163)
                    _ARRW(v.textRefresh, cp) << (1)
                    # (Line 164) }
                    # (Line 165) }
                EUDEndIf()
                # (Line 166) else {
            if EUDElse()():
                # (Line 167) for(var i = 0; i < 5; i++) {
                EUDTraceLog(167)
                i = EUDVariable()
                i << (0)
                _t39 = EUDWhile()
                EUDTraceLog(167)
                if _t39(i >= 5, neg=True):
                    def _t40():
                        EUDTraceLog(167)
                        i.__iadd__(1)
                    # (Line 168) if(v._mouseY[cp] >= 144 + 16 * i && v._mouseY[cp] <= 158 + 16 * i) {
                    _t41 = EUDIf()
                    EUDTraceLog(168)
                    if _t41(EUDSCAnd()(v._mouseY[cp] >= 144 + 16 * i)(v._mouseY[cp] <= 158 + 16 * i)()):
                        # (Line 169) mousePosition[cp] = i + 1;
                        EUDTraceLog(169)
                        _ARRW(mousePosition, cp) << (i + 1)
                        # (Line 170) if(selectedSlot[cp] != i + 1) {
                        _t42 = EUDIf()
                        EUDTraceLog(170)
                        if _t42(selectedSlot[cp] == i + 1, neg=True):
                            # (Line 171) if(strcmp(color[i], Db("\x05")) == 0) {
                            _t43 = EUDIf()
                            EUDTraceLog(171)
                            if _t43(f_strcmp(color[i], Db("\x05")) == 0):
                                # (Line 172) color[i] = Db("\x04");
                                EUDTraceLog(172)
                                _ARRW(color, i) << (Db("\x04"))
                                # (Line 173) v.textRefresh[cp] = 1;
                                EUDTraceLog(173)
                                _ARRW(v.textRefresh, cp) << (1)
                                # (Line 174) }
                                # (Line 175) }
                            EUDEndIf()
                            # (Line 176) }
                        EUDEndIf()
                        # (Line 177) else if(selectedSlot[cp] != i + 1 && strcmp(color[i], Db("\x05")) != 0) {
                    _t44 = EUDElseIf()
                    EUDTraceLog(177)
                    if _t44(EUDSCAnd()(selectedSlot[cp] == i + 1, neg=True)(f_strcmp(color[i], Db("\x05")) == 0, neg=True)()):
                        # (Line 178) color[i] = Db("\x05");
                        EUDTraceLog(178)
                        _ARRW(color, i) << (Db("\x05"))
                        # (Line 179) v.textRefresh[cp] = 1;
                        EUDTraceLog(179)
                        _ARRW(v.textRefresh, cp) << (1)
                        # (Line 180) }
                        # (Line 181) }
                    EUDEndIf()
                    # (Line 182) }
                    EUDSetContinuePoint()
                    _t40()
                EUDEndWhile()
                # (Line 183) }
            EUDEndIf()
            # (Line 184) if(v.mouse[cp] == 1) {
        EUDEndIf()
        _t45 = EUDIf()
        EUDTraceLog(184)
        if _t45(v.mouse[cp] == 1):
            # (Line 185) if(v.mouseY[cp] >= 144 && v.mouseY[cp] <= 222) {
            _t46 = EUDIf()
            EUDTraceLog(185)
            if _t46(EUDSCAnd()(v.mouseY[cp] >= 144)(v.mouseY[cp] <= 222)()):
                # (Line 186) for(var i = 0; i < 5; i++) {
                EUDTraceLog(186)
                i = EUDVariable()
                i << (0)
                _t47 = EUDWhile()
                EUDTraceLog(186)
                if _t47(i >= 5, neg=True):
                    def _t48():
                        EUDTraceLog(186)
                        i.__iadd__(1)
                    # (Line 187) if(sys.clickedLine(i + 2)) {
                    _t49 = EUDIf()
                    EUDTraceLog(187)
                    if _t49(sys.f_clickedLine(i + 2)):
                        # (Line 188) PlayWAV("staredit\\wav\\click2.ogg");
                        # (Line 189) if(IsUserCP()) {
                        EUDTraceLog(188)
                        DoActions(PlayWAV("staredit\\wav\\click2.ogg"))
                        _t50 = EUDIf()
                        EUDTraceLog(189)
                        if _t50(IsUserCP()):
                            # (Line 190) color[i] = Db("\x1f");
                            EUDTraceLog(190)
                            _ARRW(color, i) << (Db("\x1f"))
                            # (Line 191) selectedSlot[cp] = i + 1;
                            EUDTraceLog(191)
                            _ARRW(selectedSlot, cp) << (i + 1)
                            # (Line 192) v.textRefresh[cp] = 1;
                            EUDTraceLog(192)
                            _ARRW(v.textRefresh, cp) << (1)
                            # (Line 193) }
                            # (Line 194) break;
                        EUDEndIf()
                        EUDTraceLog(194)
                        EUDBreak()
                        # (Line 195) }
                        # (Line 196) }
                    EUDEndIf()
                    # (Line 197) }
                    EUDSetContinuePoint()
                    _t48()
                EUDEndWhile()
                # (Line 198) else if(sys.clickedLine(8)) {
            _t51 = EUDElseIf()
            EUDTraceLog(198)
            if _t51(sys.f_clickedLine(8)):
                # (Line 199) var x = 0;
                EUDTraceLog(199)
                x = EUDVariable()
                x << (0)
                # (Line 200) if(v.screenMode[cp] == 2) x = 106;
                _t52 = EUDIf()
                EUDTraceLog(200)
                if _t52(v.screenMode[cp] == 2):
                    EUDTraceLog(200)
                    x << (106)
                    # (Line 201) if(v.mouseX[cp] >= 273 + x && v.mouseX[cp] <= 317 + x) {
                EUDEndIf()
                _t53 = EUDIf()
                EUDTraceLog(201)
                if _t53(EUDSCAnd()(v.mouseX[cp] >= 273 + x)(v.mouseX[cp] <= 317 + x)()):
                    # (Line 202) PlayWAV("staredit\\wav\\click2.ogg");
                    # (Line 203) user.currentSlot[cp] = selectedSlot[cp];
                    EUDTraceLog(202)
                    DoActions(PlayWAV("staredit\\wav\\click2.ogg"))
                    EUDTraceLog(203)
                    _ARRW(user.currentSlot, cp) << (selectedSlot[cp])
                    # (Line 204) sys.TextClear();
                    EUDTraceLog(204)
                    sys.TextClear()
                    # (Line 205) step[cp] = 6;
                    EUDTraceLog(205)
                    _ARRW(step, cp) << (6)
                    # (Line 206) v.started[cp] = 1;
                    EUDTraceLog(206)
                    _ARRW(v.started, cp) << (1)
                    # (Line 207) user.inConv[cp] = 0;
                    EUDTraceLog(207)
                    _ARRW(user.inConv, cp) << (0)
                    # (Line 208) screen.SetLight(31);
                    EUDTraceLog(208)
                    screen.SetLight(31)
                    # (Line 209) char.NewCharacter();
                    EUDTraceLog(209)
                    char.NewCharacter()
                    # (Line 210) }
                    # (Line 211) else if(v.mouseX[cp] >= 324 + x && v.mouseX[cp] <= 368 + x) {
                _t54 = EUDElseIf()
                EUDTraceLog(211)
                if _t54(EUDSCAnd()(v.mouseX[cp] >= 324 + x)(v.mouseX[cp] <= 368 + x)()):
                    # (Line 212) PlayWAV("staredit\\wav\\click2.ogg");
                    # (Line 213) }
                    EUDTraceLog(212)
                    DoActions(PlayWAV("staredit\\wav\\click2.ogg"))
                    # (Line 214) }
                EUDEndIf()
                # (Line 215) }
            EUDEndIf()
            # (Line 216) }
        EUDEndIf()
        # (Line 228) }
    EUDEndIf()
