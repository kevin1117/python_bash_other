#!/usr/bin/env bash

while read line
 do
        echo $line
        #ssh -i SSHKey 10.204.188.3 'date'
        ssh  root@192.168.1.50 -n 'read sshVar && echo "ssh output:"$sshVar '
done << EOF
1
2
3
4
5
EOF