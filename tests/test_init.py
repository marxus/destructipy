from destructipy import _ as ds
from destructipy import get_tokens, get_line, get_keys

source = '''
from destructipy import _ as ds
abcd = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d, c, \\
b, a = ds.i(abcd)
print(a, b, c, d)
'''.strip().splitlines()


def test_get_tokens():
    assert get_tokens(source) == ('=ds(', '=ds.')


def test_get_line():
    lineidx = 3
    line = source[lineidx]
    assert get_line(lineidx, line, source) == 'd,c,b,a=ds.i(abcd)'


def test_get_key():
    tokens = get_tokens(source)
    lineidx = 3
    line = source[lineidx]
    line = get_line(lineidx, line, source)
    assert get_keys(line, tokens) == ['d', 'c', 'b', 'a']


def test_runtime():
    abcd = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    d, c, \
    b, a = ds.i(abcd)
    assert [a, b, c, d] == [1, 2, 3, 4]
