import glob
import os

#pathを全て受け取る
"""
files = glob.glob("./images/*")
for file in files:
    print(file)
"""

#file名を受け取る
path = "./images"

files = os.listdir(path)
print(files)        # ['dir1', 'dir2', 'file1', 'file2.txt', 'file3.jpg']