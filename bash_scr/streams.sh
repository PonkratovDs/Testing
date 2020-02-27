#!/bin/bash

ls -l xfile 2> ./file.txt 

echo 'Error' >&2

cat ./file.txt

echo
exec 0< file.txt 
while read line; do 
    echo $line 
done
exec 0<&-

ls -al badfile anotherfile 2> /dev/null 