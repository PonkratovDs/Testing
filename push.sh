#!/bin/bash

comment=$1
if [ -n "$1" ]; then
    git add -A | git commit -m $comment | git push
else 
    echo "No comment"
fi