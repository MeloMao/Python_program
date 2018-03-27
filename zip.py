#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import time

source = 'E://tmp'
target_dir = 'E://backup'

target = target_dir + os.sep + \
         time.strftime('%Y-%m-%d %H%M%S')	+	'.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command=('rar a "%s" "%s"'%(target,''.join(source)))

print('Zip	command	is:')
print(zip_command)
print('Running:')
if	os.system(zip_command)	==	0:
    print('Successful	backup	to',	target)
else:
    print('Backup	FAILED')