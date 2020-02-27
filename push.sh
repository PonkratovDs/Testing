#!/bin/bash

if [ -n "$*" ]; then
    git add -A | git commit -m $* | git push
else 
    echo "No comment"
fi