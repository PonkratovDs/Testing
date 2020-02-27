#!/bin/bash
read -t 100 -p "Enter comment, please: " comment

if ! [ -z "$comment" ]; then
    git add -A && git commit -m "$comment" && git push
else    
    echo
    echo "No comment"
fi