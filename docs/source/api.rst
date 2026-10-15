API reference
=============

The most commonly used classes and connection helpers are re-exported from
the top-level :mod:`portapyc` package.

Connection helpers
-------------------

.. autofunction:: portapyc.connect
.. autofunction:: portapyc.ssl_connect
.. autofunction:: portapyc.connect_by_service
.. autofunction:: portapyc.connect_subproc
.. autofunction:: portapyc.connect_thread
.. autofunction:: portapyc.connect_stdpipes
.. autofunction:: portapyc.ssh_connect

Core objects
------------

.. autoclass:: portapyc.Connection
   :members:

.. autoclass:: portapyc.Service
   :members:

.. autoclass:: portapyc.VoidService
   :members:

Asynchronous calls
------------------

.. autoclass:: portapyc.AsyncResult
   :members:

Additional public names
-----------------------

.. autoclass:: portapyc.AsyncResultTimeout
.. autoclass:: portapyc.GenericException
.. autoclass:: portapyc.BaseNetref
