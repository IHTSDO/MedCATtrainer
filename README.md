 # Medical <img src="https://github.com/CogStack/MedCATtrainer/blob/master/webapp/frontend/src/assets/cat-logo.png" width=45>oncept Annotation Tool Trainer

[![Build Status](https://github.com/CogStack/MedCATtrainer/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/CogStack/MedCATtrainer/actions/workflows/qa.yml?query=branch%3Amaster)
[![Build Status](https://github.com/CogStack/MedCATtrainer/actions/workflows/qa.yml/badge.svg?branch=master)](https://github.com/CogStack/MedCATtrainer/actions/workflows/qa.yml?query=branch%3Amaster)
[![Build Status](https://github.com/CogStack/MedCATtrainer/actions/workflows/release.yml/badge.svg?branch=master)](https://github.com/CogStack/MedCATtrainer/actions/workflows/qa.yml?query=branch%3Amaster)
[![Documentation Status](https://readthedocs.org/projects/medcattrainer/badge/?version=latest)](https://medcattrainer.readthedocs.io/en/latest/?badge=latest)
[![Latest release](https://img.shields.io/github/v/release/CogStack/MedCATtrainer)](https://github.com/CogStack/MedCATtrainer/releases/latest)

MedCATTrainer is an interface for building, improving and customising a given Named Entity Recognition 
and Linking (NER+L) model (MedCAT) for biomedical domain text.

MedCATTrainer was presented at EMNLP/IJCNLP 2019 :tada:
[here](https://www.aclweb.org/anthology/D19-3024.pdf)

# Document and Discussion

Official docs available [here](https://medcattrainer.readthedocs.io/en/latest/)

If you have any questions why not reach out to the community [discourse forum here](https://discourse.cogstack.org/)

# Snomed Annotation Trial Server Setup

The annotation trial runs the production docker compose with a customised Nginx config to run the connection over HTTPS to the MedCat server and JupyterHub. 
The JupyterHub runs as a standalone JupyterHub application.

This requires that Docker install installed on the target server. 

## Setup JupyterHub Server

The JupyterHub needs the following to setup.

1. Make sure at least Python 3.8 is installed and install the following packages:
* jupyterhub
* jupyter\_server
* dockerspawner
2. Make sure at least Node `lts/hydrogen` (v18.12.1) is installed and install the package `configurable-http-proxy`.
3. Update the `jupyter/jupyter_config.py` file and following fields:
* `c.JupyterHub.bind_url`
* `c.JupyterHub.hub_connect_ip` 
* `def start` function with the location of the medcat server as defined in the docker-compose-prod file.
4. Update the `scripts/start_jupyter_lab.sh` file with correct paths.
5. Update the `scripts/jupyter.service` file with correct paths. 
6. Copy the `scripts/jupyter.service` file to the `/etc/systemd/system` folder
7. Pull the `jupyter/scipy-notebook` docker container with `docker pull jupyter/scipy-notebook`
7. Enable the `jupyter.service` with `systemctl enable jupyter.service`
8. Start the `jupyter.service` with `systemctl start jupyter.service`

Currently the JupyterHub is configured for the PAM user authentication so users which need to access JupyterHub need to have login accounts on the VM hosting the JupyterHub. Users can be created on the VM with the `adduser <username>` command. The User account used to run the JupyterHub requires read access to the `/etc/shadow`. Normally this can be granted by adding the user running the JupyterHub to the `shadow` group. 


## Setup Medcat Server
### Nginx Container
The Nginx image configuration file has been updated with following:
1. Forward HTTP port 80 to HTTPS 443. 
2. Forward HTTPS port 443 to HTTP port 8000 on the medcattrainer docker container.
3. Forward HTTPS port 1000 to HTTP port 8000 to the local IP of the JupyterHub. The forwarding on port 1000 also includes locations which are required for the notebooks. The notebooks requires custom locations and webhooks to be forwarded. Currently there is an issue with CORS which impacts on feedback notebooks loading. Refreshing the load page will still load the notebook when it is ready. 

Configure the Nginx `nginx/sites-enabled/medcattrainer` file with the following:
* `server_name` with the server external URL/IP
* `proxy_pass` in the port 1000 server block with the internal IP of the JupyterHub. 

Running the Nginx server requires Let's Encrypt certificate and key. Once generated the certificate and key can be place in the `nginx/ssl` folder and Ngnix Docker image built. 

One the config file has been updated and ssl certificates are in place the Nginx image needs to be built. 

Build the Nginx Docker image with the following command: 
`sudo docker build ./ -t cogstacksystems/medcat-trainer-nginx:latest`

### Configure Medcat Server for Autostart

1. Update the paths in `scripts/start_med_cat_trainer.sh`
2. Update the paths in `scripts/medcat.service`
3. Copy the `scrits/medcat.service` to `/etc/systemd/system` 
4. Enable the medcat service with `systemctl enable medcat.service`
5. Start the medcat service with `systemctl start medcat.service`

Ensure the service is running correctly by visting the external URL/IP on port 80 or port 443 and port 1000
