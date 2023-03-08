import os
from glob import glob

print('-------------------------------------------------')
print(os.environ)
print('-------------------------------------------------')

file_path = glob('/lambda/')
print(file_path)