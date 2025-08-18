=============================
Manual de Usuario de Giswater
=============================
 
 
 aaaaa


.. raw:: html

	<details>
		<summary>Arc Type:: arc_type - cat_arctype_id - Type of arc. It is auto-populated based on the arccat_id</summary>
		<ul>
			<li><strong>Tipo de dato:</strong> string.</li>
			<li><strong>Obligatorio:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
			<li><strong>Valores:</strong> Los valores de este desplegable estan determinados por la consulta: 
            <pre><code>SELECT id as id, id as idval FROM cat_feature_arc WHERE id IS NOT NULL </code></pre>.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Controles:</strong> Controles del campo</summary>
					<ul>
						<li>setMultiline (False)</li>
						<li>labelPosition (top)</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>

aaaa 


.. toctree::
   :maxdepth: 2
   :numbered: 4

   introduccion
   que-es-giswater
   instalacion-puesta-marcha
   creacion-conexiones-previas
   modelo-de-datos-giswater
   entorno-trabajo
   digitalization
   toolbox
   export-options
   ../dialogs/info_feature/index