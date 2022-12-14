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
    mana = 0
    if 0 in i:
        mana = mana + len(i) - i.count(0)
    else:
        if len(set(i)) == len(i):
            mana = mana + len(i) + 1
        else:
            mana = mana + len(i)
    print(mana)
