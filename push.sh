#!/bin/bash

comment=$*
if [ -n "$*" ]; then
    git add -A | git commit -m "$comment" | git push
else 
    echo "No comment"
fi