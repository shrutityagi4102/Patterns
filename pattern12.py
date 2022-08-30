"""
1    1
12  21
123321
"""

n = int(input("Number : "))
for i in range(1,n+1):
    s = ""
    for j in range(i):
        s += str(j+1)
    x = s+" "*(n-i)
    print(x+x[::-1])
