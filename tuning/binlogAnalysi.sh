mysqlbinlog -v -v --base64-output=decode-rows mysql-bin.000051 | awk '/###/{if($0~/UPDATE|INSERT|DELETE/)count[$2""$NF]++}END{for(i in count)print i,"\t",count[i]}' | column -t | sort -k3nr | more

---- output like this -----
DELETE`tempdb`.`sbtest10`  3
DELETE`tempdb`.`sbtest1`   2
INSERT`tempdb`.`sbtest8`   12744
INSERT`tempdb`.`sbtest9`   12547

