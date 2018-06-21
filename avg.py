nb_cases = 5

while True:
    try:
        count_op = 0
        for i in range(nb_cases):
            n, op, dist = input().split()
            count_op += int(op)
        print('%s %d' % (n, count_op / nb_cases))
    except:
        pass