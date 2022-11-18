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

# Snomed Annotation Trial

The annotation trial runs the production docker compose with a customised Nginx setup to run the connection over HTTPS. 

Running the Nginx server requires Let's Encrypt certificate and key. Once generated the certificate and key can be place in the `nginx/ssl` folder and Ngnix Docker image built. 

Build the Nginx Docker image with the following command: 
`sudo docker build ./ -t cogstacksystems/medcat-trainer-nginx:latest`

