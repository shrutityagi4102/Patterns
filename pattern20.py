"""
*    *
**  **
******
**  **
*    *
"""

n = int(input("Number : "))
ans = []
for i in range(1,n+1):
    if i!=n:
        x = "*"*i+" "*(n-i)
        print(x+x[::-1])
        ans.append(x+x[::-1])
    else:
        print("*"*i+"*"*i)
print(*ans[::-1], sep="\n")
