print('I am the %s:' % __name__)
if __package__ is None or __package__ == '':
    print('Load MODULE12 from %s using current directory visibility' % __name__)
    import module12
else:
    print('Load MODULE12 from %s using current package visibility' % __name__)
    from . import module12
