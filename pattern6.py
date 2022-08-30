"""
123
12
1
"""

n = int(input("Number : "))
for i in range(n,0,-1):
    s = ""
    for j in range(i):
        s += str(j+1)
    print(s) 