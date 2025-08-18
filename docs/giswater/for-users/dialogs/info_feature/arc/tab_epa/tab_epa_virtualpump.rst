.. _tab-epa-virtualpump

====================
Virtualpump: Tab Epa
====================

The feature virtualpump, has the following data:

.. raw:: html
	<details>
		<summary>Tabla Virtualpump: tbl_inp_virtualpump - None</summary>
		<ul>
			<li>**Tipo de dato:** None.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** No.</li>
			<li>
				<details class='no-square'>
					<summary><b>Controles:</b> Controles del campo</summary>
					<ul>
						<li>saveValue (False): Hola</li>
						<li>tableUpsert (ve_inp_dscenario_virtualpump): Hola</li>
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
		<summary>Power:: power - Power</summary>
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
		<summary>Max Flow:: flow_max - Max Flow</summary>
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
		<summary>Curve Id:: curve_id - Curve id</summary>
		<ul>
			<li>**Tipo de dato:** string.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** Sí.</li>
			<li>**Valores:** Los valores de este desplegable estan determinados por la consulta: SELECT id, id AS idval FROM inp_curve WHERE id IS NOT NULL.</li>
			<li>
				<details class='no-square'>
					<summary><b>Controles:</b> Controles del campo</summary>
					<ul>
						<li>valueRelation ({'nullValue': False, 'layer': 've_inp_curve', 'activated': True, 'keyColumn': 'id', 'valueColumn': 'id', 'filterExpression': None}): Hola</li>
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
		<summary>Min Flow:: flow_min - Min Flow</summary>
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
		<summary>Speed:: speed - Speed</summary>
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
		<summary>Max Velocity:: vel_max - Max velocity</summary>
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
		<summary>Min Velocity:: vel_min - Min velocity</summary>
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
		<summary>Status:: status - Status</summary>
		<ul>
			<li>**Tipo de dato:** string.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** Sí.</li>
			<li>**Valores:** Los valores de este desplegable estan determinados por la consulta: SELECT DISTINCT (id) AS id,  idval  AS idval FROM inp_typevalue WHERE id IS NOT NULL AND typevalue='inp_value_status_pump'.</li>
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
		<summary>Max Headloss:: headloss_max - Max headloss</summary>
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
		<summary>Min Headloss:: headloss_min - Min headloss</summary>
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
		<summary>Quality:: quality - Quality</summary>
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
		<summary>Usage Factor:: usage_fact - Usage factor</summary>
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
		<summary>Pump Type:: pump_type - Pump type</summary>
		<ul>
			<li>**Tipo de dato:** string.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** Sí.</li>
			<li>**Valores:** Los valores de este desplegable estan determinados por la consulta: SELECT id, idval FROM inp_typevalue WHERE typevalue = 'inp_typevalue_pumptype'.</li>
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
		<summary>Average Efficiency:: avg_effic - Average efficiency</summary>
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
		<summary>Effic Curve Id:: effic_curve_id - effic_curve_id</summary>
		<ul>
			<li>**Tipo de dato:** string.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** Sí.</li>
			<li>**Valores:** Los valores de este desplegable estan determinados por la consulta: SELECT id, id AS idval FROM inp_curve 
WHERE id IS NOT NULL.</li>
			<li>
				<details class='no-square'>
					<summary><b>Controles:</b> Controles del campo</summary>
					<ul>
						<li>setMultiline (False): Hola</li>
						<li>valueRelation ({'nullValue': True, 'layer': 've_inp_curve', 'activated': True, 'keyColumn': 'id', 'valueColumn': 'id', 'filterExpression': None}): Hola</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>

.. raw:: html
	<details>
		<summary>Kwh Mgal:: kwhr_mgal - KWh mgal</summary>
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
		<summary>Energy Price:: energy_price - Energy price</summary>
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
		<summary>Energy Pattern:: energy_pattern_id - Energy pattern</summary>
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
		<summary>Average Kw:: avg_kw - Average KW</summary>
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
		<summary>Peak Kw:: peak_kw - Peak KW</summary>
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
		<summary>Cost Day:: cost_day - Cost day</summary>
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

