# encoding: cinje

: from web.core import local

: def base_block_list_item block, wrap=False
	<li&{data_id=block.id}>
		<label&{class_={'fa', 'fa-' + block.__icon__}}>
			${block.name}
		</label>
		<a&{href="#" + str(block.properties.get('id', block.id)), class_={'fa', 'fa-hashtag'}}>
			<tt&{class_={'sr-only'} if not block.properties.get('id', None) else ()}>${str(block.properties.get('id', block.id))}</tt>
		</a>
		: if wrap
			: yield
		: end
		<a&{href=local.context.asset.path + '/' + str(block.id), class_={'fa', 'fa-times'}, data_verb='delete', data_trigger='block-deleted'}><span class="sr-only"> Delete</span></a>
	</li>
: end

