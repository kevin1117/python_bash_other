#!/bin/sh

mysql -hlocalhost -P3306  -uroot -proot << EOF
use gopub;
update t_action set extra='7891000' where id=1;
EOF

#-------------   -p  需要密码

mysql -hlocalhost -P3306  -uroot -p << EOF
use gopub;
update t_action set extra='7891000' where id=1;
EOF
