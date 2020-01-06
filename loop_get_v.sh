#!/usr/bin/env bash

OUT_FILE=out.txt

# echo "time,v1,v2" >> $OUT_FILE

while true; do
  date >> $OUT_FILE
  echo get_v >> $OUT_FILE
  echo . >> $OUT_FILE
  echo . >> $OUT_FILE
  sleep 10
done
