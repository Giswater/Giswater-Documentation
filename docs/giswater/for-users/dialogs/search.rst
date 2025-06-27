.. _dialog-search:

========
Buscador
========

Herramienta que permite realizar búsquedas sobre distintos objetos y ámbitos del proyecto.

.. figure:: img/basic/search.png

    Ventana de la pestaña Network en el Buscador.

Se divide en las pestañas:

- Network: permite buscar elementos concretos de la red en función de su tipo de elemento y su código. El buscador nos llevará sobre el elemento en cuestión y abrirá su formulario.
- Address: permite realizar búsquedas seleccionando el municipio, la calle y el número del callejero, donde Giswater irá mostrando las filas coincidentes. Clicando sobre una de las filas, se hará zum a la extensión de la calle.
  Para poder utilizarlo hay que configurar previamente las capas *ext_streetaxis*, *ext_address* y *municipality* donde las dos primeras deben tener geometría de tipo línea y de tipo punto respectivamente
  (la tercera es la correspondiente zona del mapa).
- Hydrometer (WS): permite buscar abonados en el caso de que se tengan asociados a las acometidas. A cada acometida se le pueden vincular múltiples abonados y a éstos, los consumos registrados en diferentes periodos.
  Si los tenemos asociados, al escribir el código del abonado y clicar sobre él se abrirá un formulario con su información haciéndose zum a la ubicación de la acometida relacionada.
  Si se tiene marcada la casilla *Use contains* permite buscar con cualquier carácter. Si está desmarcada, el motor de búsqueda solo mostrará resultados al coincidir con los primeros caracteres.
- Workcat: permite identificar qué elementos de la red están relacionados con un mismo expediente de obras. Al seleccionar uno entre los disponibles, se mostrará un polígono con la extensión máxima de los elementos relacionados 
  y se abrirá una ventana mostrándolos todos junto con un resumen del número de ellos así como de la longitud total de los arcos.
- Psector: permite buscar, para cada una de las explotaciones del proyecto, los sectores de planificación que se hayan creado. Al seleccionar uno se hará zum a la extensión del psector y abrirá su formulario.
- Visit: permite buscar una visita vinculada a cualquier tipo de operación hecha en campo sobre los elementos de la red. Al seleccionar una se hará zum a su elemento vinculado y se abrirá su formulario.

