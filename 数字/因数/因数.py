while True:
     y = 1
     def allFactor(n):
         if n == 0: return [0]
         if n == 1: return [1]
         rlist = [1]
         i = 2
 
         while i <= n:
             if n % i == 0:
                 rlist.append(i)
                 n = n // i
                 i = 2
                 continue
             i += 1
         print(rlist)
     allFactor(int(input()))


