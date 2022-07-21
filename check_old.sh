for i in $(cat existing_data.txt);
do
FILES=$(echo "$i") 

if [[ $FILES =~ .*CSV.*|.*upload.*|.*rules.* ]]
then
   echo "Found old files"
   echo "removing $FILES"
   rm -rf $FILES
else
   echo "No files old files found"
fi

done
