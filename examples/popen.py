import os, sys, subprocess
from subprocess import Popen
from multiprocessing import forkserver

pythonw = os.path.dirname(sys.executable) + '/pythonw.exe'

p = Popen([pythonw, 'examples/share.py'], start_new_session=True, stdout=subprocess.DEVNULL)

