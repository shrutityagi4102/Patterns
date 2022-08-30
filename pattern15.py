"""
ABC
AB
A
"""

n = int(input("Number : "))
for i in range(n,0,-1):
    s = ""
    for j in range(i):
        s += chr(64+(j+1))
    print(s)
