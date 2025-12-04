======
Frpump
======


Epa

.. raw:: html

	<p class='layout-header'>The fields in the layout lyt_epa_data_1 are:</p>

.. raw:: html

	<details>
		<summary><strong>Curve Id:</strong> curve_id - Curve Id</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> The values of this dropdown are determined by the query:
				<code>
					SELECT id, id AS idval FROM inp_curve WHERE id IS NOT NULL
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
		<summary><strong>Status:</strong> status - Status</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> The values of this dropdown are determined by the query:
				<code>
					SELECT  id, idval FROM inp_typevalue WHERE id IS NOT NULL AND typevalue='inp_value_status'
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
		<summary><strong>Startup:</strong> startup - Startup</summary>
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
		<summary><strong>Shutoff:</strong> shutoff - Shutoff</summary>
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

	<p class='layout-header'>The fields in the layout lyt_epa_data_2 are:</p>

.. raw:: html

	<details>
		<summary><strong>Percent:</strong> percent - Percent</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
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
		<summary><strong>Number Of Startups:</strong> num_startup - Number of Startups</summary>
		<ul>
			<li><strong>Datatype:</strong> Integer.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
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
		<summary><strong>Minimum Flow:</strong> min_flow - Minimum Flow</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
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
		<summary><strong>Average Flow:</strong> avg_flow - Average Flow</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
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
		<summary><strong>Maximum Flow:</strong> max_flow - Maximum Flow</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
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
		<summary><strong>Volume (Liters):</strong> vol_ltr - Volume (Liters)</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
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
		<summary><strong>Power Usage (Kwh):</strong> powus_kwh - Power Usage (kWh)</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
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
		<summary><strong>Time Off Minimum:</strong> timoff_min - Time Off Minimum</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
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
		<summary><strong>Time Off Maximum:</strong> timoff_max - Time Off Maximum</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
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


