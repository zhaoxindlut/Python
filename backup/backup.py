#coding: utf-8
#!/usr/bin/python
#Filename : backup.py
#用于文件备份的python脚本,会按照日期创建目录并将备份文件保存到对应的目录下
import os 
import time

#需要备份的文件路径，保存在list中，每个条目表示一条需要备份的路径
source = [r'C:\Users\xiaoxin\Desktop\POX\ESLOFDP\pox\pox\openflow\discovery.py']

#设置备份路径，字符串前添加r表示该字符串不需要进行转义等操作，为自然字符串
#linux系统路径为 '/usr/bin' 等，注意路径格式
target_dir = r'C:\Users\xiaoxin\Desktop\backup\backup'

today = target_dir + time.strftime('%y%m%d')
now = time.strftime('%H%M%S')

# Take a comment from the user to create the name of the zip file
#设置备份文件的名称格式
comment = raw_input('Enter a comment --> ')
if len(comment) == 0: # check if a comment was entered
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip' 

if not os.path.exists( today ):
    os.mkdir( today )
    print 'Successfully created directory', today

#采用压缩工具进行压缩，不同压缩工具需要更改zip为相应的命令
#makecab 为windows命令行自带的压缩命令，没有zip好用啊
zip_command = "makecab %s %s" %( ''.join(source), target )

#执行备份命令
if os.system( zip_command ) == 0:
    print 'Successful backup to', target_dir
else:
    print 'Backup Failed'