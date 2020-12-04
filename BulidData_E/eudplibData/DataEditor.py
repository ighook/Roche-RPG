from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x6644F8, Add, 1024),# units:Graphics  index:1    from 74 To 78
        SetMemory(0x664508, Add, 1),# units:Graphics  index:16    from 77 To 78
        SetMemory(0x664558, Add, 67108864),# units:Graphics  index:99    from 74 To 78
        SetMemory(0x66455C, Add, 4),# units:Graphics  index:100    from 74 To 78
        SetMemory(0x6647B0, Add, 0),# units:Shield Enable  index:0    from 0 To 0
        SetMemory(0x662354, Add, -1280),# units:Hit Points  index:1    from 11520 To 10240
        SetMemory(0x662390, Add, -53760),# units:Hit Points  index:16    from 64000 To 10240
        SetMemory(0x6623A0, Add, -40960),# units:Hit Points  index:20    from 51200 To 10240
        SetMemory(0x6624DC, Add, -40960),# units:Hit Points  index:99    from 51200 To 10240
        SetMemory(0x6624E0, Add, -53760),# units:Hit Points  index:100    from 64000 To 10240
        SetMemory(0x663DD0, Add, -1),# units:Rank/Sublabel  index:0    from 2 To 1
        SetMemory(0x663DD0, Add, -768),# units:Rank/Sublabel  index:1    from 5 To 2
        SetMemory(0x663DE0, Add, -15),# units:Rank/Sublabel  index:16    from 18 To 3
        SetMemory(0x663DE4, Add, -16),# units:Rank/Sublabel  index:20    from 17 To 1
        SetMemory(0x663E30, Add, -285212672),# units:Rank/Sublabel  index:99    from 18 To 1
        SetMemory(0x663E34, Add, -21),# units:Rank/Sublabel  index:100    from 22 To 1
        SetMemory(0x6636B8, Add, -256),# units:Ground Weapon  index:1    from 2 To 1
        SetMemory(0x6636C8, Add, -1),# units:Ground Weapon  index:16    from 3 To 2
        SetMemory(0x6636CC, Add, 2),# units:Ground Weapon  index:20    from 1 To 3
        SetMemory(0x663718, Add, -1811939328),# units:Ground Weapon  index:99    from 112 To 4
        SetMemory(0x66371C, Add, -111),# units:Ground Weapon  index:100    from 116 To 5
        SetMemory(0x6616E0, Add, -256),# units:Air Weapon  index:1    from 2 To 1
        SetMemory(0x6616F0, Add, -1),# units:Air Weapon  index:16    from 3 To 2
        SetMemory(0x6616F4, Add, 2),# units:Air Weapon  index:20    from 1 To 3
        SetMemory(0x661740, Add, -1811939328),# units:Air Weapon  index:99    from 112 To 4
        SetMemory(0x661744, Add, -111),# units:Air Weapon  index:100    from 116 To 5
        SetMemory(0x660188, Add, -3),# units:AI Internal  index:16    from 3 To 0
        SetMemory(0x66018C, Add, -3),# units:AI Internal  index:20    from 3 To 0
        SetMemory(0x6601D8, Add, -50331648),# units:AI Internal  index:99    from 3 To 0
        SetMemory(0x6601DC, Add, -3),# units:AI Internal  index:100    from 3 To 0
        SetMemory(0x664084, Add, -2097664),# units:Special Ability Flags  index:1    from 404816384 To 402718720
        SetMemory(0x6640C0, Add, -2097728),# units:Special Ability Flags  index:16    from 404816448 To 402718720
        SetMemory(0x6640D0, Add, -64),# units:Special Ability Flags  index:20    from 402718784 To 402718720
        SetMemory(0x66420C, Add, -2097728),# units:Special Ability Flags  index:99    from 404816448 To 402718720
        SetMemory(0x664210, Add, -2097728),# units:Special Ability Flags  index:100    from 404816448 To 402718720
        SetMemory(0x662DB8, Add, -768),# units:Target Acquisition Range  index:1    from 7 To 4
        SetMemory(0x662DC8, Add, -2),# units:Target Acquisition Range  index:16    from 6 To 4
        SetMemory(0x662DCC, Add, -1),# units:Target Acquisition Range  index:20    from 5 To 4
        SetMemory(0x662E18, Add, -33554432),# units:Target Acquisition Range  index:99    from 6 To 4
        SetMemory(0x662E1C, Add, -2),# units:Target Acquisition Range  index:100    from 6 To 4
        SetMemory(0x663238, Add, -512),# units:Sight Range  index:1    from 9 To 7
        SetMemory(0x663248, Add, -4),# units:Sight Range  index:16    from 11 To 7
        SetMemory(0x663298, Add, -50331648),# units:Sight Range  index:99    from 10 To 7
        SetMemory(0x66329C, Add, -4),# units:Sight Range  index:100    from 11 To 7
        SetMemory(0x6635D0, Add, 256),# units:Armor Upgrade  index:1    from 0 To 1
        SetMemory(0x6635DC, Add, 1006632960),# units:Armor Upgrade  index:15    from 0 To 60
        SetMemory(0x6635E0, Add, 2),# units:Armor Upgrade  index:16    from 0 To 2
        SetMemory(0x6635E4, Add, 3),# units:Armor Upgrade  index:20    from 0 To 3
        SetMemory(0x663630, Add, 67108864),# units:Armor Upgrade  index:99    from 0 To 4
        SetMemory(0x663634, Add, 5),# units:Armor Upgrade  index:100    from 0 To 5
        SetMemory(0x65FED8, Add, -3),# units:Armor  index:16    from 3 To 0
        SetMemory(0x65FEDC, Add, -3),# units:Armor  index:20    from 3 To 0
        SetMemory(0x65FF28, Add, -33554432),# units:Armor  index:99    from 2 To 0
        SetMemory(0x65FF2C, Add, -3),# units:Armor  index:100    from 3 To 0
        SetMemory(0x661FC0, Add, -275),# units:Ready Sound  index:0    from 275 To 0
        SetMemory(0x661FC0, Add, -14745600),# units:Ready Sound  index:1    from 225 To 0
        SetMemory(0x65FFB0, Add, -287),# units:What Sound Start  index:0    from 287 To 0
        SetMemory(0x65FFB0, Add, -15073280),# units:What Sound Start  index:1    from 230 To 0
        SetMemory(0x65FFD0, Add, -462),# units:What Sound Start  index:16    from 462 To 0
        SetMemory(0x65FFD8, Add, -411),# units:What Sound Start  index:20    from 411 To 0
        SetMemory(0x660074, Add, -64815104),# units:What Sound Start  index:99    from 989 To 0
        SetMemory(0x660078, Add, -230),# units:What Sound Start  index:100    from 230 To 0
        SetMemory(0x662BF0, Add, -290),# units:What Sound End  index:0    from 290 To 0
        SetMemory(0x662BF0, Add, -15269888),# units:What Sound End  index:1    from 233 To 0
        SetMemory(0x662C10, Add, -465),# units:What Sound End  index:16    from 465 To 0
        SetMemory(0x662C18, Add, -414),# units:What Sound End  index:20    from 414 To 0
        SetMemory(0x662CB4, Add, -65011712),# units:What Sound End  index:99    from 992 To 0
        SetMemory(0x662CB8, Add, -233),# units:What Sound End  index:100    from 233 To 0
        SetMemory(0x663B38, Add, -280),# units:Piss Sound Start  index:0    from 280 To 0
        SetMemory(0x663B38, Add, -14811136),# units:Piss Sound Start  index:1    from 226 To 0
        SetMemory(0x663B58, Add, -457),# units:Piss Sound Start  index:16    from 457 To 0
        SetMemory(0x663B60, Add, -407),# units:Piss Sound Start  index:20    from 407 To 0
        SetMemory(0x663BFC, Add, -64225280),# units:Piss Sound Start  index:99    from 980 To 0
        SetMemory(0x663C00, Add, -226),# units:Piss Sound Start  index:100    from 226 To 0
        SetMemory(0x661EE8, Add, -286),# units:Piss Sound End  index:0    from 286 To 0
        SetMemory(0x661EE8, Add, -15007744),# units:Piss Sound End  index:1    from 229 To 0
        SetMemory(0x661F08, Add, -461),# units:Piss Sound End  index:16    from 461 To 0
        SetMemory(0x661F10, Add, -410),# units:Piss Sound End  index:20    from 410 To 0
        SetMemory(0x661FAC, Add, -64749568),# units:Piss Sound End  index:99    from 988 To 0
        SetMemory(0x661FB0, Add, -229),# units:Piss Sound End  index:100    from 229 To 0
        SetMemory(0x663C10, Add, -291),# units:Yes Sound Start  index:0    from 291 To 0
        SetMemory(0x663C10, Add, -15335424),# units:Yes Sound Start  index:1    from 234 To 0
        SetMemory(0x663C30, Add, -466),# units:Yes Sound Start  index:16    from 466 To 0
        SetMemory(0x663C38, Add, -415),# units:Yes Sound Start  index:20    from 415 To 0
        SetMemory(0x663CD4, Add, -65077248),# units:Yes Sound Start  index:99    from 993 To 0
        SetMemory(0x663CD8, Add, -234),# units:Yes Sound Start  index:100    from 234 To 0
        SetMemory(0x661440, Add, -294),# units:Yes Sound End  index:0    from 294 To 0
        SetMemory(0x661440, Add, -15532032),# units:Yes Sound End  index:1    from 237 To 0
        SetMemory(0x661460, Add, -469),# units:Yes Sound End  index:16    from 469 To 0
        SetMemory(0x661468, Add, -418),# units:Yes Sound End  index:20    from 418 To 0
        SetMemory(0x661504, Add, -65273856),# units:Yes Sound End  index:99    from 996 To 0
        SetMemory(0x661508, Add, -237),# units:Yes Sound End  index:100    from 237 To 0
        SetMemory(0x662864, Add, 2),# units:StarEdit Placement Box Width  index:1    from 15 To 17
        SetMemory(0x6628A0, Add, 2),# units:StarEdit Placement Box Width  index:16    from 15 To 17
        SetMemory(0x6628B0, Add, -1),# units:StarEdit Placement Box Width  index:20    from 18 To 17
        SetMemory(0x6629EC, Add, 2),# units:StarEdit Placement Box Width  index:99    from 15 To 17
        SetMemory(0x6629F0, Add, 2),# units:StarEdit Placement Box Width  index:100    from 15 To 17
        SetMemory(0x662864, Add, -131072),# units:StarEdit Placement Box Height  index:1    from 22 To 20
        SetMemory(0x6628A0, Add, -131072),# units:StarEdit Placement Box Height  index:16    from 22 To 20
        SetMemory(0x6628B0, Add, -131072),# units:StarEdit Placement Box Height  index:20    from 22 To 20
        SetMemory(0x6629EC, Add, -131072),# units:StarEdit Placement Box Height  index:99    from 22 To 20
        SetMemory(0x6629F0, Add, -131072),# units:StarEdit Placement Box Height  index:100    from 22 To 20
        SetMemory(0x6617D0, Add, 1),# units:Unit Size Left  index:1    from 7 To 8
        SetMemory(0x661848, Add, 1),# units:Unit Size Left  index:16    from 7 To 8
        SetMemory(0x661AE0, Add, 1),# units:Unit Size Left  index:99    from 7 To 8
        SetMemory(0x661AE8, Add, 1),# units:Unit Size Left  index:100    from 7 To 8
        SetMemory(0x6617D0, Add, -65536),# units:Unit Size Up  index:1    from 10 To 9
        SetMemory(0x661848, Add, -65536),# units:Unit Size Up  index:16    from 10 To 9
        SetMemory(0x661AE0, Add, -65536),# units:Unit Size Up  index:99    from 10 To 9
        SetMemory(0x661AE8, Add, -65536),# units:Unit Size Up  index:100    from 10 To 9
        SetMemory(0x6617D4, Add, 1),# units:Unit Size Right  index:1    from 7 To 8
        SetMemory(0x66184C, Add, 1),# units:Unit Size Right  index:16    from 7 To 8
        SetMemory(0x661AE4, Add, 1),# units:Unit Size Right  index:99    from 7 To 8
        SetMemory(0x661AEC, Add, 1),# units:Unit Size Right  index:100    from 7 To 8
        SetMemory(0x6617D4, Add, -65536),# units:Unit Size Down  index:1    from 11 To 10
        SetMemory(0x66184C, Add, -65536),# units:Unit Size Down  index:16    from 11 To 10
        SetMemory(0x661AE4, Add, -65536),# units:Unit Size Down  index:99    from 11 To 10
        SetMemory(0x661AEC, Add, -65536),# units:Unit Size Down  index:100    from 11 To 10
        SetMemory(0x662F88, Add, 215),# units:Portrait  index:0    from 0 To 215
        SetMemory(0x662F88, Add, -65536),# units:Portrait  index:1    from 1 To 0
        SetMemory(0x662FA8, Add, -12),# units:Portrait  index:16    from 12 To 0
        SetMemory(0x662FB0, Add, -13),# units:Portrait  index:20    from 13 To 0
        SetMemory(0x66304C, Add, -6160384),# units:Portrait  index:99    from 94 To 0
        SetMemory(0x663050, Add, -93),# units:Portrait  index:100    from 93 To 0
        SetMemory(0x663888, Add, 1638400),# units:Mineral Cost  index:1    from 25 To 50
        SetMemory(0x66394C, Add, -9830400),# units:Mineral Cost  index:99    from 200 To 50
        SetMemory(0x663950, Add, -150),# units:Mineral Cost  index:100    from 200 To 50
        SetMemory(0x65FD00, Add, -4915200),# units:Vespene Cost  index:1    from 75 To 0
        SetMemory(0x65FD20, Add, -150),# units:Vespene Cost  index:16    from 150 To 0
        SetMemory(0x65FDC4, Add, -4915200),# units:Vespene Cost  index:99    from 75 To 0
        SetMemory(0x65FDC8, Add, -75),# units:Vespene Cost  index:100    from 75 To 0
        SetMemory(0x660428, Add, -25559040),# units:Build Time  index:1    from 750 To 360
        SetMemory(0x660448, Add, -1140),# units:Build Time  index:16    from 1500 To 360
        SetMemory(0x660450, Add, 359),# units:Build Time  index:20    from 1 To 360
        SetMemory(0x6604EC, Add, -74711040),# units:Build Time  index:99    from 1500 To 360
        SetMemory(0x6604F0, Add, -1140),# units:Build Time  index:100    from 1500 To 360
        SetMemory(0x663CE8, Add, -2),# units:Supply Required  index:0    from 2 To 0
        SetMemory(0x663CE8, Add, -512),# units:Supply Required  index:1    from 2 To 0
        SetMemory(0x663408, Add, -8192000),# units:Build Score  index:1    from 175 To 50
        SetMemory(0x663428, Add, 50),# units:Build Score  index:16    from 0 To 50
        SetMemory(0x663430, Add, 50),# units:Build Score  index:20    from 0 To 50
        SetMemory(0x6634CC, Add, 3276800),# units:Build Score  index:99    from 0 To 50
        SetMemory(0x6634D0, Add, 50),# units:Build Score  index:100    from 0 To 50
        SetMemory(0x663EB8, Add, -16384000),# units:Destroy Score  index:1    from 350 To 100
        SetMemory(0x663ED8, Add, -600),# units:Destroy Score  index:16    from 700 To 100
        SetMemory(0x663EE0, Add, -100),# units:Destroy Score  index:20    from 200 To 100
        SetMemory(0x663F7C, Add, -39321600),# units:Destroy Score  index:99    from 700 To 100
        SetMemory(0x663F80, Add, -600),# units:Destroy Score  index:100    from 700 To 100
        SetMemory(0x660738, Add, -16777216),# units:Broodwar Unit Flag  index:99    from 1 To 0
        SetMemory(0x66073C, Add, -1),# units:Broodwar Unit Flag  index:100    from 1 To 0
        SetMemory(0x661538, Add, 8),# units:Staredit Availability Flags  index:16    from 455 To 463
        SetMemory(0x661540, Add, 8),# units:Staredit Availability Flags  index:20    from 455 To 463
        SetMemory(0x6615DC, Add, -33030144),# units:Staredit Availability Flags  index:99    from 967 To 463
        SetMemory(0x6615E0, Add, -504),# units:Staredit Availability Flags  index:100    from 967 To 463
        SetMemory(0x6CA014, Add, 699),# flingy:Speed  index:71    from 1 To 700
        SetMemory(0x6CA030, Add, 749),# flingy:Speed  index:78    from 1 To 750
        SetMemory(0x6C9D04, Add, 45809664),# flingy:Acceleration  index:71    from 1 To 700
        SetMemory(0x6C9D14, Add, 749),# flingy:Acceleration  index:78    from 1 To 750
        SetMemory(0x6C9E64, Add, 1459617792),# flingy:Turn Radius  index:71    from 40 To 127
        SetMemory(0x6C9E6C, Add, 5701632),# flingy:Turn Radius  index:78    from 40 To 127
        SetMemory(0x6C989C, Add, -33554432),# flingy:Movement Control  index:71    from 2 To 0
        SetMemory(0x6C98A4, Add, -131072),# flingy:Movement Control  index:78    from 2 To 0
        SetMemory(0x669EAC, Add, 655360),# images:Draw Function  index:134    from 0 To 10
    ])

