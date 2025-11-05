from app import app as application
import sys
import os

INTERP = os.path.expanduser(
    "/home/USERNAME/virtualenv/PATH_TO_VENV/bin/python")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())
