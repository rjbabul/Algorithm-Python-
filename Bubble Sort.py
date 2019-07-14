a= list()
print('how number is are input? ',end=' ')
num=int(input())
for i in range(0,num):
    x=int(input())
    a.append(x)


for i in range(0,num):
    for j in range(0,num-1):
        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp

print(a)
