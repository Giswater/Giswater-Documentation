.. _dialog-non-visual-obj:

=============================
Non-visual objects manager
=============================

.. only:: html

   .. contents::
      :local:

Tool that allows managing all the non-visual objects that are needed for the hydraulic modeling.

.. figure:: img/epa/non-visual-obj-ws.png

     Window of the Non-visual objects manager tool for ws schemes.

Depending on whether we are working with a ws or ud project, the tabs available will be one or the other.

The objects to manage are *Roughness* (roughness), *Curves* (curves), *Patterns* (patterns), *Timeseries* (time series), *Controls* (controls), *Rules* (rules) and *Lids* (SUDS).

To create a specific non-visual object we will have to position ourselves on the corresponding tab, click on the *Create* button and fill in the necessary data in the popup window.

Roughness (ws)
==============

Tool that allows creating roughness of materials.

.. figure:: img/epa/roughness.png

     Window to create roughness.

In the popup window we will have to specify the material, the initial and final ages, the roughness value as well as mark the *Active* box to be able to have it available.

Curves
======

Tool that allows creating different types of curves according to the needs of the project.

.. figure:: img/epa/curves.png

     Window to create curves.

In the top part of the popup window we will have to indicate the ID of the curve as well as the type of curve we want to create. Depending on whether we are working with a ws or ud project, we will have available one or the other types of curve.

Selected the type of curve we will have to assign pairs of values to build it in the table that we have in the own window. We have a representation of the curve to be able to visualize it once introduced.

Patterns
========

Tool that allows creating patterns for ws and ud projects.

Patterns ws
-----------

.. figure:: img/epa/pattern-ws.png

     Window to create ws patterns.

We will have to indicate the name of the pattern in the *Pattern ID* field and fill in the corresponding values. Once all the values have been filled in, we will see them represented in the graph located in the bottom part of the window.

The 24 hours patterns should be entered in two rows of 12 values.

Patterns ud
-----------

.. figure:: img/epa/pattern-ud.png

     Window to create ud patterns.

We will have to indicate the name of the pattern in the *Pattern ID* field, specify its type and fill in the corresponding values. Once all the values have been filled in, we will see them represented in the graph located in the bottom part of the window.

Timeseries (ud)
===============

Tool that allows creating time series of different types.

.. figure:: img/epa/timeseries.png

     Window to create time series.

We will have to indicate the name of the time series in the *Time Series ID* field, the type of time series in *Time Series Type*, the type of time in *Times Type*, fill in the values of the time series as well as mark the *Active* box to be able to have it available.

Controls
========

Tool that allows introducing controls.

.. figure:: img/epa/controls.png

     Window to create controls.

We will have to indicate the sector to which the control belongs, indicate if it is active and write it in the text box that we have available.

Rules (ws)
==========

Tool that allows introducing rules.

.. figure:: img/epa/rules.png

     Window to create rules.

We will have to indicate the sector to which the rule belongs, indicate if it is active and write it in the text box that we have available.

Lids (ud)
=========

Tool that allows introducing the *Low Impact Developments*, (low impact developments, also called SUDS or sustainable urban drainage systems).

.. figure:: img/epa/lids.png

     Window to create lids.

To create a Lid we will have to select one of the available in the dropdown *LID Type* and fill in its data in the corresponding tabs that are found on the right.
Depending on the type of Lid chosen we will have one or the other tabs.

.. note::

     The Lids available in Giswater are the ones available in SWMM.
