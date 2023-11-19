
import sys
from cx_Freeze import setup, Executable



base = None


if sys.platform == 'win32':
    base = 'Win32GUI'


exe = Executable(
    script='src/application.py',
    base=base,
)

options = {
    'build_exe' : {
        'excludes' : ['curses', 'email', 'tcl', 'ttk', 'tkinter'],
        'compressed' : True,
        'packages': ['numpy.lib.format']
    }
}



setup(
    name="Pxlee",
    version="0.1",
    description="A Sprite editor and animator",
    executables=[exe],
    options=options, requires=['PyQt5', 'PIL', 'numpy']
)