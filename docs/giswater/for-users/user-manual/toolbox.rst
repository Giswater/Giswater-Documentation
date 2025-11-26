.. _toolbox:

================================
Giswater toolbox
================================

.. only:: html

   .. contents::
      :local:

The toolbox contains a set of processes propios of Giswater with which we can, among other things, detect and correct errors in the network.

.. figure:: img/toolbox/toolbox.png

      Giswater toolbox window.

When clicking on its button an window will open in which we will see that there are two large groups: *Processes* and *Reports*, each of which has some subgroups.

Within *Processes* we will find tools oriented to operations and maintenance (*om*), editing (*edit*), hydraulic simulation (*epa*), alternative management (*master*) and network administration (*admin*).

Within *Reports* we will find tools oriented to reports on basic aspects of the network (*basic*) and operations and maintenance (*om*).

To execute a process only double click on its name in the toolbox.

Process dialog
=============================

After double clicking on the process an dialog similar to the one shown in the following figure will open.

.. figure:: img/toolbox/toolbox-dialog.png

      Process dialog for checking duplicated nodes in a ws schema.

The dialog shows two tabs on the left (*Config* and *Info log*), the process description on the right (*Info*) and a set of buttons at the bottom.

Tab *Config*
----------------

In this tab we must set the input values that the process needs to be executed as well as the configuration parameters that are necessary to specify.

The input values will depend on the process that is being executed so that the dialog will be different for each process.

Tab *Info Log*
------------------

Shows a summary of the process that has been carried out.

.. figure:: img/toolbox/toolbox-infolog.png

      Example of a process summary.

Process results
======================

The execution of certain processes involves the creation of some temporary layers with the results. These layers will be loaded in the ToC in a group called *GW Temporal Layers* and their geometry will depend on the geometry of the input layer.

To obtain information about the resulting layer we can open its attribute table.
