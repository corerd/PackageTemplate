print('I am the %s:' % __name__)
if __package__ is None or __package__ == '':
    print('Load MODULE11 from %s using current directory visibility' % __name__)
    from package.subpackage1 import module11
else:
    print('Load MODULE11 from %s using current package visibility' % __name__)
    from ..subpackage1 import module11
