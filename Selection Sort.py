a= list()
print('how number is are input? ',end=' ')
num=int(input())
for i in range(0,num):
    x=int(input())
    a.append(x)


def insertion_sort(a):
    for i in range(0,len(a)-1):
        min_dex =i
        for j in range(i+1,len(a)):
            if(a[j]<a[min_dex]):
                min_dex=j
        if(min_dex!=i):
            temp=a[i]
            a[i]=a[min_dex]
            a[min_dex]=temp

insertion_sort(a)

print(a)
