.. _zonas-mapa:

==============
Zonas del mapa
==============

.. only:: html

   .. contents::
      :local:

La definición de las zonas del mapa que existen en Giswater son:

Zonas del mapa administrativas
==============================

- Region: 
- Province:
- Municipality: límites municipales con los que se crearán todos los municipios que se encuentren en el ámbito de la red de estudio.
  En el ToC, es la única zona del mapa que no está dentro del grupo *MAP ZONES* sino que está en el grupo *BASEMAP*.
- District:

Zonas del mapa operacionales
============================

- Macroexploitation: agrupa las explotaciones y será útil cuando se pretendan gestionar muchas de ellas.
  Es obligatoria para todos los proyectos, no tiene geometría asociada y ya viene creada una por defecto.
- Exploitation: es la entidad básica de gestión en los proyectos Giswater y permite delimitar zonas para que sean gestionadas de manera diferenciada.
  Habitualmente, coinciden con los términos municipales aunque no tiene que ser así obligatoriamente. Mediante la herramienta *Selector* podemos filtrar qué explotaciones ver.
  Es **obligatorio** crear al menos una para poder empezar a trabajar y, **obligatoriamente**, tiene que tener asociada una macroexplotación.
- Macroomzone:
- Omzone:

Zonas del mapa comerciales (ws)
===============================

- Macrocrmzone:
- Crmzone:

Zonas del mapa funcionales
==========================

- Macrosector: agrupa los sectores y permite gestionar los sectores hidráulicos en grandes grupos.
- Sector: zona del mapa vinculada directamente con el modelo hidráulico. Su delimitación responde directamente a conceptos hidráulicos lo cual puede dar como resultado sectores muy grandes o muy pequeños.
  En este sentido, un sector hidráulico puede ser solo una calle o todo un municipio. El único requisito que tiene que tener es que tenga coherencia hidráulica.
- Presszone (ws): son zonas de la red que tienen todas la misma presión permitiendo calcular la máxima y mínima **presión estática** en la red. Sus cabeceras habituales serán los depósitos y las válvulas reductoras de presión.
- Macrodma (ws):agrupación de las distintas DMA.
- DMA (ws): son zonas de medición (District Meter Area) que tienen como cabecera un caudalímetro y como límite otros caudalímetros o válvulas que estén cerradas.
  Sirven para generar agrupaciones de consumo, útiles para el cálculo de balances hidráulicos.
- Macrodqa (ws): agrupación de las distintas DQA.
- DQA (ws): son zonas de calidad de agua (District Quality Area) y representan aquellas zonas de la red que tienen la misma calidad de agua, seccionadas a través de sensores de muestreo y calidad.
  Sirven para calcular el tiempo de permanencia y la evolución de parámetros de calidad en sectores de consumo.
- Supplyzone (ws):
- Minsector (ws): sector mínimo afectado por un corte en la red. Todos los elementos que pertenecen a un sector mínimo pueden actuar como un sector propiamente dicho ya que están conectados. El elemento que los delimita son las válvulas de corte.
- Drainzone (ud): zona del mapa que **permite determinar todo lo que está aguas arriba de un nodo** o una serie de nodos que previamente han sido configurados con este fin.
  Para ello, **la red debe tener continuidad y estar digitalizada en el sentido de las aguas (de aguas arriba hacia aguas abajo)**.
- Dwfzone: (ud):