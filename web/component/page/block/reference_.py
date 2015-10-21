# encoding: cinje

: def render_reference_block block, content

<div&{id=block.properties.get('id', block.id), class_=block.properties.get('cls', None)}>
: if callable(content)
	: use content
: else
	: _buffer.extend(content)
: end
</div>
