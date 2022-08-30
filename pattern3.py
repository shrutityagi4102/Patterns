"""
1
12
123
"""

n = int(input("Number : "))
for i in range(1,n+1):
    s = ""
    for j in range(i):
        s += str(j+1)
    print(s)   