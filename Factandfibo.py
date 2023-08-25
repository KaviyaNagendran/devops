def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    print(f)
def fibo(n):
    a,b=1,2
    print("0 1",end=" ")
    print(a,end=" ")
    print(b,end=" ")
    for i in range(n-4):
        c=a+b
        print(c,end=" ")
        a,b=b,c
n=int(input())
fibo(n)
print()
fact(n)
