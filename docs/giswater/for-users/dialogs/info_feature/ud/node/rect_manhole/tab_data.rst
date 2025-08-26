.. _tab-data-rect_manhole

====
Data
====


Data



Si quieres consultar la distribución de los layouts puedes ir a :ref:`Partes del formulario <partes-del-formulario>`

.. raw:: html

	<p class='layout-header'>Los campos en el layout lyt_top_1 son:</p>

.. raw:: html

	<details>
		<summary><strong>Tipo De Nodo:</strong> node_type - Tipo de nodo. Se rellena automáticamente basándose en nodecat_id</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> Sí.</li>
			<li><strong>Editable:</strong> No.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, id as idval FROM cat_feature_node WHERE id IS NOT NULL
				</code>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Establece la posibilidad de campos multilinea para escritura con enter</li>
						<li><strong>labelPosition</strong> (top): Si se define este valor [top, left, none], el label ocupará la posición relativa respecto al widget. Por defecto se sobreentiende left. Si el campo label está vacío, labelPosition se omite.</li>
						<li>
							<details class='no-square'>
								<summary><strong>valueRelation:</strong> </summary>
								<ul>
									<li>layer: ve_cat_feature_node</li>
									<li>activated: True</li>
									<li>keyColumn: id</li>
									<li>nullValue: False</li>
									<li>valueColumn: id</li>
									<li>filterExpression: None</li>
								</ul>
							</details>
						</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Nodecat_Id:</strong> nodecat_id - nodecat_id</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> Sí.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, id as idval FROM cat_node WHERE id IS NOT NULL AND active IS TRUE 
				</code>
			</li>
			<li><strong>Filterc:</strong> La consulta anterior esta filtrada por:
				<code>
					 AND cat_node.node_type IS NULL OR cat_node.node_type
				</code>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Establece la posibilidad de campos multilinea para escritura con enter</li>
						<li><strong>labelPosition</strong> (top): Si se define este valor [top, left, none], el label ocupará la posición relativa respecto al widget. Por defecto se sobreentiende left. Si el campo label está vacío, labelPosition se omite.</li>
						<li>
							<details class='no-square'>
								<summary><strong>valueRelation:</strong> </summary>
								<ul>
									<li>layer: cat_node</li>
									<li>activated: True</li>
									<li>keyColumn: id</li>
									<li>nullValue: False</li>
									<li>valueColumn: id</li>
									<li>filterExpression: None</li>
								</ul>
							</details>
						</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Tipo Epa:</strong> epa_type - Tipo de nodo a utilizar para el modelo hidráulico. No es necesario introducirlo, es automático dependiendo del tipo de nodo.</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, id as idval FROM sys_feature_epa_type WHERE active AND feature_type = 'NODE'
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
		<summary><strong>Código:</strong> code - código</summary>
		<ul>
			<li><strong>Datatype:</strong> Text.</li>
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
		<summary><strong>Top_Elev:</strong> top_elev - top_elev</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>autoupdateReloadFields</strong> (['sys_top_elev', 'sys_ymax', 'sys_elev']): Recarga al momento otros campos en caso de que uno sea modificado. Actua en combinación con isautoupdate</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Custom_Top_Elev:</strong> custom_top_elev - custom_top_elev</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>autoupdateReloadFields</strong> (['sys_top_elev', 'sys_ymax', 'sys_elev']): Recarga al momento otros campos en caso de que uno sea modificado. Actua en combinación con isautoupdate</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Sys_Top_Elev:</strong> sys_top_elev - sys_top_elev</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
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
		<summary><strong>Ymax:</strong> ymax - ymax</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>autoupdateReloadFields</strong> (['sys_top_elev', 'sys_ymax', 'sys_elev']): Recarga al momento otros campos en caso de que uno sea modificado. Actua en combinación con isautoupdate</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Custom_Ymax:</strong> custom_ymax - custom_ymax</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>autoupdateReloadFields</strong> (['sys_top_elev', 'sys_ymax', 'sys_elev']): Recarga al momento otros campos en caso de que uno sea modificado. Actua en combinación con isautoupdate</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Sys_Ymax:</strong> sys_ymax - sys_ymax</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
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
		<summary><strong>Custom_Elev:</strong> custom_elev - custom_elev</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>autoupdateReloadFields</strong> (['sys_top_elev', 'sys_ymax', 'sys_elev']): Recarga al momento otros campos en caso de que uno sea modificado. Actua en combinación con isautoupdate</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Sys_Elev:</strong> sys_elev - sys_elev</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
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
		<summary><strong>Matcat_Id:</strong> matcat_id - matcat_id</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, id AS idval FROM cat_material WHERE 'NODE' = ANY(feature_type)
				</code>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Establece la posibilidad de campos multilinea para escritura con enter</li>
						<li>
							<details class='no-square'>
								<summary><strong>valueRelation:</strong> </summary>
								<ul>
									<li>nullValue: False</li>
									<li>layer: cat_material</li>
									<li>activated: True</li>
									<li>keyColumn: id</li>
									<li>valueColumn: descript</li>
									<li>filterExpression: None</li>
								</ul>
							</details>
						</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Identificación Workcat:</strong> workcat_id - ID de la obra relacionada con el nodo.</summary>
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
		<summary><strong>Fecha De Construcción:</strong> builtdate - fecha de construcción</summary>
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
		<summary><strong>Ownercat_Id:</strong> ownercat_id - ownercat_id</summary>
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
		<summary><strong>Workcat_Id_End:</strong> workcat_id_end - workcat_id_end</summary>
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
		<summary><strong>Fecha Final:</strong> enddate - fecha final</summary>
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
		<summary><strong>Portada:</strong> cover - portada</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Protector De Superficie:</strong> prot_surface - Información sobre si existe el protector de superficie.</summary>
		<ul>
			<li><strong>Datatype:</strong> Boolean.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Paso_Fe:</strong> step_fe - paso_fe</summary>
		<ul>
			<li><strong>Datatype:</strong> Integer.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Paso_Pp:</strong> step_pp - paso_pp</summary>
		<ul>
			<li><strong>Datatype:</strong> Integer.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Paso_Reemplazar:</strong> step_replace - paso_reemplazar</summary>
		<ul>
			<li><strong>Datatype:</strong> Integer.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Adate:</strong> adate - aguja</summary>
		<ul>
			<li><strong>Datatype:</strong> Text.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Adescript:</strong> adescript - adescript</summary>
		<ul>
			<li><strong>Datatype:</strong> Text.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Tipo De Colocación:</strong> placement_type - Tipo de colocación</summary>
		<ul>
			<li><strong>Datatype:</strong> Text.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Tipo_Acceso:</strong> access_type - tipo_acceso</summary>
		<ul>
			<li><strong>Datatype:</strong> Text.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Cuadrante_Etiqueta:</strong> label_quadrant - cuadrante_etiqueta</summary>
		<ul>
			<li><strong>Datatype:</strong> Text.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					select id, idval from edit_typevalue where typevalue = 'label_quadrant'
				</code>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Minsector_Id:</strong> minsector_id - minsector_id</summary>
		<ul>
			<li><strong>Datatype:</strong> Integer.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Macrominsector_Id:</strong> macrominsector_id - macrominsector_id</summary>
		<ul>
			<li><strong>Datatype:</strong> Integer.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Número_De_Serie:</strong> serial_number - número_de_serie</summary>
		<ul>
			<li><strong>Datatype:</strong> Text.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Altura:</strong> height - Height:</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Código_De_Tubo:</strong> manhole_code - Manhole code:</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Rect. Mhole Param_1:</strong> recmanhole_param_1 - Rect. mhole param 1:</summary>
		<ul>
			<li><strong>Datatype:</strong> Text.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Rect. Mhole Param_2:</strong> recmanhole_param_2 - Rect. mhole param 2:</summary>
		<ul>
			<li><strong>Datatype:</strong> Text.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Dma Id:</strong> dma_id - ID del área de gestión relacionada con el arco (Área de contadores de distrito)</summary>
		<ul>
			<li><strong>Datatype:</strong> Integer.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
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
		<summary><strong>Hemisferio:</strong> hemisphere - hemisferio</summary>
		<ul>
			<li><strong>Datatype:</strong> Text.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<p class='layout-header'>Los campos en el layout lyt_data_2 son:</p>

.. raw:: html

	<details>
		<summary><strong>Sin Conexión:</strong> unconnected - sin conexión</summary>
		<ul>
			<li><strong>Datatype:</strong> Boolean.</li>
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
		<summary><strong>Tipo_Fluido:</strong> fluid_type - tipo_fluido</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, idval FROM om_typevalue WHERE typevalue = 'fluid_type'
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
		<summary><strong>Categoría:</strong> category_type - ID del tipo de categoría relacionado con el nodo.</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT category_type as id, category_type as idval FROM man_type_category WHERE ((featurecat_id is null AND feature_type='NODE')) AND active IS TRUE  OR 'RECT_MANHOLE' = ANY(featurecat_id::text[])
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
		<summary><strong>Identificación De Soilcat:</strong> soilcat_id - Relacionado con el catalogo de suelos (cat_soil)</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, id as idval FROM cat_soil WHERE id IS NOT NULL AND active IS TRUE 
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
		<summary><strong>Tipo_Función:</strong> function_type - tipo_función</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT function_type as id, function_type as idval FROM man_type_function WHERE ((featurecat_id is null AND feature_type='NODE') ) AND active IS TRUE  OR 'RECT_MANHOLE' = ANY(featurecat_id::text[])
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
		<summary><strong>Tipo_Ubicación:</strong> location_type - tipo_ubicación</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT location_type as id, location_type as idval FROM man_type_location WHERE ((featurecat_id is null AND feature_type='NODE') ) AND active IS TRUE  OR 'RECT_MANHOLE' = ANY(featurecat_id::text[])
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
		<summary><strong>Rotación:</strong> rotation - Campo a utilizar para rotar la simbología del lienzo del SIG</summary>
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
		<summary><strong>Etiqueta Del Catálogo:</strong> label - etiqueta</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
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
		<summary><strong>Etiqueta X:</strong> label_x - Coordenada X de la ubicación de la etiqueta</summary>
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
		<summary><strong>Etiqueta_Y:</strong> label_y - etiqueta_y</summary>
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
		<summary><strong>Rotación De Etiquetas:</strong> label_rotation - Ángulo de rotación de la etiqueta</summary>
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
		<summary><strong>Fecha_Xyz:</strong> xyz_date - fecha_xyz</summary>
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
		<summary><strong>Explotación Id:</strong> expl_id - Explotación ID</summary>
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
						<li>
							<details class='no-square'>
								<summary><strong>valueRelation:</strong> </summary>
								<ul>
									<li>layer: ve_exploitation</li>
									<li>activated: True</li>
									<li>keyColumn: expl_id</li>
									<li>nullValue: False</li>
									<li>valueColumn: name</li>
									<li>filterExpression: None</li>
								</ul>
							</details>
						</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Plan De Identificación Workcat:</strong> workcat_id_plan - Registro de planificación de artículos</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, id as idval FROM cat_work WHERE id IS NOT NULL
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
		<summary><strong>Asset_Id:</strong> asset_id - asset_id</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Canal Inferior:</strong> bottom_channel - Canal inferior</summary>
		<ul>
			<li><strong>Datatype:</strong> Boolean.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Profundidad_Lijadora:</strong> sander_depth - profundidad_lijadora</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Longitud:</strong> length - Length:</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Anchura:</strong> width - Anchura total de la cámara</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Marca_Id:</strong> brand_id - marca_id</summary>
		<ul>
			<li><strong>Datatype:</strong> Text.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, id as idval FROM cat_brand WHERE 'RECT_MANHOLE' = ANY(featurecat_id::text[]) OR featurecat_id IS NULL
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
		<summary><strong>Modelo_Id:</strong> model_id - model_id</summary>
		<ul>
			<li><strong>Datatype:</strong> Text.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, id as idval FROM cat_brand_model WHERE 'RECT_MANHOLE' = ANY(featurecat_id::text[]) OR featurecat_id IS NULL
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

	<p class='layout-header'>Los campos en el layout lyt_data_3 son:</p>

.. raw:: html

	<details>
		<summary><strong>Muni_Id:</strong> muni_id - muni_id</summary>
		<ul>
			<li><strong>Datatype:</strong> Integer.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT muni_id as id, name as idval from v_ext_municipality WHERE muni_id IS NOT NULL
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
		<summary><strong>Código Postal:</strong> postcode - código postal</summary>
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
		<summary><strong>Nombre De La Calle:</strong> streetname - nombre de la calle</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id AS id, a.descript AS idval FROM v_ext_streetaxis a JOIN ext_municipality m USING (muni_id) WHERE id IS NOT NULL
				</code>
			</li>
			<li><strong>Filterc:</strong> La consulta anterior esta filtrada por:
				<code>
					 AND m.name
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
		<summary><strong>Código Postal:</strong> postnumber - código postal</summary>
		<ul>
			<li><strong>Datatype:</strong> Integer.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT a.postnumber AS id, a.postnumber AS idval FROM ext_address a JOIN ext_streetaxis m ON streetaxis_id=m.id WHERE a.id IS NOT NULL
				</code>
			</li>
			<li><strong>Filterc:</strong> La consulta anterior esta filtrada por:
				<code>
					 AND m.name
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
		<summary><strong>Postcomplemento:</strong> postcomplement - postcomplemento</summary>
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
		<summary><strong>Nombredecalle2:</strong> streetname2 - nombredecalle2</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id AS id, a.descript AS idval FROM v_ext_streetaxis a JOIN ext_municipality m USING (muni_id) WHERE id IS NOT NULL
				</code>
			</li>
			<li><strong>Filterc:</strong> La consulta anterior esta filtrada por:
				<code>
					 AND m.name
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
		<summary><strong>Número De La Segunda Calle:</strong> postnumber2 - Segundo número de calle</summary>
		<ul>
			<li><strong>Datatype:</strong> Integer.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT a.postnumber AS id, a.postnumber AS idval FROM ext_address a JOIN ext_streetaxis m ON streetaxis_id=m.id WHERE a.id IS NOT NULL
				</code>
			</li>
			<li><strong>Filterc:</strong> La consulta anterior esta filtrada por:
				<code>
					 AND m.name
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
		<summary><strong>Postcomplemento2:</strong> postcomplement2 - postcomplemento2</summary>
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
		<summary><strong>Descripción:</strong> descript - Descripción</summary>
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
		<summary><strong>Anotación:</strong> annotation - anotación</summary>
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
		<summary><strong>Consulte:</strong> observ - consulte</summary>
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
		<summary><strong>Enlace:</strong> link - Campo para almacenar el enlace a la información relacionada con el nodo.</summary>
		<ul>
			<li><strong>Datatype:</strong> Text.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
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

	<p class='layout-header'>Los campos en el layout lyt_bot_1 son:</p>

.. raw:: html

	<details>
		<summary><strong>Omzone:</strong> omzone_id - omzone_id</summary>
		<ul>
			<li><strong>Datatype:</strong> Integer.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT omzone_id as id, name as idval FROM omzone WHERE omzone_id = 0 UNION SELECT omzone_id as id, name as idval FROM omzone WHERE omzone_id IS NOT NULL AND active IS TRUE 
				</code>
			</li>
			<li><strong>Filterc:</strong> La consulta anterior esta filtrada por:
				<code>
					 AND omzone.expl_id
				</code>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Establece la posibilidad de campos multilinea para escritura con enter</li>
						<li><strong>labelPosition</strong> (top): Si se define este valor [top, left, none], el label ocupará la posición relativa respecto al widget. Por defecto se sobreentiende left. Si el campo label está vacío, labelPosition se omite.</li>
						<li>
							<details class='no-square'>
								<summary><strong>valueRelation:</strong> </summary>
								<ul>
									<li>layer: ve_dma</li>
									<li>activated: True</li>
									<li>keyColumn: dma_id</li>
									<li>nullValue: False</li>
									<li>valueColumn: name</li>
									<li>filterExpression: None</li>
								</ul>
							</details>
						</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Sector:</strong> sector_id - sector_id</summary>
		<ul>
			<li><strong>Datatype:</strong> Integer.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT sector_id as id,name as idval FROM sector WHERE sector_id IS NOT NULL AND active IS TRUE 
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
						<li>
							<details class='no-square'>
								<summary><strong>valueRelation:</strong> </summary>
								<ul>
									<li>layer: ve_sector</li>
									<li>activated: True</li>
									<li>keyColumn: sector_id</li>
									<li>nullValue: False</li>
									<li>valueColumn: name</li>
									<li>filterExpression: None</li>
								</ul>
							</details>
						</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Estado:</strong> state - estado</summary>
		<ul>
			<li><strong>Datatype:</strong> Smallint.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					WITH psector_value AS (   		SELECT value::integer AS psector_value    		FROM config_param_user    		WHERE parameter = 'plan_psector_current' AND cur_user = current_user), 	 tg_op_value AS (   		SELECT value::text AS tg_op_value    		FROM config_param_user    		WHERE parameter = 'utils_transaction_mode' AND cur_user = current_user)   SELECT id::integer as id, name as idval FROM value_state  WHERE id IS NOT NULL  AND CASE    WHEN (SELECT tg_op_value FROM tg_op_value)!='INSERT' THEN id IN (0,1,2)   WHEN (SELECT tg_op_value FROM tg_op_value) ='INSERT' AND (SELECT psector_value FROM psector_value) IS NOT NULL THEN id = 2    ELSE id < 2  END
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
		<summary><strong>Tipo De Estado:</strong> state_type - El tipo de estado del elemento. Permite obtener más detalles del estado. Para seleccionar entre los disponibles en función del estado elegido</summary>
		<ul>
			<li><strong>Datatype:</strong> Smallint.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, name as idval FROM value_state_type WHERE id IS NOT NULL 
				</code>
			</li>
			<li><strong>Filterc:</strong> La consulta anterior esta filtrada por:
				<code>
					AND value_state_type.state
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


