#!/bin/bash

file=lines.txt
count=0
while read file
do
	count=$((count + 1))
	tesseract --psm 3 --oem 3 "$file" output$count
done
