mysqlbinlog -v -v --base64-output=decode-rows mysql-bin.000051 | awk '/###/{if($0~/UPDATE|INSERT|DELETE/)count[$2""$NF]++}END{for(i in count)print i,"\t",count[i]}' | column -t | sort -k3nr | more

---- output like this -----
DELETE`tempdb`.`sbtest10`  3
DELETE`tempdb`.`sbtest1`   2
DELETE`tempdb`.`sbtest12`  1
DELETE`tempdb`.`sbtest13`  1
DELETE`tempdb`.`sbtest14`  4
DELETE`tempdb`.`sbtest15`  5
DELETE`tempdb`.`sbtest16`  1
DELETE`tempdb`.`sbtest2`   1
DELETE`tempdb`.`sbtest3`   4
DELETE`tempdb`.`sbtest5`   2
DELETE`tempdb`.`sbtest6`   2
DELETE`tempdb`.`sbtest7`   1
DELETE`tempdb`.`sbtest8`   1
DELETE`tempdb`.`sbtest9`   4
INSERT`tempdb`.`sbtest10`  12777
INSERT`tempdb`.`sbtest11`  12794
INSERT`tempdb`.`sbtest1`   12555
INSERT`tempdb`.`sbtest12`  12595
INSERT`tempdb`.`sbtest13`  12436
INSERT`tempdb`.`sbtest14`  12640
INSERT`tempdb`.`sbtest15`  12573
INSERT`tempdb`.`sbtest16`  12565
INSERT`tempdb`.`sbtest2`   12782
INSERT`tempdb`.`sbtest3`   12699
INSERT`tempdb`.`sbtest4`   12693
INSERT`tempdb`.`sbtest5`   12702
INSERT`tempdb`.`sbtest6`   12621
INSERT`tempdb`.`sbtest7`   12573
INSERT`tempdb`.`sbtest8`   12744
INSERT`tempdb`.`sbtest9`   12547

