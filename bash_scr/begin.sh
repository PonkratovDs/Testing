#!/bin/bash

echo "Current directory:"
pwd

echo "Home dir is: $HOME"

echo "\$1"

dir="/home"
echo $dir

curr_dir=$(pwd)
echo $curr_dir

sum=$(( 10 + 235 ))
echo $sum

if pwd
then 
echo $sum
fi

if grep -i "bdgdf*" * | whoami
then 
echo "find"
elif pwd
then 
echo pwd
else 
echo whoami
fi

if [ 6 -gt 5 ]
then 
echo 6
fi

user="saf"
if [ $user != $USER ] && [ $user \> "$USER" ]
then 
echo $USER
fi

if [ -d $HOME ]
then
cd -e $hostname
ls
fi