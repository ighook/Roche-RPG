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
# (Line 4) const single = EUDVariable();
single = _CGFW(lambda: [EUDVariable()], 1)[0]
# (Line 5) const useSCA = EUDVariable();
useSCA = _CGFW(lambda: [EUDVariable()], 1)[0]
# (Line 7) function SetNextUnitPTR();
# (Line 8) function SetNextUnitEPD();
# (Line 9) function SetAlliance();
# (Line 10) function ButtonRefresh();
# (Line 11) function SetPColor(pnum, color);
# (Line 12) function Heal();
# (Line 42) function Stop() {
@EUDFunc
def Stop():
    # (Line 43) const cp = getcurpl();
    cp = f_getcurpl()
    # (Line 44) MoveUnit(1, v.playerUnit[cp], cp, "Anywhere", "Black");
    # (Line 45) }
    DoActions(MoveUnit(1, v.playerUnit[cp], cp, "Anywhere", "Black"))
    # (Line 47) function SetNextUnitPTR() {

@EUDFunc
def SetNextUnitPTR():
    # (Line 48) return dwread_epd(EPD(0x628438));
    EUDReturn(f_dwread_epd(EPD(0x628438)))
    # (Line 49) }
    # (Line 51) function SetNextUnitEPD() {

@EUDFunc
def SetNextUnitEPD():
    # (Line 52) return epdread_epd(EPD(0x628438));
    EUDReturn(f_epdread_epd(EPD(0x628438)))
    # (Line 53) }
    # (Line 55) function SetLocation(locationNum: TrgLocation, x, y, size) {

@EUDTypedFunc([TrgLocation, None, None, None])
def SetLocation(locationNum, x, y, size):
    # (Line 56) const loc = EPD(0x58DC4C) + locationNum * 5;
    loc = EPD(0x58DC4C) + locationNum * 5
    # (Line 57) SetMemoryEPD(loc + 0, SetTo, x - size);
    # (Line 58) SetMemoryEPD(loc + 1, SetTo, y - size);
    DoActions(SetMemoryEPD(loc + 0, SetTo, x - size))
    # (Line 59) SetMemoryEPD(loc + 2, SetTo, x + size);
    DoActions(SetMemoryEPD(loc + 1, SetTo, y - size))
    # (Line 60) SetMemoryEPD(loc + 3, SetTo, y + size);
    DoActions(SetMemoryEPD(loc + 2, SetTo, x + size))
    # (Line 61) }
    DoActions(SetMemoryEPD(loc + 3, SetTo, y + size))
    # (Line 63) function SetPlayerLoc() {

@EUDFunc
def SetPlayerLoc():
    # (Line 64) const cp = getcurpl();
    cp = f_getcurpl()
    # (Line 65) if(user.alive[cp] == true) {
    if EUDIf()(user.alive[cp] == True):
        # (Line 66) MoveLocation(v.playerLoc[cp], v.playerUnit[cp], cp, "Anywhere");
        # (Line 67) }
        DoActions(MoveLocation(v.playerLoc[cp], v.playerUnit[cp], cp, "Anywhere"))
        # (Line 68) }
    EUDEndIf()
    # (Line 70) function TextClear() {

@EUDFunc
def TextClear():
    # (Line 71) v.s.print("\n\n\n\n\n\n\n\n\n\n");
    v.s.print("\n\n\n\n\n\n\n\n\n\n")
    # (Line 72) }
    # (Line 74) function EPDBring(Location: TrgLocation, UnitEPD) {

@EUDTypedFunc([TrgLocation, None])
def EPDBring(Location, UnitEPD):
    # (Line 75) const posUnitX, posUnitY = dwbreak(dwread_epd(UnitEPD + 0x28 / 4))[[0,1]];
    posUnitX, posUnitY = List2Assignable([_SRET(f_dwbreak(f_dwread_epd(UnitEPD + 0x28 // 4)), [0, 1])])
    # (Line 76) const LocEPD = Location * 5 + EPD(0x58DC4C);
    LocEPD = Location * 5 + EPD(0x58DC4C)
    # (Line 77) if(
    _t1 = EUDIf()
    # (Line 78) MemoryEPD(LocEPD, AtMost, posUnitX) &&
    # (Line 79) MemoryEPD(LocEPD + 2, AtLeast, posUnitX) &&
    # (Line 80) MemoryEPD(LocEPD + 1, AtMost, posUnitY) &&
    # (Line 81) MemoryEPD(LocEPD + 3, AtLeast, posUnitY)
    # (Line 82) ){
    if _t1(EUDSCAnd()(MemoryEPD(LocEPD, AtMost, posUnitX))(MemoryEPD(LocEPD + 2, AtLeast, posUnitX))(MemoryEPD(LocEPD + 1, AtMost, posUnitY))(MemoryEPD(LocEPD + 3, AtLeast, posUnitY))()):
        # (Line 83) return True;
        EUDReturn(True)
        # (Line 84) }
        # (Line 85) return False;
    EUDEndIf()
    EUDReturn(False)
    # (Line 86) }
    # (Line 88) function StructMemoryXEPD(unitEPD ,StructOffset ,value ,comparison: TrgComparison) {

@EUDTypedFunc([None, None, None, TrgComparison])
def StructMemoryXEPD(unitEPD, StructOffset, value, comparison):
    # (Line 89) var Mask;
    Mask = EUDVariable()
    # (Line 90) switch(StructOffset % 4) {
    EUDSwitch(StructOffset % 4)
    # (Line 91) case 0:
    _t1 = EUDSwitchCase()
    # (Line 92) if(MemoryEPD(unitEPD + StructOffset / 4, comparison, value))
    if _t1(0):
        if EUDIf()(MemoryEPD(unitEPD + StructOffset // 4, comparison, value)):
            # (Line 93) return True;
            EUDReturn(True)
            # (Line 94) else return False;
        if EUDElse()():
            EUDReturn(False)
            # (Line 95) break;
        EUDEndIf()
        EUDBreak()
        # (Line 96) case 1:
    _t3 = EUDSwitchCase()
    # (Line 97) Mask = 0xFF00;
    if _t3(1):
        Mask << (0xFF00)
        # (Line 98) value = value*256;
        value << (value * 256)
        # (Line 99) break;
        EUDBreak()
        # (Line 100) case 2:
    _t4 = EUDSwitchCase()
    # (Line 101) Mask = 0xFF0000;
    if _t4(2):
        Mask << (0xFF0000)
        # (Line 102) value = value*65536;
        value << (value * 65536)
        # (Line 103) break;
        EUDBreak()
        # (Line 104) case 3:
    _t5 = EUDSwitchCase()
    # (Line 105) Mask = 0xFF000000;
    if _t5(3):
        Mask << (0xFF000000)
        # (Line 106) value = value*16777216;
        value << (value * 16777216)
        # (Line 107) break;
        EUDBreak()
        # (Line 108) }
    # (Line 109) if(MemoryXEPD(unitEPD + StructOffset / 4, comparison, value, Mask)) return true;
    EUDEndSwitch()
    if EUDIf()(MemoryXEPD(unitEPD + StructOffset // 4, comparison, value, Mask)):
        EUDReturn(True)
        # (Line 110) else return false;
    if EUDElse()():
        EUDReturn(False)
        # (Line 111) }
    EUDEndIf()
    # (Line 113) function StructSetMemoryXEPD(unitEPD ,StructOffset ,value ,modifier: TrgModifier) {

@EUDTypedFunc([None, None, None, TrgModifier])
def StructSetMemoryXEPD(unitEPD, StructOffset, value, modifier):
    # (Line 114) var Mask;
    Mask = EUDVariable()
    # (Line 115) switch(StructOffset % 4) {
    EUDSwitch(StructOffset % 4)
    # (Line 116) case 0:
    _t1 = EUDSwitchCase()
    # (Line 117) SetMemoryEPD(unitEPD + StructOffset / 4, modifier, value);
    if _t1(0):
        # (Line 118) return;
        DoActions(SetMemoryEPD(unitEPD + StructOffset // 4, modifier, value))
        EUDReturn()
        # (Line 119) break;
        EUDBreak()
        # (Line 120) case 1:
    _t2 = EUDSwitchCase()
    # (Line 121) Mask = 0xFF00;
    if _t2(1):
        Mask << (0xFF00)
        # (Line 122) value = value*256;
        value << (value * 256)
        # (Line 123) break;
        EUDBreak()
        # (Line 124) case 2:
    _t3 = EUDSwitchCase()
    # (Line 125) Mask = 0xFF0000;
    if _t3(2):
        Mask << (0xFF0000)
        # (Line 126) value = value*65536;
        value << (value * 65536)
        # (Line 127) break;
        EUDBreak()
        # (Line 128) case 3:
    _t4 = EUDSwitchCase()
    # (Line 129) Mask = 0xFF000000;
    if _t4(3):
        Mask << (0xFF000000)
        # (Line 130) value = value*16777216;
        value << (value * 16777216)
        # (Line 131) break;
        EUDBreak()
        # (Line 132) }
    # (Line 133) SetMemoryXEPD(unitEPD + StructOffset / 4, modifier, value, Mask);
    EUDEndSwitch()
    # (Line 134) }
    DoActions(SetMemoryXEPD(unitEPD + StructOffset // 4, modifier, value, Mask))
    # (Line 136) function CloseWindow() {

@EUDFunc
def CloseWindow():
    # (Line 139) }
    # (Line 141) function clickedLine(line) {
    pass

@EUDFunc
def f_clickedLine(line):
    # (Line 142) const cp = getcurpl();
    cp = f_getcurpl()
    # (Line 143) if(line == 0) {
    if EUDIf()(line == 0):
        # (Line 144) if(v.mouseY[cp] >= 112 && v.mouseY[cp] <= 126) return true;
        if EUDIf()(EUDSCAnd()(v.mouseY[cp] >= 112)(v.mouseY[cp] <= 126)()):
            EUDReturn(True)
            # (Line 145) else return false;
        if EUDElse()():
            EUDReturn(False)
            # (Line 146) }
        EUDEndIf()
        # (Line 147) else if(line == 1) {
    if EUDElseIf()(line == 1):
        # (Line 148) if(v.mouseY[cp] >= 128 && v.mouseY[cp] <= 142) return true;
        if EUDIf()(EUDSCAnd()(v.mouseY[cp] >= 128)(v.mouseY[cp] <= 142)()):
            EUDReturn(True)
            # (Line 149) else return false;
        if EUDElse()():
            EUDReturn(False)
            # (Line 150) }
        EUDEndIf()
        # (Line 151) else if(line == 2) {
    if EUDElseIf()(line == 2):
        # (Line 152) if(v.mouseY[cp] >= 144 && v.mouseY[cp] <= 158) return true;
        if EUDIf()(EUDSCAnd()(v.mouseY[cp] >= 144)(v.mouseY[cp] <= 158)()):
            EUDReturn(True)
            # (Line 153) else return false;
        if EUDElse()():
            EUDReturn(False)
            # (Line 154) }
        EUDEndIf()
        # (Line 155) else if(line == 3) {
    if EUDElseIf()(line == 3):
        # (Line 156) if(v.mouseY[cp] >= 160 && v.mouseY[cp] <= 174) return true;
        if EUDIf()(EUDSCAnd()(v.mouseY[cp] >= 160)(v.mouseY[cp] <= 174)()):
            EUDReturn(True)
            # (Line 157) else return false;
        if EUDElse()():
            EUDReturn(False)
            # (Line 158) }
        EUDEndIf()
        # (Line 159) else if(line == 4) {
    if EUDElseIf()(line == 4):
        # (Line 160) if(v.mouseY[cp] >= 176 && v.mouseY[cp] <= 190) return true;
        if EUDIf()(EUDSCAnd()(v.mouseY[cp] >= 176)(v.mouseY[cp] <= 190)()):
            EUDReturn(True)
            # (Line 161) else return false;
        if EUDElse()():
            EUDReturn(False)
            # (Line 162) }
        EUDEndIf()
        # (Line 163) else if(line == 5) {
    if EUDElseIf()(line == 5):
        # (Line 164) if(v.mouseY[cp] >= 192 && v.mouseY[cp] <= 206) return true;
        if EUDIf()(EUDSCAnd()(v.mouseY[cp] >= 192)(v.mouseY[cp] <= 206)()):
            EUDReturn(True)
            # (Line 165) else return false;
        if EUDElse()():
            EUDReturn(False)
            # (Line 166) }
        EUDEndIf()
        # (Line 167) else if(line == 6) {
    if EUDElseIf()(line == 6):
        # (Line 168) if(v.mouseY[cp] >= 208 && v.mouseY[cp] <= 222) return true;
        if EUDIf()(EUDSCAnd()(v.mouseY[cp] >= 208)(v.mouseY[cp] <= 222)()):
            EUDReturn(True)
            # (Line 169) else return false;
        if EUDElse()():
            EUDReturn(False)
            # (Line 170) }
        EUDEndIf()
        # (Line 171) else if(line == 7) {
    if EUDElseIf()(line == 7):
        # (Line 172) if(v.mouseY[cp] >= 224 && v.mouseY[cp] <= 238) return true;
        if EUDIf()(EUDSCAnd()(v.mouseY[cp] >= 224)(v.mouseY[cp] <= 238)()):
            EUDReturn(True)
            # (Line 173) else return false;
        if EUDElse()():
            EUDReturn(False)
            # (Line 174) }
        EUDEndIf()
        # (Line 175) else if(line == 8) {
    if EUDElseIf()(line == 8):
        # (Line 176) if(v.mouseY[cp] >= 240 && v.mouseY[cp] <= 254) return true;
        if EUDIf()(EUDSCAnd()(v.mouseY[cp] >= 240)(v.mouseY[cp] <= 254)()):
            EUDReturn(True)
            # (Line 177) else return false;
        if EUDElse()():
            EUDReturn(False)
            # (Line 178) }
        EUDEndIf()
        # (Line 179) else if(line == 9) {
    if EUDElseIf()(line == 9):
        # (Line 180) if(v.mouseY[cp] >= 256 && v.mouseY[cp] <= 270) return true;
        if EUDIf()(EUDSCAnd()(v.mouseY[cp] >= 256)(v.mouseY[cp] <= 270)()):
            EUDReturn(True)
            # (Line 181) else return false;
        if EUDElse()():
            EUDReturn(False)
            # (Line 182) }
        EUDEndIf()
        # (Line 183) }
    EUDEndIf()
    # (Line 185) function UDPBan() {

@EUDFunc
def UDPBan():
    # (Line 186) const a = 0x6D0F48; //방이름
    a = 0x6D0F48
    # (Line 187) const b = 0x6D0F78; //방장닉
    b = 0x6D0F78
    # (Line 188) if(strcmp(a, b) == 0) {
    if EUDIf()(f_strcmp(a, b) == 0):
        # (Line 189) for(var i=0; i<4; i++) {
        i = EUDVariable()
        i << (0)
        if EUDWhile()(i >= 4, neg=True):
            def _t3():
                i.__iadd__(1)
            # (Line 190) setcurpl(i);
            f_setcurpl(i)
            # (Line 191) v.s.print("\x13\x1EUDP에서 플레이는 금지하고 있습니다."); Defeat();
            v.s.print("\x13\x1EUDP에서 플레이는 금지하고 있습니다.")
            # (Line 192) }
            DoActions(Defeat())
            # (Line 193) }
            EUDSetContinuePoint()
            _t3()
        EUDEndWhile()
        # (Line 194) }
    EUDEndIf()
    # (Line 196) function SpeedBan() {

@EUDFunc
def SpeedBan():
    # (Line 197) const a = dwread_epd_safe(EPD(0x51CE84));
    a = f_dwread_epd_safe(EPD(0x51CE84))
    # (Line 198) const b = dwread_epd_safe(EPD(0x51CE88));
    b = f_dwread_epd_safe(EPD(0x51CE88))
    # (Line 199) if(a == 1000){if(b == 1000) return;}		    //턴레이트24
    if EUDIf()(a == 1000):
        if EUDIf()(b == 1000):
            EUDReturn()
        EUDEndIf()
        # (Line 200) else if(a == 1042) { if(b == 1190) return; }	//턴레이트20
    if EUDElseIf()(a == 1042):
        if EUDIf()(b == 1190):
            EUDReturn()
        EUDEndIf()
        # (Line 201) else if(a == 1302) { if(b == 1488) return; }	//턴레이트16
    if EUDElseIf()(a == 1302):
        if EUDIf()(b == 1488):
            EUDReturn()
        EUDEndIf()
        # (Line 202) else if(a == 1488) { if(b == 1701) return; }	//턴레이트14
    if EUDElseIf()(a == 1488):
        if EUDIf()(b == 1701):
            EUDReturn()
        EUDEndIf()
        # (Line 203) else if(a == 1736) { if(b == 1984) return; }	//턴레이트12
    if EUDElseIf()(a == 1736):
        if EUDIf()(b == 1984):
            EUDReturn()
        EUDEndIf()
        # (Line 204) else if(a == 2083) { if(b == 2381) return; }	//턴레이트10
    if EUDElseIf()(a == 2083):
        if EUDIf()(b == 2381):
            EUDReturn()
        EUDEndIf()
        # (Line 205) else if(a == 2604) { if(b == 2976) return; }	//턴레이트8
    if EUDElseIf()(a == 2604):
        if EUDIf()(b == 2976):
            EUDReturn()
        EUDEndIf()
        # (Line 206) else{
    if EUDElse()():
        # (Line 207) foreach(cp : EUDLoopPlayer('Human', None, None)) {
        for cp in EUDLoopPlayer('Human', None, None):
            # (Line 208) setcurpl(cp); v.s.print("\x13\x1E배속 플레이는 금지하고 있습니다.");
            f_setcurpl(cp)
            v.s.print("\x13\x1E배속 플레이는 금지하고 있습니다.")
            # (Line 209) }
            # (Line 210) dwread(0);

        f_dwread(0)
        # (Line 211) }
        # (Line 212) }
    EUDEndIf()
    # (Line 214) function GetMousePos() {

@EUDFunc
def GetMousePos():
    # (Line 215) const cp = getcurpl();
    cp = f_getcurpl()
    # (Line 216) v._mouseX[cp] = dwread_epd(EPD(0x6CDDC4));
    _ARRW(v._mouseX, cp) << (f_dwread_epd(EPD(0x6CDDC4)))
    # (Line 217) v._mouseY[cp] = dwread_epd(EPD(0x6CDDC8));
    _ARRW(v._mouseY, cp) << (f_dwread_epd(EPD(0x6CDDC8)))
    # (Line 218) if(v.mouseClick[cp] == 1) {
    if EUDIf()(v.mouseClick[cp] == 1):
        # (Line 219) v.mouseX[cp] = dwread_epd(cp + 504);
        _ARRW(v.mouseX, cp) << (f_dwread_epd(cp + 504))
        # (Line 220) v.mouseY[cp] = dwread_epd(cp + 684);
        _ARRW(v.mouseY, cp) << (f_dwread_epd(cp + 684))
        # (Line 221) }
        # (Line 222) }
    EUDEndIf()
    # (Line 224) function SetName() {

@EUDFunc
def SetName():
    # (Line 225) const cp = getcurpl();
    cp = f_getcurpl()
    # (Line 227) settbl2(v.playerUnit[cp] + 1, 0, "\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D");
    f_settbl2(v.playerUnit[cp] + 1, 0, "\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D\x0D")
    # (Line 228) settbl2(v.playerUnit[cp] + 1, 0, "\x04", PName(cp));
    f_settbl2(v.playerUnit[cp] + 1, 0, "\x04", PName(cp))
    # (Line 229) }
    # (Line 252) function Heal() {

@EUDFunc
def Heal():
    # (Line 253) const cp = getcurpl();
    cp = f_getcurpl()
    # (Line 254) ModifyUnitHitPoints(1, v.playerUnit[cp], cp, "Anywhere", 100);
    # (Line 255) }
    DoActions(ModifyUnitHitPoints(1, v.playerUnit[cp], cp, "Anywhere", 100))
    # (Line 257) function ButtonRefresh() {

@EUDFunc
def ButtonRefresh():
    # (Line 258) const btntemp1 = wread_epd(EPD(0x6615AA), 2);
    btntemp1 = f_wread_epd(EPD(0x6615AA), 2)
    # (Line 259) SetMemoryX(0x6615AA, SetTo, 0x20000, 0xFFFF0000);
    # (Line 260) const btntemp2, btntemp3 = cunitepdread_epd(EPD(0x628438));
    DoActions(SetMemoryX(0x6615AA, SetTo, 0x20000, 0xFFFF0000))
    btntemp2, btntemp3 = List2Assignable([f_cunitepdread_epd(EPD(0x628438))])
    # (Line 261) CreateUnit(1, 73, 64, 7);
    # (Line 262) if(!Memory(0x628438, Exactly, btntemp2)) {
    DoActions(CreateUnit(1, 73, 64, 7))
    if EUDIf()(Memory(0x628438, Exactly, btntemp2), neg=True):
        # (Line 263) wwrite_epd(btntemp3 + 0x110/4, 0, 1);
        f_wwrite_epd(btntemp3 + 0x110 // 4, 0, 1)
        # (Line 264) wwrite_epd(EPD(0x6615AA), 2, btntemp1);
        f_wwrite_epd(EPD(0x6615AA), 2, btntemp1)
        # (Line 265) };
    EUDEndIf()
    # (Line 266) }
    # (Line 268) function SetPColor(pnum, color) {

@EUDFunc
def SetPColor(pnum, color):
    # (Line 269) const pcolor_dst = 0x581D76 + 8 * pnum;
    pcolor_dst = 0x581D76 + 8 * pnum
    # (Line 270) const mcolor_dst = 0x581DD6 + pnum;
    mcolor_dst = 0x581DD6 + pnum
    # (Line 271) bwrite(pcolor_dst, color);
    f_bwrite(pcolor_dst, color)
    # (Line 272) bwrite(mcolor_dst, color);
    f_bwrite(mcolor_dst, color)
    # (Line 273) }
    # (Line 275) function SetUnitColorEPD(UnitEPD, Color) {

@EUDFunc
def SetUnitColorEPD(UnitEPD, Color):
    # (Line 276) var spriteEPD = epdread_epd(UnitEPD + 0x00C / 4);
    spriteEPD = EUDVariable()
    spriteEPD << (f_epdread_epd(UnitEPD + 0x00C // 4))
    # (Line 277) bwrite_epd(spriteEPD + 0x0A/4, 0x0A%4, Color);
    f_bwrite_epd(spriteEPD + 0x0A // 4, 0x0A % 4, Color)
    # (Line 278) }
    # (Line 280) function SetHP(val, modify:TrgModifier) {

@EUDTypedFunc([None, TrgModifier])
def SetHP(val, modify):
    # (Line 281) const cp = getcurpl();
    cp = f_getcurpl()
    # (Line 282) SetMemoryEPD(user.character[cp] + 0x8 / 4, modify, val * 256);
    # (Line 283) if(MemoryEPD(user.character[cp] + 0x8 / 4, AtLeast, user.maxHP[cp] * 256)) {
    DoActions(SetMemoryEPD(user.character[cp] + 0x8 // 4, modify, val * 256))
    if EUDIf()(MemoryEPD(user.character[cp] + 0x8 // 4, AtLeast, user.maxHP[cp] * 256)):
        # (Line 284) SetMemoryEPD(user.character[cp] + 0x8 / 4, SetTo, user.maxHP[cp] * 256);
        # (Line 285) }
        DoActions(SetMemoryEPD(user.character[cp] + 0x8 // 4, SetTo, user.maxHP[cp] * 256))
        # (Line 286) }
    EUDEndIf()
    # (Line 288) function SetMaxHP() {

@EUDFunc
def SetMaxHP():
    # (Line 289) const cp = getcurpl();
    cp = f_getcurpl()
    # (Line 290) SetMemoryEPD(EPD(0x662350) + v.unitNum[cp] * 4, SetTo, user.maxHP[cp] * 256);
    # (Line 291) }
    DoActions(SetMemoryEPD(EPD(0x662350) + v.unitNum[cp] * 4, SetTo, user.maxHP[cp] * 256))
    # (Line 293) function SetAlly() {

@EUDFunc
def SetAlly():
    # (Line 294) foreach (cp : EUDLoopPlayer()) {
    for cp in EUDLoopPlayer():
        # (Line 295) setcurpl(cp);
        f_setcurpl(cp)
        # (Line 296) SetAllianceStatus(P7, Ally);
        # (Line 297) }
        DoActions(SetAllianceStatus(P7, Ally))
        # (Line 298) setcurpl(6);

    f_setcurpl(6)
    # (Line 299) SetAllianceStatus(Force1, Ally);
    # (Line 300) }
    DoActions(SetAllianceStatus(Force1, Ally))
    # (Line 302) function AllyCheck() {

@EUDFunc
def AllyCheck():
    # (Line 303) if(!MemoryEPD(EPD(0x58D634), Exactly, 16843009) || !MemoryEPD(EPD(0x58D638), Exactly, 65793)) {
    if EUDIf()(EUDSCOr()(MemoryEPD(EPD(0x58D634), Exactly, 16843009), neg=True)(MemoryEPD(EPD(0x58D638), Exactly, 65793), neg=True)()):
        # (Line 304) setcurpl(0);
        f_setcurpl(0)
        # (Line 305) SetAllianceStatus(Force1, Ally);
        # (Line 306) }
        DoActions(SetAllianceStatus(Force1, Ally))
        # (Line 307) if(!MemoryEPD(EPD(0x58D640), Exactly, 16843009) || !MemoryEPD(EPD(0x58D644), Exactly, 65793)) {
    EUDEndIf()
    if EUDIf()(EUDSCOr()(MemoryEPD(EPD(0x58D640), Exactly, 16843009), neg=True)(MemoryEPD(EPD(0x58D644), Exactly, 65793), neg=True)()):
        # (Line 308) setcurpl(1);
        f_setcurpl(1)
        # (Line 309) SetAllianceStatus(Force1, Ally);
        # (Line 310) }
        DoActions(SetAllianceStatus(Force1, Ally))
        # (Line 311) if(!MemoryEPD(EPD(0x58D64C), Exactly, 16843009) || !MemoryEPD(EPD(0x58D650), Exactly, 65793)) {
    EUDEndIf()
    if EUDIf()(EUDSCOr()(MemoryEPD(EPD(0x58D64C), Exactly, 16843009), neg=True)(MemoryEPD(EPD(0x58D650), Exactly, 65793), neg=True)()):
        # (Line 312) setcurpl(2);
        f_setcurpl(2)
        # (Line 313) SetAllianceStatus(Force1, Ally);
        # (Line 314) }
        DoActions(SetAllianceStatus(Force1, Ally))
        # (Line 315) if(!MemoryEPD(EPD(0x58D658), Exactly, 16843009) || !MemoryEPD(EPD(0x58D65C), Exactly, 65793)) {
    EUDEndIf()
    if EUDIf()(EUDSCOr()(MemoryEPD(EPD(0x58D658), Exactly, 16843009), neg=True)(MemoryEPD(EPD(0x58D65C), Exactly, 65793), neg=True)()):
        # (Line 316) setcurpl(3);
        f_setcurpl(3)
        # (Line 317) SetAllianceStatus(Force1, Ally);
        # (Line 318) }
        DoActions(SetAllianceStatus(Force1, Ally))
        # (Line 319) if(!MemoryEPD(EPD(0x58D664), Exactly, 16843009) || !MemoryEPD(EPD(0x58D668), Exactly, 65793)) {
    EUDEndIf()
    if EUDIf()(EUDSCOr()(MemoryEPD(EPD(0x58D664), Exactly, 16843009), neg=True)(MemoryEPD(EPD(0x58D668), Exactly, 65793), neg=True)()):
        # (Line 320) setcurpl(4);
        f_setcurpl(4)
        # (Line 321) SetAllianceStatus(Force1, Ally);
        # (Line 322) }
        DoActions(SetAllianceStatus(Force1, Ally))
        # (Line 323) if(!MemoryEPD(EPD(0x58D670), Exactly, 16843009) || !MemoryEPD(EPD(0x58D674), Exactly, 65793)) {
    EUDEndIf()
    if EUDIf()(EUDSCOr()(MemoryEPD(EPD(0x58D670), Exactly, 16843009), neg=True)(MemoryEPD(EPD(0x58D674), Exactly, 65793), neg=True)()):
        # (Line 324) setcurpl(5);
        f_setcurpl(5)
        # (Line 325) SetAllianceStatus(Force1, Ally);
        # (Line 326) }
        DoActions(SetAllianceStatus(Force1, Ally))
        # (Line 327) }
    EUDEndIf()
    # (Line 329) function RegisterMSQC() {

@EUDFunc
def RegisterMSQC():
    # (Line 330) EUDRegisterObjectToNamespace("mouseClick", v.mouseClick);
    EUDRegisterObjectToNamespace("mouseClick", v.mouseClick)
    # (Line 331) EUDRegisterObjectToNamespace("KeyC", v.KeyC);
    EUDRegisterObjectToNamespace("KeyC", v.KeyC)
    # (Line 332) EUDRegisterObjectToNamespace("KeyI", v.KeyI);
    EUDRegisterObjectToNamespace("KeyI", v.KeyI)
    # (Line 333) EUDRegisterObjectToNamespace("KeyD", v.KeyD);
    EUDRegisterObjectToNamespace("KeyD", v.KeyD)
    # (Line 334) EUDRegisterObjectToNamespace("KeyF", v.KeyF);
    EUDRegisterObjectToNamespace("KeyF", v.KeyF)
    # (Line 335) EUDRegisterObjectToNamespace("KeyU", v.KeyU);
    EUDRegisterObjectToNamespace("KeyU", v.KeyU)
    # (Line 336) EUDRegisterObjectToNamespace("KeyALT", v.KeyALT);
    EUDRegisterObjectToNamespace("KeyALT", v.KeyALT)
    # (Line 337) EUDRegisterObjectToNamespace("screen", v.screen);
    EUDRegisterObjectToNamespace("screen", v.screen)
    # (Line 338) EUDRegisterObjectToNamespace("cheat", v.cheat);
    EUDRegisterObjectToNamespace("cheat", v.cheat)
    # (Line 339) }
    # (Line 341) function SinglePlayCheck() {

@EUDFunc
def SinglePlayCheck():
    # (Line 342) if(Memory(0x57F0B4, Exactly, 0)) {
    if EUDIf()(Memory(0x57F0B4, Exactly, 0)):
        # (Line 343) SetVariables(v.singlePlay, 1);
        SetVariables(v.singlePlay, 1)
        # (Line 344) v.s.print("\x07[System.eps] \x04싱글플레이입니다");
        v.s.print("\x07[System.eps] \x04싱글플레이입니다")
        # (Line 345) }
        # (Line 346) else {
    if EUDElse()():
        # (Line 347) SetVariables(v.singlePlay, 0);
        SetVariables(v.singlePlay, 0)
        # (Line 348) v.s.print("\x07[System.eps] \x04싱글플레이가 아닙니다");
        v.s.print("\x07[System.eps] \x04싱글플레이가 아닙니다")
        # (Line 349) }
        # (Line 350) }
    EUDEndIf()