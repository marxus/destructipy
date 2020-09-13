# destructipy
es6 style dict/object destructure for python

#### install:
```
$ pip install destructipy
```

#### usage:
```python
# must import this way...
ds = __import__('destructipy')

# support dicts using operator.itemgetter
abcd = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# supports multiline
d, c, \
b, a = ds(abcd)

print(a, b, c, d)
```
```python
# func can be named however you wish...
unpack = __import__('destructipy')

# supports objects as well using operator.attrgetter
class ABCD:
    a = 1
    b = 2
abcd = ABCD()
abcd.c = 3
abcd.d = 4

d, c, b, a = unpack(abcd)

print(a, b, c, d)
```

#### caveats:  
* Does not work on the Interactive Python Console
* If you plan to compile your .py to .pyc and delete the source, run the following in your root folder to create .destructipy cache file 
```
$ python -m destructipy
```

#### benchmark:
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
destructipy : ... # couldn't wait, guess it's around 12 minutes or so...
```
