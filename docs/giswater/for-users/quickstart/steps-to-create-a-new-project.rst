===============
Guía de inicio rápido
===============

.. only:: html

   .. contents::
      :local:

Esta guía te ayudará a crear un nuevo proyecto, asumiendo que tienes todos los programas requeridos instalados y una conexión de base de datos correctamente configurada con todas las extensiones necesarias.

.. note::
   Recomendamos instalar el proyecto de ejemplo primero. Esto proporciona una referencia que puedes usar cuando surjan preguntas.

Creación del esquema del proyecto de base de datos
-----------------------------

1. Elige tu idioma [LANG] y el sistema de coordenadas [EPSG]
2. Selecciona un proyecto vacío (sin datos de ejemplo o archivos INP)

.. important::
   Necesitas privilegios de superadministrador de PostgreSQL para trabajar con Giswater.

Creación del archivo de proyecto de QGIS
-----------------------------

Elige tu tipo de rol cuando creas el archivo de proyecto de QGIS.

.. note::
   * Siempre protege tu contraseña
   * Para principiantes, el tipo de rol [basic] es recomendado ya que tiene menos funciones y capas para gestionar
   * Los roles avanzados proporcionan acceso a vistas adicionales y características de Giswater

.. figure:: img/roles-projects.png
