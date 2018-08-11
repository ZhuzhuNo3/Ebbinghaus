#-*- coding=utf-8 -*-#
import datetime,re
try:
    from wordslist import wordslist
except ModuleNotFoundError:#不存在则新建存档
    with open('wordslist.py','w') as f:
        f.write('wordslist={\n}')
    print('新建存档')
    from wordslist import wordslist

timelist = [1,2,4,7,15,31,36,41]

def learn(x):
    value = [i for i in wordslist.items() if x in i[1]]
    if value != []:#如果输入内容已存在
        print('%s已存在复习列表中'%x)
    else:
        data = []
        now = datetime.datetime.now()#今天的日期
        q = r'^\d+-(\d+-\d+)\s'#保留月份和日
        data += re.findall(q,str(now))
        for i in timelist:#计算需要复习的日期
            delta = datetime.timedelta(days=i)
            days = now + delta
            data += re.findall(q,str(days))
        data1 = ','.join(data)
        #需要记忆的日期存储为键
        #输入内容存储为键值
        if data1 in wordslist.keys():
            wordslist[data1] += ',' + x
        else:
            wordslist[data1] = x
        save()

def save():
    #格式化词典(方便看wordslist.py)
    diclist = ["'%s':'%s'"%(i,wordslist[i]) for i in wordslist]
    data = 'wordslist={\n' + ',\n'.join(diclist) + '\n}'
    with open('wordslist.py','w') as f:#保存存档
        f.write(data)
        
def check(x):
    value = [i[1] for i in wordslist.items() if x in i[0]]
    print('%s'%(','.join(value)))

def dele(x):
    key = [i[0] for i in wordslist.items() if x in i[1]][0]
    value = wordslist[key].split(',')
    value.remove(x)
    value = ','.join(value)
    wordslist[key] = value
    save()

while True:
    print('1.新增 2.复习 3.删除 4.退出')
    n = int(input())
    if n == 1:
        print('新增内容:(q/退出循环)')
        while True:
            x = str(input())
            if x == 'q':
                break
            else:
                learn(x)
    elif n == 2:
        now = datetime.datetime.now()
        q = r'^\d+-(\d+-\d+)\s'
        x = re.findall(q,str(now))[0]
        print('今日需复习:')
        check(x)
    elif n == 3:
        for i in wordslist:
            print(wordslist[i])
        print('删除:')
        dele(str(input()))

    elif n == 4:
        break

