===============
Giswater update notes
===============

This section of the documentation is dedicated to providing detailed information about the Giswater update processes.
Here we document significant changes between versions, important considerations during migration,
and specific steps that developers and administrators must follow to ensure a successful update.

The documentation includes:

- Structural changes to the database
- Modifications to the API and functionalities
- Recommended procedures for updating
- Solutions to common problems during migration
- Notes on compatibility between versions

This section is particularly useful for technical teams responsible for maintaining and updating Giswater installations in production environments.

Update from version 36016
------------------------------------

When updating the Giswater plugin from version 36016 to a higher version, please be aware of a possible error in the update.

.. note::
   This error may not occur in all installations. Its appearance depends on whether the mentioned views exist in the database and whether they contain the incorrect column name.
   Before executing the correction queries, it is recommended to verify the current structure of the affected views.

The specific error is related to the column name `preszone_name` that must be renamed to `presszone_name` in several views. To solve this problem, execute the following SQL queries:

.. code-block:: sql

   -- Rename column in node views
   ALTER VIEW vu_node RENAME COLUMN preszone_name TO presszone_name;
   ALTER VIEW v_edit_node RENAME COLUMN preszone_name TO presszone_name;

   -- Rename column in arc views
   ALTER VIEW vu_arc RENAME COLUMN preszone_name TO presszone_name;
   ALTER VIEW v_edit_arc RENAME COLUMN preszone_name TO presszone_name;

After executing these SQL queries to correct the column name, the update from version 36016 should proceed without problems. It is important to perform this step before the update to avoid errors during the process.

Once this correction is completed, you can proceed with the normal update of the plugin and database following the standard update procedure of Giswater.

If you encounter any other problem during the update, please let us know.
