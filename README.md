# paramiko
A Python implementation of SSHv2

Installation of paramiko
pip install paramiko=2.4.2
pip install cryptography=2.4.2 (If error msg appeared)

# Getting started

The primary client of Paramiko as documented in the API, is Paramiko.SSHClient. An instance of the Paramiko.SSHClient can be used to make connections to the remote server and transfer files

MAKING A CONNECTION

import paramiko
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=’hostname’,username=’mokgadi’,password=’mypassword’)

RUNNING COMMANDS ON THE REMOTE MACHINE
stdin,stdout,stderr=ssh_client.exec_command(“ls”)

Getting the type for each of the returned,
type(stdin) and type(stdout) is ‘paramiko.channel.ChannelFile’
type(stderr) is class ‘paramiko.channel.ChannelStderrFile’

According to paramiko.org they are all python file like objects.

The stdin is a write-only file which can be used for commands requiring input
The stdout file give the output of the command
The stderr gives the errors returned on executing the command. 
	Will be empty if there is no error
