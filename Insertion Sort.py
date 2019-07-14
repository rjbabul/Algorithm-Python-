a= list()
print('how number is are input? ',end=' ')
num=int(input())
for i in range(0,num):
    x=int(input())
    a.append(x)


def insertion_sort(a):
    for i in range(1,len(a)):
        j=i-1
        while(a[j]>a[j+1] and j>=0):
            temp= a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            j-=1

insertion_sort(a)

print(a)

