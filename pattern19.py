"""
******
**  **
*    *
*    *
**  **
******
"""

n = int(input("Number : "))
for i in range(n,0,-1):
    ch = "*"*i+" "*(n-i)
    print(ch+ch[::-1])
for i in range(1,n+1):
    ch1 = "*"*i+" "*(n-i)
    print(ch1+ch1[::-1])
