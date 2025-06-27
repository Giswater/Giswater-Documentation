.. _dialog-flow-trace:

================
Rastreo de flujo
================

Herramienta que permite determinar todo lo que está aguas arriba de un nodo establecido. 

.. warning::

    Para que el análisis resulte exitoso, **la red debe tener continuidad y estar digitalizada en el sentido de las aguas**
    (de aguas arriba hacia aguas abajo).

Para poder realizar el análisis, tras clicar en la herramienta, solo será necesario pinchar sobre el nodo en cuestión. Si la red es continua el algoritmo de cálculo
se detendrá en el nodo de cabecera. En caso contrario, se verá una discontinuidad.

Tras realizarse el análisis se cargarán un conjunto de **capas temporales** en el ToC con los resultados donde se mostrarán todos los elementos (nodos, arcos, connecs y gullys) que están aguas arriba del nodo de estudio.
