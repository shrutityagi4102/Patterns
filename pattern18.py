"""
C
BC
ABC
"""

n = int(input("Number : "))
for i in range(1,n+1):
    s = ""
    x = n
    for j in range(i):
        s += chr(64+x)
        x -= 1
    print(s[::-1])
