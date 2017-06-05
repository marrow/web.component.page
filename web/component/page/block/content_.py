# encoding: cinje

: def render_text_block context, block, content
	: kind = block.properties.get('element', 'section')
	:
	: attributes = {}
	: attributes['id'] = block.properties.get('id', block.id)
	: attributes['class_'] = classes = set(block.properties.get('cls', '').split())
	:
	: # TODO: Block must be editable by the user.
	: attributes['data_block'] = block.id
	: attributes['data_format'] = block.format
	: attributes['data_editable'] = True
	: attributes['data_asset'] = block._instance.path
	:
	: if kind == 'a'
		: attributes['href'] = block.properties.get('href', '#missing-href')
	: elif kind == 'iframe'
		: attributes['src'] = block.properties.get('src', 'about:blank#missing-src')
	: end
	:
	: classes.add('wc-content')
	:
	: # Legacy support.
	: if 'width' in block.properties
		: classes.add('col-md-' + str(block.properties.width))
	: end

<${kind}&{attributes}>
	: if getattr(context, 'replacements', None)
		: _buffer.append(content.format(**context.replacements))
	: else
		: _buffer.append(content)
	: end
</${kind}>
