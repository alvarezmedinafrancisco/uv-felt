import importlib
m = importlib.import_module('flet')
print('flet version:', getattr(m,'__version__','unknown'))
print('has colors?', hasattr(m,'colors'))
print('module file:', getattr(m,'__file__','<builtin>'))
print('\nSome attrs:')
for a in sorted([x for x in dir(m) if not x.startswith('_')])[:40]:
    print(a)
