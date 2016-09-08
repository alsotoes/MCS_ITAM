#!/bin/bash

for i in $(seq 0 50 1000000)
do
	sort=$(./mergeSortLinkedList.out ${i})
	echo ${sort},${i}
done
