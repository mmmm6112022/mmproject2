a = (lambda x,y:x*y)(6,6)
print(a)

print((lambda x,y:x*y)(5,7))
o = (lambda x,y:x if x>y else y)(20,50)
print(o)

r = (lambda num:"even numbers" if num%2==0
     else "odd numbers")(3)
print(r)

