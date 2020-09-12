from datetime import datetime

ds = __import__('destructipy')

abc = {'a': 1, 'b': 2, 'c': 3}
for iterations in [int(f'9{"9" * e}') for e in range(9)]:
    print(f'\n{iterations} iterations:')

    now = datetime.now()
    for i in range(iterations):
        a, b, c = abc['a'], abc['b'], abc['c']
    print(f'regular     : {datetime.now() - now}')

    now = datetime.now()
    for i in range(iterations):
        a, b, c = ds(abc)
    print(f'destructipy : {datetime.now() - now}')
