select (@@innodb_buffer_pool_size +
    @@innodb_log_buffer_size +
    @@key_buffer_size +
    @@innodb_sort_buffer_size +
    @@innodb_online_alter_log_max_size +
    @@max_connections *(@@bulk_insert_buffer_size + @@sort_buffer_size + @@read_buffer_size + @@read_rnd_buffer_size + @@binlog_cache_size) +
    @@max_connections * @@thread_stack) /1024/1024/1024 as totalGB;