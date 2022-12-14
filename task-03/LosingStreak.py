import math
num = input()
lst = num.split()
n = int(lst[0])
m = int(lst[1])
if m % n != 0 :
    print(-1)
elif m / n == 1 :
    print(0)
else:
    l1 = []
    n1 = m / n
    while n1 % 2 == 0:
        l1.append(2)
        n1 = n1/2
    for i in range(3,int(math.sqrt(n1)),2):
        while n1 % i == 0:
            l1.append(i)
            n1 = n1/i
    if n1 > 2:
        l1.append(n1)
    if len(set(l1)) == 2 and 2 in set(l1) and 3 in set(l1):
        sum = l1.count(2) + l1.count(3)
        print(sum)
    else :
        print(-1)