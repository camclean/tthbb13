#!/bin/bash

for site in T2_EE_Estonia T3_CH_PSI; do
	python ~/util/data_replica.py --delete --from LOCAL --to $site to-copy-step2.txt /store/user/jpata/tth/step2/s1_nov19_3a4602f__s2_b7e13a1
done
