for i in $(cat check_old_files.txt);
do
FILES=$(echo "$i") 
echo "$FILES" 

if [[ $FILES =~ .*CSV.*|.*upload.*|.*rules.* ]]
then
   echo "removing $FILES"
   rm -rf $FILES
fi

done
