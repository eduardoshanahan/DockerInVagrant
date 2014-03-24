# Running Docker.io in Vagrant
I am trying this script in Ubuntu 13.04. If you don't have that vagrant box in your machine, the first step should be:
```
#!bash
vagrant box add raring64 http://goo.gl/ceHWg
```
From then on, your machine will have the box available to fire a fresh instance on demand.

I already setup a Vagrant file, doing
```
#!bash
vagrant init raring64
```
Now the real thing. Get the machine ready
```
#!bash
vagrant up
```
To run the scripts I am using Python Fabric. If you don't have it, here is a script to deploy it in Ubuntu
```
#!bash
sudo ./install_fabric.sh
```
Make sure that all is in the right place:
```
#!bash
fab vagrant server_update
fab vagrant update_virtualbox
fab vagrant fix_vagrant_guest_additions
```
Now go with Docker:
```
#!bash
fab vagrant ensure_machine
fab vagrant install_docker
vagrant reload
```
Nos you are deady to try it
```
#!bash
sudo docker run -i -t ubuntu /bin/bash
```
A few character bars should move around, and if there are no errors you have a Docker instance
```
#!bash
exit
```
Now make it work out of root
```
#!bash
fab vagrant docker_add_vagrant
```
And do a hello world to call it a day
```
#!bash
fab vagrant hello_world
```
You should see something like
```
#!bash
[127.0.0.1:2222] out: Hello World
```
Time to bed!