#!/bin/sh

command="python generate_data.py $@"

echo $command

trap "exit" SIGINT
while :
do
  echo $(date) Generating data
  $(echo $command)
  sleep 10
done
