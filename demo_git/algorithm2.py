x = int(input('enter integer x: '))
y = int(input('enter integer y: '))

def findStep(x,y):
    step = 0
    while(True):
        if x > y:
            x = x - 1
        elif x*2 <= y:
            x = x*2
        elif x*2 > y and y%2 == 1:
            x = x*2
        elif x*2 > y and y%2 == 0:
            x = x - 1
        else:
            print('error')
        step += 1
        if x == y:
            return step
step = findStep(x,y)
print('step = ',step)

