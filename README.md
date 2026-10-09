PortaPyC (pronounced *port-a-pike*) is a Python 3.x port of version 3.3.0 of the RPyC library.
It is a work in progress and may present bugs.

[RPyC](http://rpyc.sourceforge.net) (pronounced like *are-pie-see*), or *Remote Python Call*, 
is a **transparent** library for **symmetrical** 
[remote procedure calls](http://en.wikipedia.org/wiki/Remote_procedure_calls), 
[clustering](http://en.wikipedia.org/wiki/Clustering), and 
[distributed-computing](http://en.wikipedia.org/wiki/Distributed_computing).
RPyC makes use of [object-proxying](http://en.wikipedia.org/wiki/Proxy_pattern),
a technique that employs python's dynamic nature, to overcome the physical boundaries
between processes and computers, so that remote objects can be manipulated as if they were local.

![Screenshot](https://rpyc.readthedocs.org/en/latest/_images/screenshot.png)
   
A screenshot of a Windows client connecting to a Linux server.

Note that text written to the server's ``stdout`` is actually printed on 
the server's console.
