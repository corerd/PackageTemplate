"""Example loading a module from the current directory (when python is run)
vs part of a package.

# See: https://stackoverflow.com/a/49480246
"""

print('I am the %s:' % __name__)
if __package__ is None or __package__ == '':
    print('Load SUBMODULEAB from %s using current directory visibility' % __name__)
    import submoduleAB
else:
    print('Load SUBMODULEAB from %s using current package visibility' % __name__)
    from . import submoduleAB
