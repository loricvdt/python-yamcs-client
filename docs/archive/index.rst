Archive
=======

The Archive API provides methods that you can use to programmatically retrieve the content of a Yamcs Archive.

Reference
---------

.. toctree::

    client
    model

Snippets
--------

Create an :class:`.ArchiveClient` for a specific instance:

.. code-block:: python

    from yamcs.client import YamcsClient

    client = YamcsClient('localhost:8090')
    archive = client.get_archive(instance='simulator')


Packet Retrieval
^^^^^^^^^^^^^^^^

Print the last 10 packets:

.. literalinclude:: ../../yamcs-client/examples/archive_retrieval.py
    :pyobject: print_last_packets
    :start-after: """
    :dedent: 4

Print available range of archived packets:

.. literalinclude:: ../../yamcs-client/examples/archive_retrieval.py
    :pyobject: print_packet_range
    :start-after: """
    :dedent: 4

Iterate a specific range of packets:

.. literalinclude:: ../../yamcs-client/examples/archive_retrieval.py
    :pyobject: iterate_specific_packet_range
    :start-after: """
    :dedent: 4

Download raw packet binary to a file:

.. literalinclude:: ../../yamcs-client/examples/archive_retrieval.py
    :pyobject: export_raw_packets
    :start-after: """
    :dedent: 4


Parameter Retrieval
^^^^^^^^^^^^^^^^^^^

Retrieve the last 10 values of a parameter:

.. literalinclude:: ../../yamcs-client/examples/archive_retrieval.py
    :pyobject: print_last_values
    :start-after: """
    :dedent: 4

Iterate a specific range of values:

.. literalinclude:: ../../yamcs-client/examples/archive_retrieval.py
    :pyobject: iterate_specific_parameter_range
    :start-after: """
    :dedent: 4

Iterate values of multiple parameters by unique generation time:

.. literalinclude:: ../../yamcs-client/examples/archive_retrieval.py
    :pyobject: stream_specific_parameter_range
    :start-after: """
    :dedent: 4


Event Retrieval
^^^^^^^^^^^^^^^

Iterate a specific range of events:

.. literalinclude:: ../../yamcs-client/examples/archive_retrieval.py
    :pyobject: iterate_specific_event_range
    :start-after: """
    :dedent: 4


Command Retrieval
^^^^^^^^^^^^^^^^^

Retrieve the last 10 issued commands:

.. literalinclude:: ../../yamcs-client/examples/archive_retrieval.py
    :pyobject: print_last_commands
    :start-after: """
    :dedent: 4


Histogram Retrieval
^^^^^^^^^^^^^^^^^^^

Print the number of packets grouped by packet name:

.. literalinclude:: ../../yamcs-client/examples/archive_breakdown.py
    :pyobject: print_packet_count
    :start-after: """
    :dedent: 4

Print the number of events grouped by source:

.. literalinclude:: ../../yamcs-client/examples/archive_breakdown.py
    :pyobject: print_event_count
    :start-after: """
    :dedent: 4

Print the number of processed parameter frames grouped by group name:

.. literalinclude:: ../../yamcs-client/examples/archive_breakdown.py
    :pyobject: print_pp_groups
    :start-after: """
    :dedent: 4

Print the number of commands grouped by name:

.. literalinclude:: ../../yamcs-client/examples/archive_breakdown.py
    :pyobject: print_command_count
    :start-after: """
    :dedent: 4
