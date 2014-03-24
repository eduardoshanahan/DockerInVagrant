# Running Docker.io in Vagrant

I am trying this script in Bubuntu 13.04. If you don't have the vagrant box in your machine, the first step should be:

```
#!bash
vagrant box add raring64 http://goo.gl/ceHWg
```

From then on, your machine will have the box available to fire a fresh instance on demand.

Now the real thing. Get the machine ready
```
#!bash
vagrant init raring64
vagrant up
```

Make sure that all is in the right place:
```
#!bash
fab vagrant server_update
fab vagrant update_virtualbox
vagrant reload
fab vagrant fix_vagrant_guest_additions
```
Now go with Docker:
```
#!bash
fab vagrant ensure_machine
fab vagrant install_docker
vagrant reload
```
```
#!bash
```
```
#!bash
```
```
#!bash
```
```
#!bash
```
