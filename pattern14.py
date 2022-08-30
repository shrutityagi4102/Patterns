"""
A
AB
ABC
"""

n = int(input("Number : "))
for i in range(1,n+1):
    s = ""
    for j in range(i):
        s += chr(64+(j+1))
    print(s)
