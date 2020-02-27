#!/bin/bash
read -t 100 -p "Enter comment, please: " comment

if [ -z "$comment" ]; then
    echo
    echo "No comment"
else    
    git add -A && git commit -m "$comment" && git push
fi