#!/usr/bin/env bash

cd /home/ubuntu/MedCATtrainer || exit

systemctl stop nginx.service
docker-compose -f docker-compose-prod.yml up -d --build

exit 0;

