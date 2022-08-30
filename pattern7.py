"""
  *  
 ***
*****
"""

n = int(input("Number : "))
l = (n*2)-1
x = 1
for i in range(n):
    ch = i+x
    print(" "*((l-ch)//2)+"*"*(ch))
    x += 1