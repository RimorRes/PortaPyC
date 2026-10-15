.. raw:: html

    <div style="float:right; margin:1em 0em 1em 1em; padding: 0em 1em 1em 1em;">
    <img style="display: block; margin-left: auto; margin-right: auto; width: 120px; height: 120px;" alt="PortaPyC logo"
    src="_static/logo.svg" title="PortaPyC"/>
    <br/>
    </div>

PortaPyC - Cross-Version Python Communication
=============================================

PortaPyC is a Python 3 port of RPyC 3.3.0 that preserves the RPyC wire
protocol. Its central use case is cross-version communication: a Python 3
application can connect to a legacy Python 2 RPyC server that cannot be
upgraded, and Python 2 and Python 3 endpoints can communicate despite their
normally incompatible runtime and data-model differences.

It lets applications call remote Python code and work with remote objects
through ordinary Python syntax. Connections can be made over TCP, SSL, SSH
tunnels, pipes, or service discovery.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   usage
   compatibility
   api

.. note::

   PortaPyC is a compatibility-focused port. Consult the :doc:`usage`
   examples for the supported connection patterns and treat remote objects as
   network resources: close connections when they are no longer needed.
