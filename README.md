# paramiko
A Python implementation of SSHv2

# Installation of paramiko
pip install paramiko

# Getting started

The primary client of Paramiko as documented in the API, is Paramiko.SSHClient. An instance of the Paramiko.SSHClient can be used to make connections to the remote server and transfer files

MAKING A CONNECTION

import paramiko
ssh_client=paramiko.SSHClient()
ssh_client.connect(hostname=’hostname’,username=’mokgadi’,password=’mypassword’)
#Raises BadHostKeyException,AuthenticationException,SSHException,socket error

when you try this, you get the following error:
missing_host_key raise SSHException(‘Server %r not found in known_hosts’ % hostname) paramiko.ssh_exception.SSHException: Server ‘hostname’ not found in known_hosts

Understanding Known Hosts

You see this error because you have not informed your machine that the remote server you “trust” the server you are trying to access. If you go onto you command line or terminal and try to connect to a server for the first time, You will get a message similar to this:

The authenticity of host ‘hostname’ can’t be established.RSA key fingerprint is ‘key’. Are you sure you want to continue connecting (yes/no)?

When you select yes here, you let your machine know that it can trust the machine and you can now access it without the prompt until the key for that machine changes.
Paramiko similarly requires that you validate your trust with the machine. This validation is handled by calling set_missing_host_key_policy() on the SSHClient an passing the policy you want implemented when accessing a new remote machine. By default, the paramiko.SSHclient sets the policy to the RejectPolicy. The policy rejects connection without validating as we saw above. Paramiko does however give you a way to sort of “Trust all” key policy, the AutoAddPolicy. Parsing an instance of the AutoAddPolicy to set_missing_host_key_policy() changes it to allow any host.

import paramiko
ssh_client =paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=’hostname’,username=’mokgadi’,password=’mypassword’)

You should now be in the green

RUNNING COMMANDS ON THE REMOTE MACHINE
To run a command exec_command is called on the SSHClient with the command passed. The response is returned as a tuple (stdin,stdout,stderr)
For example to list all the files in a directory:

stdin,stdout,stderr=ssh_client.exec_command(“ls”)

Getting the type for each of the returned,
type(stdin) and type(stdout) is ‘paramiko.channel.ChannelFile’
type(stderr) is class ‘paramiko.channel.ChannelStderrFile’

According to paramiko.org they are all python file like objects.

The stdin is a write-only file which can be used for commands requiring input
The stdout file give the output of the command
The stderr gives the errors returned on executing the command. Will be empty if there is no error

for the command above
>>>print(stdout.readlines()) → [u’anaconda-ks.cfg\n’, u’database_backup\n’, u’Desktop\n’, u’Documents\n’, u’Downloads\n’, …. u’Public\n’, u’Templates\n’, u’Videos\n’]

>>>print(stderr.readlines) → []

COMMANDS REQUIRING INPUT
Sometimes you need to provide a password or extra input to run a command. This is what stdin is used for. Let’s run the same command above with sudo.

stdin, stdout, stderr = ssh.exec_command(“sudo ls”)
stdin.write(‘mypassword\n’)
print stdout.readlines()

Should return list of files and folders as above.

FILE TRANSFERS
File transfers are handled by the paramiko.SFTPClient which you get from calling open_sftp() on an instance of Paramiko.SSHClient.

Downloading a file from remote machine

ftp_client=ssh_client.open_sftp()
ftp_client.get(‘remotefileth’,’localfilepath’)
ftp_client.close()

Uploading file from local to remote machine

ftp_client=ssh.open_sftp()
ftp_client.put(‘localfilepath’,remotefilepath’)
ftp_client.close()

