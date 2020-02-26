#!/bin/bash

for var in first 2 "third sf"
do 
echo The $var item 
done

IFS=$'\n'
for var in $(cat loop.sh)
do 
echo $var 
done

for (( i=1; i<=10; i++ ))
do
echo $i 
done 

var1=5
sum=0
while [ $var1 -gt 0 ]
do
sum=$[ $sum + $var1 ]
if [ $sum -eq 5 ]
then 
break
fi
var1=$[ $var1 - 1 ]
done 
echo $sum

for (( var1 = 1; var1 < 15; var1++ ))
do 
if [ $var1 -gt 5 ] && [ $var1 -lt 10 ]
then 
continue
fi
echo "Iteration number: $var1"
done