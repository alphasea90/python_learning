tag = True
while tag:
    with open('user.txt','r') as f:
        username_list = [] 
        userdict = {} 
        user = f.readlines() # 读取文件中的用户信息制成列表
        for u in user:
            userinfo = u.split('|') # 把用户信息按“|”分开得到：用户名，密码，余额
            userdict[userinfo[0]] =[userinfo[1], userinfo[2]] #把用户信息制成字典

    with open('blacklist.txt','r') as f:
        black_list = f.readlines()

    get_username = input('请输入用户名').strip() #获取用户名
    if get_username not in userdict: #检查是否未注册用户名
        print('用户名尚未注册，请注册')
        get_username = input('请输入注册用户名').strip() #注册用户名
        userdict[get_username] = []  #写入词典
        while True:
            get_password1 = input('请输入密码').strip() #获取密码
            get_password2 = input('请再次输入密码').strip()
            if get_password1 != get_password2:
                print('输入的密码不相同')
            else:
                userdict[get_username].append(get_password1) #写入词典
                break
        while True:
            get_salary = input('请输入工资（作为余额）：').strip() #获取余额
            print(get_salary)
            try:
                balance = float(get_salary)
                userdict[get_username].append(balance)
                tag = False
                break
            except:
                print('请输入正确的数字')
        with open('user.txt','a') as f: #写入文档
            f.write('\n' +get_username+'|'+get_password1+'|'+str(balance))    
    elif get_username in black_list: #检查是否在黑名单
        print('该账号在黑名单')
    else:
        n = 1 
        while n<=3: #尝试3次
            get_password = input('请输入密码') #输入密码
            if get_password != userdict[get_username][0]:
                print('密码错误')
                if n<=3:
                    print('还有'+str(3-n)+'次机会')
                    n += 1
                continue
            else:
                print('密码正确，成功登录') #成功登录
                tag = False
                break
            print('错误三次，已被加入黑名单')
            with open('blacklist.txt','a') as f:
                f.write('\n' + get_username)

print('欢迎光临'+get_username +',您的余额为：'+ userdict[get_username][1])
balance = float(userdict[get_username][1])

shopping_list = []
tag_shopping = True
while tag_shopping:
    goods  = {1:['iPhone',500],2:['macbook',1000],3:['bike',100]} #商品列表
    for key in goods:
        print(str(key) +':'+goods[key][0]+'单价：'+str(goods[key][1]))
    shopping = input('请输入你要买的商品编号(退出购买请按‘q’)')
    if shopping == 'q':
        print('欢迎下次再来')
        tag_shopping = False
    if shopping.isnumeric():
        if int(shopping) not in goods:
            print('请输入正确的商品编号')
        else:
            if goods[int(shopping)][1]<=float(balance):
                shopping_list.append(goods[int(shopping)])
                balance -= goods[int(shopping)][1]
                print('您购买了'+goods[int(shopping)][0]+'。余额：'+str(balance))
            else:
                print('您余额不足了。您的余额：'+str(balance))
            
            while True:
                continue_shopping = input('是否结账Y/N')
                if continue_shopping == 'Y':
                    tag_shopping = False
                    break
                elif continue_shopping == 'N':
                    break
                else:
                    print('请输入Y或者N')
    else:
        print('请输入正确的商品编号')

print('您购买了：')
for i in shopping_list:
    print(i[0])
print('您的余额：'+str(balance))

userdict[get_username][1] = balance
with open('user.txt','w') as f:
    for key in userdict:
        f.write(key+'|'+userdict[key][0]+'|'+str(userdict[key][1]))