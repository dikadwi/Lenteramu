import sys
from jinja2 import Environment, FileSystemLoader, meta

paths = [
    'templates/siswa/base_siswa.html',
    'templates/siswa/dashboard_siswa.html'
]

env = Environment(loader=FileSystemLoader('.'))
errors = False
for p in paths:
    try:
        src = open(p, 'r', encoding='utf-8').read()
        ast = env.parse(src)
        # optional: list undeclared variables
        undeclared = meta.find_undeclared_variables(ast)
        print(f"OK: {p} (undeclared vars: {', '.join(sorted(list(undeclared)))[:200]})")
    except Exception as e:
        print(f"ERROR parsing {p}: {e}")
        errors = True

if errors:
    sys.exit(2)
else:
    sys.exit(0)
