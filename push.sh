#!/bin/bash

comment=$1

git add -A | git commit -m $comment | git push