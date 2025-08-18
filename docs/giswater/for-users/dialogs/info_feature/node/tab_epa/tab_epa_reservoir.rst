.. _tab-epa-reservoir

==================
Reservoir: Tab Epa
==================

The feature reservoir, has the following data:

.. raw:: html
	<details>
		<summary>Add To Dscenario: add_to_dscenario - None</summary>
		<ul>
			<li>**Tipo de dato:** None.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** No.</li>
			<li>
				<details class='no-square'>
					<summary><b>Estilos:</b> Modificaciones esteticas del campo</summary>
					<ul>
						<li>icon (113)</li>
					</ul>
				</details>
			</li>
			<li>
				<details class='no-square'>
					<summary><b>Controles:</b> Controles del campo</summary>
					<ul>
						<li>saveValue (False): Hola</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>

.. raw:: html
	<details>
		<summary>Pattern:: pattern_id - Pattern</summary>
		<ul>
			<li>**Tipo de dato:** string.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** Sí.</li>
			<li>**Valores:** Los valores de este desplegable estan determinados por la consulta: SELECT DISTINCT (pattern_id) AS id,  pattern_id  AS idval FROM inp_pattern WHERE pattern_id IS NOT NULL.</li>
			<li>
				<details class='no-square'>
					<summary><b>Controles:</b> Controles del campo</summary>
					<ul>
						<li>setMultiline (False): Hola</li>
						<li>valueRelation ({'nullValue': True, 'layer': 've_inp_pattern', 'activated': True, 'keyColumn': 'pattern_id', 'valueColumn': 'pattern_id', 'filterExpression': None}): Hola</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>

.. raw:: html
	<details>
		<summary>Result Id:: result_id - Result id</summary>
		<ul>
			<li>**Tipo de dato:** string.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** No.</li>
			<li>
				<details class='no-square'>
					<summary><b>Controles:</b> Controles del campo</summary>
					<ul>
						<li>filterSign (ILIKE): Hola</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>

.. raw:: html
	<details>
		<summary>Tabla Reservoir: tbl_inp_reservoir - None</summary>
		<ul>
			<li>**Tipo de dato:** None.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** No.</li>
			<li>
				<details class='no-square'>
					<summary><b>Controles:</b> Controles del campo</summary>
					<ul>
						<li>saveValue (False): Hola</li>
						<li>tableUpsert (ve_inp_dscenario_reservoir): Hola</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>

.. raw:: html
	<details>
		<summary>Remove From Dsscenario: remove_from_dscenario - None</summary>
		<ul>
			<li>**Tipo de dato:** None.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** No.</li>
			<li>
				<details class='no-square'>
					<summary><b>Estilos:</b> Modificaciones esteticas del campo</summary>
					<ul>
						<li>icon (114)</li>
					</ul>
				</details>
			</li>
			<li>
				<details class='no-square'>
					<summary><b>Controles:</b> Controles del campo</summary>
					<ul>
						<li>saveValue (False): Hola</li>
						<li>onContextMenu (Delete dscenario): Hola</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>

.. raw:: html
	<details>
		<summary>Head:: head - Head</summary>
		<ul>
			<li>**Tipo de dato:** string.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** Sí.</li>
			<li>
				<details class='no-square'>
					<summary><b>Controles:</b> Controles del campo</summary>
					<ul>
						<li>filterSign (ILIKE): Hola</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>

.. raw:: html
	<details>
		<summary>Max Demand:: demandmax - Max demand</summary>
		<ul>
			<li>**Tipo de dato:** string.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** No.</li>
			<li>
				<details class='no-square'>
					<summary><b>Controles:</b> Controles del campo</summary>
					<ul>
						<li>filterSign (ILIKE): Hola</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>

.. raw:: html
	<details>
		<summary>Edit Dscenario: edit_dscenario - None</summary>
		<ul>
			<li>**Tipo de dato:** None.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** Sí.</li>
			<li>
				<details class='no-square'>
					<summary><b>Estilos:</b> Modificaciones esteticas del campo</summary>
					<ul>
						<li>icon (101)</li>
					</ul>
				</details>
			</li>
			<li>
				<details class='no-square'>
					<summary><b>Controles:</b> Controles del campo</summary>
					<ul>
						<li>saveValue (False): Hola</li>
						<li>onContextMenu (Edit dscenario): Hola</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>

.. raw:: html
	<details>
		<summary>Initial Quality:: init_quality - Initial quality</summary>
		<ul>
			<li>**Tipo de dato:** string.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** Sí.</li>
			<li>
				<details class='no-square'>
					<summary><b>Controles:</b> Controles del campo</summary>
					<ul>
						<li>filterSign (ILIKE): Hola</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>

.. raw:: html
	<details>
		<summary>Min Demand:: demandmin - Min demand</summary>
		<ul>
			<li>**Tipo de dato:** string.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** No.</li>
			<li>
				<details class='no-square'>
					<summary><b>Controles:</b> Controles del campo</summary>
					<ul>
						<li>filterSign (ILIKE): Hola</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>

.. raw:: html
	<details>
		<summary>Source Type:: source_type - Source type</summary>
		<ul>
			<li>**Tipo de dato:** string.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** Sí.</li>
			<li>**Valores:** Los valores de este desplegable estan determinados por la consulta: SELECT (id) AS id,  idval  AS idval FROM inp_typevalue WHERE id IS NOT NULL AND typevalue='inp_typevalue_source'.</li>
			<li>
				<details class='no-square'>
					<summary><b>Controles:</b> Controles del campo</summary>
					<ul>
						<li>setMultiline (False): Hola</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>

.. raw:: html
	<details>
		<summary>Source Quality:: source_quality - Source quality</summary>
		<ul>
			<li>**Tipo de dato:** string.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** Sí.</li>
			<li>
				<details class='no-square'>
					<summary><b>Controles:</b> Controles del campo</summary>
					<ul>
						<li>filterSign (ILIKE): Hola</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>

.. raw:: html
	<details>
		<summary>Max Head:: headmax - Max head</summary>
		<ul>
			<li>**Tipo de dato:** string.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** No.</li>
			<li>
				<details class='no-square'>
					<summary><b>Controles:</b> Controles del campo</summary>
					<ul>
						<li>filterSign (ILIKE): Hola</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>

.. raw:: html
	<details>
		<summary>Source Pattern:: source_pattern_id - Source pattern</summary>
		<ul>
			<li>**Tipo de dato:** string.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** Sí.</li>
			<li>**Valores:** Los valores de este desplegable estan determinados por la consulta: SELECT DISTINCT (pattern_id) AS id,  pattern_id  AS idval FROM inp_pattern WHERE pattern_id IS NOT NULL.</li>
			<li>
				<details class='no-square'>
					<summary><b>Controles:</b> Controles del campo</summary>
					<ul>
						<li>setMultiline (False): Hola</li>
						<li>valueRelation ({'nullValue': True, 'layer': 've_inp_pattern', 'activated': True, 'keyColumn': 'pattern_id', 'valueColumn': 'pattern_id', 'filterExpression': None}): Hola</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>

.. raw:: html
	<details>
		<summary>Min Head:: headmin - Min head</summary>
		<ul>
			<li>**Tipo de dato:** string.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** No.</li>
			<li>
				<details class='no-square'>
					<summary><b>Controles:</b> Controles del campo</summary>
					<ul>
						<li>filterSign (ILIKE): Hola</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>

.. raw:: html
	<details>
		<summary>Max Pressure:: pressmax - Max pressure</summary>
		<ul>
			<li>**Tipo de dato:** string.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** No.</li>
			<li>
				<details class='no-square'>
					<summary><b>Controles:</b> Controles del campo</summary>
					<ul>
						<li>filterSign (ILIKE): Hola</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>

.. raw:: html
	<details>
		<summary>Min Pressure:: pressmin - Min pressure</summary>
		<ul>
			<li>**Tipo de dato:** string.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** No.</li>
			<li>
				<details class='no-square'>
					<summary><b>Controles:</b> Controles del campo</summary>
					<ul>
						<li>filterSign (ILIKE): Hola</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>

.. raw:: html
	<details>
		<summary>Max Quality:: qualmax - Max quality</summary>
		<ul>
			<li>**Tipo de dato:** string.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** No.</li>
			<li>
				<details class='no-square'>
					<summary><b>Controles:</b> Controles del campo</summary>
					<ul>
						<li>filterSign (ILIKE): Hola</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>

.. raw:: html
	<details>
		<summary>Min Quality:: qualmin - Min quality</summary>
		<ul>
			<li>**Tipo de dato:** string.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** No.</li>
			<li>
				<details class='no-square'>
					<summary><b>Controles:</b> Controles del campo</summary>
					<ul>
						<li>filterSign (ILIKE): Hola</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>

