import sys
import os

print('I am the %s:' % __name__)
print('\tsys.argv[0]: {0!r}'.format(sys.argv[0]))
print('\tsys.path[0]: {0!r}'.format(sys.path[0]))

try:
    user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
    user_paths = []
print('\tPYTHONPATH=', user_paths)

if __package__ is None or __package__ == '':
    print('Load MODULE21 from %s using current directory visibility' % __name__)
    from subpackage2 import module21
else:
    print('Load MODULE21 from %s using current package visibility' % __name__)
    from .subpackage2 import module21
