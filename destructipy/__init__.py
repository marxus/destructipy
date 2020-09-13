from json import load
from os import getcwd
from sys import _getframe, modules
from os.path import isabs, abspath, relpath
from operator import attrgetter, itemgetter
from linecache import getline, cache as source_cache

cwd = getcwd()
funcs_cache = {}
keys_cache = {}


def get_tokens(source):
    token = 'importdestructipy'
    for line in source:
        line = line.replace(' ', '')
        if token in line:
            line = line.split(token)[1].split(';')[0]
            token = line[2:].strip() if line else 'destructipy'
            return f'={token}(', f'={token}.'


def get_multiline(lineidx, line, source):
    multiline = line
    while 1:
        line = source[lineidx - 1].strip()
        if not line.endswith('\\'): break
        line = line.replace('\\', '')
        multiline = f'{line}{multiline}'
        lineidx -= 1
    return multiline.replace(' ', '')


def get_keys(multiline, tokens):
    return multiline.split(tokens[tokens[1] in multiline])[0].split(';')[-1].split(',')


def get_funcs(frame):
    lineno = frame.f_lineno
    funcs = funcs_cache.get((frame, lineno))
    if not funcs:
        filename = frame.f_code.co_filename
        if not isabs(filename):
            filename = abspath(f'{cwd}/{filename}')
        line = getline(filename, lineno)
        if line:
            source = source_cache[filename][2]
            tokens = get_tokens(source)
            multiline = get_multiline(lineno - 1, line, source)
            keys = get_keys(multiline, tokens)
        else:
            if not keys_cache:
                with open(f'{cwd}/.destructipy') as file:
                    keys_cache.update(load(file))
            keys = keys_cache[relpath(filename, cwd)][str(lineno)]
        funcs_cache[frame, lineno] = funcs = attrgetter(*keys), itemgetter(*keys)
    return funcs


class __class__(modules[__name__].__class__):
    __call__ = lambda self, _: get_funcs(_getframe(1))[hasattr(_, '__getitem__')](_)
    a = attr = lambda self, a: get_funcs(_getframe(1))[0](a)
    i = item = lambda self, i: get_funcs(_getframe(1))[1](i)


modules[__name__].__class__ = __class__
