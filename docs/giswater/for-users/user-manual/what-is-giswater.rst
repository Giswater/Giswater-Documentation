.. _what-is-giswater:

=================
What is Giswater?
=================

.. only:: html

   .. contents::
      :local:

Giswater is a free application thought for the management and exploitation
of hydraulic infrastructure elements (water supply and sanitation), both in the database
and graphically, through which access is obtained from any geographic information system (GIS).

In turn, Giswater also acts as a driver of connection between the spatial database and 
hydraulic analysis tools.

As shown in the following figure, Giswater is within a grouping of applications that, when used together, allow a global and solid management in relation to the water supply and urban drainage models.

The central element of the set is the **database**, where all the information and 
most of the functionality of each Giswater project is found. The database to use Giswater is 
PostgreSQL, which together with its PostGIS extension allows easily linking with the following application 
of the set: QGIS.

.. figure:: img/what-is-giswater/intro-giswater.png
    
    Application schema that uses Giswater, centralized in the database.

This GIS information system software is the one on which the development of the Giswater project is based, in its visual branch and with greater operability by the user. QGIS relates 
through PostGIS with the database, showing the spatial data organized and always taking into account all the rules, relationships and processes that the database establishes.

The central axis of the project (Database - GIS) also allows connecting with SCADA, to update in real time the information that comes directly from the physical elements of the network. 
In this way Giswater is presented as a global management system and that gives the possibility to its users to work always with data that are updated automatically.

Apart from the management of data through a GIS software there is also the possibility of 
working with Giswater data in a web and mobile environment. This functionality is apart from the usual use 
on desktop, as it is only for clients that require it.

What is the purpose of this guide?
===================================

The fundamental purpose of this guide is to provide the user with a document capable of helping to 
perform any task with Giswater, from the initial installation of the necessary programs 
to the most complex management operations.

The improvements made in version 4 will be reflected throughout the manual and it will be attempted to explain 
the best possible way the purpose of the improvements and the use that must be made of them.

.. important::

    Giswater allows creating and managing projects for water supply and urban drainage networks.
   
    Although most of the tools, processes, catalogs and other objects are common to both networks and there are no apparent differences for the user, there are some that are specific to each type of network.
   
    **Always that not specified otherwise, the tool, process, catalog... described is common for both networks**.
   
    In those cases where it is necessary to differentiate, we can find the abbreviation **ws** to refer to the water supply networks
    or the abbreviation **ud** to refer to the urban drainage and sanitation networks.