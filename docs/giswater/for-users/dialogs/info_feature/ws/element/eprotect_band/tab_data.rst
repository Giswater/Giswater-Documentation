.. _tab-data-eprotect_band

====
Data
====


Data



Si quieres consultar la distribución de los layouts puedes ir a :ref:`Partes del formulario <entorno-trabajo>`

.. raw:: html

	<p class='layout-header'>Los campos en el layout lyt_top_1 son:</p>

.. raw:: html

	<details>
		<summary><strong>Catalog:</strong> elementcat_id - Catalog</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> Sí.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, id as idval FROM cat_element WHERE element_type = 'EPROTECT_BAND'
				</code>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Establece la posibilidad de campos multilinea para escritura con enter</li>
						<li><strong>labelPosition</strong> (top): Si se define este valor [top, left, none], el label ocupará la posición relativa respecto al widget. Por defecto se sobreentiende left. Si el campo label está vacío, labelPosition se omite.</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<p class='layout-header'>Los campos en el layout lyt_data_1 son:</p>

.. raw:: html

	<details>
		<summary><strong>Code:</strong> code - Code:</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Establece la posibilidad de campos multilinea para escritura con enter</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Element Number:</strong> num_elements - Element number</summary>
		<ul>
			<li><strong>Datatype:</strong> Integer.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Establece la posibilidad de campos multilinea para escritura con enter</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Function Type:</strong> function_type - Function type</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT function_type as id, function_type as idval FROM man_type_function WHERE feature_type = 'ELEMENT' OR 'EORIFICE' = ANY(featurecat_id::text[])
				</code>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Establece la posibilidad de campos multilinea para escritura con enter</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Category Type:</strong> category_type - Category type</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT category_type as id, category_type as idval FROM man_type_category WHERE feature_type = 'ELEMENT' OR 'EORIFICE' = ANY(featurecat_id::text[])
				</code>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Establece la posibilidad de campos multilinea para escritura con enter</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Location Type:</strong> location_type - Location type</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT location_type as id, location_type as idval FROM man_type_location WHERE feature_type = 'ELEMENT' OR 'EORIFICE' = ANY(featurecat_id::text[])
				</code>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Establece la posibilidad de campos multilinea para escritura con enter</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Workcat:</strong> workcat_id - Workcat</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, id as idval FROM cat_work WHERE id IS NOT NULL AND active IS TRUE
				</code>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Establece la posibilidad de campos multilinea para escritura con enter</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Workcat Id End:</strong> workcat_id_end - Workcat ID end</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, id as idval FROM cat_work WHERE id IS NOT NULL AND active IS TRUE
				</code>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Establece la posibilidad de campos multilinea para escritura con enter</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Builtdate:</strong> builtdate - Builtdate:</summary>
		<ul>
			<li><strong>Datatype:</strong> Date.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Establece la posibilidad de campos multilinea para escritura con enter</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Enddate:</strong> enddate - Enddate</summary>
		<ul>
			<li><strong>Datatype:</strong> Date.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Establece la posibilidad de campos multilinea para escritura con enter</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Owner:</strong> ownercat_id - Related to the catalog of owners (cat_owner)</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, id as idval FROM cat_owner WHERE id IS NOT NULL AND active IS TRUE
				</code>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Establece la posibilidad de campos multilinea para escritura con enter</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Brand:</strong> brand_id - brand_id</summary>
		<ul>
			<li><strong>Datatype:</strong> Text.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, id as idval FROM cat_brand WHERE 'EPROTECT_BAND' = ANY(featurecat_id::text[])
				</code>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Model:</strong> model_id - model_id</summary>
		<ul>
			<li><strong>Datatype:</strong> Text.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, id as idval FROM cat_brand_model WHERE 'EPROTECT_BAND' = ANY(featurecat_id::text[])
				</code>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Rotation:</strong> rotation - Rotation:</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Establece la posibilidad de campos multilinea para escritura con enter</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Top Elevation:</strong> top_elev - Elevation of the node in ft or m.</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Establece la posibilidad de campos multilinea para escritura con enter</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<p class='layout-header'>Los campos en el layout lyt_data_2 son:</p>

.. raw:: html

	<details>
		<summary><strong>Exploitation:</strong> expl_id - Exploitation</summary>
		<ul>
			<li><strong>Datatype:</strong> Integer.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT expl_id as id, name as idval FROM exploitation WHERE expl_id IS NOT NULL
				</code>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Stylesheet:</strong> Modificaciones esteticas del campo</summary>
					<ul>
						<li>
							<details class='no-square'>
								<summary><strong>label:</strong></summary>
								<ul>
									<li>color: green</li>
									<li>font-weight: bold</li>
								</ul>
							</details>
						</li>
					</ul>
				</details>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Establece la posibilidad de campos multilinea para escritura con enter</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<p class='layout-header'>Los campos en el layout lyt_data_3 son:</p>

.. raw:: html

	<details>
		<summary><strong>Municipality Id:</strong> muni_id - Identifier of the municipality</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT muni_id as id, name as idval from v_ext_municipality WHERE muni_id IS NOT NULL
				</code>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Observation:</strong> observ - Observation</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>setMultiline</strong> (True): Establece la posibilidad de campos multilinea para escritura con enter</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<p class='layout-header'>Los campos en el layout lyt_bot_1 son:</p>

.. raw:: html

	<details>
		<summary><strong>Sector Id:</strong> sector_id - Sector ID</summary>
		<ul>
			<li><strong>Datatype:</strong> Integer.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT sector_id as id, name as idval FROM sector WHERE sector_id IS NOT NULL and sector_id >= 0
				</code>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Stylesheet:</strong> Modificaciones esteticas del campo</summary>
					<ul>
						<li>
							<details class='no-square'>
								<summary><strong>label:</strong></summary>
								<ul>
									<li>color: blue</li>
									<li>font-weight: bold</li>
								</ul>
							</details>
						</li>
					</ul>
				</details>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Establece la posibilidad de campos multilinea para escritura con enter</li>
						<li><strong>labelPosition</strong> (top): Si se define este valor [top, left, none], el label ocupará la posición relativa respecto al widget. Por defecto se sobreentiende left. Si el campo label está vacío, labelPosition se omite.</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>State:</strong> state - State:</summary>
		<ul>
			<li><strong>Datatype:</strong> Integer.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					WITH check_value AS (   SELECT value::integer AS psector_value    FROM config_param_user    WHERE parameter = 'plan_psector_current'   AND cur_user = current_user ) SELECT id, name as idval  FROM value_state  WHERE id IS NOT NULL  AND CASE    WHEN (SELECT psector_value FROM check_value) IS NULL THEN id != 2    ELSE id=2  END
				</code>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Establece la posibilidad de campos multilinea para escritura con enter</li>
						<li><strong>labelPosition</strong> (top): Si se define este valor [top, left, none], el label ocupará la posición relativa respecto al widget. Por defecto se sobreentiende left. Si el campo label está vacío, labelPosition se omite.</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>State Type:</strong> state_type - State type</summary>
		<ul>
			<li><strong>Datatype:</strong> Integer.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, name as idval FROM value_state_type WHERE id IS NOT NULL
				</code>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Establece la posibilidad de campos multilinea para escritura con enter</li>
						<li><strong>labelPosition</strong> (top): Si se define este valor [top, left, none], el label ocupará la posición relativa respecto al widget. Por defecto se sobreentiende left. Si el campo label está vacío, labelPosition se omite.</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


