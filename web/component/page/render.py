# encoding: cinje

: def render_page_content page

: width = 12
<div class="row">

: for block in page.content
	: size = block.properties.get('width', 12)
	: width -= size
	
	: if width < 0
		: width = 12 - size
</div>
<div class="row row-eq-height">
	: end

	: use block.as_stream
: end

</div>
