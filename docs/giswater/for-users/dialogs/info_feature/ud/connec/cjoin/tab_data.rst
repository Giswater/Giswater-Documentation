.. _tab-data-cjoin

====
Data
====


Data



Si quieres consultar la distribución de los layouts puedes ir a :ref:`Partes del formulario <partes-del-formulario>`

.. raw:: html

	<p class='layout-header'>Los campos en el layout lyt_top_1 son:</p>

.. raw:: html

	<details>
		<summary><strong>Tipo_Conexión:</strong> connec_type - tipo_conexión</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> Sí.</li>
			<li><strong>Editable:</strong> No.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, id as idval FROM cat_feature_connec WHERE id IS NOT NULL
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
									<li>layer: ve_cat_feature_connec</li>
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
		<summary><strong>Coneccat_Id:</strong> conneccat_id - conneccat_id</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> Sí.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, id as idval FROM cat_connec WHERE id IS NOT NULL AND active IS TRUE 
				</code>
			</li>
			<li><strong>Filterc:</strong> La consulta anterior esta filtrada por:
				<code>
					 AND cat_connec.connec_type IS NULL OR cat_connec.connec_type
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
									<li>layer: cat_connec</li>
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
		<summary><strong>Arco Id:</strong> arc_id - Identificador de arco</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT arc_id as id, arc_id as idval FROM arc WHERE arc_id IS NOT NULL
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
		<summary><strong>Código Cliente:</strong> customer_code - Código de cuenta</summary>
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
		<summary><strong>Omzone:</strong> dma_id - omzone_id</summary>
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
		<summary><strong>Elevación Superior:</strong> top_elev - Elevación de la conexión en pies o metros.</summary>
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
		<summary><strong>Y1:</strong> y1 - Profundidad en el punto de conexión con el edificio</summary>
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
		<summary><strong>Y2:</strong> y2 - Profundidad en el punto de conexión a la red pública</summary>
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
		<summary><strong>Private_Conneccat_Id:</strong> private_conneccat_id - private_conneccat_id</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
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
									<li>layer: cat_connec</li>
									<li>activated: True</li>
									<li>keyColumn: id</li>
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
		<summary><strong>Matcat_Id:</strong> matcat_id - matcat_id</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, id AS idval FROM cat_material WHERE 'ARC' = ANY(feature_type)
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
		<summary><strong>Solicitar:</strong> demand - solicitar</summary>
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
		<summary><strong>Profundidad_Conexión:</strong> connec_depth - profundidad_conexión</summary>
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
		<summary><strong>Workcat_Id:</strong> workcat_id - workcat_id</summary>
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
		<summary><strong>Diagonal:</strong> diagonal - diagonal</summary>
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
		<summary><strong>Propietario:</strong> ownercat_id - ID del propietario relacionado con la conexión.</summary>
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
		<summary><strong>Fecha Final:</strong> enddate - Fecha final</summary>
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

	<p class='layout-header'>Los campos en el layout lyt_data_2 son:</p>

.. raw:: html

	<details>
		<summary><strong>Identificación De Soilcat:</strong> soilcat_id - ID del suelo relacionado con la conexión.</summary>
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
		<summary><strong>Tipo_Categoría:</strong> category_type - tipo_categoría</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT category_type as id, category_type as idval FROM man_type_category WHERE ((featurecat_id is null AND feature_type='CONNEC')) AND active IS TRUE  OR 'CJOIN' = ANY(featurecat_id::text[])
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
		<summary><strong>Tipo De Fluido:</strong> fluid_type - Tipo de fluido a escoger en el desplegable personalizado por el usuario en la tabla man_type_fluid</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> Sí.</li>
			<li><strong>Editable:</strong> Sí.</li>
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
		<summary><strong>Tipo_Ubicación:</strong> location_type - tipo_ubicación</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT location_type as id, location_type as idval FROM man_type_location WHERE ((featurecat_id is null AND feature_type='CONNEC') ) AND active IS TRUE  OR 'CJOIN' = ANY(featurecat_id::text[])
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
		<summary><strong>Rotación:</strong> rotation - rotación</summary>
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
		<summary><strong>Etiqueta Del Catálogo:</strong> label - Etiqueta del catálogo de conecs, por lo tanto no será editable en el formulario</summary>
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
		<summary><strong>Etiqueta_X:</strong> label_x - etiqueta_x</summary>
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
		<summary><strong>Explotación Id:</strong> expl_id - Explotación a la que pertenece el elemento. Si no se modifica la configuración, el programa lo selecciona automáticamente en función de la geometría</summary>
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
		<summary><strong>Fin Id Workcat:</strong> workcat_id_end - ID del final de obra.</summary>
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
		<summary><strong>Plan_Id_Trabajo:</strong> workcat_id_plan - plan_id_trabajo</summary>
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
		<summary><strong>Tipo De Colocación:</strong> placement_type - Tipo de colocación</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Brand Id:</strong> brand_id - brand_id</summary>
		<ul>
			<li><strong>Datatype:</strong> Text.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, id as idval FROM cat_brand WHERE 'CJOIN' = ANY(featurecat_id::text[]) OR featurecat_id IS NULL
				</code>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Model Id:</strong> model_id - model_id</summary>
		<ul>
			<li><strong>Datatype:</strong> Text.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, id as idval FROM cat_brand_model WHERE 'CJOIN' = ANY(featurecat_id::text[]) OR featurecat_id IS NULL
				</code>
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
		<summary><strong>Código Postal:</strong> postcode - código postal - Código postal del municipio</summary>
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
		<summary><strong>Calle:</strong> streetname - Identificador de la calle.</summary>
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
		<summary><strong>Complemento Opcional Del Número De La Calle:</strong> postcomplement - Complemento opcional del número de la calle</summary>
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
		<summary><strong>Número De La Calle:</strong> postnumber - Número de la calle</summary>
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
		<summary><strong>Calle 2:</strong> streetname2 - Identificador de la segunda calle.</summary>
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
		<summary><strong>Id Del Punto De Unión:</strong> pjoint_id - Identificador del punto de conexión con la red</summary>
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
		<summary><strong>Pjoint_Type:</strong> pjoint_type - pjoint_type</summary>
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
		<summary><strong>Observación:</strong> observ - Observaciones relacionadas con connect. Información adicional</summary>
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
		<summary><strong>Enlace:</strong> link - enlace</summary>
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
		<summary><strong>Sector:</strong> sector_id - Identificador hidráulico del sector relacionado con la clave primaria de la tabla de sectores</summary>
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
		<summary><strong>Estado:</strong> state - Valor de dominio del estado de connect.</summary>
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


