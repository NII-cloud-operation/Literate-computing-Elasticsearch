#!/bin/sh

if [ $# != 2 ];then
    echo "Input params <$#> should be 2. <input> <output>."
    exit 1
fi

# 二重実行プロセス削除
sudo ps -aux | grep "sh ${0##*/}" | grep -v "grep" | awk '{ print $2 }' | grep -v $$ | xargs -I process sudo kill -9 process >/dev/null 2>&1

COUNT=0
PRE_EPOC_SEC=$(head -n 1 $1 | cut -d',' -f2 | sed -e "s/\"//g" | cut -d'.' -f1)

while read line
do
  NOW_DATE=$(date "+%s")
  #NOW_DATE=$(expr $NOW_DATE \* 1000)
  EPOC_SEC=$(echo $line  | cut -d',' -f2 | sed -e "s/\"//g" | cut -d'.' -f1)
  COUNT=`expr $COUNT + 1`

  EPOC_DIFF=`expr $EPOC_SEC - $PRE_EPOC_SEC`
  if [ $EPOC_DIFF -ge 1 ];then
    sleep $EPOC_DIFF
    PRE_EPOC_SEC=$EPOC_SEC
  fi
  echo "\"$NOW_DATE\",$line" >> $2
done < $1
