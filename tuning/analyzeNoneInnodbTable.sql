# 执行当前实例中业务库中的非innodbb表

select concat(table_schema,'.',table_name) as noneInnodbTable from information_schema.tables
    where table_schema not in ('information_schema','performance_schema','mysql','sys') and engine != 'InnoDB';
