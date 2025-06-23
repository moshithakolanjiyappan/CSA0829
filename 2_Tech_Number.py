n=3025
m=str(n)
a=m[:len(m)//2]
print (a)
b=m[len(m)//2:]
print(b)
c=int(a)+int(b)
print(c)
d=c**2
print(d)
if(d==n):
    print("Tech number")
else:
    print("Not a Tech number")
