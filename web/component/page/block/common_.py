# encoding: cinje

: def base_block_list_item block, wrap=False
	<li&{data_id=block.id}>
		<label&{class_={'fa', 'fa-' + block.__icon__}}>
			${block.name}
		</label>
		: if wrap
			: yield
		: else
		<a&{href="#" + str(block.properties.get('id', block.id)), class_={'fa', 'fa-hashtag'}}>
			<tt>${str(block.properties.get('id', block.id))}</tt>
		</a>
		: end
	</li>
: end

