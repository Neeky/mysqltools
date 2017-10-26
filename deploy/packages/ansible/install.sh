#!/bin/bash
#把安装包复制到/tmp/目录下,这样可以不污染mysqltools的相关目录
cp *.tar.gz /tmp/

cd /tmp/
tar -xvf pycparser-2.18.tar.gz -C /tmp/
cd /tmp/pycparser-2.18
python3 setup.py build
python3 setup.py install

cd /tmp/
tar -xvf six-1.11.0.tar.gz -C /tmp/
cd /tmp/six-1.11.0
python3 setup.py build
python3 setup.py install

cd /tmp/
tar -xvf asn1crypto-0.23.0.tar.gz -C /tmp/
cd /tmp/asn1crypto-0.23.0
python3 setup.py build
python3 setup.py install

cd /tmp/
tar -xvf cffi-1.11.2.tar.gz -C /tmp/
cd /tmp/cffi-1.11.2
python3 setup.py build
python3 setup.py install

cd /tmp/
tar -xvf idna-2.6.tar.gz -C /tmp/
cd /tmp/idna-2.6
python3 setup.py build
python3 setup.py install

cd /tmp/
tar -xvf cryptography-2.1.1.tar.gz -C /tmp/
cd /tmp/cryptography-2.1.1/
python3 setup.py build
python3 setup.py install

cd /tmp/
tar -xvf pyasn1-0.3.7.tar.gz -C /tmp/
cd /tmp/pyasn1-0.3.7
python3 setup.py build
python3 setup.py install

cd /tmp/
tar -xvf PyNaCl-1.1.2.tar.gz -C /tmp/
cd /tmp/PyNaCl-1.1.2
python3 setup.py build
python3 setup.py install 

cd /tmp/
tar -xvf bcrypt-3.1.4.tar.gz -C /tmp/
cd /tmp/bcrypt-3.1.4 
python3 setup.py build
python3 setup.py install

cd /tmp/
tar -xvf paramiko-2.3.1.tar.gz -C /tmp/
cd /tmp/paramiko-2.3.1
python3 setup.py build
python3 setup.py install

cd /tmp/
tar -xvf PyYAML-3.12.tar.gz -C /tmp/
cd /tmp/PyYAML-3.12
python3 setup.py build
python3 setup.py install

cd /tmp/
tar -xvf MarkupSafe-1.0.tar.gz -C /tmp/
cd /tmp/MarkupSafe-1.0
python3 setup.py build
python3 setup.py install 

cd /tmp/
tar -xvf Jinja2-2.9.6.tar.gz -C /tmp/
cd /tmp/Jinja2-2.9.6
python3 setup.py build
python3 setup.py install 

cd /tmp/
tar -xvf ansible-2.4.0.0.tar.gz -C /tmp/
cd /tmp/ansible-2.4.0.0
python3 setup.py build
python3 setup.py install 