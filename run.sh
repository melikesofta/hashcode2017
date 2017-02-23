#!/usr/bin/env sh
DATE=`date +%Y_%m_%d_%H_%M_%S`
FILE="outputs/$DATE.txt"

RESULT=$(python main.py $@)
echo ">>>>CODE>>>>>" >> $FILE
cat main.py >> $FILE
echo "" >> $FILE
echo "<<<<CODE<<<<<" >> $FILE
echo "" >> $FILE
echo "" >> $FILE


echo ">>>>OUTPUT>>>>>" >> $FILE
echo $RESULT >> $FILE
echo "" >> $FILE
echo "<<<<OUTPUT<<<<<" >> $FILE
echo "" >> $FILE
echo "" >> $FILE
echo "$RESULT"
echo "$RESULT" > out_files/$1.out
