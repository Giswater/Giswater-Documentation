.. _dialog-flow-trace:

================
Flow Trace
================

Tool that allows determining everything that is upstream of a established node. 

.. warning::

    To make the analysis successful, **the network must have continuity and be digitized in the direction of the water**
    (from upstream to downstream).

To be able to perform the analysis, after clicking on the tool, it will only be necessary to click on the node in question. If the network is continuous the calculation algorithm
will stop at the header node. Otherwise, a discontinuity will be seen.

After the analysis is performed, a set of **temporal layers** will be loaded in the ToC with the results where all the elements (nodes, arcs, connecs and gullies) that are upstream of the study node will be shown.
