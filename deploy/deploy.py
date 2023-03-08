import os
from glob import glob

print('-------------------------------------------------')

env = os.environ
for key, val in env.items():
    print('key:{} , val:{}'.format(key, val))

try:
    test = os.environ['branchs']
    print(test)
except:
    raise Exception('Error')

print('-------------------------------------------------')

file_path = glob('../*')
print(file_path)

print('-------------------------------------------------')