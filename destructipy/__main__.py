from json import dump
from os import listdir
from os.path import isdir, islink, relpath
from . import get_token, get_multiline, get_keys


def listdir_recursive(path):
    files = []
    for item in listdir(path):
        item = f'{path}/{item}'
        if islink(item):
            continue
        if isdir(item):
            files.extend(listdir_recursive(item))
        else:
            files.append(relpath(item))
    return files


def gen_cache(file):
    with open(file) as file:
        source = file.read().splitlines()

    token = get_token(source)
    if not token: return

    cache = {}
    for lineidx, line in enumerate(source):
        multiline = get_multiline(lineidx, line, source)
        if token in multiline:
            cache[lineidx + 1] = get_keys(multiline, token)
    return cache


cache = {}
for file in listdir_recursive('.'):
    if file.endswith('.py'):
        _cache = gen_cache(file)
        if _cache:
            cache[file] = _cache

with open('.destructipy', 'w') as file:
    dump(cache, file)
