"""
1
23
456
"""

n = int(input("Number : "))
x = 1
for i in range(1,n+1):
    ans = []
    for j in range(i):
        ans.append(x)
        x += 1
    print(*ans, sep=" ")
