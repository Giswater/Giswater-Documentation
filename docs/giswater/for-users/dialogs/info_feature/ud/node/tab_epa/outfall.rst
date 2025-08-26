.. _tab-epa-outfall

=======
Outfall
=======


None

.. raw:: html

	<p class='layout-header'>Los campos en el layout lyt_epa_data_1 son:</p>

.. raw:: html

	<details>
		<summary><strong>Tipo De Emisario:</strong> outfall_type - Tipo de vertido</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, idval FROM inp_typevalue WHERE id IS NOT NULL AND typevalue='inp_typevalue_outfall' 
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
		<summary><strong>Etapa:</strong> stage - escenario</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>filterSign</strong> (ILIKE): </li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Id De Curva:</strong> curve_id - Identificador de la curva - curve_id </summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, id AS idval FROM inp_curve  WHERE id IS NOT NULL
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
									<li>nullValue: True</li>
									<li>layer: ve_inp_curve</li>
									<li>activated: True</li>
									<li>keyColumn: id</li>
									<li>valueColumn: id</li>
									<li>filterExpression: </li>
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
		<summary><strong>Id De Serie Temporal:</strong> timser_id - timser_id</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, id as idval FROM inp_timeseries WHERE id IS NOT NULL 
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
									<li>nullValue: True</li>
									<li>layer: ve_inp_timeseries</li>
									<li>activated: True</li>
									<li>keyColumn: id</li>
									<li>valueColumn: id</li>
									<li>filterExpression: </li>
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
		<summary><strong>Puerta:</strong> gate - puerta</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>filterSign</strong> (ILIKE): </li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<p class='layout-header'>Los campos en el layout lyt_epa_data_2 son:</p>

.. raw:: html

	<details>
		<summary><strong>Frecuencia De Flujo:</strong> flow_freq - Frecuencia de flujo</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>filterSign</strong> (ILIKE): </li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Caudal Medio:</strong> avg_flow - Caudal medio</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>filterSign</strong> (ILIKE): </li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Flujo Máximo:</strong> max_flow - Flujo máximo - max_flow </summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>filterSign</strong> (ILIKE): </li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Volumen Total:</strong> total_vol - Volumen total</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>filterSign</strong> (ILIKE): </li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<p class='layout-header'>Los campos en el layout lyt_epa_dsc_1 son:</p>

.. raw:: html

	<details>
		<summary><strong>Add_To_Dscenario:</strong> add_to_dscenario - None</summary>
		<ul>
			<li><strong>Datatype:</strong> Unknown.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Stylesheet:</strong> Modificaciones esteticas del campo</summary>
					<ul>
						<li>icon: 113</li>
					</ul>
				</details>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>saveValue</strong> (False): </li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Remove_From_Dscenario:</strong> remove_from_dscenario - None</summary>
		<ul>
			<li><strong>Datatype:</strong> Unknown.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Stylesheet:</strong> Modificaciones esteticas del campo</summary>
					<ul>
						<li>icon: 114</li>
					</ul>
				</details>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>saveValue</strong> (False): </li>
						<li><strong>onContextMenu</strong> (Delete dscenario): </li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Edit_Dscenario:</strong> edit_dscenario - None</summary>
		<ul>
			<li><strong>Datatype:</strong> Unknown.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Stylesheet:</strong> Modificaciones esteticas del campo</summary>
					<ul>
						<li>icon: 101</li>
					</ul>
				</details>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>saveValue</strong> (False): </li>
						<li><strong>onContextMenu</strong> (Edit dscenario): </li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<p class='layout-header'>Los campos en el layout lyt_epa_dsc_3 son:</p>

.. raw:: html

	<details>
		<summary><strong>Tabla Inp Outfall:</strong> tbl_inp_outfall - None</summary>
		<ul>
			<li><strong>Datatype:</strong> Unknown.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Controles del campo</summary>
					<ul>
						<li><strong>saveValue</strong> (False): </li>
						<li><strong>tableUpsert</strong> (ve_inp_dscenario_outfall): </li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


