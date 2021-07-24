import glob
import shutil
import os

os.chdir('/home/jmartin/working_dir')
dst_dir = "/home/jmartin/working_dir"

for f in os.listdir():

    for i in range(902,961):
        name = f.split(".")[0]
        name = f'{i:04}'+ ".png"
        shutil.copy(f,name)