n = input()
num_list = []
for i in range(int(n)):
    num_list.append(input())
num_eng = {"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine","0":"zero"}
for i in num_list:
    print(num_eng[i])