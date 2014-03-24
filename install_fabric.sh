#!/usr/bin/env bash
printf "\nLoad pip and fabric\n"
apt-get update
apt-get install -y python-pip
apt-get install -y python-dev
apt-get install -y build-essential
pip install setuptools --no-use-wheel --upgrade
pip install --upgrade pip
/usr/local/bin/pip install fabric