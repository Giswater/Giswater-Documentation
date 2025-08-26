.. _tab-epa-outlet

======
Outlet
======


List of Result EPA values

.. raw:: html

	<p class='layout-header'>Los campos en el layout lyt_epa_data_1 son:</p>

.. raw:: html

	<details>
		<summary><strong>Tipo De Salida:</strong> outlet_type - Una salida puede ser: TABULAR / PROFUNDIDAD, TABULAR / CABEZAL, FUNCIONALÂ / PROFUNDIDAD o FUNCIONAL / CABEZAL.</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, idval FROM inp_typevalue WHERE id IS NOT NULL AND typevalue='inp_typevalue_outlet' 
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
		<summary><strong>Compensación:</strong> offsetval - Desplazamiento</summary>
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
		<summary><strong>Cd1:</strong> cd1 - Coeficiente de una función de descarga FUNCIONAL</summary>
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
		<summary><strong>Cd2:</strong> cd2 - Exponente de una función de descarga FUNCIONAL</summary>
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
		<summary><strong>Compuerta:</strong> flap - SÍ si el conducto tiene una compuerta que impide el reflujo, NO en caso contrario (por defecto es NO).</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> Los valores de este desplegable estan determinados por la consulta:
				<code>
					SELECT id, idval FROM inp_typevalue WHERE id IS NOT NULL AND typevalue='inp_value_yesno' 
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

	<p class='layout-header'>Los campos en el layout lyt_epa_data_2 son:</p>

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
		<summary><strong>Tiempo En Días:</strong> time_days - tiempo_días</summary>
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
		<summary><strong>Tiempo En Horas:</strong> time_hour - hora</summary>
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
		<summary><strong>Velocidad Máxima:</strong> max_veloc - Velocidad máxima - max_velocity </summary>
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
		<summary><strong>Mfull_Flow:</strong> mfull_flow - mfull_flow</summary>
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
		<summary><strong>Mfull_Profundidad:</strong> mfull_depth - mfull_profundidad</summary>
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


