import json
import time
import os
import socket
import datetime

from fabric.api import *


env.colorize_errors = True


@task
def hello_world():
    """
    Run the Ubuntu hello world example
    """
    run('docker run ubuntu echo "Hello World"')


@task
def docker_add_vagrant():
    """
    Add Vagrant to the Docker group to not need sudo all the time
    """
    sudo('gpasswd -a vagrant docker')
    sudo('service docker restart')
    local('vagrant reload')


@task
def ensure_machine():
    """
    Make sure all is up to date
    """
    sudo('apt-get update')
    sudo('apt-get install -y linux-image-extra-`uname -r`')


@task
def install_docker():
    """
    Get Docker from the repository
    """
    sudo('apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9')
    sudo('sh -c "echo deb http://get.docker.io/ubuntu docker main > /etc/apt/sources.list.d/docker.list"')
    sudo('apt-get update')
    sudo('apt-get install -y lxc-docker')
    sudo('apt-get install -y cgroup-lite')


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
    local('vagrant reload')
