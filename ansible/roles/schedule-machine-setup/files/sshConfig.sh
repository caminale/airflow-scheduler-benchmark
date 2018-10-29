#!/usr/bin/env bash

#PROJECT_PATH=$1
file=inventory.json
touch $file
chmod 777 $file

(cd /usr/bin && exec terraform-inventory --list  /opt/cockroach-ansible-terraform/terraform/terraform.tfstate) > $file

COCKROACH_IP="$(jq '.cockroach' $file)"
echo "${cockroachIP}"

length="$(jq '.cockroach | length' $file)"
echo "${length}"

CONFIG_FILE=config

if [ ! -e "$CONFIG_FILE" ] ; then
    touch "$CONFIG_FILE"
    chmod 777 $CONFIG_FILE
fi

if [  -e "$CONFIG_FILE" ] ; then
    chmod 777 $CONFIG_FILE
    echo "" > $CONFIG_FILE
fi

PREFIX=cockorach

for ((i = 0; i < $length; i++)); do

          echo  " Host $PREFIX$i" >> $CONFIG_FILE
          echo  "   Hostname "$(jq -r --arg index $i '.cockroach | .[$index | tonumber]' $file)" " >> $CONFIG_FILE
          echo  "   IdentityFile ~/.ssh/google_compute_engine" >> $CONFIG_FILE

done