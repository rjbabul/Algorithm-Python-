num = list()

n=int(input('How number you input: '))
i=0
while(i<n):
    x=int(input())
    num.append(x)
    i=i+1

xx=int(input('What number you search? :'))
i=0
c=0
for i in range (0,n):
    if(num[i]==xx):
        c=c+1
        number=i
        break

    i=i+1
if(c==1):
    print(xx,' is preasent in this list of position ',number+1)
else:
    print('this number isnot present in this list')
