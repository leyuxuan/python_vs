while True:
     num = input("请输入一个数字: ")
     try:
          while True:
               if int(num) == int(str(num)[::-1]):
                    print('回文数是：' + str(num))
                    break
               else:
                    y = num
                    x = str(num)[::-1]
                    x = int(x)
                    num = int(num)
                    num = eval('num + x')
                    print(str(y) +'+' + str(x) +'=' + str(num))
     except:
          print('')
          print('请输入一个数字！')
          print('')
          continue
