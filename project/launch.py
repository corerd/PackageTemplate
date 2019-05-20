
import sys
import os

import package.module0
import submoduleA.submoduleAA

print('I am the %s:' % __name__)
print('\tsys.argv[0]: {0!r}'.format(sys.argv[0]))
print('\tsys.path[0]: {0!r}'.format(sys.path[0]))

try:
    user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
    user_paths = []
print('\tPYTHONPATH=', user_paths)
