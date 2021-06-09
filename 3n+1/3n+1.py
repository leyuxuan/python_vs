import time
n=int(input('从几开始(按0从上次开始)？\n     '))
def return_3n_and_1(n):
    y=n
    num=[]
    x=0
    while n!=1:
        if n%2==1:
            n=eval('n*3+1')
        else:
            n=eval('n/2')
        x+=1
    num.append(y)
    num.append(x)
    return num

def main():
    global n
    if n==0:
        with open(('save.js.h.file.java.c.exe'),'r') as f:
            n=int(f.read())
    c=0
    while 1:
        l=return_3n_and_1(n)
        print('数%s用了%s步'%(l[0],l[1]))
        n+=1
        if c%10==0:
            try:
                with open(('save.js.h.file.java.c.exe'),'w') as f:
                    f.write(str(n))
            except:
                time.sleep(0.1)
                with open(('save.js.h.file.java.c.exe'),'w') as f:
                    f.write(str(n))
        c+=1

if __name__ == '__main__':
    main()
