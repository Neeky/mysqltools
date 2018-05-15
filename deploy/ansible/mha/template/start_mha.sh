#!/bin/bash

nohup masterha_manager --conf=/etc/masterha/app.cnf --ignore_last_failover < /dev/null > /var/log/masterha/manager.log 2>&1 &