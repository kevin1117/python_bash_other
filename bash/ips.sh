#/bin/bash
IPS="10.1.1.10 3001
10.1.1.10 3003
10.1.1.11 3001
10.1.1.11 3002
10.1.1.11 3004
10.1.1.11 3005
10.1.1.13 3002
10.1.1.13 3003
10.1.1.13 3004
10.1.1.14 3002"
echo "====while test ===="
i=0

echo $IPS | while read line
do
    echo $(($i+1))
    echo $line
done


echo "====for test ===="
n=0
for ip in $IPS ;
do
   n=$(($n+1))
   echo $ip
   echo $n
done