import shutil
import os

src = '../Shadow-Thief2/assets'
dst = './assets'

if not os.path.exists(dst):
    shutil.copytree(src, dst)
    print("Assets copied successfully.")
else:
    print("Assets already exists.")
