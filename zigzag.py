import time
def zigzag(k):
    for i in range(k):
       # print(' ')
        print(' ',end='')

    for j in range(8):
        print('*', end='')

    print('')
try:

    n=4
    while True:
        for i in range(n,-1,-1):
            zigzag(i)
        for j in range(1,n+1,1):
            zigzag(j)
        time.sleep(0.4)
except KeyboardInterrupt:
    print('KeyboardInterrup')

