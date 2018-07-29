xtrabackup --host=127.0.0.1 --port=3306 --user=backup --password=DX3906 --no-version-check \
 --compress --compress-threads=4 --backup --target-dir=/database/backups/ 

xtrabackup --defaults-file=/etc/my.cnf --host=127.0.0.1 --port=3306 --user=backup --password=DX3906 --no-version-check \
 --compress --compress-threads=4 --use-memory=200M --stream=xbstream  --parallel=8 \
 --backup --target-dir=/database/backups/ >/database/backups/2018.xbstream

  #yum install http://www.percona.com/downloads/percona-release/redhat/0.1-4/percona-release-0.1-4.noarch.rpm

cd /database/backups/

xbstream -x < /database/backups/2018.xbstream

xtrabackup --decompress --target-dir=/database/backups/

for qpf in `find /database/backups/ -iname "*\.qp"`;
do
    echo going to remove ${qpf};
    rm -rf ${qpf};
done


xtrabackup --defaults-file=/etc/my.cnf --host=127.0.0.1 --port=3306 --user=backup --password=DX3906 \
 --compress --compress-threads=4 --use-memory=200M --stream=xbstream  --parallel=8 --no-version-check \
 --extra-lsndir=/database/backups/3306/check_point/2018-07-07T16:58:00 --target-dir=/database/backups/3306/temp/ \
 --backup  >/database/backups/3306/data/2018-07-07T16:58:00/2018-07-07T16:58:00.xbstream

xtrabackup --defaults-file=/etc/my.cnf --host=127.0.0.1 --port=3306 --user=backup --password=DX3906 \
 --compress --compress-threads=4 --use-memory=200M --stream=xbstream  --parallel=8 --no-version-check \
 --extra-lsndir=/database/backups/3306/check_point/2018-07-07T17:58:00 --target-dir=/database/backups/3306/temp/ \
 --incremental-lsn=2589200 \
 --backup  >/database/backups/3306/data/2018-07-07T16:58:00/2018-07-07T17:58:00.xbstream


