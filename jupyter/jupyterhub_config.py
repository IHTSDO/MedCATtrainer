# Configuration file for jupyterhub.
from jupyter_client.localinterfaces import public_ips
from dockerspawner import SystemUserSpawner
import socket
import os

c = get_config()  # noqa

class UnaiDockerSpawner(SystemUserSpawner):

    def start(self):
        self.volumes[f'/home/ubuntu/data'] = {
            'bind': f'/home/{self.user.name}/data',
            'mode': 'rw',  # or ro for read-only
        }
        return super().start()


# dummy for testing. Don't use this in production!
# c.JupyterHub.authenticator_class = "dummy"
# c.DummyAuthenticator.password = "test"

# launch with docker
c.JupyterHub.spawner_class = UnaiDockerSpawner
c.JupyterHub.hub_ip = '0.0.0.0'


c.JupyterHub.bind_url = 'http://<JupyterHubIP>:8000'
c.JupyterHub.hub_connect_ip = '<JupyterHubIP>'

c.DockerSpawner.image = 'unai/scipy-notebook-extended'
c.DockerSpawner.network_name = 'jupyterhub'
c.DockerSpawner.remove = True
