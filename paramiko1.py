"""
Simple program to run ls command to remote machine

"""

import paramiko

# Making a connection
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname="10.47.12.77", username="sa186063", 
                   password="Docker@123")

# Running commands on the remote machine
stdin, stdout, stderr = ssh_client.exec_command("ls")
#print "stdin: ", stdin
print "stdout: ", stdout.readlines()
print "stderr: ", stderr.readlines()

# Commands requiring input

stdin, stdout, stderr = ssh_client.exec_command("sudo ls")
stdin.write("Docker@123\n")
print stdout.readlines()
