from multipledispatch import dispatch
@dispatch(int,int)
def product(a,b):
    p=a*b
    return p
@dispatch(int,int,int)
def product(a,b,c):
    p=a*b*c
    return p
print(product(4,5,30))
print(product(7,3))