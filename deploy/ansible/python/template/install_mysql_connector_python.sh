#!/bin/bash

cd /tmp/{{mtls_mysql_connector_python | replace('.tar.gz','')}}
python3 setup.py build
python3 setup.py install
