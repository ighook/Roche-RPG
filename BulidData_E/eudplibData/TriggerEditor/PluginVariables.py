from eudplib import *
import TriggerEditor.SCArchive as sca


VChatIndex = EUDArray(8)

def Reg():
    print('... TERegVar ...')
    EUDRegisterObjectToNamespace("VChatIndex", VChatIndex)
    sca.Init()
EUDOnStart(Reg)
