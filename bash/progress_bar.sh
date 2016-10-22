#!/bin/bash

x=''

for ((i=0;$i<=100;i+=2))
do
    printf "test:[%-50s]%d%%\r" $x $i
    sleep 0.1

    x=#$x
done
