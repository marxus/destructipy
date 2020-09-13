from json import load
from sys import _getframe, modules, path
from operator import attrgetter, itemgetter
from linecache import getline, cache as source_cache

funcs_cache = {}
keys_cache = {}


def get_token(source):
    token = '=__import__("destructipy")'
    for line in source:
        line = line.replace(' ', '').replace("'", '"')
        if token in line:
            return f'={line.split(token)[0].split(";")[-1]}('


def get_multiline(lineidx, line, source):
    multiline = line
    while 1:
        line = source[lineidx - 1].strip()
        if not line.endswith('\\'): break
        line = line.replace('\\', '')
        multiline = f'{line}{multiline}'
        lineidx -= 1
    return multiline.replace(' ', '')


def get_keys(multiline, token):
    return multiline.split(token)[0].split(';')[-1].split(',')


def get_funcs(filename, lineno):
    funcs = funcs_cache.get((filename, lineno))
    if not funcs:
        line = getline(filename, lineno)
        if line:
            source = source_cache[filename][2]
            token = get_token(source)
            multiline = get_multiline(lineno - 1, line, source)
            keys = get_keys(multiline, token)
        else:
            if not keys_cache:
                with open(f'{path[0]}/.destructipy') as file:
                    keys_cache.update(load(file))
            keys = keys_cache[filename][str(lineno)]
        funcs_cache[filename, lineno] = funcs = attrgetter(*keys), itemgetter(*keys)
    return funcs


class __class__(modules[__name__].__class__):
    def __call__(self, item):
        frame = _getframe(1)
        filename, lineno = frame.f_code.co_filename, frame.f_lineno
        funcs = get_funcs(filename, lineno)
        return funcs[hasattr(item, '__getitem__')](item)


modules[__name__].__class__ = __class__
