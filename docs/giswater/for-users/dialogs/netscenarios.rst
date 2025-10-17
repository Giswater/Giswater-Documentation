.. _dialog-netscenarios:

===========================
Gestor de escenarios de red
===========================

.. only:: html

   .. contents::
      :local:

Herramienta que permite plantear escenarios en la red para realizar cambios en las zonas del mapa para conseguir optimizarlas.

.. figure:: img/masterplan/netscenarios.png

    Ventana de la herramienta Gestor de escenarios de red.

Para crear un netscenario pincharemos en el botón *Create* y seleccionaremos una de las opciones disponibles:

- Create empty scenario: permite crear un escenario vacío.
- Create Netscenario from ToC: permite crear un escenario con datos de la ToC.

Podremos crear escenarios de DMA y escenarios de PRESSZONE. En ambos casos, los campos a rellenar en la ventana de creación
son el nombre, el tipo (*DMA* o *PRESSZONE*), si está activo y la explotación.

Escenario de *DMA*
==================

Una vez creado el escenario podremos visualizarlo en el gestor de escenarios de red donde, si hacemos doble clic sobre él,
podremos acceder al escenario.

.. figure:: img/masterplan/netscenario-dma.png

   Ventana de Dma netscenario creado.

Para poder crear las distintas zonas de medición contenidas en el escenario pincharemos en el botón *Create* y en la ventana emergente
especificaremos el *Dma id* (debe ser numérico), un nombre así como marcaremos la casilla *Active*.

Con la zona de medición creada, la configuraremos seleccionándola y pinchando en el botón *Config*.

.. figure:: img/masterplan/config-dma.png

   Ventana de configuración de la DMA.

Tendremos que especificar:

- nodeParent: nodo cabecera respecto del cual se inicia la zonificación.
- toArc: sentido hacia el cual se dirige el flujo del agua.
- ignore: nodos que se ignorarán en el proceso (opcional).
- forceClosed: nodos en los cuales se detendrá el proceso.

Se crearán y configurarán tantas zonas de medición como se necesiten.

Cuando las tengamos todas creadas y configuradas las determinaremos utilizando el botón *Execute mapzones analysis*.

.. figure:: img/masterplan/execute-dma.png

   Ventana de ejecución de Mapzones Netscenario analysis.

En la ventan emergente especificaremos, como mínimo:

- Exploitation: explotación respecto de la cual realizamos el análisis.
- Mapzone constructor method: método para construir la mapzone. Podemos elegir entre:

     - NONE: no dibujará nada.
     - CONCAVE POLYGON: dibujará un polígono cóncavo.
     - PIPE BUFFER: dibujará un buffer alrededor de las tuberías.
     - PLOT & PIPE BUFFER: dibujará un buffer alrededor de las tuberías junto con los edificios que esté relacionados siempre que los tengamos incluidos en la capa *Plot*.
     - LINK & PIPE BUFFER: dibujará un buffer alrededor de las tuberías y los links.

- Pipe buffer: tamaño del buffer a dibujar en el análisis en función del método de construcción elegido.

Escenario de *PRESSZONE*
========================

Una vez creado el escenario podremos visualizarlo en el gestor de escenarios de red donde, si hacemos doble clic sobre él,
podremos acceder al escenario.

.. figure:: img/masterplan/netscenario-presszone.png

   Ventana de Presszone netscenario creado.

Para poder crear las distintas zonas de presión contenidas en el escenario pincharemos en el botón *Create* y en la ventana emergente
especificaremos el *Presszone id* (debe ser numérico), un nombre, indicaremos un valor en *Head* así como marcaremos la casilla *Active*.

El campo *Head* representa la altura de la carga (medida en metros) respecto de la cual se calcularán las presiones estáticas.

Con la zona de medición creada, la configuraremos seleccionándola y pinchando en el botón *Config*.

.. figure:: img/masterplan/config-presszone.png

   Ventana de configuración de la PRESSZONE.

Tendremos que especificar:

- nodeParent: nodo cabecera respecto del cual se inicia la zonificación.
- toArc: sentido hacia el cual se dirige el flujo del agua.
- ignore: nodos que se ignorarán en el proceso (opcional).
- forceClosed: nodos en los cuales se detendrá el proceso.

Se crearán y configurarán tantas zonas de presión como se necesiten.

Cuando las tengamos todas creadas y configuradas las determinaremos utilizando el botón *Execute mapzones analysis*.

.. figure:: img/masterplan/execute-presszone.png

   Ventana de ejecución de Mapzones Netscenario analysis.

En la ventan emergente especificaremos, como mínimo:

- Exploitation: explotación respecto de la cual realizamos el análisis.
- Mapzone constructor method: método para construir la mapzone. Podemos elegir entre:

     - NONE: no dibujará nada.
     - CONCAVE POLYGON: dibujará un polígono cóncavo.
     - PIPE BUFFER: dibujará un buffer alrededor de las tuberías.
     - PLOT & PIPE BUFFER: dibujará un buffer alrededor de las tuberías junto con los edificios que esté relacionados siempre que los tengamos incluidos en la capa *Plot*.
     - LINK & PIPE BUFFER: dibujará un buffer alrededor de las tuberías y los links.

- Pipe buffer: tamaño del buffer a dibujar en el análisis en función del método de construcción elegido.




