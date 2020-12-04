from eudplib import *
import Variable as v;

def Reg():
    print('MSQCVariable')
    EUDRegisterObjectToNamespace("screen", v.screen)
    EUDRegisterObjectToNamespace("chatAddr", v.chatAddr)
    EUDRegisterObjectToNamespace("chatPattern", v.chatPattern)
    EUDRegisterObjectToNamespace("chatLen", v.chatLen)
    
EUDOnStart(Reg)