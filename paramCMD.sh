#!/bin/bash
#set -u

for param in $@; do
    echo $param
done

echo
while [ -n "$1" ]; do 
    case "$1" in
    -a) echo "found the -a option" ;;
    -b) echo "found the -b option"
        param="$2"
        echo "param b is $param"
        shift;;
    -c) echo -n "found the -c option. Write numbers: "
        read -t 10
        echo $REPLY ;;
    *) echo "$1 is not an option" ;;
    esac 
    shift
done 

echo
count=1
cat ./file.txt | while read line; do
    echo "Line $count: $line"
    count=$(( $count + 1 ))
done