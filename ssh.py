#!/usr/bin/env python
import paramiko
import os, sys,glob 
import tarfile
import json
import xlrd
from xlrd import open_workbook
from json import loads, dumps
from pprint import pprint
from os import path, system, listdir, walk
from paramiko import client
import time

host = '64.137.221.233'
username = 'krutagna'
password = 'krutagna'
# SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

localpath = 'D:/ZipFiles/'
remotepath = '/testData/'

start_time = time.clock()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, username=username, password=password)

stdin, stdout, stderr = ssh.exec_command("find /testData/ -name '*.tar.gz' ")
output = stdout.read()
sftp = ssh.open_sftp()
# files = sftp.listdir(remotepath) 
 
for file in output.splitlines():
	try:
		file_name = path.basename(file)
		file_remote = file
		file_local = localpath + file_name
		sftp.get(file_remote, file_local)	
	except Exception,e:
			print "Error: " + str(e)
			continue	

updatepath = localpath + 'ExtractedFiles/'

data = {}

for tarFile in glob.glob1(localpath,'*.tar.gz'):
	try:	
		tar = tarfile.open(localpath + tarFile) 
		new_path = updatepath + tarFile
		tar.extractall(new_path)
		tar.close()

		data[tarFile] = {}

		for excelfile in glob.glob1(new_path,'*.xlsx'):
			book = xlrd.open_workbook(new_path + '/' + excelfile)
			sheetnames = book.sheet_names()

			data[tarFile][excelfile] = {}

			for index, sheetnames in enumerate(sheetnames,1):
				data[tarFile][excelfile][index] = sheetnames
			
	except Exception, e:
		print "Error: "+tarFile + " " +str(e)
		continue

print json.dumps(data, indent = 4, sort_keys = True)

print("----%s minutes---" % ((time.clock() - start_time)/60))
sftp.close()
ssh.close()	