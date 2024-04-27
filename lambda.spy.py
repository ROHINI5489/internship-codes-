add=lambda x,y:x+y
result=add(3,5)
print(result)


numbers=(3,7,5,3)
squared=tuple(map(lambda x:x**2,numbers))
print(squared)


def fun(n):
     if n==4:
         return 5
     print(fun(n+1))
fun(1)