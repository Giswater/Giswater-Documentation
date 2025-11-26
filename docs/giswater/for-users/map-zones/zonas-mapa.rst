.. _zonas-mapa:

==============
Map zones
==============

.. only:: html

   .. contents::
      :local:

The definition of the map zones that exist in Giswater are:

Map administrative zones
==============================

- Region: 
- Province:
- Municipality: municipal limits with which all municipalities that are within the scope of the study network will be created.
  En el ToC, es la única zona del mapa que no está dentro del grupo *MAP ZONES* sino que está en el grupo *BASEMAP*.
- District:

Map operational zones
============================

- Macroexploitation: groups theexplotations and will be useful when many of them are to be managed.
  It is mandatory for all projects, no has geometry associated and already comes created one by default.
- Exploitation: is the basic management entity in Giswater projects and allows delimiting zones to be managed differently.
  Usually, they coincide with municipal terms although it is not necessarily mandatory. Through the *Selector* tool we can filter whichexplotations to see.
  It is **mandatory** to create at least one and **mandatory** to have an associated macroexploitation.
- Macroomzone:
- Omzone:

Map commercial zones (ws)
===============================

- Macrocrmzone:
- Crmzone:

Map functional zones
==========================

- Macrosector: groups the sectors and allows managing the hydraulic sectors in large groups.
- Sector: map zone linked directly with the hydraulic model. Its delimitation responds directly to hydraulic concepts which can result in very large or very small sectors.
  In this sense, a hydraulic sector can be only a street or an entire municipality. The only requirement it has to have is that it has hydraulic coherence.
- Presszone (ws): are network zones that have all the same pressure allowing to calculate the maximum and minimum **static pressure** in the network. Their usual headers will be the reservoirs and the pressure reducing valves.
- Macrodma (ws): grouping of the different DMA.
- DMA (ws): are measurement zones (District Meter Area) that have a meter as a header and other meters or valves that are closed as a limit.
  They are useful for generating consumption groups, useful for calculating hydraulic balances.
- Macrodqa (ws): grouping of the different DQA.
- DQA (ws): are quality zones (District Quality Area) and represent those zones of the network that have the same water quality, sectioned through sampling and quality sensors.
  They are useful for calculating the time of residence and the evolution of quality parameters in consumption sectors.
- Supplyzone (ws):
- Minsector (ws): minimum sector affected by a cut in the network. All elements that belong to a minimum sector can act as a properly sector since they are connected. The element that delimitates them are the cut valves.
- Drainzone (ud): map zone that **allows determining everything that is upstream of a node** or a series of nodes that have previously been configured with this purpose.
  For this, **the network must have continuity and be digitalized in the direction of the water (from upstream to downstream)**.
- Dwfzone: (ud):