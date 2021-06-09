print('小组统分工具 v1.0\n')
print('现在统计纪律分（只输入数字(如106、87)即可）！！！')
def bl(list):
    rr = ''
    for d in list:
        rr += d + ' '
    return rr
f_j = []
for i in range(14):
    f_j.append(input('第%s组纪律分:'%(str(i+1))))
print()

print('现在统计作业分（只输入数字(如1、2)即可）！！！')
f_z = []
for x in range(14):
    f_z.append(input('第%s组作业扣的分:'%(str(x+1))))
print()

#获取总分
zf = {}
zf2=[]
print('现在获取总分！！！')
for w in range(14):
    z = str(w+1)
    f = int(f_j[w]) - int(f_z[w])
    zf2.append(f)
    zf[z] = f
    print('第' + str(z) + '组' + str(f) + '分')
print()

#获取排名
def get_key(dic, value):
    return [k for k, v in dic.items() if v == value]
zf2.sort(reverse = True)
for n in range(14):
    y = str(n+1)
    s = len(get_key(zf,zf2[n]))
    if s == 1:
        print('第' + y +'名第 ' + str(bl(get_key(zf,zf2[n]))) + '组')
    else:
        print('第' + y +'名第 ' + str(bl(get_key(zf,zf2[n]))) + '组        有并列！！！')
input()


