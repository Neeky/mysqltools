#!/bin/bash
cd /tmp/{{ mtls_apr | replace('.tar.gz','') }} ;
./configure --prefix=/usr/local/apr && make && make install