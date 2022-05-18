#!/bin/bash

img_dir="./wallpaper"
cache_dir="./cache"
if [[ ${OSTYPE} == "linux"* ]];then
    word_count="wc --lines"
elif [[ ${OSTYPE} == "darwin"* ]];then
    word_count="wc -l"
else
    echo "Unsupported system of ${OSTYPE}"
    exit 2
fi


if [ -d wallpaper ];then
    true
else
    mkdir wallpaper
fi

# wget -O ${cache_dir}/bing-wallpaper.md https://raw.githubusercontent.com/niumoo/bing-wallpaper/main/bing-wallpaper.md

wget -O ${cache_dir}/bing-wallpaper.md https://raw.staticdn.net/niumoo/bing-wallpaper/main/bing-wallpaper.md


line_num=`${word_count} ${cache_dir}/bing-wallpaper.md | awk '{print $1}'`
if [ -f ${cache_dir}/bing-wallpaper.md ] && [ ${line_num} != 0 ]
then
    true
else
    exit 1
fi


sed -n '2,$p' ${cache_dir}/bing-wallpaper.md > ${cache_dir}/tmp

sed -e '/^$/d' -e 's/^20\(.*-[0-9][0-9]\).*$/\1/g' -e 's/-//g' ${cache_dir}/tmp > ${cache_dir}/dates
sed -e '/^$/d' -e 's/^.*\(https.*\.jpg\).*$/\1/g' ${cache_dir}/tmp > ${cache_dir}/urls
sed -n '1p' ${cache_dir}/tmp | sed 's/^.*\[\(.*\)\].*$/\1/' > ${cache_dir}/today

line_num=`${word_count} ${cache_dir}/dates | awk '{print $1}'`
for ((i=1; i<=line_num; i++));do
    img_date=`cat ${cache_dir}/dates | head -n ${i} | tail -n 1`
    img_url=`cat ${cache_dir}/urls | head -n ${i} | tail -n 1`

    if [ -f "${img_dir}/BW-${img_date}.jpg" ];then
        true
    else
        wget -O "${cache_dir}/img_cache" ${img_url}
        mv "${cache_dir}/img_cache" "${img_dir}/BW-${img_date}.jpg"
    fi
done


python3 generate_html.py

line_num=`${word_count} html/bing.html | awk '{print $1}'`
if [ ${line_num} != 0 ];then
    cp html/bing.html wallpaper/
else
    exit 1
fi

rm -f ${cache_dir}/img_cache ${cache_dir}/tmp wget-log

exit 0


