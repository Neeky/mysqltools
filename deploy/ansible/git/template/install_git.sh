cd /tmp/{{mtls_git | replace('.tar.gz','')}}/
./configure --prefix=/usr/local/git && make && make install