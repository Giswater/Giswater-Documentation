.. _dialog-go2epa:

======
Go2Epa
======

.. only:: html

   .. contents::
      :local:

Tool that allows establishing which sectors or sectors of the network are simulated hydraulically as well as their export options.

From here we can export the network to INP to then simulate it in EPANET or SWMM or perform the complete simulation cycle (export-simulation-import of results) in the QGIS environment.

.. figure:: img/epa/go2epa.png

     Window of the Go2Epa tool.

The window is formed by three parts: the upper part (1), the central part (2) and the lower part (3).

In the upper part, thanks to the two available buttons, we will select which areas of the network we will simulate (sector, demand scenario, psector...) and establish their export options.
The export options can be seen in detail in the :ref:`export-options` section.

In the central part we will specify a name for the result and mark the boxes corresponding to the type of export we want to perform. If we only want to export the INP we will mark only the corresponding box.
If on the other hand we want to perform the complete cycle, we will mark all the boxes and indicate a path and a name for the INP and RPT files that will be generated.

In the lower part there are the buttons corresponding to the accept, cancel, close and help actions of this window.

During the export of the INP file Giswater performs checks to verify that the state of the network is correct and that it does not contain any errors. If all the checks are successful, it will return a summary about the 
analysis performed. In case of failure, it will show a summary in which we will see a series of critical errors (*CRITICAL ERRORS*) that we will have to correct. For this we can use the tools of the Giswater toolbox.