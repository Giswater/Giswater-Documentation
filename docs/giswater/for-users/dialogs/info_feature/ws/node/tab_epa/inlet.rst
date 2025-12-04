=====
Inlet
=====


None

.. raw:: html

	<p class='layout-header'>The fields in the layout lyt_epa_data_1 are:</p>

.. raw:: html

	<details>
		<summary><strong>Init Level:</strong> initlevel - Initial level</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
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
		<summary><strong>Min Level:</strong> minlevel - Minimum level</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
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
		<summary><strong>Max Level:</strong> maxlevel - Maximum level</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
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
		<summary><strong>Diameter:</strong> diameter - Diameter</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
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
		<summary><strong>Min Volume:</strong> minvol - Minimum volume</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
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
		<summary><strong>Curve Id:</strong> curve_id - Curve id</summary>
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
						<li>
							<details class='no-square'>
								<summary><strong>valueRelation:</strong> </summary>
								<ul>
									<li>nullValue: False</li>
									<li>layer: ve_inp_curve</li>
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
		<summary><strong>Overflow:</strong> overflow - Overflow</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
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
		<summary><strong>Mixing Model:</strong> mixing_model - Mixing model</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> The values of this dropdown are determined by the query:
				<code>
					SELECT id, idval FROM inp_typevalue WHERE typevalue='inp_value_mixing'
				</code>
			</li>
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
		<summary><strong>Mixing Fraction:</strong> mixing_fraction - Mixing fraction</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
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
		<summary><strong>Reaction Coefficient:</strong> reaction_coeff - Reaction coefficient</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
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
		<summary><strong>Initial Quality:</strong> init_quality - Initial quality</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
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
		<summary><strong>Source Type:</strong> source_type - Source type</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> The values of this dropdown are determined by the query:
				<code>
					SELECT (id) AS id,  idval  AS idval FROM inp_typevalue WHERE id IS NOT NULL AND typevalue='inp_typevalue_source'
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
		<summary><strong>Source Quality:</strong> source_quality - Source quality</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
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
		<summary><strong>Source Pattern:</strong> source_pattern_id - Source pattern</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> The values of this dropdown are determined by the query:
				<code>
					SELECT DISTINCT (pattern_id) AS id,  pattern_id  AS idval FROM inp_pattern WHERE pattern_id IS NOT NULL
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
									<li>layer: ve_inp_pattern</li>
									<li>activated: True</li>
									<li>keyColumn: pattern_id</li>
									<li>valueColumn: pattern_id</li>
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
		<summary><strong>Pattern Id:</strong> pattern_id - Pattern id</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> The values of this dropdown are determined by the query:
				<code>
					SELECT DISTINCT (pattern_id) AS id,  pattern_id  AS idval FROM inp_pattern WHERE pattern_id IS NOT NULL
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
									<li>layer: ve_inp_pattern</li>
									<li>activated: True</li>
									<li>keyColumn: pattern_id</li>
									<li>valueColumn: pattern_id</li>
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
		<summary><strong>Head:</strong> head - Head</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
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
		<summary><strong>Demand:</strong> demand - Demand</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Demand Pattern:</strong> demand_pattern_id - Demand pattern</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
			<li><strong>Dvquerytext:</strong> The values of this dropdown are determined by the query:
				<code>
					SELECT pattern_id as id, pattern_id as idval FROM inp_pattern
				</code>
			</li>
		</ul>
	</details>


.. raw:: html

	<details>
		<summary><strong>Emitter Coef:</strong> emitter_coeff - Emitter coef</summary>
		<ul>
			<li><strong>Datatype:</strong> String.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> Sí.</li>
		</ul>
	</details>


.. raw:: html

	<p class='layout-header'>The fields in the layout lyt_epa_data_2 are:</p>

.. raw:: html

	<details>
		<summary><strong>Result Id:</strong> result_id - Result id</summary>
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
		<summary><strong>Max Demand:</strong> demandmax - Max demand</summary>
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
		<summary><strong>Min Demand:</strong> demandmin - Min demand</summary>
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
		<summary><strong>Max Head:</strong> headmax - Max head</summary>
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
		<summary><strong>Min Head:</strong> headmin - Min head</summary>
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
		<summary><strong>Max Pressure:</strong> pressmax - Max pressure</summary>
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
		<summary><strong>Min Pressure:</strong> pressmin - Min pressure</summary>
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
		<summary><strong>Max Quality:</strong> qualmax - Max quality</summary>
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
		<summary><strong>Min Quality:</strong> qualmin - Min quality</summary>
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

	<p class='layout-header'>The fields in the layout lyt_epa_dsc_1 are:</p>

.. raw:: html

	<details>
		<summary><strong>Add_To_Dscenario:</strong> add_to_dscenario - None</summary>
		<ul>
			<li><strong>Datatype:</strong> Unknown.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Stylesheet:</strong> Aesthetic modifications of the field</summary>
					<ul>
						<li>icon: 113</li>
					</ul>
				</details>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Field controls</summary>
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
					<summary><strong>Stylesheet:</strong> Aesthetic modifications of the field</summary>
					<ul>
						<li>icon: 114</li>
					</ul>
				</details>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Field controls</summary>
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
					<summary><strong>Stylesheet:</strong> Aesthetic modifications of the field</summary>
					<ul>
						<li>icon: 101</li>
					</ul>
				</details>
			</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Field controls</summary>
					<ul>
						<li><strong>saveValue</strong> (False): </li>
						<li><strong>onContextMenu</strong> (Edit dscenario): </li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


.. raw:: html

	<p class='layout-header'>The fields in the layout lyt_epa_dsc_3 are:</p>

.. raw:: html

	<details>
		<summary><strong>Tabla Inp Inlet:</strong> tbl_inp_inlet - None</summary>
		<ul>
			<li><strong>Datatype:</strong> Unknown.</li>
			<li><strong>Mandatory:</strong> No.</li>
			<li><strong>Editable:</strong> No.</li>
			<li>
				<details class='no-square'>
					<summary><strong>Widgetcontrols:</strong> Field controls</summary>
					<ul>
						<li><strong>saveValue</strong> (False): </li>
						<li><strong>tableUpsert</strong> (ve_inp_dscenario_inlet): </li>
					</ul>
				</details>
			</li>
		</ul>
	</details>


