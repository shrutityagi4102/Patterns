"""
  *  
 ***
*****
*****
 ***
  *
"""

n = int(input("Number : "))
l = (n*2)-1
x = 1
for i in range(n):
    ch = i+x
    print(" "*((l-ch)//2)+"*"*(ch))
    x += 1

x = n
for i in range(n-1,-1,-1):
    ch = i+x
    print(" "*((l-ch)//2)+"*"*(ch))
    x -= 1