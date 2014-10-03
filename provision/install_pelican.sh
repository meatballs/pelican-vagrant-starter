#!/usr/bin/env bash

apt-get install -y python-pip
pip install -r /vagrant/provision/requirements.txt
cp /vagrant/provision/*.conf /etc/init
start pelican-server