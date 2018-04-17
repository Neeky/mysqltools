cd /tmp/{{mtls_nginx | replace('.tar.gz','')}}/
./configure --prefix=/usr/local/{{mtls_nginx | replace('.tar.gz','')}}/ --user=nginx --group=nginx --with-http_ssl_module && make && make install && chown -R nginx:nginx /usr/local/{{mtls_nginx | replace('.tar.gz','')}}

