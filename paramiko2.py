"""
File transfer to and from remote machine

"""

import paramiko
import os

presentDir= os.path.abspath(os.path.dirname(__file__))

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh_client.connect(hostname='10.47.12', username='sa186063',
                  password='Docker@123')

localfilepath = presentDir + '/README.md'
remotefilepath = '/home/sa186063/paramiko/README.txt'

print 'Uploading a file from local to remote machine'
ftp_client = ssh_client.open_sftp()
ftp_client.put(localfilepath, remotefilepath)
ftp_client.close()

localfilepath = presentDir + '/README.txt'
remotefilepath = '/home/sa186063/paramiko/README.txt'

print 'Downloading a file from remote machiine'
ftp_client = ssh_client.open_sftp()
ftp_client.get(remotefilepath, localfilepath)
ftp_client.close()

print 'Removing downloaded file'
os.remove(localfilepath)
