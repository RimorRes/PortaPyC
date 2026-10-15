Compatibility with RPyC
=======================

Why PortaPyC exists
--------------------

Python 2 and Python 3 differ in important runtime and data-model details.
Those differences can prevent a normal Python 3 RPyC client from connecting
to a legacy Python 2 RPyC server, even when the application-level service
itself has not changed. PortaPyC provides a Python 3 implementation of the
RPyC 3.3.0 protocol so that the two runtimes can communicate.

Typical migration scenario
---------------------------

The most common arrangement is:

* a legacy Python 2 process runs an RPyC 3.3.0 server;
* a new Python 3 process uses PortaPyC as its client;
* remote calls, objects, exceptions, and iterators cross the existing RPyC
  connection.

The reverse arrangement is also supported when a Python 2 RPyC client needs
to connect to a PortaPyC server.

Implementation changes
----------------------

Compared with the regular RPyC 3.3.0 library, PortaPyC includes:

* a compatibility module for Python 2/3 built-ins, execution, iterators,
  queues, pickling, byte strings, and platform-specific polling;
* Python 3 implementations of the stream, channel, server, registry, and
  command-line entry-point layers;
* cross-version Brine serialization for protocol values such as text,
  bytes, integers, tuples, and exceptions;
* proxy and protocol handling adapted for Python 3 while retaining the RPyC
  3.3.0 message format;
* the ``convert_str`` connection option for applications that need explicit
  conversion between Python 2 byte strings and Python 3 text strings.

The compatibility layer concerns the transport and protocol boundary. Code
executed remotely still runs in the remote interpreter, so Python 3 syntax
cannot be sent to a Python 2 process and Python 2-only modules are not
available in Python 3.

Version scope
-------------

PortaPyC is a compatibility-focused port of RPyC 3.3.0. It is not a general
translation layer between all RPyC releases, and applications should avoid
assuming that features introduced by newer upstream versions are available.
When upgrading either endpoint, verify the protocol and application behavior
with an integration test.
