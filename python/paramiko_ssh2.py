# coding=utf-8

import paramiko
import traceback

def sshclient_execmd(hostname, port, username, password, execmd):
    paramiko.util.log_to_file("paramiko.log")

    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    s.connect(hostname=hostname, port=port, username=username, password=password)
    stdin, stdout, stderr = s.exec_command (execmd)
    stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.

    for line in stdout.readlines():
        print  line ,  # ,用于不换行

    s.close()



def main():
    try:
        hostname = '192.168.1.50'
        port = 22
        username = 'root'
        password = '5430696'
        #execmd = "cat /proc/cpuinfo"
        execmd = "ls /"

        sshclient_execmd(hostname, port, username, password, execmd)

    except  Exception,e:
        print e


if __name__ == "__main__":
    main()
