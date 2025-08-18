.. _tab-epa-pipe

=============
Pipe: Tab Epa
=============

The feature pipe, has the following data:

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
		<summary>Minorloss:: minorloss - Minorloss</summary>
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
		<summary>Tabla Pipe: tbl_inp_pipe - None</summary>
		<ul>
			<li>**Tipo de dato:** None.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** No.</li>
			<li>
				<details class='no-square'>
					<summary><b>Controles:</b> Controles del campo</summary>
					<ul>
						<li>saveValue (False): Hola</li>
						<li>tableUpsert (ve_inp_dscenario_pipe): Hola</li>
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
			<li>**Valores:** Los valores de este desplegable estan determinados por la consulta: SELECT DISTINCT (id) AS id,  idval  AS idval FROM inp_typevalue WHERE id IS NOT NULL AND typevalue='inp_value_status_pipe'.</li>
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
		<summary>Material:: cat_matcat_id - Material</summary>
		<ul>
			<li>**Tipo de dato:** string.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** No.</li>
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
		<summary>Builtdate:: builtdate - Builtdate</summary>
		<ul>
			<li>**Tipo de dato:** string.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** No.</li>
		</ul>
	</details>

.. raw:: html
	<details>
		<summary>Cat Roughness:: cat_roughness - Cat roughness</summary>
		<ul>
			<li>**Tipo de dato:** string.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** No.</li>
		</ul>
	</details>

.. raw:: html
	<details>
		<summary>Custom Roughness:: custom_roughness - Custom roughness</summary>
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
		<summary>Cat Dint:: cat_dint - Cat dint</summary>
		<ul>
			<li>**Tipo de dato:** string.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** No.</li>
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
		<summary>Custom Dint:: custom_dint - Custom dint</summary>
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
		<summary>Reaction Parameter:: reactionparam - Reaction parameter</summary>
		<ul>
			<li>**Tipo de dato:** string.</li>
			<li>**Obligatorio:** No.</li>
			<li>**Editable:** Sí.</li>
			<li>**Valores:** Los valores de este desplegable estan determinados por la consulta: SELECT id, idval FROM inp_typevalue WHERE typevalue='inp_value_reactions'.</li>
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
		<summary>Reaction Value:: reactionvalue - Reaction value</summary>
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
		<summary>Buk Coefficient:: bulk_coeff - Buk coefficient</summary>
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
		<summary>Wall Coefficient:: wall_coeff - Wall coefficient</summary>
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
		<summary>Max Setting:: setting_max - Max setting</summary>
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
		<summary>Min Setting:: setting_min - Min setting</summary>
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
		<summary>Max Reaction:: reaction_max - Max reaction</summary>
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
		<summary>Min Reaction:: reaction_min - Min reaction</summary>
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
		<summary>Max Ffactor:: ffactor_max - Max Ffactor</summary>
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
		<summary>Min Ffactor:: ffactor_min - Min Ffactor</summary>
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
		<summary>Max Tot Headloss:: tot_headloss_max - Max Tot Headloss</summary>
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
		<summary>Min Tot Headloss:: tot_headloss_min - Min Tot Headloss</summary>
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

