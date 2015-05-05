#!/bin/sh

while :
do
	message=$(date +"%k")
	res=$(($message))
	echo ${res}

	if test ${res} -gt 17 -a ${res} -lt 23 ; then
		echo "start zanryu.py"
		python zanryu.py
		break
		
	else
		sleep 3600
		./zanryu.sh 1>out/out.txt &
		break

	fi

done

exit 0
