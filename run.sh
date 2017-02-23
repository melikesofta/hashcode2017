#!/usr/bin/env bash
DATE=`date +%Y_%m_%d_%H_%M_%S`
FILE="outputs/$DATE.txt"

echo ">>>>CODE>>>>>" >> $FILE
cat main.py >> $FILE
echo "" >> $FILE
echo "<<<<CODE<<<<<" >> $FILE
echo "" >> $FILE
echo "" >> $FILE


echo ">>>>OUTPUT>>>>>" >> $FILE
python main.py $@ >> $FILE
echo "" >> $FILE
echo "<<<<OUTPUT<<<<<" >> $FILE
echo "" >> $FILE
echo "" >> $FILE