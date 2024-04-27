def pattern1():
    n=5
    for i in range(1,n):
        print(""*(n-i),"*"*i)
pattern1()
        
def pattern2():
    n=-5
    for i in range(-1,n-1):
        print("*"*i)
    for i in range(-1,0,n-1):
        print("*"*(n-i),"*"*i)
pattern2()

