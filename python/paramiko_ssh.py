#!/usr/bin/python
# coding=utf-8

import paramiko



ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect("192.168.1.50",22,"root", "5430696")

stdin, stdout, stderr = ssh.exec_command("ls /")

print stdout.readlines()

ssh.close()