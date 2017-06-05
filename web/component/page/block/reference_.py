# encoding: cinje

: from .common_ import base_block_list_item

: def reference_block_list_item block, wrap=False
	: using base_block_list_item block, True
		<a&{href=block.target.path, class_={'fa', 'fa-bullseye'}, title=block.target.path}></a>
	: end
: end


: def render_reference_block context, block, content
	: kind = block.target.properties.get('element', block.properties.get('element', 'section'))
	:
	: attributes = {}
	: attributes['id'] = block.target.properties.get('id', block.properties.get('id', block.target.id))
	: attributes['class_'] = classes = set(block.properties.get('cls', '').split())
	:
	: # TODO: Block must be editable by the user.
	: attributes['data_block'] = block.id
	: attributes['data_editable'] = False
	: attributes['data_asset'] = block._instance.path
	: attributes['data_reference'] = block.target.path
	:
	: data = {}
	: data.update(block.target.properties.get('data', {}))
	: data.update(block.properties.get('data', {}))
	:
	: for k, v in data.items()
		: attributes['data_' + k] = v
	: end
	:
	: classes.update(block.target.properties.get('cls', '').split())
	: classes.add('wc-reference')
	:
	: # Legacy support.
	: if 'width' in block.properties
		: classes.add('col-md-' + str(block.properties.width))
	: end

<${kind}&{attributes}>
: if callable(content)
	: use content context
: else
	: _buffer.extend(content)
: end
</${kind}>
