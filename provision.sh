#!/usr/bin/env bash

locale="en_GB.UTF-8"

/usr/sbin/locale-gen $locale
/usr/sbin/update-locale LANG=$locale LC_ALL=$locale

apt-get update
apt-get install -y zsh curl git python-pip

su -c "curl https://raw.githubusercontent.com/meatballs/dotfiles/master/install.sh > ~/install.sh" vagrant
su -c "chmod 774 ~/install.sh" vagrant
su -c "~/install.sh" vagrant
chsh -s /bin/zsh vagrant

cd /vagrant
pip install -r requirements.txt
