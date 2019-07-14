a= list()
x=0
def call():
    print('push : 1')
    print('pop : 2')
    print('Top : 3')
    print('Display : 4')
    print('Exit : 5')
    s=int(input('Enter Your Choice : '))

    if(s==1):
        if(len(a)==10):
            print('queue is full')
        else:
            x = int(input('enter a number: '))
            a.append(x)
    if(s==2):
        if(len(a)==0):
            print('queue is Empty')
        else:
            print('Pop number is: ',a[0])
            a.reverse()
            a.pop()
            a.reverse()
    if(s==3):
        if (len(a) == 0):
            print('queue is Empty')
        else:
            print('Top element is: ', a[0])
    if(s==4):
        if (len(a) == 0):
            print('queue is Empty')
        else:
            print('queue is :',a)

    return s

num=int(2)
while(x!=5):
    x=call()

