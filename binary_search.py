a = list()
def sumr(l,a,r,x):
    if(r>=l):
        mid=l+int((r-l)//2)

        if(a[mid]==x):
            return mid
        if(a[mid]>x):
            return sumr(l,a,mid-1,x)
        if(a[mid]<x):
            return sumr(mid+1,a,r,x)
    else:
        return 0

num=int(input('How number you input: '))


for i in range (0,num):
    x = int(input())
    a.append(x)


a.sort()

x=int(input('What number you are search? '))
l=0
r=num
s=int()
if(x== a[0]):
    print(x, ' number is present')
else:
    s = sumr(l, a, r - 1, x)
    if (s == 0):
        print(x ,'  is no present')
    else:
        print(x, ' number is present')
