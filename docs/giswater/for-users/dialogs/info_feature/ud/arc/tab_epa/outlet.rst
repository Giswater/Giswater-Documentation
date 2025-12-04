======
Outlet
======


List of Result EPA values

.. raw:: html

	<p class='layout-header'>The fields in the layout lyt_epa_data_1 are:</p>

.. raw:: html

	<details>
		<summary><strong>Outlet Type:</strong> outlet_type - outlet_type</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> The values of this dropdown are determined by the query:
				<code>
					SELECT id, idval FROM inp_typevalue WHERE id IS NOT NULL AND typevalue='inp_typevalue_outlet' 
				</code>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Field controls</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Sets the possibility of multiline fields for writing with enter</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Offset:</strong> offsetval - offsetval</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Field controls</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Sets the possibility of multiline fields for writing with enter</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Curve Id:</strong> curve_id - curve_id</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> The values of this dropdown are determined by the query:
				<code>
					SELECT id, id AS idval FROM inp_curve  WHERE id IS NOT NULL
				</code>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Field controls</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Sets the possibility of multiline fields for writing with enter</li>
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
		<summary><strong>Cd1:</strong> cd1 - cd1</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Field controls</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Sets the possibility of multiline fields for writing with enter</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Cd2:</strong> cd2 - cd2</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Field controls</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Sets the possibility of multiline fields for writing with enter</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Flap:</strong> flap - flap</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> The values of this dropdown are determined by the query:
				<code>
					SELECT id, idval FROM inp_typevalue WHERE id IS NOT NULL AND typevalue='inp_value_yesno' 
				</code>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Field controls</summary>
					<ul>
						<li><strong>setMultiline</strong> (False): Sets the possibility of multiline fields for writing with enter</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<p class='layout-header'>The fields in the layout lyt_epa_data_2 are:</p>

.. raw:: html

	<details>
		<summary><strong>Max Flow:</strong> max_flow - max_flow</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Field controls</summary>
					<ul>
						<li><strong>filterSign</strong> (ILIKE): </li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Time Days:</strong> time_days - time_days</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Field controls</summary>
					<ul>
						<li><strong>filterSign</strong> (ILIKE): </li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Time Hour:</strong> time_hour - time_hour</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Field controls</summary>
					<ul>
						<li><strong>filterSign</strong> (ILIKE): </li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Max Veloc:</strong> max_veloc - max_veloc</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Field controls</summary>
					<ul>
						<li><strong>filterSign</strong> (ILIKE): </li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Mfull Flow:</strong> mfull_flow - mfull_flow</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Field controls</summary>
					<ul>
						<li><strong>filterSign</strong> (ILIKE): </li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Mfull Depth:</strong> mfull_depth - mfull_depth</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Field controls</summary>
					<ul>
						<li><strong>filterSign</strong> (ILIKE): </li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


