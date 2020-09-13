from destructipy import _ as ds
from datetime import datetime

abc = {'a': 1, 'b': 2, 'c': 3}

for iterations in [int('9%s' % ('9' * i)) for i in range(9)]:
    print('\n%s iterations:' % iterations)

    now = datetime.now()
    for i in range(iterations):
        a, b, c = abc['a'], abc['b'], abc['c']
    print('regular   : %s' % (datetime.now() - now))

    now = datetime.now()
    for i in range(iterations):
        a, b, c = ds(abc)
    print('ds        : %s' % (datetime.now() - now))

    now = datetime.now()
    for i in range(iterations):
        a, b, c = ds.i(abc)
    print('ds.i/ds.a : %s' % (datetime.now() - now))
