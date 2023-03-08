import os
import subprocess
from glob import glob

BRANCH = 'test'

print('-------------------------------------------------')

env = os.environ
for key, val in env.items():
    print('key:{} , val:{}'.format(key, val))

print('-------------------------------------------------')

file_path = '../allfree-web-api/'
query = glob('{}lambda/*'.format(file_path))
os.makedirs('{}/lambda/lambda/'.format(file_path))
for val in query:
    print(val)
    if val == '{}/lambda/insert_sync':
        mv_cmd = 'mv {}lambda/update_sync/lambda_function.py {}lambda/lambda && rmdir {}lambda/insert_sync'.format(
            file_path, file_path, file_path
        )
        cp_cmd = 'cp -r {}commons {}lambda/lambda'.format(file_path, file_path)
        cd_cmd = 'cd {}lambda/lambda && zip -r package.zip ./*'
        aws_cmd = 'aws lambda update-function-code --function-name allfree-web-api-test-insert_sync --zip-file fileb://package.zip --publish'

        subprocess.call(mv_cmd.split())
        subprocess.call(cp_cmd.split())
        subprocess.call(cd_cmd.split())
        subprocess.call(aws_cmd.split())

print('-------------------------------------------------')