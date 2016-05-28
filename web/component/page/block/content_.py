# encoding: cinje

: def render_text_block context, block, content
: classes = set(block.properties.get('cls', '').split())

: if 'width' in block.properties
	: classes.add('col-md-' + str(block.properties.width))
: end

<section&{id=block.properties.get('id', block.id), class_=classes, data_block=block.id, data_format=block.format, data_editable="yes", data_asset=block._instance.path}>
: if getattr(context, 'replacements', None)
	: _buffer.append(content.format(**context.replacements))
: else
	: _buffer.append(content)
: end
</section>
