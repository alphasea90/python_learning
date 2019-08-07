menu = {
    '汽车':{
        '德国':{
            '奥迪':{},
            '大众':{}
        },
        '中国':{
            '红旗':{},
            '吉利':{}
        }
    },
    '飞机':{
        '战斗机':{
            '美国':{},
            '中国':{}
        },
        '客机':{
            '波音':{},
            '空客':{}
        }
    },
    '坦克':{
        '一代':{
            '德国':{},
            '苏联':{}
        },
        '二代':{
            '德国':{},
            '苏联':{}
        },
        '三代':{
            '德国':{},
            '美国':{}
        }
    }
}

tag = True
while tag:
    menu1 = menu
    for key in menu1:
        print(key)
    get_tag1 = input('请输入你想进入的菜单：(退出请输入‘q’)').strip()
    if get_tag1 == 'q':
        tag = False
        break
    elif get_tag1 not in menu1:
        print('请重新输入')
        continue
    else:
        while tag:
            menu2 = menu1[get_tag1]
            for key in menu2:
                print(key)
            get_tag2 = input('请输入你想进入的菜单：(退出请输入‘q’,返回上级请输入‘b’)').strip()
            if get_tag2 == 'b':
                break
            elif get_tag2 == 'q':
                tag = False
                continue
            elif get_tag2 not in menu2:
                print('请重新输入')
                continue
            else:
                for key in menu2[get_tag2]:
                    print(key)
                    tag = False
                    continue