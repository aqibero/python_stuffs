#! /usr/bin/env python
# Download file via paramiko sshclient
# February 1, 2019 - Arnold Ibero

import os
import socket
from paramiko import *
import paramiko

host = "192.168.236.100"
ssh_port = "22"
name = "ansible"
passwd = "**********"
target_file = 'ansible-rtpa.zip'
destination = 'C:\Temp\\rtpa.zip'

client = SSHClient()
#client.load_system_host_keys()
client.set_missing_host_key_policy(AutoAddPolicy())
client.connect(hostname=host, port=ssh_port, username=name, password=passwd)
stdin, stdout, stderr = client.exec_command('ls -ltrh')
print stdout.readlines()

ftpclient = client.open_sftp()
# Download syntax
ftpclient.get("/home/ansible/" + target_file, destination)
ftpclient.close()
client.close()
