===============
Notas de actualización de Giswater
===============

Este apartado de la documentación está dedicado a proporcionar información detallada sobre los procesos de actualización de Giswater.
Aquí se documentan los cambios significativos entre versiones, consideraciones importantes durante la migración,
y pasos específicos que los desarrolladores y administradores deben seguir para garantizar una actualización exitosa.

La documentación incluye:

- Cambios estructurales en la base de datos
- Modificaciones en la API y funcionalidades
- Procedimientos recomendados para la actualización
- Soluciones a problemas comunes durante la migración
- Notas sobre compatibilidad entre versiones

Esta sección es especialmente útil para los equipos técnicos responsables de mantener y actualizar instalaciones de Giswater en entornos de producción.


Actualización desde la versión 36016
------------------------------------

Cuando se actualiza el plugin de Giswater desde la versión 36016 a una versión superior, hay que tener en cuenta un posible error en la actualización.

.. note::
   Este error puede no presentarse en todas las instalaciones. Su aparición depende de si las vistas mencionadas existen en la base de datos y si contienen la columna con el nombre incorrecto.
   Antes de ejecutar las consultas de corrección, es recomendable verificar la estructura actual de las vistas afectadas.

El error específico está relacionado con el nombre de la columna `preszone_name` que debe ser renombrada a `presszone_name` en varias vistas. Para solucionar este problema, ejecuta las siguientes consultas SQL:

.. code-block:: sql

   -- Renombrar columna en vistas de nodos
   ALTER VIEW vu_node RENAME COLUMN preszone_name TO presszone_name;
   ALTER VIEW v_edit_node RENAME COLUMN preszone_name TO presszone_name;

   -- Renombrar columna en vistas de arcos
   ALTER VIEW vu_arc RENAME COLUMN preszone_name TO presszone_name;
   ALTER VIEW v_edit_arc RENAME COLUMN preszone_name TO presszone_name;

Después de ejecutar estas consultas SQL para corregir el nombre de la columna, el proceso de actualización desde la versión 36016 debería proceder sin problemas. Es importante realizar este paso previo a la actualización para evitar errores durante el proceso.

Una vez completada esta corrección, puedes proceder con normalidad a la actualización del plugin y la base de datos siguiendo el procedimiento estándar de actualización de Giswater.

Si durante la actualización encuentras algún otro problema, haznoslo saber.
