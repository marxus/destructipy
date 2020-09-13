import destructipy as ds
from datetime import datetime

abc = {'a': 1, 'b': 2, 'c': 3}

for iterations in [int(f'9{"9" * e}') for e in range(9)]:
    print(f'\n{iterations} iterations:')

    now = datetime.now()
    for i in range(iterations):
        a, b, c = abc['a'], abc['b'], abc['c']
    print(f'regular   : {datetime.now() - now}')

    now = datetime.now()
    for i in range(iterations):
        a, b, c = ds(abc)
    print(f'ds        : {datetime.now() - now}')

    now = datetime.now()
    for i in range(iterations):
        a, b, c = ds.i(abc)
    print(f'ds.i/ds.a : {datetime.now() - now}')
