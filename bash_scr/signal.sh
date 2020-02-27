#!/bin/bash
trap "echo bye " EXIT 
for (( i=0; i < 10; i++ )); do 
    echo $i
done