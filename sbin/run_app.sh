#!/bin/sh

arguments=""

for keyword in "$@"
do
    key=$(echo $keyword| cut -d = -f 1)
    word=$(echo $keyword| cut -d = -f 2)
    if test $key = "--data_path"; then
        arguments=$(echo "data_path='$word'")
    fi
done

gunicorn "app:create_app($arguments)" --bind 0.0.0.0:80\
         --access-logfile logs/gunicorn-access.log\
         --error-logfile logs/gunicorn-error.log
