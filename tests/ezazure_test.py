from os import remove
from os.path import isfile
from platform import python_version
from random import random
from subprocess import run

from ezazure import Azure

def safe_remove(fname: str):
    if isfile(fname):
            remove(fname)


def test_api_download():
    fname = 'test0.file'
    try:
        safe_remove(fname)
        Azure().download(fname)
        assert(open(fname, 'r').read().strip() == '0')
    finally:
        safe_remove(fname)


def test_api_upload():
    fname = f'test1.{python_version()}.file'
    try:
        value = f'{random()}'
        with open(fname, 'w') as file:
            print(value, file=file)
        Azure().upload(fname)
        safe_remove(fname)
        assert(not isfile(fname))
        Azure().download(fname)
        assert(open(fname, 'r').read().strip() == value)
    finally:
        safe_remove(fname)


def test_cli_download():
    fname = 'test0.file'
    try:
        safe_remove(fname)
        run(f'python ezazure {fname} --download'.split())
        assert(open(fname, 'r').read().strip() == '0')
    finally:
        safe_remove(fname)


def test_cli_upload():
    fname = f'test1.{python_version()}.file'
    try:
        value = f'{random()}'
        with open(fname, 'w') as file:
            print(value, file=file)
        run(f'python ezazure {fname} --upload'.split())
        safe_remove(fname)
        assert(not isfile(fname))
        run(f'python ezazure {fname} --download'.split())
        assert(open(fname, 'r').read().strip() == value)
    finally:
        safe_remove(fname)


if __name__ == '__main__':
    test_api_download()
    test_api_upload()
    test_cli_download()
    test_cli_upload()
