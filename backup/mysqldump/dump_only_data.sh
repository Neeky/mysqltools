#!/bin/bash

mysqldump --skip-extended-insert --no-create-db --no-create-info \
          --skip-lock-tables --skip-add-locks --set-gtid-purged=OFF --single-transaction \
          --databases tempdb > /tmp/tempdb.sql
