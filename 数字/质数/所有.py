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
