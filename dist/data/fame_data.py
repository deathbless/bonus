#coding=utf-8#
#声望_数据表.csv
# 任务发布服 : publishTag
# 数据序列 : id
# 声望名 : name
# 声望类型 : type
# 是否为NPC声望 : isNpcFame
# 声望1级升2级条件类型 : lvUpCondition
# 声望初始值 : initVal
# 声望最大等级 : maxLv
# 声望升级数值区间 : lvUpNeed
# 每日获得数量限制 : dayGainLimit
# 每周获得数量限制 : weekGainLimit
# 上一周期转换比例 : weekLimitTransRatio
# 周期增加声望类型 : incType
# 周期增加数值 : incVal
# 持有数量限制 : maxVal
# 友好方 : friend
# 敌对方 : enemy
# 工资 : pay
# 专属奖励 : reward
# 废弃 : payBonus
# 工资的奖励id : payBonusNew
# 专属邮件id : rewardMail

data = {
    1:{'name': '测试货币1', 'type': 1, },
    2:{'name': '测试货币2', 'type': 1, },
    3:{'name': '师门任务声望', 'type': 2, 'initVal': 3000, 'maxLv': 6, 'lvUpNeed': {1: 3000, 2: 12000
, 3: 24000
, 4: 48000
, 5: 96000
, 6: 192000
}, },
    4:{'name': '测试声望', 'type': 1, 'dayGainLimit': '100', },
    11:{'name': '竞技场积分', 'type': 1, },
    12:{'name': '战场积分', 'type': 1, },
    100:{'name': '竞技场兑换货币', 'type': 1, },
    300:{'name': '战勋', 'type': 1, },
    301:{'name': '军资', 'type': 1, },
    400:{'name': '通关积分', 'type': 1, },
    401:{'name': '黑帝积分', 'type': 1, },
    403:{'name': '天谕之光', 'type': 1, },
    404:{'name': '意念', 'type': 1, },
    405:{'name': '酒力', 'type': 3, 'initVal': 100, 'incType': 1, 'incVal': 100, 'maxVal': 500, },
    406:{'name': '食量', 'type': 3, 'initVal': 100, 'incType': 1, 'incVal': 100, 'maxVal': 500, },
    410:{'name': '冒险家声望', 'type': 2, 'lvUpCondition': (1, {1: 3000, 2: 33000
, 3: 183000
, 4: 1083000
, 5: 1083000
, 6: 1083000
}), },
    411:{'name': '飞鸟令', 'type': 2, },
    412:{'name': '苍龙令', 'type': 2, },
    413:{'name': '砥石高级信物', 'type': 2, },
    414:{'name': '星纪高级信物', 'type': 2, },
    415:{'name': '四帝积分', 'type': 1, },
    416:{'name': '赤帝积分', 'type': 1, },
    417:{'name': '白帝积分', 'type': 1, },
    418:{'name': '熊族声望（废弃）', 'type': 2, 'initVal': 3000, 'maxLv': 6, 'lvUpNeed': {1: 3000, 2: 12000
, 3: 24000
, 4: 48000
, 5: 96000
, 6: 192000
}, },
    419:{'name': '翼族声望（废弃）', 'type': 2, 'initVal': 3000, 'maxLv': 6, 'lvUpNeed': {1: 3000, 2: 12000
, 3: 24000
, 4: 48000
, 5: 96000
, 6: 192000
}, },
    420:{'name': '帝社功勋', 'type': 1, 'weekGainLimit': '(lv*30+2000)*7', 'weekLimitTransRatio': 0.6, },
    421:{'name': '苏澜城声望', 'type': 2, 'initVal': 5000, 'maxLv': 7, 'lvUpNeed': {1: 5000, 2: 21000
, 3: 64000
, 4: 105000
, 5: 185000
, 6: 300000
, 7: 480000
}, 'maxVal': 480000, 'reward': {1: 0, 2: 0
, 3: 0
, 4: 0
, 5: 0
, 6: 206105
, 7: 0
}, 'payBonus': {1: 0, 2: 0
, 3: 10583
, 4: 10594
, 5: 10605
, 6: 10616
, 7: 10627
}, 'payBonusNew': {1: (), 2: ()
, 3: (42101,)
, 4: (42102,)
, 5: (42103,)
, 6: (42104,)
, 7: (42105,)
}, 'rewardMail': {1: 0, 2: 0
, 3: 0
, 4: 0
, 5: 0
, 6: 46
, 7: 0
}, },
    422:{'name': '砥石城声望', 'type': 2, 'initVal': 5000, 'maxLv': 7, 'lvUpNeed': {1: 5000, 2: 21000
, 3: 64000
, 4: 105000
, 5: 185000
, 6: 300000
, 7: 480000
}, 'maxVal': 480000, 'reward': {1: 0, 2: 0
, 3: 0
, 4: 0
, 5: 0
, 6: 206106
, 7: 0
}, 'payBonus': {1: 0, 2: 0
, 3: 10591
, 4: 10602
, 5: 10613
, 6: 10624
, 7: 10635
}, 'payBonusNew': {1: (), 2: ()
, 3: (42201,)
, 4: (42202,)
, 5: (42203,)
, 6: (42204,)
, 7: (42205,)
}, 'rewardMail': {1: 0, 2: 0
, 3: 0
, 4: 0
, 5: 0
, 6: 47
, 7: 0
}, },
    423:{'name': '平海镇声望', 'type': 2, 'initVal': 5000, 'maxLv': 7, 'lvUpNeed': {1: 5000, 2: 21000
, 3: 64000
, 4: 105000
, 5: 185000
, 6: 300000
, 7: 480000
}, 'maxVal': 480000, 'reward': {1: 0, 2: 0
, 3: 0
, 4: 0
, 5: 0
, 6: 206107
, 7: 0
}, 'payBonus': {1: 0, 2: 0
, 3: 10587
, 4: 10598
, 5: 10609
, 6: 10620
, 7: 10631
}, 'payBonusNew': {1: (), 2: ()
, 3: (42301,)
, 4: (42302,)
, 5: (42303,)
, 6: (42304,)
, 7: (42305,)
}, 'rewardMail': {1: 0, 2: 0
, 3: 0
, 4: 0
, 5: 0
, 6: 48
, 7: 0
}, },
    424:{'name': '汐族声望', 'type': 2, 'initVal': 3000, 'maxLv': 7, 'lvUpNeed': {1: 3000, 2: 14500
, 3: 48000
, 4: 82000
, 5: 155000
, 6: 260000
, 7: 430000
}, 'maxVal': 430000, 'reward': {1: 0, 2: 0
, 3: 0
, 4: 0
, 5: 0
, 6: 206108
, 7: 0
}, 'payBonus': {1: 0, 2: 0
, 3: 10584
, 4: 10595
, 5: 10606
, 6: 10617
, 7: 10628
}, 'payBonusNew': {1: (), 2: ()
, 3: (42401,)
, 4: (42402,)
, 5: (42403,)
, 6: (42404,)
, 7: (42405,)
}, 'rewardMail': {1: 0, 2: 0
, 3: 0
, 4: 0
, 5: 0
, 6: 49
, 7: 0
}, },
    425:{'name': '神语书院声望', 'type': 2, 'initVal': 5000, 'maxLv': 7, 'lvUpNeed': {1: 5000, 2: 21000
, 3: 64000
, 4: 105000
, 5: 185000
, 6: 300000
, 7: 480000
}, 'maxVal': 480000, 'payBonus': {1: 0, 2: 0
, 3: 10586
, 4: 10597
, 5: 10608
, 6: 10619
, 7: 10630
}, 'payBonusNew': {1: (), 2: ()
, 3: (42501,)
, 4: (42502,)
, 5: (42503,)
, 6: (42504,)
, 7: (42505,)
}, },
    426:{'name': '仙菇声望', 'type': 2, 'initVal': 3000, 'maxLv': 7, 'lvUpNeed': {1: 3000, 2: 14500
, 3: 48000
, 4: 82000
, 5: 155000
, 6: 260000
, 7: 430000
}, 'maxVal': 430000, 'reward': {1: 0, 2: 0
, 3: 0
, 4: 0
, 5: 0
, 6: 206110
, 7: 410379
}, 'payBonus': {1: 0, 2: 0
, 3: 10585
, 4: 10596
, 5: 10607
, 6: 10618
, 7: 10629
}, 'payBonusNew': {1: (), 2: ()
, 3: (42601,)
, 4: (42602,)
, 5: (42603,)
, 6: (42604,)
, 7: (42605,)
}, 'rewardMail': {1: 0, 2: 0
, 3: 0
, 4: 0
, 5: 0
, 6: 51
, 7: 137
}, },
    427:{'name': '熊雳声望', 'type': 2, 'initVal': 3000, 'maxLv': 7, 'lvUpNeed': {1: 3000, 2: 14500
, 3: 48000
, 4: 82000
, 5: 155000
, 6: 260000
, 7: 430000
}, 'maxVal': 430000, 'reward': {1: 0, 2: 0
, 3: 0
, 4: 0
, 5: 0
, 6: 206111
, 7: 410246
}, 'payBonus': {1: 0, 2: 0
, 3: 10588
, 4: 10599
, 5: 10610
, 6: 10621
, 7: 10632
}, 'payBonusNew': {1: (), 2: ()
, 3: (42701,)
, 4: (42702,)
, 5: (42703,)
, 6: (42704,)
, 7: (42705,)
}, 'rewardMail': {1: 0, 2: 0
, 3: 0
, 4: 0
, 5: 0
, 6: 52
, 7: 138
}, },
    428:{'name': '翼族声望', 'type': 2, 'initVal': 3000, 'maxLv': 7, 'lvUpNeed': {1: 3000, 2: 14500
, 3: 48000
, 4: 82000
, 5: 155000
, 6: 260000
, 7: 430000
}, 'maxVal': 430000, 'reward': {1: 0, 2: 0
, 3: 0
, 4: 0
, 5: 0
, 6: 206112
, 7: 0
}, 'payBonus': {1: 0, 2: 0
, 3: 10589
, 4: 10600
, 5: 10611
, 6: 10622
, 7: 10633
}, 'payBonusNew': {1: (), 2: ()
, 3: (42801,)
, 4: (42802,)
, 5: (42803,)
, 6: (42804,)
, 7: (42805,)
}, 'rewardMail': {1: 0, 2: 0
, 3: 0
, 4: 0
, 5: 0
, 6: 53
, 7: 0
}, },
    429:{'name': '北狼声望', 'type': 2, 'initVal': 3000, 'maxLv': 7, 'lvUpNeed': {1: 3000, 2: 14500
, 3: 48000
, 4: 82000
, 5: 155000
, 6: 260000
, 7: 430000
}, 'maxVal': 430000, 'reward': {1: 0, 2: 0
, 3: 0
, 4: 0
, 5: 0
, 6: 206113
, 7: 0
}, 'payBonus': {1: 0, 2: 0
, 3: 10590
, 4: 10601
, 5: 10612
, 6: 10623
, 7: 10634
}, 'payBonusNew': {1: (), 2: ()
, 3: (42901,)
, 4: (42902,)
, 5: (42903,)
, 6: (42904,)
, 7: (42905,)
}, 'rewardMail': {1: 0, 2: 0
, 3: 0
, 4: 0
, 5: 0
, 6: 54
, 7: 0
}, },
    430:{'name': '桃夭夭声望', 'type': 2, 'initVal': 5000, 'maxLv': 7, 'lvUpNeed': {1: 5000, 2: 21000
, 3: 64000
, 4: 105000
, 5: 185000
, 6: 300000
, 7: 480000
}, 'maxVal': 480000, },
    431:{'name': '黑市声望', 'type': 2, 'initVal': 1000, 'maxLv': 7, 'lvUpNeed': {1: 1000, 2: 21000
, 3: 64000
, 4: 105000
, 5: 185000
, 6: 300000
, 7: 480000
}, 'maxVal': 480000, },
    432:{'name': '玉木村声望', 'type': 2, 'initVal': 5000, 'maxLv': 7, 'lvUpNeed': {1: 5000, 2: 21000
, 3: 64000
, 4: 105000
, 5: 185000
, 6: 300000
, 7: 480000
}, 'maxVal': 480000, 'reward': {1: 0, 2: 0
, 3: 0
, 4: 0
, 5: 0
, 6: 206114
, 7: 0
}, 'payBonus': {1: 0, 2: 0
, 3: 10593
, 4: 10604
, 5: 10615
, 6: 10626
, 7: 10637
}, 'payBonusNew': {1: (), 2: ()
, 3: (43201,)
, 4: (43202,)
, 5: (43203,)
, 6: (43204,)
, 7: (43205,)
}, 'rewardMail': {1: 0, 2: 0
, 3: 0
, 4: 0
, 5: 0
, 6: 55
, 7: 0
}, },
    433:{'name': 'KFZ的信任', 'type': 2, 'initVal': 1000, 'maxLv': 7, 'lvUpNeed': {1: 1000, 2: 1500
, 3: 3000
, 4: 5500
, 5: 8500
, 6: 12500
, 7: 18500
}, 'maxVal': 18500, },
    434:{'name': '馈灵六社', 'type': 2, },
    435:{'name': '阅历', 'type': 2, 'maxLv': 7, 'lvUpNeed': {1: 500, 2: 1500
, 3: 3000
, 4: 5500
, 5: 8500
, 6: 12500
, 7: 200000
}, 'maxVal': 200000, },
    436:{'name': '学识', 'type': 2, 'initVal': 100, },
    437:{'name': '木妖声望', 'type': 2, 'initVal': 3000, 'maxLv': 7, 'lvUpNeed': {1: 3000, 2: 14500
, 3: 48000
, 4: 82000
, 5: 155000
, 6: 260000
, 7: 430000
}, 'maxVal': 430000, },
    438:{'name': '元狸声望', 'type': 2, 'initVal': 3000, 'maxLv': 7, 'lvUpNeed': {1: 3000, 2: 14500
, 3: 48000
, 4: 82000
, 5: 155000
, 6: 260000
, 7: 430000
}, 'maxVal': 430000, 'reward': {1: 0, 2: 0
, 3: 0
, 4: 0
, 5: 0
, 6: 206115
, 7: 0
}, 'payBonus': {1: 0, 2: 0
, 3: 10592
, 4: 10603
, 5: 10614
, 6: 10625
, 7: 10636
}, 'payBonusNew': {1: (), 2: ()
, 3: (43801,)
, 4: (43802,)
, 5: (43803,)
, 6: (43804,)
, 7: (43805,)
}, 'rewardMail': {1: 0, 2: 0
, 3: 0
, 4: 0
, 5: 0
, 6: 56
, 7: 0
}, },
    439:{'name': '星纪城声望', 'type': 2, 'initVal': 5000, 'maxLv': 7, 'lvUpNeed': {1: 5000, 2: 21000
, 3: 64000
, 4: 105000
, 5: 185000
, 6: 300000
, 7: 480000
}, 'maxVal': 480000, 'reward': {1: 0, 2: 0
, 3: 0
, 4: 0
, 5: 0
, 6: 206109
, 7: 0
}, 'rewardMail': {1: 0, 2: 0
, 3: 0
, 4: 0
, 5: 0
, 6: 158
, 7: 0
}, },
    440:{'name': '馈灵贡献', 'type': 1, },
    441:{'name': '馈灵贡献', 'type': 1, },
    442:{'name': '馈灵贡献', 'type': 1, },
    443:{'name': '馈灵贡献', 'type': 1, },
    444:{'name': '馈灵贡献', 'type': 1, },
    445:{'name': '馈灵贡献', 'type': 1, },
    446:{'name': '九尾声望', 'type': 2, 'initVal': 3000, 'maxLv': 7, 'lvUpNeed': {1: 3000, 2: 14500
, 3: 48000
, 4: 82000
, 5: 155000
, 6: 260000
, 7: 430000
}, 'maxVal': 430000, 'reward': {1: 0, 2: 0
, 3: 0
, 4: 0
, 5: 0
, 6: 206130
, 7: 0
}, 'rewardMail': {1: 0, 2: 0
, 3: 0
, 4: 0
, 5: 0
, 6: 161
, 7: 0
}, },
    447:{'name': '妖精旅社声望', 'type': 2, 'initVal': 5000, 'maxLv': 7, 'lvUpNeed': {1: 5000, 2: 21000
, 3: 64000
, 4: 105000
, 5: 185000
, 6: 300000
, 7: 480000
}, 'maxVal': 480000, },
    448:{'name': '海贼团声望', 'type': 2, 'initVal': 3000, 'maxLv': 7, 'lvUpNeed': {1: 3000, 2: 14500
, 3: 48000
, 4: 82000
, 5: 155000
, 6: 260000
, 7: 430000
}, 'maxVal': 430000, },
    449:{'name': '五帝声望', 'type': 2, 'initVal': 5000, 'maxLv': 7, 'lvUpNeed': {1: 5000, 2: 21000
, 3: 64000
, 4: 105000
, 5: 185000
, 6: 300000
, 7: 480000
}, 'maxVal': 480000, },
    451:{'name': '测试NPC声望01', 'type': 2, 'isNpcFame': 1, 'initVal': 3000, 'maxLv': 6, 'lvUpNeed': {1: 3000, 2: 12000
, 3: 24000
, 4: 48000
, 5: 96000
, 6: 192000
}, 'maxVal': 192000, },
    452:{'name': '测试NPC声望02', 'type': 2, 'isNpcFame': 1, 'initVal': 3000, 'maxLv': 6, 'lvUpNeed': {1: 3000, 2: 12000
, 3: 24000
, 4: 48000
, 5: 96000
, 6: 192000
}, 'maxVal': 192000, },
    453:{'name': '云垂积分', 'type': 1, },
    454:{'name': '行者无疆声望', 'type': 2, 'initVal': 5000, 'maxLv': 7, 'lvUpNeed': {1: 5000, 2: 21000
, 3: 64000
, 4: 105000
, 5: 185000
, 6: 300000
, 7: 480000
}, 'weekGainLimit': '30000', 'maxVal': 480000, },
    455:{'name': '苦劳', 'type': 1, },
    500:{'name': '斩妖除魔值', 'type': 2, },
    501:{'name': '长城修为值', 'type': 2, 'maxVal': 1000, },
    502:{'name': '长城逃杀修为值', 'type': 2, 'maxVal': 1500, },
    503:{'name': '长城弑神修为值', 'type': 2, 'maxVal': 2000, },
    506:{'name': '灵墟单人修为值', 'type': 2, 'maxVal': 200, },
    507:{'name': '灵墟修为值', 'type': 2, 'maxVal': 800, },
    508:{'name': '灵墟修为值', 'type': 2, 'maxVal': 800, },
    511:{'name': '神祠剧情修为值', 'type': 2, 'maxVal': 200, },
    512:{'name': '神祠修为值', 'type': 2, 'maxVal': 800, },
    513:{'name': '神祠弑神修为值', 'type': 2, 'maxVal': 2000, },
    514:{'name': '奇谈会声望', 'type': 2, 'initVal': 1, 'maxLv': 7, 'lvUpNeed': {1: 1, 2: 10
, 3: 30
, 4: 50
, 5: 70
, 6: 100
, 7: 150
}, 'maxVal': 150, },
    516:{'name': '雾谷试炼修为值', 'type': 2, 'maxVal': 2000, },
    517:{'name': '雾谷普通修为值', 'type': 2, 'maxVal': 2000, },
    518:{'name': '雾谷困难修为值', 'type': 2, 'maxVal': 2000, },
    521:{'name': '镇妖试炼修为值', 'type': 2, 'maxVal': 2000, },
    522:{'name': '镇妖困难修为值', 'type': 2, 'maxVal': 2000, },
    523:{'name': '驱魔积分', 'type': 1, 'weekGainLimit': 'int((0.105*(max(min(int(lv/5)*5,55+int((lv-55)/5)*1.5),30)**2.87+(0.2*lv+min(0.8*lv,50))**2.4-(max(min(int(lv/5)*5,55),30))**2.4)+max(2500,(60-int(lv/5)*5)*100+2500))*1.15)', 'weekLimitTransRatio': 0.6, },
    524:{'name': '迷城修为值', 'type': 2, 'maxVal': 2000, },
    525:{'name': '迷城弑神修为值', 'type': 2, 'maxVal': 2000, },
    526:{'name': '剑冢修为值', 'type': 2, 'maxVal': 2000, },
    527:{'name': '剑冢弑神修为值', 'type': 2, 'maxVal': 2000, },
    601:{'name': '公会商票', 'type': 1, },
}
