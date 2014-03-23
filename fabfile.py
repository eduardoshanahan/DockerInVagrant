import json
import time
import os
import socket
import datetime

from fabric.api import *


env.colorize_errors = True


@task
def fix_vagrant_guest_additions():
    """
    Version 4.3 of Virtual Box makes Vagrant bomb
    fab host_vagrant fix_vagrant_guest_additions
    """
    local('vagrant plugin install vagrant-vbguest')
    local('vagrant up --no-provision')
    sudo('apt-get -y -q purge virtualbox-guest-dkms')
    sudo('apt-get -y -q purge virtualbox-guest-utils')
    sudo('apt-get -y -q purge virtualbox-guest-x11')
    local('vagrant halt')
    local('vagrant up --provision')
    #local('vagrant halt')


@task
def vagrant():
    """
    Connect to Vagrant from the host machine
    """
    env.user = 'vagrant'
    result = dict(line.split() for line in local(
        'vagrant ssh-config', capture=True).splitlines())
    env.hosts = ['{0}:{1}'.format(result['HostName'], result['Port'])]
    env.key_filename = result['IdentityFile'].replace('"', '')


@task
def server_update():
    """
    Ubuntu full update
    """
    sudo('apt-get clean')
    sudo('rm -rf /var/lib/apt/lists/*')
    sudo('apt-get clean')
    sudo('apt-get update')
    sudo('apt-get install python-software-properties -y ')
    sudo(('DEBIAN_FRONTEND=noninteractive apt-get -y '
          '-o Dpkg::Options::="--force-confdef" '
          '-o Dpkg::Options::="--force-confold" dist-upgrade'))


@task
def update_virtualbox():
    """
    Fix Vagrant in Virtual Box after an update in Ubuntu
    """
    sudo('/etc/init.d/vboxadd setup')
