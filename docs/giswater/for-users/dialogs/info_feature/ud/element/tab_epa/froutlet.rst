.. _tab-epa-froutlet

========
Froutlet
========


Epa

.. raw:: html

	<p class='layout-header'>Los campos en el layout lyt_epa_data_1 son:</p>

.. raw:: html

	<details>
		<summary><strong>Tipo De Salida:</strong> outlet_type - Tipo de salida</summary>
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
		<summary><strong>Valor De Desplazamiento:</strong> offsetval - Valor de desplazamiento</summary>
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
		<summary><strong>Id De Curva:</strong> curve_id - ID de curva</summary>
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
		<summary><strong>Coeficiente De Descarga 1:</strong> cd1 - Coeficiente de descarga 1</summary>
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
		<summary><strong>Coeficiente De Descarga 2:</strong> cd2 - Coeficiente de descarga 2</summary>
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
		<summary><strong>Solapa:</strong> flap - Solapa</summary>
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

	<p class='layout-header'>Los campos en el layout lyt_epa_data_2 son:</p>

.. raw:: html

	<details>
		<summary><strong>Caudal Máximo:</strong> max_flow - Caudal máximo</summary>
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
		<summary><strong>Tiempo Días:</strong> time_days - Tiempo Días</summary>
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
		<summary><strong>Hora:</strong> time_hour - Hora</summary>
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
		<summary><strong>Velocidad Máxima:</strong> max_veloc - Velocidad máxima</summary>
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
		<summary><strong>Flujo Total:</strong> mfull_flow - Flujo total</summary>
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
		<summary><strong>Profundidad Total:</strong> mfull_dept - Profundidad total</summary>
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
		<summary><strong>Cizallamiento Máximo:</strong> max_shear - Cizallamiento máximo</summary>
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
		<summary><strong>Radio Hidráulico Máximo:</strong> max_hr - Radio hidráulico máximo</summary>
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
		<summary><strong>Pendiente Máxima:</strong> max_slope - Pendiente máxima</summary>
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
		<summary><strong>Día Máximo:</strong> day_max - Día Máximo</summary>
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
		<summary><strong>Tiempo Máximo:</strong> time_max - Tiempo Máximo</summary>
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
		<summary><strong>Cizallamiento Mínimo:</strong> min_shear - Cizallamiento mínimo</summary>
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
		<summary><strong>Día Mínimo:</strong> day_min - Día Mínimo</summary>
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
		<summary><strong>Tiempo Mínimo:</strong> time_min - Tiempo Mínimo</summary>
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


