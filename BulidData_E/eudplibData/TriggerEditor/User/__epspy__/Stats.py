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

# (Line 1) import User.Info as user;
from User import Info as user
# (Line 2) import Variable as v;
import Variable as v
# (Line 3) import System as sys;
import System as sys
# (Line 5) function SetDamage() {
@EUDFunc
def SetDamage():
    # (Line 6) const cp = getcurpl();
    cp = f_getcurpl()
    # (Line 7) var increase = 0;
    increase = EUDVariable()
    increase << (0)
    # (Line 8) for(var i = 0; i < user.level[cp]; i++)
    i = EUDVariable()
    i << (0)
    if EUDWhile()(i >= user.level[cp], neg=True):
        def _t2():
            i.__iadd__(1)
        # (Line 9) increase += v.increaseDmg[user.level[cp] - 1];
        increase.__iadd__(v.increaseDmg[user.level[cp] - 1])
        # (Line 10) var amountDmg = user.physDmg[cp] + increase + user.weaponPhyDmg[cp];
        EUDSetContinuePoint()
        _t2()
    EUDEndWhile()
    amountDmg = EUDVariable()
    amountDmg << (user.physDmg[cp] + increase + user.weaponPhyDmg[cp])
    # (Line 11) wwrite(0x6564E0 + 2512 + cp * 2, amountDmg);
    f_wwrite(0x6564E0 + 2512 + cp * 2, amountDmg)
    # (Line 13) }
    # (Line 15) function SetHP() {

@EUDFunc
def SetHP():
    # (Line 16) const cp = getcurpl();
    cp = f_getcurpl()
    # (Line 17) var increase = 0;
    increase = EUDVariable()
    increase << (0)
    # (Line 18) for(var i = 0; i < user.level[cp]; i++)
    i = EUDVariable()
    i << (0)
    if EUDWhile()(i >= user.level[cp], neg=True):
        def _t2():
            i.__iadd__(1)
        # (Line 19) increase += v.increaseHP[user.level[cp] - 1];
        increase.__iadd__(v.increaseHP[user.level[cp] - 1])
        # (Line 20) var amountHP = v.defaultHP + increase;
        EUDSetContinuePoint()
        _t2()
    EUDEndWhile()
    amountHP = EUDVariable()
    amountHP << (v.defaultHP + increase)
    # (Line 21) user.maxHP[cp] = amountHP;
    _ARRW(user.maxHP, cp) << (amountHP)
    # (Line 22) sys.SetMaxHP();
    sys.SetMaxHP()
    # (Line 23) }
    # (Line 25) function RefreshExp() {

@EUDFunc
def RefreshExp():
    # (Line 26) const cp = getcurpl();
    cp = f_getcurpl()
    # (Line 27) settbl2(1303 + cp, 8, "\x0D\x0D\x0D\x0D\x0D\x0D");
    f_settbl2(1303 + cp, 8, "\x0D\x0D\x0D\x0D\x0D\x0D")
    # (Line 28) settbl2(1303 + cp, 8, user.exp[cp]);
    f_settbl2(1303 + cp, 8, user.exp[cp])
    # (Line 29) settbl2(1303 + cp, 19, "\x0D\x0D\x0D\x0D\x0D\x0D");
    f_settbl2(1303 + cp, 19, "\x0D\x0D\x0D\x0D\x0D\x0D")
    # (Line 30) settbl2(1303 + cp, 19, v.maxExp[user.level[cp]]);
    f_settbl2(1303 + cp, 19, v.maxExp[user.level[cp]])
    # (Line 31) }
    # (Line 33) function SetDefense() {

@EUDFunc
def SetDefense():
    # (Line 34) const cp = getcurpl();
    cp = f_getcurpl()
    # (Line 35) var amountDef = user.armorDefense[cp];
    amountDef = EUDVariable()
    amountDef << (user.armorDefense[cp])
    # (Line 36) bwrite(0x65FD00 + 456 + v.unitNum[cp], amountDef);
    f_bwrite(0x65FD00 + 456 + v.unitNum[cp], amountDef)
    # (Line 37) }