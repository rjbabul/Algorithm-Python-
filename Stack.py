a = list()
x = 0


def call():
    print('push : 1')
    print('pop : 2')
    print('Top : 3')
    print('Display : 4')
    print('Exit : 5')
    s = int(input())
    if (s == 1):
        if (len(a) == 10):
            print('Stack is full')
        else:
            x = int(input('enter a number: '))
            a.append(x)
    if (s == 2):
        if (len(a) == 0):
            print('Stack is Empty')
        else:
            print('Pop number is: ', a[len(a) - 1])
            a.pop()
    if (s == 3):
        if (len(a) == 0):
            print('Stack is Empty')
        else:
            print('Top element is: ', a[len(a) - 1])
    if (s == 4):
        if (len(a) == 0):
            print('Stack is Empty')
        else:
            print('Stack is :', a)

    return s


num = int(2)
while (x != 5):
    x = call()
