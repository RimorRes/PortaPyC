![PortaPyC](docs/source/_static/banner.png)

[PortaPyC](https://portapyc.readthedocs.io/en/latest/) (pronounced *port-a-pike*) 
is a Python 3 port of [RPyC 3.3.0](https://rpyc.readthedocs.io/en/latest/) that
preserves the RPyC wire protocol. Its primary use case is connecting matching
and differing Python runtimes: a Python 3 application can communicate with a
legacy Python 2 RPyC server (and vice versa) even when that server cannot be
upgraded. Without a compatibility layer, Python 2/3 runtime and data-model
differences would normally prevent this connection.

PortaPyC provides transparent, symmetric remote procedure calls: code on one
machine can call functions, access objects, and use services on another
machine as if they were local. This makes it useful for lightweight
distributed computing, remote administration, test control, and integrating
new Python 3 applications with systems that still depend on Python 2.

PortaPyC keeps the RPyC programming model while adding Python 3 support. It
supports direct TCP connections, SSL-wrapped connections, SSH tunnels,
standard-input/output pipes, subprocess and thread helpers, and optional
service discovery through a registry.

## Installation

```console
python -m pip install portapyc
```

The package requires Python 3.7 or newer. Install the documentation
dependencies with:

```console
python -m pip install "portapyc[docs]"
```

## Cross-version compatibility

Start a classic server on the machine that should expose Python:

```console
rpyc_classic.py --port 18812
```

Connect to it from a Python 3 client:

```python
import portapyc

connection = portapyc.classic.connect("server.example.com", port=18812)
print(connection.eval("1 + 2"))
print(connection.modules.os.listdir("."))
connection.close()
```

The same approach works when the PortaPyC endpoint is the server and a
compatible Python 2 RPyC client connects to it. Compatibility is based on the
RPyC 3.3.0 protocol, not arbitrary combinations of RPyC releases.

## Changes compared with RPyC

PortaPyC is based on RPyC 3.3.0, but its implementation is adapted for
Python 3 and cross-version communication:

- A compatibility layer isolates Python 2/3 differences in execution,
  built-in types, iterators, queues, threads, sockets, and platform polling.
- The Brine protocol serializer handles Python 2 `str`/`unicode` and Python 3
  `bytes`/`str` representations on the wire.
- Optional `convert_str` connection configuration converts received Python 2
  byte strings to Python 3 text, or Python 3 text to Python 2 strings, when
  application-level text conversion is needed.
- Protocol, proxy, exception, iterator, and pickle handling are kept aligned
  with the RPyC 3.3.0 protocol so remote objects remain usable across runtimes.
- The package exposes the familiar RPyC-style API under `portapyc`, with
  Python 3 connection factories for TCP, SSL, SSH, pipes, subprocesses,
  threads, and discovery.

These changes target interoperability with RPyC 3.3.0. They do not make
different, unrelated RPyC protocol versions universally compatible.

## Quick start

For an application-specific service, connect directly and use the remote root
object:

```python
import portapyc

connection = portapyc.connect("server.example.com", 18812)
result = connection.root.calculate_total(10, 20)
connection.close()
```

## Documentation

See this project's documentation on [ReadTheDocs](https://portapyc.readthedocs.io/en/latest/) 
or read [RPyC's documentation](https://rpyc.readthedocs.io/en/latest/) for information about the connection model,
service discovery, security options, and the public API reference. 

You can also build this project's documentation locally with Sphinx. 
After installing the documentation dependencies, 
run the following command in the project root directory to build the HTML documentation:

```console
pip install portapyc[docs]
python -m sphinx -b html docs docs/_build/html
```

## License

PortaPyC is distributed under the MIT license. See `LICENSE`.
