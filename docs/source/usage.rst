Usage
=====

Installation
------------

Install PortaPyC from PyPI:

.. code-block:: console

   python -m pip install portapyc

The package supports Python 3.7 and newer. The examples below use the public
helpers re-exported by :mod:`portapyc`.

Python 2/3 interoperability
---------------------------

PortaPyC is intended for the migration boundary between Python 2 and Python
3. For example, install PortaPyC in a Python 3 application and use it to
connect to a legacy Python 2 RPyC 3.3.0 server that cannot be upgraded:

.. code-block:: console

   # Run on the legacy Python 2 host
   rpyc_classic.py --port 18812

.. code-block:: python

   # Run in the Python 3 application
   import portapyc

   connection = portapyc.classic.connect("legacy-host", port=18812)
   try:
       print(connection.eval("2 + 2"))
   finally:
       connection.close()

The reverse arrangement is supported as well: a Python 2 RPyC client can
connect to a PortaPyC endpoint. This compatibility targets the RPyC 3.3.0
protocol; it does not guarantee interoperability between arbitrary RPyC
versions.

Calling a remote service
------------------------

The simplest client connection is a TCP connection. The remote endpoint must
run a compatible RPyC service.

.. code-block:: python

   import portapyc

   connection = portapyc.connect("server.example.com", 18812)
   try:
       value = connection.root.calculate_total(10, 20)
       print(value)
   finally:
       connection.close()

Objects returned by a remote call are proxies. They can be passed back to the
remote service, inspected, and used with normal Python operations, but each
operation may perform network I/O.

Classic mode
------------

For a general-purpose remote Python endpoint, use the classic service:

.. code-block:: console

   rpyc_classic.py --port 18812

Then use the classic client helpers:

.. code-block:: python

   import portapyc

   connection = portapyc.classic.connect("server.example.com", port=18812)
   try:
       print(connection.eval("1 + 2"))
       print(connection.modules.os.listdir("."))
   finally:
       connection.close()

The classic service is convenient for administration and experimentation. For
production applications, prefer a purpose-built service that exposes only the
operations clients need.

Discovery
---------

When a service is registered on the local network, it can be discovered by
name instead of by host and port:

.. code-block:: python

   import portapyc

   connection = portapyc.connect_by_service("MY_SERVICE")
   try:
       print(connection.root.status())
   finally:
       connection.close()

Start a registry server with ``rpyc_registry.py``. Discovery uses UDP by
default; use the registry and server command-line options to select TCP,
ports, logging, and pruning timeouts.

Transport and security
----------------------

Use :func:`portapyc.ssl_connect` for an SSL-wrapped connection and
:func:`portapyc.ssh_connect` when an SSH tunnel is provided by a Plumbum
``RemoteMachine``. For subprocesses, threads, and standard I/O, the
corresponding helpers are :func:`portapyc.connect_subproc`,
:func:`portapyc.connect_thread`, and :func:`portapyc.connect_stdpipes`.

Always use authentication and encryption when remote code or data crosses an
untrusted network. SSL certificate and key arguments are passed to Python's
SSL layer; configure certificate verification for your deployment.

Building the documentation
--------------------------

Install the documentation extra and build HTML output:

.. code-block:: console

   python -m pip install "portapyc[docs]"
   python -m sphinx -b html docs docs/_build/html

The generated site is in ``docs/_build/html``. On Windows, the included
``docs/make.bat html`` command is equivalent.
