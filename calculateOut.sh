#!/bin/bash

tt=/tmp/blabla.py
find StudentProblem -type f -name "*.py" -print0 | while read -d $'\0' file
do
  if [ -e "$tt" ]; then
     rm "$tt"
  fi
  mkdir -p `dirname output/"$file"`
  LC_ALL=C tr -dc '\0-\177' < "$file" > $tt
  if [ ! -e "$tt" ]; then
     echo "tr error, could not create file $tt from $file"
     return
  fi
  echo "Processing file ${file}..."
  # how many seconds before a timeout
  to=4
  timeout $to pytest "$tt" > output/"$file" 2>&1
done
