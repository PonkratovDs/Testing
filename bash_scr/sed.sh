#!/bin/bash

echo "/Four five" | sed -e 's!/Fo!/jo!; s/fi/vi/'
sed -e '1,$s/xfile/bla-bla/g' file.txt 
sed -e '/ls/s/Error/bla-bla/g' file.txt 
sed '1d' file.txt
sed '/Error/, /fo/d' file.txt
sed -n '/Er/=' file.txt