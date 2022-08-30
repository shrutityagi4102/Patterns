"""
  A
 ABA
ABCBA
"""

n = int(input("Number : "))
for i in range(1,n+1):
    ans = []
    for j in range(i):
        if j!=i-1:
            ans.append(chr(64+(j+1)))
        else:
            print(" "*(n-i)+"".join(ans)+chr(64+(j+1))+"".join(ans[::-1]))
