# encoding: cinje

: def render_reference_block context, block, content

<div&{id=block.properties.get('id', block.id), class_=block.properties.get('cls', None)}>
: if callable(content)
	: use content context
: else
	: _buffer.extend(content)
: end
</div>
