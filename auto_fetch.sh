#!/bin/bash

while true
do
    ./fetch.sh
    r_code=$?
    if [ ${r_code} = 1 ];then
        sleep 180
        continue
        echo -e "-> Fetch failed.\n   Retry in 3 mins."
    elif [ ${r_code} = 0 ];then
        sleep 3600
    else
        exit 1
    fi
done


