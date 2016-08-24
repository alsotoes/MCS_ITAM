#!/bin/bash

for i in $(seq 0 50 500000)
do
	sort=$(./insertionSortLinkedList.out ${i})
	echo ${sort},${i}
done
