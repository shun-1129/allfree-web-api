import os
from glob import glob

print('-------------------------------------------------')

env = os.environ
for key, val in env.items():
    print('key:{} , val:{}'.format(key, val))

print('-------------------------------------------------')

file_path = glob('../*')
print(file_path)

print('-------------------------------------------------')