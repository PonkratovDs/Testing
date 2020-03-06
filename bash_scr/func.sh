#!/bin/bash

function glue_str {
    if [ $# -eq 2 ]; then 
        ans="$1$2"
    else 
        ans"Enter two string"
    fi
}

glue_str "sf" "sfsa"
echo "$ans"

function iter_array {
    local newarray 
    newarray=("$@")
    for value in "${newarray[@]}"; do 
        echo "$value"
    done
}
myarray=(1 "2 3" "4 5")
iter_array "${myarray[@]}"