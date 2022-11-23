#!/usr/bin/env bash

cd /home/ubuntu/MedCATtrainer/jupyter || exit

. /home/ubuntu/.nvm/nvm.sh
nvm use lts/hydrogen
/home/ubuntu/.local/bin/jupyterhub -f ./jupyterhub_config.py

exit 0;

