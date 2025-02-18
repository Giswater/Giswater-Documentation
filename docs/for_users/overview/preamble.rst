.. _giswater.documentation.preamble:

===============
Preamble
===============

Welcome to Giswater, the first open-source software for water cycle management (water supply and urban drainage).

The software has been licensed under the `GNU General Public License v3.0 <https://www.gnu.org/licenses/gpl-3.0.en.html>`_.

The following document is licensed under a `Creative Commons Attribution-ShareAlike 4.0 International License <https://creativecommons.org/licenses/by-sa/4.0/>`_.

This user’s guide aims to help you start working with Giswater.

What is Giswater?
-----------------

Giswater is an open-source application for management and exploitation of hydraulic infrastructure
elements in both water supply and urbain drainage. It is accessible using database and graphic
representation using any kind of geographic information system (GIS).

At the same time, Giswater can act as a driver connecting spatial database with tools used for hydraulic
analysis. Currently Giswater is on the third version of the software, which represents notable improvements
comparing with previous versions, not only graphically but also in usability and capabilities.

As presented on this image , Giswater is located between the applications, which used all together allow a
solid and global management in relation to water supply and urban drainage models. The central element of
the set is the database, where all the information and most of the functionalities of each Giswater project is located.
Giswater uses PostgreSQL database, which together with its PostGIS extension allows to conveniently link it with the next
application of the set: QGIS.