# destructipy
es6 style dict/object destructure for python

```
$ pip install destructipy
```

```python
# must import this way...
ds = __import__('destructipy')

abc = {'a': 1, 'b': 2, 'c': 3}
c, b, a = ds(abc)
print(a, b, c)
```

benchmark:
```
$ python benchmark.py 

9 iterations:
regular     : 0:00:00.000006
destructipy : 0:00:00.000091

99 iterations:
regular     : 0:00:00.000016
destructipy : 0:00:00.000068

999 iterations:
regular     : 0:00:00.000153
destructipy : 0:00:00.000701

9999 iterations:
regular     : 0:00:00.001571
destructipy : 0:00:00.006198

99999 iterations:
regular     : 0:00:00.012533
destructipy : 0:00:00.055433

999999 iterations:
regular     : 0:00:00.116429
destructipy : 0:00:00.509979

9999999 iterations:
regular     : 0:00:01.150795
destructipy : 0:00:05.044853

99999999 iterations:
regular     : 0:00:11.541131
destructipy : 0:00:59.538018

999999999 iterations:
regular     : 0:02:14.472381
destructipy : ... # couldn't wait, guess it's around 10 minutes or so...
```
