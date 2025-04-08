====================================
Caja de herramientas de Giswater
====================================
.. figure:: img/caja-herramientas/caja_herramientas_0.png

*Este capítulo tiene como objetivo presentar la caja de herramientas de Giswater que se 
puede aplicar a la identificación y corrección de datos topológicos faltantes o inconsistentes de la información.*

La caja de herramientas de Giswater es una herramienta muy útil, ya que permite al usuario, con solo hacer clic en sus herramientas, 
visualizar capas vectoriales temporales que muestran espacialmente dónde están las inconsistencias topológicas y geométricas de la red. 
Además, a través de las tablas de atributos, el usuario puede calcular automática o manualmente las correcciones necesarias para que un 
modelo hidráulico funcione.

.. figure:: img/caja-herramientas/caja_herramientas_1.png

*Ilustración de la caja de herramientas auxiliar de Giswater en un esquema de UD para encontrar inconsistencias topológicas en la red CSS*

Usaremos los procesos para identificar los errores de la red.

**Processes** (procesos) se divide en:

* *om:* herramientas disponibles para operaciones y mantenimiento.

* *edit:* herramientas disponibles para la edición de la red. Aquí encontraremos la mayor parte de las que necesitamos para corregir los errores.

* *epa:* herramientas disponibles para gestionar las capas desde el punto de vista de la simulación.

* *master:* herramientas variadas relacionadas con la gestión de alternativas, pero también con zonificación dinámica y balances hidráulicos.

* *admin:* herramientas disponibles desde el punto de vista de la administración de la red.

**Reports** (informes) se divide en:

* *basic:* informes sobre aspectos básicos de la red.

* *om:* informes sobre aspectos referentes a operaciones y mantenimiento.

Por datos topológicos, nos referimos a todas las relaciones topológicas y geométricas entre nodos y arcos u otros elementos 
geométricos de la red. Tienen valores de atributos, como profundidad, elevación superior, pendiente de arco, etc. 
Estos atributos están muy bien explicados en la imagen representativa a continuación, para un esquema UD.

.. figure:: img/caja-herramientas/caja_herramientas_2.png

*Ilustración de datos topológicos de red para el esquema UD.*

Esta información también se puede verificar, elemento por elemento, utilizando el botón de información. Para los nodos, 
también es posible calcular la profundidad del nodo y la elevación superior con la herramienta de interpolación y extrapolación, 
tal como se muestra a continuación.

.. figure:: img/caja-herramientas/caja_herramientas_3.png

Por ejemplo, para un CSS (sistema de alcantarillado combinado - esquema UD), los primeros cambios en la red pueden basarse en los datos
ráster DEM, la interpolación o la extrapolación de valores de elevación de nodos cercanos mediante herramientas Giswater específicas. 
Luego, después de completar toda la información que falta para la capa de nodos, se puede realizar otra verificación de las pendientes 
de arco y los valores de desplazamiento negativo mediante el uso de la caja de herramientas de Giswater. Los cambios en la elevación 
del fondo del arco al entrar o salir de un nodo, o la profundidad del nodo y los datos del fondo, permiten al usuario configurar 
fácilmente pendientes hidráulicas consistentes e información topológica para los nodos y arcos. Todos esos cambios se pueden guardar 
como datos del cliente, manteniendo, al mismo tiempo, los datos del inventario sin modificar, al construir modelos hidráulicos.

A continuación, puede encontrar algunos ejemplos de la aplicación de la caja de herramientas para encontrar inconsistencias 
topológicas y otras incongruencias geométricas típicas en los datos de inventario del sistema de red:

**1. Verificador Proyecto**

Esta función verifica tanto el proyecto como la base de datos. Para la verificación de la base de datos, 
se revisan todos los objetos seleccionados por el usuario a través de su selector de sector y explotación.

.. figure:: img/caja-herramientas/caja_herramientas_4.png

Se ejecutará después de la importación y seleccionada las opciones correspondientes.

La ventana de resultados se divide en las secciones:
 
* **Audit check project:** contiene información general sobre la versión de Giswater, de PostgreSQL, sobre el usuario logeado…
* **Critical errors:** contiene información sobre aquellos errores críticos de la red (topológicos o geométricos) que debemos corregir obligatoriamente
* **Warnings:** contiene información sobre ciertos avisos de la red.
* **Info:** contiene información sobre las comprobaciones llevadas a cabo.

Los errores críticos los podremos corregir utilizando las herramientas contenidas en 
la Caja de herramientas de Giswater.

.. figure:: img/caja-herramientas/caja_herramientas_5.png

*Información de verificación de auditoría sobre el modelo hidráulico*


**2. Check arcs without node start/end: busca arcos sin nodos inicial/final.**

.. figure:: img/caja-herramientas/caja_herramientas_6.png

*Comprobar arcos sin herramienta de inicio/fin de nodo*

.. figure:: img/caja-herramientas/caja_herramientas_7.png

*Capas temporales con arcos sin nodos en QGIS ToC y Canvas, así como pestaña info log con la lista de los arcos que presentan 
este tipo de problema.*

**3. Slope consistency: Inconsistencia de la pendiente**

.. figure:: img/caja-herramientas/caja_herramientas_8.png

*Generación de inconsistencia de pendiente de arco, creando capa temporal para todas las incongruencias encontradas e 
información de metadatos de atributos*


**4. Check data for o&m process: chequea los datos comprobando parámetros necesarios para procesos de operaciones y mantenimiento.**

.. figure:: img/caja-herramientas/caja_herramientas_9.png

*La función permite detectar errores e inconsistencias de datos antes del primer proceso OM (mincut, zonas dinámicas de mapeo (ws), perfil (ud)).*
 
**5. Check nodes duplicated: comprueba si hay nodos duplicados.**

.. figure:: img/caja-herramientas/caja_herramientas_10.png

*Verifica el asistente de topología. Para revisar cuántos nodos están duplicados.*

.. figure:: img/caja-herramientas/caja_herramientas_11.png

*Capas temporales con nodos duplicados en QGIS ToC y Canvas, así como pestaña info log con la lista de los nodos que presentan 
este tipo de problema.*

**6. Check nodes orphan: comprueba si hay nodos huérfanos (los que no están conectados a ningún otro elemento de red).**

.. figure:: img/caja-herramientas/caja_herramientas_12.png

*Verifica el asistente de topología. Para revisar cuántos nodos están desconectados de la red.*

.. figure:: img/caja-herramientas/caja_herramientas_13.png

*Capas temporales con nodos desconectados en QGIS ToC y Canvas, así como pestaña info log con la lista de los nodos que presentan 
este tipo de problema.*

**7. Check nodes T candidate: comprueba si hay nodos candidatos a ser una T (unión entre tres tramos).**

.. figure:: img/caja-herramientas/caja_herramientas_14.png

*Verifica los nodos "T candidato" con topología incorrecta.*

**8. Check connecs duplicated: comprueba si hay connec duplicados.**

.. figure:: img/caja-herramientas/caja_herramientas_15.png

*Verifica el asistente de topología. Para revisar cuántas conexiones están duplicadas.*

**9. Check data according to EPA rules: chequea los datos comprobando parámetros necesarios para la exportación a EPA**

.. figure:: img/caja-herramientas/caja_herramientas_16.png

*No se necesitan parámetros de entrada. La función permite detectar errores e inconsistencias de datos antes de la exportación a modelos EPA.*