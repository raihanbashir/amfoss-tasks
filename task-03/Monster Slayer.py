lst = []
t = int(input())
for i in range(t):
    l1 = []
    n = int(input())
    ai = input()
    l2 = ai.split()
    for j in range(n):
        l1.append(int(l2[j]))
    lst.append(l1)
for i in lst:
    m = 0
    for j in range(len(i)):
        if i[j] % i[0] == 0:
            m += 1
            continue
        else :
            break
    if m == len(i):
        print('YES')
    else:
        print('NO')