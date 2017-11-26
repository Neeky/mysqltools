create user {{mysql_mha_user}}@'%' identified by '{{ mysql_mha_password }}' ;
grant all on *.* to {{mysql_mha_user}}@'%' ;