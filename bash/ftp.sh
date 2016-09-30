#!/usr/bin/env bash

#ftp data to 10.178.37.244
rq=`date +%Y%m%d`
cd /data/product/song
ftp -i -n <<!
open 10.178.37.244
user oracle post
cd ems
bin
put ${rq}.dat
bye
!