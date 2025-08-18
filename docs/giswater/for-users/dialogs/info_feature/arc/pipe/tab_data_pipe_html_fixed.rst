.. _tab-data-pipe-html-fixed

==============================
Pipe: Tab Data (Fixed Raw HTML)
==============================

The feature pipe has the following data:

.. raw:: html

   <details>
       <summary><strong>Arc Type:</strong> arc_type - Type of arc. Auto-populated based on arccat_id</summary>
       <ul>
           <li><strong>Data Type:</strong> string</li>
           <li><strong>Required:</strong> No</li>
           <li><strong>Editable:</strong> No</li>
           <li><strong>Values:</strong> Determined by query: 
               <code>SELECT id as id, id as idval FROM cat_feature_arc WHERE id IS NOT NULL</code>
           </li>
           <li>
               <details class="no-square">
                   <summary><strong>Field Controls:</strong></summary>
                   <ul>
                       <li>setMultiline (False)</li>
                       <li>labelPosition (top)</li>
                   </ul>
               </details>
           </li>
       </ul>
   </details>

.. raw:: html

   <details>
       <summary><strong>Arccat Id:</strong> arccat_id - To be selected from catalog of arcs</summary>
       <ul>
           <li><strong>Data Type:</strong> string</li>
           <li><strong>Required:</strong> Yes</li>
           <li><strong>Editable:</strong> Yes</li>
           <li><strong>Values:</strong> Determined by query: 
               <code>SELECT id, id as idval FROM cat_arc WHERE id IS NOT NULL AND active IS TRUE</code>
           </li>
           <li><strong>Filtered by:</strong> AND arc_type</li>
           <li>
               <details class="no-square">
                   <summary><strong>Field Controls:</strong></summary>
                   <ul>
                       <li>setMultiline (False)</li>
                       <li>labelPosition (top)</li>
                       <li>valueRelation ({'layer': 'cat_arc', 'activated': True, 'keyColumn': 'id', 'nullValue': False, 'valueColumn': 'id', 'filterExpression': None})</li>
                   </ul>
               </details>
           </li>
       </ul>
   </details>
