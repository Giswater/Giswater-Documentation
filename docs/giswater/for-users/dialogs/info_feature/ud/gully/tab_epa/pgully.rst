======
Pgully
======


None

.. raw:: html

	<p class='layout-header'>The fields in the layout lyt_epa_data_1 are:</p>

.. raw:: html

	<details>
		<summary><strong>Outlet Type:</strong> outlet_type - Outlet type</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> The values of this dropdown are determined by the query:
				<code>
					SELECT id, idval FROM inp_typevalue WHERE id IS NOT NULL AND typevalue = 'inp_typevalue_gully_type'
				</code>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Custom Top Elev:</strong> custom_top_elev - custom_top_elev</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Field controls</summary>
					<ul>
						<li><strong>autoupdateReloadFields</strong> (['sys_top_elev', 'sys_ymax', 'sys_elev']): Instantly reloads other fields if one is modified. Acts in combination with isautoupdate</li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Custom Width:</strong> custom_width - Custom width</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Custom Depth:</strong> custom_depth - Custom depth</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Method:</strong> gully_method - Method</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> The values of this dropdown are determined by the query:
				<code>
					SELECT id, idval FROM inp_typevalue WHERE id IS NOT NULL AND typevalue = 'inp_typevalue_gully_method'
				</code>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Weir Cd:</strong> weir_cd - Weir cd</summary>
		<ul>
			<li><strong>Datatype:</strong> Numeric.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Orifice Cd:</strong> orifice_cd - Orifice cd</summary>
		<ul>
			<li><strong>Datatype:</strong> Numeric.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Custom A Parameter:</strong> custom_a_param - Custom a parameter</summary>
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
		<summary><strong>Custom B Parameter:</strong> custom_b_param - Custom b parameter</summary>
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
		<summary><strong>Efficiency:</strong> efficiency - Efficiency</summary>
		<ul>
			<li><strong>Datatype:</strong> Double.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


