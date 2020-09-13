# destructipy
es6 style dict/object destructure for python

#### install:
```
$ pip install destructipy
```

#### usage:
```python
# must import this way...
import destructipy as ds

# support dicts
abcd = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# destructipy.i()/destructipy.item() - using operator.itemgetter
# dict safe, will probably raise error if not dict
d, c, \
b, a = ds.i(abcd)
print(a, b, c, d)
```
```python
# func can be named however you wish...
import destructipy as unpack

# supports objects
class ABCD:
    a = 1
    b = 2
abcd = ABCD()
abcd.c = 3
abcd.d = 4

# destructipy.a()/destructipy.attr() - using operator.attrgetter
# notice: dicts can also be passed but it will get their attributes, not items)
d, c, \
b, a = unpack.a(abcd)
print(a, b, c, d)
```
```python
import destructipy as ds

abcd_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

class ABCD:
    a = 5
    b = 6
abcd_obj = ABCD()
abcd_obj.c = 7
abcd_obj.d = 8

# destructipy() - auto decide if it's dict or object
# good for one time or mixed dict-object/small lists
# got minor performance penalty, see benchmark below
d, c, b, a = ds(abcd_dict)
print(a, b, c, d)

d, c, b, a = ds(abcd_obj)
print(a, b, c, d)
```

#### caveats:  
* Does not work on the Interactive Python Console (no source to analyze...)
* If you plan to compile your `.py` to `.pyc` and delete the source, run `$ python -m destructipy` in your project root to create `.destructipy` cache file before doing so
* It is recommended to place a `import destructipy` on your project init for destructipy to keep the initial cwd (current working directory), just incase you switch the cwd later on using `os.chdir` or such...

#### benchmark:
```
$ python benchmark.py

9 iterations:
regular   : 0:00:00.000005
ds        : 0:00:00.000093
ds.i/ds.a : 0:00:00.000022

99 iterations:
regular   : 0:00:00.000015
ds        : 0:00:00.000059
ds.i/ds.a : 0:00:00.000054

999 iterations:
regular   : 0:00:00.000157
ds        : 0:00:00.000579
ds.i/ds.a : 0:00:00.000537

9999 iterations:
regular   : 0:00:00.001400
ds        : 0:00:00.005192
ds.i/ds.a : 0:00:00.004649

99999 iterations:
regular   : 0:00:00.012717
ds        : 0:00:00.049448
ds.i/ds.a : 0:00:00.043185

999999 iterations:
regular   : 0:00:00.119332
ds        : 0:00:00.432324
ds.i/ds.a : 0:00:00.407021

9999999 iterations:
regular   : 0:00:01.137975
ds        : 0:00:04.321336
ds.i/ds.a : 0:00:04.119790

99999999 iterations:
regular   : 0:00:11.641548
ds        : 0:00:53.457250
ds.i/ds.a : 0:00:51.059966

999999999 iterations:
regular   : 0:02:23.456980
ds        : ... # couldn't wait
ds.i/ds.a : ... # guess it's around 10 minutes or so...
```
