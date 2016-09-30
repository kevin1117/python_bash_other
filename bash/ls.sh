#!/usr/bin/env bash
echo "zfj"

echo '赋值=左右不能有空格'

#遍历目录

cd /Users/kevinzhang

list=`ls`
for fpath in $list
do
 if [ -f $fpath ];then
    echo "======file";
 else
    echo "#####other"
 fi
done



#打印日期
d=`date '+%Y-%m-%d %H:%M:S'`
echo $d


