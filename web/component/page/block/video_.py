# encoding: cinje

: from orderedset import OrderedSet
: from marrow.util.url import QueryString

: def render_video_block context, block
: """Render a YouTube video embed."""

: classes = OrderedSet(block.properties.get('cls', '').split() + ['block', 'video'])

: if 'width' in block.properties
	: classes.add('col-md-' + str(block.properties.width))
: end

: if block.videos
	: uri = block.videos[context.lang]
: else
	: uri = block.video
: end

<div&{id=block.properties.get('id', block.id), class_=classes}>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/${uri}" frameborder="0" allowfullscreen></iframe>
</div>

