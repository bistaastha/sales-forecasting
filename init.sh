#!/bin/bash

source env/bin/activate
export ACCESS_KEY_ID=
export ACCESS_KEY_SECRET=
export BUCKET_NAME='foldercsv'
export FLASK_APP=app.py

echo "Do you want to update the dataset?(y/n)(default: no)"

read character

if [ "$character" = "y" ] || [ "$character" -eq "Y" ] ; then
rm -rf /data/out.csv
python3  config_download.py
fi

export FLASK_APP=app.py
flask run