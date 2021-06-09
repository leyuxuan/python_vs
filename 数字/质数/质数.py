def all():
    x = 1
    def main():
        num = x
        # 质数大于 1
        if num > 1:
            # 查看因子
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                print(num,'\n')
                print('')
    while True:
        main()
        x += 1
def pan_duan():
    def main():
        num = int(input("请输入一个数字: "))
        # 质数大于 1
        if num > 1:
            # 查看因子
            for i in range(2,num):
                if (num % i) == 0:
                    print(num,"不是质数")
                    print(i,"乘于",num//i,"是",num)
                    print('')
                    break
            else:
                print(num,"是质数")
                print('')
        # 如果输入的数字小于或等于 1，不是质数
        else:
            print(num,"不是质数")
            print('')
    while True:
        main()

z = int(input('要判断质数（1）还是求出所有质数（2）？'))
if z == 1:
    pan_duan()
if z == 2:
    all()
