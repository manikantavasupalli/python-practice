#Fibonaccii series
def fib(n):
    fseries=[]
    a,b=0,1
    while b<=n:
        fseries.append(b)
        a,b=b,a+b
    return fseries
n=int(input("Enter range for fibonacci: "))
print(fib(n))
    