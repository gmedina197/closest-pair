from random import randint

with open('in2.txt', 'w') as out:
    for i in range(1000, 50001, 1000):
        for k in range(5):
            out.write('%d\n' % i)
            for j in range(i):
                out.write('%d %d ' % (randint(-2**30+1, 2**30-1), randint(-2**30+1, 2**30-1)))
            out.write('\n')
