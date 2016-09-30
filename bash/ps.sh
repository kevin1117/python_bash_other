#!/usr/bin/env bash

echo "============"

process=`ps -ef|grep java `

for p in $process :
do
  echo "====:"$p
done


echo "======while read line: all "
ps -ef | grep java | while read line
do
    echo $line
done

echo "======while read line: awk"

ps -ef | grep java |awk -F ' ' '{print $2}'| while read line
do
    echo $line
done