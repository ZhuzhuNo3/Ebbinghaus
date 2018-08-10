#-*- coding=utf-8 -*-#
import datetime,re
timelist = [1,2,4,7,15,31,36,41]
def learn(x):
    data = []
    now = datetime.datetime.now()
    q = r'^\d+-(\d+-\d+)\s'
    data += re.findall(q,str(now))
    data1 = "'%s':\n'"%x
    for i in timelist:
        delta = datetime.timedelta(days=i)
        days = now + delta
        data += re.findall(q,str(days))
    data1 += ','.join(data)
    data1 += "'"
    try:
        with open('wordslist.py','r') as f:
            filex = f.read()
        data1 = filex[:-1] + ',\n' + data1 + '}'
        with open('wordslist.py','w') as f:
            f.write(data1)
    except:
        print('新建存档')
        data1 = 'data={' + data1 + '}'
        with open('wordslist.py','w') as f:
            f.write(data1)

def check(x):
    try:
        from wordslist import data
        keys = [i[0] for i in data.items() if x in i[1]]
        print('%s'%(','.join(keys)))
    except:
        print('无数据')

print('1.新增 2.复习')
n = int(input())
if n == 1:
    print('新增内容:')
    learn(input())
elif n == 2:
    now = datetime.datetime.now()
    q = r'^\d+-(\d+-\d+)\s'
    x = re.findall(q,str(now))[0]
    print('今日需复习:')
    check(x)
