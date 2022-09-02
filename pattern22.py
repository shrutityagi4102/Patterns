"""
4444444
4333334
4322234
4321234
4322234
4333334
4444444
"""

n = int(input("Number : "))
l = (n*2)-1
ans = []
for i in range(1,n+1):
    subans = []
    ch = l
    ni = n
    s = ""
    subs = ""
    for j in range(i):
        if j==i-1:
            s += ch*str(ni)
        else:
            s+=str(ni)
            subs += str(ni)
            ch-=2
            subans.append(str(ni))
            ni-=1
    print(s+subs[::-1])
    if i!=n:
        ans.append(s+subs[::-1])
print(*ans[::-1],sep="\n")
