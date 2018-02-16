#!/bin/bash
######## - $1 - file list $2 - file path
files_list=`cat $1`
PWD=`pwd`
for file_name in $files_list;
do
	complete_filename=$2'/'$file_name
	echo "Starting the command"
	mkdir log
	log_path=$PWD/"log"
	echo $log_path
	cmd="./bin/darknet_detections -r $complete_filename"
	time $cmd | tee $log_path'/'$file_name
	echo $cmd
	echo "Command execution complete"
done
wait
echo "Done"
