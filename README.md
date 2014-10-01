blog-starter
============
Starter project for a pelican based blog using a vagrant virtual machine.

Installation
============
* Download and install virtualbox (https://www.virtualbox.org/wiki/Downloads)
* Download and install vagrant (https://www.vagrantup.com/downloads.html)
* Clone this repository with --recursive option (or fork it and clone your fork)
* Start the vagrant vm (vagrant up)

Usage
=====
* Create your articles in the content folder on your host machine
* Edit any of the pelican config files on your host machine
* Your vm will be running a web server so you can see your site at http://localhost:800
* Login to your vm (using 'vagrant ssh') to publish your site