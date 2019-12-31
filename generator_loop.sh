#!/bin/sh

config_fn=$1 

if test -z "$config_fn" 
then
    command="python generate_data.py"
else
    command="python generate_data.py --config_fn="$config_fn
fi

echo $command

trap "exit" SIGINT
while :
do
  echo $(date) Generating data
  $(echo $command)
  sleep 10
done
