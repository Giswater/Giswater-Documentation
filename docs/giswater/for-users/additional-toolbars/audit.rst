.. _additional-toolbars-audit:

======
Audit Module
======

.. only:: html

   .. contents::
      :local:

The audit module in Giswater is based on the addition of a new schema in the database, which we will call **audit**. In this document we will explain how to set it up and how to use the tools linked to this schema, which will store information about the changes made in our Giswater work schemas.


Initialization and management of the audit schema
======

The first phase in the implementation of the audit environment consists in the configuration of the audit schema in the PostgreSQL database. To facilitate this process and ensure efficient management, an advanced management tool has been developed within the Giswater plugin. This functionality is available exclusively for users with administrative privileges and is located in the “Advanced” tab of the schema management panel.

.. figure:: img/gw-audit-manager.png

   Form for managing audit schema

The tool consists of three main functionalities, each accessible through a specific button:
1. **Create database audit schema.** This option executes the process of creating the audit schema, using the resources contained in the plugin folders ``giswater\dbmodel\audit\structure`` and ``giswater\dbmodel\audit\audit_checkproject``. The resources used include:

    - DDL and DDLVIEW files: Define the necessary table and view structures.
    - DML files: Establish procedures for data manipulation in audit tables.
    - Report type scripts: Incorporate complementary functionalities to the Giswater toolbar.
    - Role definitions: Configure the required permissions for proper schema management.

2. **Activate audit environment.** This functionality allows activating the audit environment for the currently used GIS schema. To do this, the scripts available in the folder ``giswater\dbmodel\audit\activate`` are used.
Before completing the activation, the tool automatically generates an image of the operational network in the audit schema, which will serve as the initial reference point. This image will constitute the oldest consultable state during the audit processes.
The GIS schema target of the activation is determined based on the active user connection, visible in the panel interface.

3. **Update audit.** This option allows applying changes over a previously configured GIS instance with the audit environment. It allows updating the configuration parameters or incorporating new audit layers, without the need to restart the entire schema.

4. **Activate additional tools in the Giswater plugin**. When the module is already running, it is time to activate the visualization of the 2 tools developed for the audit data query. These are integrated into the existing Giswater toolbars, but in projects where the audit module has not been activated, it is recommended to keep them hidden, as they would not be functional at all.
To activate them, you have to go to the Giswater menu, in the Advanced section, and change the value to True of the ``audit_active`` variable within the ``toolbars_add`` group. This will have to be done in each QGIS client.

.. figure:: img/advanced-menu-audit.png

   Advanced configuration where to activate the audit module tools

Before starting, the system administrator must perform a detailed configuration of the audit environment, adjusting the parameters according to the technical requirements of the project. The configurable parameters are the following:

- Frequency of network image generation: Determines the interval of days from which an automatically generated new complete image of the network state is generated.
- Retention of network images: Sets the number of days during which each historical image will remain available. When this threshold is exceeded, the images are automatically deleted from the system.
- GIS elements auditables: Define which elements of the network must be subject to tracking. For this, the specific tables that will be included in the audit process are specified.

All these values can be modified at any time by the administrator. Any change made should be applied through the “Update audit” functionality, so that the system adopts the new configuration in an effective and immediate manner.

Implications of the activation of the audit environment
======
The activation of the audit environment in Giswater implies the integration of a transversal tracking mechanism within the GIS, which records all changes made on spatial data in a structured manner. This record is automatically made in the **log** table located in the audit schema, which guarantees an exhaustive control over the evolution of the network.
From this moment on, any modification operation executed on the model layers —whether an insertion, an update or a deletion— generates a corresponding entry in this table, allowing the precise reconstruction of each previous state of the managed objects.
The behavior is as follows according to the type of operation:
- **Insertion**: The name of the affected schema and table, the user performing the operation, the action type (INSERT), the current data of the inserted object (in JSON format), the executed command and the date/time of the operation are recorded.
- **Update**: The schema, table, user and action type (UPDATE) information, as well as the previous and current object data (both in JSON format), together with the executed SQL command and the corresponding timestamp are recorded.
- **Deletion**: The affected schema and table, user, action type (DELETE), previous object data (JSON), executed command and execution date/time are recorded.

The JSON data column provides a structured representation of the complete object, including all attributes existing in the table at the time of the operation. This feature allows not only knowing which values have changed, but also reproducing with total fidelity the previous or subsequent state of any entity, both in alphanumeric and geometric terms.

.. figure:: img/log-table.png

   Table log with records of modifications made

This storage mechanism constitutes the basis for versioning management within the GIS, as it allows performing historical queries, change audits, and restoration processes of previous versions in a selective and controlled manner. The information contained in the audit schema therefore becomes a strategic asset to ensure integrity, traceability and recovery capacity in the face of errors or unwanted modifications.

Change inspection tool
======
Once the information related to the operations performed on the GIS objects has been stored, it is possible to query historical versions directly from the user interface.

To do this, a new functionality is incorporated into the object forms, accessible through a specific button in the toolbar. When this option is activated, the system performs a query in the audit schema, locating all operations registered on the object in question —identified by its primary key— and presenting the results in an additional form. This list of versions, ordered chronologically, allows examining the complete evolution of the object over time.

.. figure:: img/audit-custom-form.png

   Button for the change inspection tool

Each entry in the list represents a historical instant linked to a specific operation (insertion, modification or deletion), and includes both the object attributes and its geometry, faithfully reflecting the state of the object at that moment. 

.. figure:: img/audit-object-manager.png

   Form for the change inspection tool

This tool not only strengthens traceability, but constitutes the basis for detailed inspection and selective restoration actions, through the following utilities:
- **Open**: Allows selecting a record from the list and viewing in an auxiliary form the values of the attributes affected by the operation, showing both the previous and new state. This facilitates, in a clear and immediate way, the understanding of the applied change and its impact.
- **Open date**: Offers the possibility of selecting a date on which there are modification records, showing in a single auxiliary form all the audit changes made on that day. This functionality is particularly useful for comparing the object state before and after the end of the working day, allowing a complete review of the modifications made on the selected date.

.. figure:: img/audit-object-values.png

   Form for the change inspection tool with a record selected to specifically see what changes were made

Temporal recovery tool for the network state
======
Based on the information registered by the audit environment, a new utility within Giswater has been developed that allows reconstructing the historical state of the network on a specific date in a precise manner, facilitating analysis, diagnosis or advanced audit tasks.

Since this tool is useful for any Giswater user, it has been embedded in the Utilities toolbar (necessary activation required).

.. figure:: img/toolbar-audit-utilities.png

   Temporal recovery tool for the network state, embedded in the Utilities toolbar

Esta funcionalidad permite al usuario configurar una serie de parámetros clave a través de un formulario específico:
- Reference date: Allows selecting the temporal moment from which the network state is to be recovered.
- Spatial extension: The geographical area of analysis can be defined in two ways: using a drawing tool on the QGIS canvas or reusing the current visible map extent.
- Elements to recover: The user can select one or more types of object on which the reconstruction is to be applied: arcs, nodes, connections, links, elements or documents.

.. figure:: img/audit-network-manager.png

   Form for the temporal recovery tool for the network state

Once the parameters are set, the process identifies the closest previous network image to the selected date and applies, sequentially, all the changes registered between that image and the target date. This way, a faithful reconstruction of the network state as it was at that moment is generated.

The result is stored in temporary tables, which are automatically loaded in QGIS with a customized symbology. This symbology includes differentiated color and style categories that allow visually identifying which elements have been **modified** (orange), which have been **deleted** (red) and which remain **unchanged** (blue). Additionally, this reconstructed layer is completely consultable, allowing the user to explore in detail the properties of each element as they were on the selected date.

.. figure:: img/audit-network-result.png

   Result of the temporal recovery process, showing the changes made through different layers and symbologies

This tool significantly expands the analytical capabilities of Giswater, providing a detailed historical view of the behavior and evolution of the network, without altering the integrity of the current operational data.






