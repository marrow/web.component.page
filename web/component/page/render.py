# encoding: cinje

: import traceback

: log = __import__('logging').getLogger(__name__)




: def render_block context, page, block
	<!-- ${repr(block)} -->
	: try
		: use block.__html_stream__ context
	: except
		: log.exception("Error processing block: " + repr(block), extra=dict(block=block.id, page=page.id))
		: if __debug__
			<pre class="text-error"><code>${traceback.format_exc()}</code></pre>
		: else
			<b class="text-error">An unknown error occurred.</b>
		: end
	: end
: end


: def render_page_content context, page
	<!-- ${repr(page)} -->
	
	# Load page content if not already loaded.
	: content = page.content if page.content else page.__class__.objects.scalar('content').get(id=page.id)
	
	: columns = False
	: width = 12
	
	: for block in page.content
		: size = block.properties.get('width', 12)
		: width -= size
		
		: if width and not columns
			: columns = True
<div class="container row-fluid clearfix">
		: end
		
		: use render_block context, page, block

		: if width <= 0
			: width = 12
			: if columns
				: columns = False
</div>
			: end
		: end
	: end

	: if columns
</div>
	: end
	
	: end
: end


: def render_page context, asset

	# First, we work out what the title should look like.
	: title = [str(asset), str(context.croot)]
	: if context.croot.properties.get('direction', 'rtl') == 'ltr'
		: title.reverse()
	: end
	: title = context.croot.properties.get('separator', ' - ').join(title)
	: title = title.upper() if context.croot.properties.get('titlecase', 'normal') == 'upper' else title
	
	: using context.theme title=title, styles=['/public/css/site.css'], scripts=['/public/js/site.js'], lang=context.lang

<article>

	: flush

	: for chunk in asset.__html_stream__(context)
		: yield chunk
	: end

</article>

: end
