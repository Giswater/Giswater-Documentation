.. _tab-data-pipe-example

======================
Pipe: Tab Data Example
======================

Using Sphinx-native togglebutton extension:

.. toggle::

    **Arc Type**
    
    - **Field:** arc_type
    - **Description:** Type of arc, auto-populated based on arccat_id  
    - **Data Type:** string
    - **Editable:** No
    - **Values:** Determined by query: ``SELECT id as id, id as idval FROM cat_feature_arc WHERE id IS NOT NULL``
    
    **Field Controls:**
    
    - setMultiline (False)
    - labelPosition (top)

.. toggle::

    **Arccat Id**
    
    - **Field:** arccat_id
    - **Description:** To be selected from the catalog of arcs
    - **Data Type:** string
    - **Required:** Yes
    - **Editable:** Yes
    - **Values:** Determined by query: ``SELECT id, id as idval FROM cat_arc WHERE id IS NOT NULL AND active IS TRUE``
    - **Filtered by:** AND arc_type
    
    **Field Controls:**
    
    - setMultiline (False)
    - labelPosition (top)
    - valueRelation ({'layer': 'cat_arc', 'activated': True, 'keyColumn': 'id', 'nullValue': False, 'valueColumn': 'id', 'filterExpression': None})
