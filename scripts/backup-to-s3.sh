#!/bin/sh

pwd

DATESTR=$(date +%y%m%d%H%M%S)
TEMPDIR=var/backup/$DATESTR
S3DIR=s3://hhb-x/iamhhb-backup/$DATESTR

mkdir -p $TEMPDIR
python manage.py dumpdata -o $TEMPDIR/data.json
python manage.py dumpfile $TEMPDIR/files.zip

aws s3 cp $TEMPDIR $S3DIR --recursive

rm -r $TEMPDIR
