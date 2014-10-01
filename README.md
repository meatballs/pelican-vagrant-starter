pelican-vagrant-starter
============
Starter project for a pelican based blog using a vagrant virtual machine.

Installation
============
* Download and install virtualbox (https://www.virtualbox.org/wiki/Downloads)
* Download and install vagrant (https://www.vagrantup.com/downloads.html)
* Clone this repository (with --recursive option) or fork it and clone your fork
* cd into your repository folder and start the vagrant vm (vagrant up)
* Point your browser at http://localhost:8000

Usage
=====
* Create your articles in the content folder on your host machine
* Edit any of the pelican config files on your host machine
* Your vm runs a web server which will detect changes to your content
* Login to your vm (using 'vagrant ssh') to publish your site
