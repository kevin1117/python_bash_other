#!/usr/bash
#echo "pls input your name:"
#read line
#printf "myname is  %s"  $line


str=''
for ((i=0;$i<=5;i+=2))
do
  printf "%-50s\r" $str
   sleep 0.1
   str=#$str
done

sleep 1
printf  "%s\r"  "----"
sleep 1
printf  "%s\r"  "##########"
sleep 1

echo "aaaa"
echo  -e "eeeeeeee/r"