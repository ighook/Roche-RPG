from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x6645A8, Add, 2617245696),# units:Graphics  index:179    from 43 To 199
        SetMemory(0x66137C, Add, -325),# units:Construction Animation  index:179    from 325 To 0
        SetMemory(0x6647B0, Add, 1),# units:Shield Enable  index:0    from 0 To 1
        SetMemory(0x6647B0, Add, 256),# units:Shield Enable  index:1    from 0 To 1
        SetMemory(0x6647C0, Add, 1),# units:Shield Enable  index:16    from 0 To 1
        SetMemory(0x664814, Add, 1),# units:Shield Enable  index:100    from 0 To 1
        SetMemory(0x660E00, Add, -100),# units:Shield Amount  index:0    from 100 To 0
        SetMemory(0x660E00, Add, -6553600),# units:Shield Amount  index:1    from 100 To 0
        SetMemory(0x660E20, Add, -100),# units:Shield Amount  index:16    from 100 To 0
        SetMemory(0x660EC8, Add, -100),# units:Shield Amount  index:100    from 100 To 0
        SetMemory(0x662350, Add, 20480),# units:Hit Points  index:0    from 10240 To 30720
        SetMemory(0x662354, Add, 19200),# units:Hit Points  index:1    from 11520 To 30720
        SetMemory(0x662390, Add, -33280),# units:Hit Points  index:16    from 64000 To 30720
        SetMemory(0x6624E0, Add, -33280),# units:Hit Points  index:100    from 64000 To 30720
        SetMemory(0x663200, Add, 134217728),# units:Elevation Level  index:179    from 4 To 12
        SetMemory(0x663DD0, Add, -1),# units:Rank/Sublabel  index:0    from 2 To 1
        SetMemory(0x663DD0, Add, -768),# units:Rank/Sublabel  index:1    from 5 To 2
        SetMemory(0x663DE0, Add, -15),# units:Rank/Sublabel  index:16    from 18 To 3
        SetMemory(0x663DE4, Add, -13),# units:Rank/Sublabel  index:20    from 17 To 4
        SetMemory(0x663E30, Add, -218103808),# units:Rank/Sublabel  index:99    from 18 To 5
        SetMemory(0x663E34, Add, -16),# units:Rank/Sublabel  index:100    from 22 To 6
        SetMemory(0x662268, Add, 105),# units:Human AI Idle  index:0    from 2 To 107
        SetMemory(0x662268, Add, 14080),# units:Human AI Idle  index:1    from 2 To 57
        SetMemory(0x662278, Add, 55),# units:Human AI Idle  index:16    from 2 To 57
        SetMemory(0x66227C, Add, 55),# units:Human AI Idle  index:20    from 2 To 57
        SetMemory(0x6622C8, Add, 922746880),# units:Human AI Idle  index:99    from 2 To 57
        SetMemory(0x6622CC, Add, 55),# units:Human AI Idle  index:100    from 2 To 57
        SetMemory(0x6636B8, Add, -256),# units:Ground Weapon  index:1    from 2 To 1
        SetMemory(0x6636C8, Add, -1),# units:Ground Weapon  index:16    from 3 To 2
        SetMemory(0x6636CC, Add, 2),# units:Ground Weapon  index:20    from 1 To 3
        SetMemory(0x663718, Add, -1811939328),# units:Ground Weapon  index:99    from 112 To 4
        SetMemory(0x66371C, Add, -111),# units:Ground Weapon  index:100    from 116 To 5
        SetMemory(0x6616E0, Add, 130),# units:Air Weapon  index:0    from 0 To 130
        SetMemory(0x6616E0, Add, 32768),# units:Air Weapon  index:1    from 2 To 130
        SetMemory(0x6616F0, Add, 127),# units:Air Weapon  index:16    from 3 To 130
        SetMemory(0x6616F4, Add, 129),# units:Air Weapon  index:20    from 1 To 130
        SetMemory(0x661740, Add, 301989888),# units:Air Weapon  index:99    from 112 To 130
        SetMemory(0x661744, Add, 14),# units:Air Weapon  index:100    from 116 To 130
        SetMemory(0x664080, Add, 0),# units:Special Ability Flags  index:0    from 402718720 To 402718720
        SetMemory(0x664084, Add, -2097664),# units:Special Ability Flags  index:1    from 404816384 To 402718720
        SetMemory(0x6640C0, Add, -2097728),# units:Special Ability Flags  index:16    from 404816448 To 402718720
        SetMemory(0x6640D0, Add, -64),# units:Special Ability Flags  index:20    from 402718784 To 402718720
        SetMemory(0x664114, Add, -128),# units:Special Ability Flags  index:37    from 403768448 To 403768320
        SetMemory(0x664120, Add, -128),# units:Special Ability Flags  index:40    from 402718848 To 402718720
        SetMemory(0x664124, Add, -1048712),# units:Special Ability Flags  index:41    from 403767432 To 402718720
        SetMemory(0x66420C, Add, -2097728),# units:Special Ability Flags  index:99    from 404816448 To 402718720
        SetMemory(0x664210, Add, -2097728),# units:Special Ability Flags  index:100    from 404816448 To 402718720
        SetMemory(0x664254, Add, -2),# units:Special Ability Flags  index:117    from 1140850691 To 1140850689
        SetMemory(0x66434C, Add, -62857217),# units:Special Ability Flags  index:179    from 603987969 To 541130752
        SetMemory(0x66438C, Add, 4194303),# units:Special Ability Flags  index:195    from 536870913 To 541065216
        SetMemory(0x6643F8, Add, 528545792),# units:Special Ability Flags  index:222    from 8390656 To 536936448
        SetMemory(0x662DB8, Add, 0),# units:Target Acquisition Range  index:0    from 4 To 4
        SetMemory(0x662DB8, Add, -768),# units:Target Acquisition Range  index:1    from 7 To 4
        SetMemory(0x662DC8, Add, -2),# units:Target Acquisition Range  index:16    from 6 To 4
        SetMemory(0x662DCC, Add, -1),# units:Target Acquisition Range  index:20    from 5 To 4
        SetMemory(0x662DE0, Add, 512),# units:Target Acquisition Range  index:41    from 1 To 3
        SetMemory(0x662E18, Add, -33554432),# units:Target Acquisition Range  index:99    from 6 To 4
        SetMemory(0x662E1C, Add, -2),# units:Target Acquisition Range  index:100    from 6 To 4
        SetMemory(0x663238, Add, -1),# units:Sight Range  index:0    from 7 To 6
        SetMemory(0x663238, Add, -768),# units:Sight Range  index:1    from 9 To 6
        SetMemory(0x663248, Add, -5),# units:Sight Range  index:16    from 11 To 6
        SetMemory(0x66324C, Add, -1),# units:Sight Range  index:20    from 7 To 6
        SetMemory(0x663260, Add, -768),# units:Sight Range  index:41    from 7 To 4
        SetMemory(0x663298, Add, -67108864),# units:Sight Range  index:99    from 10 To 6
        SetMemory(0x66329C, Add, -5),# units:Sight Range  index:100    from 11 To 6
        SetMemory(0x6635D0, Add, 256),# units:Armor Upgrade  index:1    from 0 To 1
        SetMemory(0x6635DC, Add, 1006632960),# units:Armor Upgrade  index:15    from 0 To 60
        SetMemory(0x6635E0, Add, 2),# units:Armor Upgrade  index:16    from 0 To 2
        SetMemory(0x6635E4, Add, 3),# units:Armor Upgrade  index:20    from 0 To 3
        SetMemory(0x663630, Add, 67108864),# units:Armor Upgrade  index:99    from 0 To 4
        SetMemory(0x663634, Add, 5),# units:Armor Upgrade  index:100    from 0 To 5
        SetMemory(0x660114, Add, -983040),# units:What Sound Start  index:179    from 15 To 0
        SetMemory(0x662D54, Add, -983040),# units:What Sound End  index:179    from 15 To 0
        SetMemory(0x66288C, Add, -48),# units:StarEdit Placement Box Width  index:11    from 49 To 1
        SetMemory(0x662B2C, Add, -63),# units:StarEdit Placement Box Width  index:179    from 64 To 1
        SetMemory(0x662B6C, Add, -32),# units:StarEdit Placement Box Width  index:195    from 96 To 64
        SetMemory(0x66288C, Add, -2424832),# units:StarEdit Placement Box Height  index:11    from 37 To 0
        SetMemory(0x662B2C, Add, -4128768),# units:StarEdit Placement Box Height  index:179    from 64 To 1
        SetMemory(0x6617D0, Add, 1),# units:Unit Size Left  index:1    from 7 To 8
        SetMemory(0x661820, Add, -23),# units:Unit Size Left  index:11    from 24 To 1
        SetMemory(0x661848, Add, 1),# units:Unit Size Left  index:16    from 7 To 8
        SetMemory(0x6618F0, Add, -1),# units:Unit Size Left  index:37    from 8 To 7
        SetMemory(0x661910, Add, -1),# units:Unit Size Left  index:41    from 11 To 10
        SetMemory(0x661AE0, Add, 1),# units:Unit Size Left  index:99    from 7 To 8
        SetMemory(0x661AE8, Add, 1),# units:Unit Size Left  index:100    from 7 To 8
        SetMemory(0x661D60, Add, -24),# units:Unit Size Left  index:179    from 32 To 8
        SetMemory(0x661DE0, Add, -47),# units:Unit Size Left  index:195    from 48 To 1
        SetMemory(0x6617D0, Add, -65536),# units:Unit Size Up  index:1    from 10 To 9
        SetMemory(0x661820, Add, -983040),# units:Unit Size Up  index:11    from 16 To 1
        SetMemory(0x661848, Add, -65536),# units:Unit Size Up  index:16    from 10 To 9
        SetMemory(0x6618F0, Add, -65536),# units:Unit Size Up  index:37    from 4 To 3
        SetMemory(0x661910, Add, -65536),# units:Unit Size Up  index:41    from 11 To 10
        SetMemory(0x661AE0, Add, -65536),# units:Unit Size Up  index:99    from 10 To 9
        SetMemory(0x661AE8, Add, -65536),# units:Unit Size Up  index:100    from 10 To 9
        SetMemory(0x661D60, Add, -1507328),# units:Unit Size Up  index:179    from 32 To 9
        SetMemory(0x661DE0, Add, -2031616),# units:Unit Size Up  index:195    from 32 To 1
        SetMemory(0x6617D4, Add, 1),# units:Unit Size Right  index:1    from 7 To 8
        SetMemory(0x661824, Add, -23),# units:Unit Size Right  index:11    from 24 To 1
        SetMemory(0x66184C, Add, 1),# units:Unit Size Right  index:16    from 7 To 8
        SetMemory(0x6618F4, Add, -1),# units:Unit Size Right  index:37    from 7 To 6
        SetMemory(0x661914, Add, -1),# units:Unit Size Right  index:41    from 11 To 10
        SetMemory(0x661AE4, Add, 1),# units:Unit Size Right  index:99    from 7 To 8
        SetMemory(0x661AEC, Add, 1),# units:Unit Size Right  index:100    from 7 To 8
        SetMemory(0x661D64, Add, -23),# units:Unit Size Right  index:179    from 31 To 8
        SetMemory(0x661DE4, Add, -46),# units:Unit Size Right  index:195    from 47 To 1
        SetMemory(0x6617CC, Add, -65536),# units:Unit Size Down  index:0    from 10 To 9
        SetMemory(0x6617D4, Add, -131072),# units:Unit Size Down  index:1    from 11 To 9
        SetMemory(0x661824, Add, -1245184),# units:Unit Size Down  index:11    from 20 To 1
        SetMemory(0x66184C, Add, -131072),# units:Unit Size Down  index:16    from 11 To 9
        SetMemory(0x66186C, Add, -65536),# units:Unit Size Down  index:20    from 10 To 9
        SetMemory(0x6618F4, Add, -65536),# units:Unit Size Down  index:37    from 11 To 10
        SetMemory(0x661914, Add, -65536),# units:Unit Size Down  index:41    from 11 To 10
        SetMemory(0x661AE4, Add, -131072),# units:Unit Size Down  index:99    from 11 To 9
        SetMemory(0x661AEC, Add, -131072),# units:Unit Size Down  index:100    from 11 To 9
        SetMemory(0x661D64, Add, -1441792),# units:Unit Size Down  index:179    from 31 To 9
        SetMemory(0x661DE4, Add, -1966080),# units:Unit Size Down  index:195    from 31 To 1
        SetMemory(0x663888, Add, -50),# units:Mineral Cost  index:0    from 50 To 0
        SetMemory(0x663888, Add, -1638400),# units:Mineral Cost  index:1    from 25 To 0
        SetMemory(0x6638A8, Add, -50),# units:Mineral Cost  index:16    from 50 To 0
        SetMemory(0x663950, Add, -200),# units:Mineral Cost  index:100    from 200 To 0
        SetMemory(0x65FD00, Add, -4915200),# units:Vespene Cost  index:1    from 75 To 0
        SetMemory(0x65FD20, Add, -150),# units:Vespene Cost  index:16    from 150 To 0
        SetMemory(0x65FDC8, Add, -75),# units:Vespene Cost  index:100    from 75 To 0
        SetMemory(0x660428, Add, -360),# units:Build Time  index:0    from 360 To 0
        SetMemory(0x660428, Add, -49152000),# units:Build Time  index:1    from 750 To 0
        SetMemory(0x660448, Add, -1500),# units:Build Time  index:16    from 1500 To 0
        SetMemory(0x6604F0, Add, -1500),# units:Build Time  index:100    from 1500 To 0
        SetMemory(0x66387C, Add, -8388608),# units:Staredit Group Flags  index:222    from 128 To 0
        SetMemory(0x663CE8, Add, -2),# units:Supply Required  index:0    from 2 To 0
        SetMemory(0x663CE8, Add, -512),# units:Supply Required  index:1    from 2 To 0
        SetMemory(0x663D10, Add, -512),# units:Supply Required  index:41    from 2 To 0
        SetMemory(0x663408, Add, -50),# units:Build Score  index:0    from 50 To 0
        SetMemory(0x663408, Add, -11468800),# units:Build Score  index:1    from 175 To 0
        SetMemory(0x663EB8, Add, -100),# units:Destroy Score  index:0    from 100 To 0
        SetMemory(0x663EB8, Add, -22937600),# units:Destroy Score  index:1    from 350 To 0
        SetMemory(0x663ED8, Add, -700),# units:Destroy Score  index:16    from 700 To 0
        SetMemory(0x663F80, Add, -700),# units:Destroy Score  index:100    from 700 To 0
        SetMemory(0x6615C0, Add, 0),# units:Staredit Availability Flags  index:85    from 452 To 452
        SetMemory(0x66167C, Add, 131072),# units:Staredit Availability Flags  index:179    from 0 To 2
        SetMemory(0x6616D4, Add, 463),# units:Staredit Availability Flags  index:222    from 0 To 463
        SetMemory(0x6579A0, Add, 1),# weapons:Target Flags  index:4    from 2 To 3
        SetMemory(0x6579A0, Add, 65536),# weapons:Target Flags  index:5    from 2 To 3
        SetMemory(0x6571D4, Add, -1),# weapons:Damage Upgrade  index:4    from 8 To 7
        SetMemory(0x6571D4, Add, -256),# weapons:Damage Upgrade  index:5    from 8 To 7
        SetMemory(0x657258, Add, 65536),# weapons:Weapon Type  index:2    from 2 To 3
        SetMemory(0x657258, Add, 16777216),# weapons:Weapon Type  index:3    from 2 To 3
        SetMemory(0x65725C, Add, 1),# weapons:Weapon Type  index:4    from 2 To 3
        SetMemory(0x65725C, Add, 256),# weapons:Weapon Type  index:5    from 2 To 3
        SetMemory(0x656994, Add, -48),# weapons:Attack Angle  index:4    from 64 To 16
        SetMemory(0x656994, Add, -12288),# weapons:Attack Angle  index:5    from 64 To 16
        SetMemory(0x657914, Add, -20),# weapons:Forward Offset  index:4    from 20 To 0
        SetMemory(0x657914, Add, -5120),# weapons:Forward Offset  index:5    from 20 To 0
        SetMemory(0x656784, Add, -1),# weapons:Icon  index:2    from 324 To 323
        SetMemory(0x656784, Add, -65536),# weapons:Icon  index:3    from 324 To 323
        SetMemory(0x656788, Add, -2),# weapons:Icon  index:4    from 325 To 323
        SetMemory(0x656788, Add, -131072),# weapons:Icon  index:5    from 325 To 323
        SetMemory(0x6CA014, Add, 599),# flingy:Speed  index:71    from 1 To 600
        SetMemory(0x6CA020, Add, 649),# flingy:Speed  index:74    from 1 To 650
        SetMemory(0x6CA02C, Add, 649),# flingy:Speed  index:77    from 1 To 650
        SetMemory(0x6CA030, Add, 649),# flingy:Speed  index:78    from 1 To 650
        SetMemory(0x6C9D04, Add, 39256064),# flingy:Acceleration  index:71    from 1 To 600
        SetMemory(0x6C9D0C, Add, 649),# flingy:Acceleration  index:74    from 1 To 650
        SetMemory(0x6C9D10, Add, 42532864),# flingy:Acceleration  index:77    from 1 To 650
        SetMemory(0x6C9D14, Add, 649),# flingy:Acceleration  index:78    from 1 To 650
        SetMemory(0x6C9DF0, Add, 723),# flingy:Acceleration  index:188    from 27 To 750
        SetMemory(0x6C9944, Add, -12226),# flingy:Halt Distance  index:5    from 12227 To 1
        SetMemory(0x6C9C20, Add, -13473),# flingy:Halt Distance  index:188    from 13474 To 1
        SetMemory(0x6C9E20, Add, 25600),# flingy:Turn Radius  index:1    from 27 To 127
        SetMemory(0x6C9E24, Add, 22272),# flingy:Turn Radius  index:5    from 40 To 127
        SetMemory(0x6C9E2C, Add, 1677721600),# flingy:Turn Radius  index:15    from 27 To 127
        SetMemory(0x6C9E64, Add, 1459617792),# flingy:Turn Radius  index:71    from 40 To 127
        SetMemory(0x6C9E68, Add, 5701632),# flingy:Turn Radius  index:74    from 40 To 127
        SetMemory(0x6C9E6C, Add, 22272),# flingy:Turn Radius  index:77    from 40 To 127
        SetMemory(0x6C9E6C, Add, 5701632),# flingy:Turn Radius  index:78    from 40 To 127
        SetMemory(0x6C9EDC, Add, 87),# flingy:Turn Radius  index:188    from 40 To 127
        SetMemory(0x6C9858, Add, -512),# flingy:Movement Control  index:1    from 2 To 0
        SetMemory(0x6C985C, Add, 0),# flingy:Movement Control  index:5    from 0 To 0
        SetMemory(0x6C9864, Add, -33554432),# flingy:Movement Control  index:15    from 2 To 0
        SetMemory(0x6C989C, Add, -33554432),# flingy:Movement Control  index:71    from 2 To 0
        SetMemory(0x6C98A0, Add, -131072),# flingy:Movement Control  index:74    from 2 To 0
        SetMemory(0x6C98A4, Add, -512),# flingy:Movement Control  index:77    from 2 To 0
        SetMemory(0x6C98A4, Add, -131072),# flingy:Movement Control  index:78    from 2 To 0
        SetMemory(0x6C9914, Add, -2),# flingy:Movement Control  index:188    from 2 To 0
        SetMemory(0x666398, Add, 204),# sprites:Image File  index:284    from 356 To 560
        SetMemory(0x66A058, Add, -2),# images:Draw Function  index:560    from 11 To 9
        SetMemory(0x66A098, Add, 9),# images:Draw Function  index:624    from 0 To 9
        SetMemory(0x66A09C, Add, 589824),# images:Draw Function  index:630    from 0 To 9
        SetMemory(0x66A0A0, Add, 589824),# images:Draw Function  index:634    from 0 To 9
        SetMemory(0x66A0A4, Add, 9),# images:Draw Function  index:636    from 0 To 9
        SetMemory(0x66A0A4, Add, 589824),# images:Draw Function  index:638    from 0 To 9
        SetMemory(0x66FB80, Add, -173),# images:Iscript ID  index:974    from 390 To 217
        SetMemory(0x655AC0, Add, -65536),# upgrades:Icon  index:1    from 293 To 292
        SetMemory(0x655AC4, Add, 1),# upgrades:Icon  index:2    from 291 To 292
        SetMemory(0x655AC4, Add, -327680),# upgrades:Icon  index:3    from 297 To 292
        SetMemory(0x655AC8, Add, -6),# upgrades:Icon  index:4    from 298 To 292
        SetMemory(0x655AC8, Add, -720896),# upgrades:Icon  index:5    from 303 To 292
    ])

