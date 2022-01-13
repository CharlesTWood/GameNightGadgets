import os
import shutil

try:
    os.remove('app/website/dev.db')
except: pass

try:
    shutil.rmtree('app/migrations')
except: pass

os.system('flask db init')
os.system('flask db migrate')
os.system('flask db upgrade')