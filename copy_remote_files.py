import os
import paramiko
import glob
from paramiko import client
paramiko.util.log_to_file('/tmp/paramiko.log')
# paramiko.util.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))

host = '64.137.221.233'
username = 'krutagna'
password = 'krutagna'
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__)) 


remotepath = '/testData/'
localpath = SCRIPT_DIR +'/'


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, username=username, password=password)

sftp = ssh.open_sftp()

files = sftp.listdir(remotepath)

for file in files:
	print type(file)
	if '.tar.gz' in file:

		file_remote = remotepath + file
    	file_local = localpath + file

    	print file_remote + ' >>> ' + file_local

    	sftp.get(file_remote, file_local)


sftp.close()
ssh.close()