"""
1
01
101
0101
"""

n = int(input("Number : "))
for i in range(1,n+1):
    if i%2!=0:
        x = 0
        s = ""
        while x<i:
            if x%2==0:
                s += "1"
            else:
                s += "0"
            x += 1
        print(s)
    else:
        x = 0
        s = ""
        while x<i:
            if x%2==0:
                s += "0"
            else:
                s += "1"
            x += 1
        print(s)




