cd /tmp/{{mtls_nginx | replace('.tar.gz','')}}/
./configure --prefix=/usr/local/nginx/ --user=nginx --group=nginx --with-http_ssl_module && make && make install

