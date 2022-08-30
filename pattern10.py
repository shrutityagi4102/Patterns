"""
*
**
***
**
*
"""

n = int(input("Number : "))
ans = []
for i in range(1,n+1):
    if i!=n:
        x = "*"*i
        print(x)
        ans.append(x)
    else:
        print("*"*i)
print(*ans[::-1], sep="\n")