# encoding: cinje

: from web.theme.bootstrap.base import page


: def render_page_content context, page

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

	: use block.__html_stream__ context
: end

</div>

: end


: def render_page context, asset
: using page title=str(asset), styles=['/public/css/site.css'], scripts=['//cdn.ckeditor.com/4.5.4/full/ckeditor.js', '/public/js/site.js']

: flush

<article class="container">

: use asset.__html_stream__ context

: flush

<div class="wc-properties panel" role="tabpanel">
	<ul class="wc-tabs" role="tablist">
		<li role="presentation" class="active">
			<a href="#wc-cfg-struct" aria-controls="wc-cfg-site" role="tab" data-toggle="tab" title="Site Settings">
				<i class="fa fa-sitemap fa-lg"></i>
				<span class="sr-only">Site Structure</span>
			</a>
		</li>
		<li role="presentation">
			<a href="#wc-cfg-page" aria-controls="wc-cfg-page" role="tab" data-toggle="tab">
				<i class="fa fa-newspaper-o fa-lg"></i>
				<span class="sr-only">Page</span>
			</a>
		</li>
		<li role="presentation" class="disabled">
			<a href="#wc-cfg-block" aria-controls="wc-cfg-block" role="tab" data-toggle="tab">
				<i class="fa fa-cube fa-lg"></i>
				<span class="sr-only">Block</span>
			</a>
		</li>
		<li role="presentation" class="disabled">
			<a href="#wc-cfg-text" aria-controls="wc-cfg-text" role="tab" data-toggle="tab">
				<i class="fa fa-edit fa-lg"></i>
				<span class="sr-only">Content</span>
			</a>
		</li>
		<li role="presentation">
			<a href="#wc-cfg-site" aria-controls="wc-cfg-site" role="tab" data-toggle="tab" title="Site Settings">
				<i class="fa fa-cog fa-lg"></i>
				<span class="sr-only">Site Settings</span>
			</a>
		</li>
	</ul>
	<div class="tab-content">
		<ul class="tab-pane active list-group" id="wc-cfg-struct" role="tabpanel">
			<li class="list-group-item" id="">
				<h4>
					Site Structure
					<a href="#" style="display: inline-block; margin: -10px;"><sup style="display: inline-block; padding: 10px 10px 0;"><i class="fa fa-question-circle small"></i></sup></a>
				</h4>
				<menu class="list-unstyled wc-cfg-flist">
					: from web.component.asset.model import Asset
					: for child in Asset.objects.only('id').get(path='/careers.illicohodes.com').children
						<li>
							<a href="${child.path[24:]}">
								<i class="fa fa-${child.__icon__} fa-lg fa-fw"></i>
								${child.title['en']}
							</a>
							: if child.children.count()
							<menu class="list-unstyled">
							: for descendant in child.children
								<a href="${descendant.path[24:]}">
									<i class="fa fa-${descendant.__icon__} fa-lg fa-fw"></i>
									${descendant.title['en']}
								</a>
								: if descendant.children.count()
								<menu class="list-unstyled">
								: for d2 in descendant.children
									<a href="${d2.path[24:]}">
										<i class="fa fa-${d2.__icon__} fa-lg fa-fw"></i>
										${d2.title['en']}
									</a>
								: end
								</menu>
								: end
							: end
							</menu>
							: end
						</li>
					: end
				</menu>
			</li>
		</ul>
		
		: flush
		
		<ul class="tab-pane list-group" id="wc-cfg-page" role="tabpanel">
			<li class="list-group-item">
				<h4>
					General
					<a href="#" style="display: inline-block; margin: -10px;"><sup style="display: inline-block; padding: 10px 10px 0;"><i class="fa fa-question-circle small"></i></sup></a>
				</h4>
				<dl>
					<dt>Name</dt>
					<dd>${asset.name}</dd>
					<dt>Title</dt>
					<dd>${asset.title['en']}</dd>
					<dt>Description</dt>
					: if asset.description.get('en', None)
					<dd>${asset.title['en']}</dd>
					: else
					<dd><em>None entered.</em></dd>
					: end
					<dt>Tags</dt>
					: if asset.tags
					<dd>${','.join(asset.tags)}</dd>
					: else
					<dd><em>None entered.</em></dd>
					: end
					<dt>Created</dt>
					<dd>${asset.created.isoformat()}</dd>
					<dt>Modified</dt>
					<dd>${asset.modified.isoformat()}</dd>
				</dl>
			</li>
			<!--
			<li class="list-group-item">
				<h4>
					
					<a href="#" style="display: inline-block; margin: -10px;"><sup style="display: inline-block; padding: 10px 10px 0;"><i class="fa fa-question-circle small"></i></sup></a>
				</h4>
			</li>
			-->
			<li class="list-group-item" id="">
				<h4>
					Block Structure
					<a href="#" style="display: inline-block; margin: -10px;"><sup style="display: inline-block; padding: 10px 10px 0;"><i class="fa fa-question-circle small"></i></sup></a>
				</h4>
				
				<menu class="list-unstyled wc-cfg-flist">
					: for child in asset.content
					<li>
						<a href="#${child.id}">
							<i class="fa fa-${child.__icon__} fa-lg fa-fw"></i>
							${str(child)}
						</a>
					</li>
					: end
			</menu>
			</li>
		</ul>
		
		: flush
		
		: if asset.content
		<ul class="tab-pane list-group" id="wc-cfg-block" role="tabpanel">
			<li class="list-group-item">
				<h4>
					Text Block
					<a href="#" style="display: inline-block; margin: -10px;"><sup style="display: inline-block; padding: 10px 10px 0;"><i class="fa fa-question-circle small"></i></sup></a>
				</h4>
				<dl>
					<dt>Unique Identifier</dt>
					<dd><tt>${asset.content[0].id}</tt></dd>
					<dt>Format Engine</dt>
					<dd>HTML</dd>
				</dl>
			</li>
			<li class="list-group-item">
				<h4>
					Cascading Style Sheets
					<a href="#" style="display: inline-block; margin: -10px;"><sup style="display: inline-block; padding: 10px 10px 0;"><i class="fa fa-question-circle small"></i></sup></a>
				</h4>
				<dl>
					<dt>Unique Identifier</dt>
					<dd><em>None entered.</em></dd>
					<dt>Classes</dt>
					<dd><tt>${asset.content[0].properties.get('cls', "None entered.")}</tt></dd>
				</dl>
			</li>
		</ul>
		: end
		
		: flush
		
		<ul class="tab-pane list-group" id="wc-cfg-site" role="tabpanel">
			<li class="list-group-item loading" id="wc-p-notice">
				<h4>
					<div class="wc-ld"><i class="fa fa-lg fa-refresh fa-spin"></i></div>
					<i class="fa fa-exclamation-triangle fa-lg text-warning"></i>
					Important Notices
					<a href="#" style="display: inline-block; margin: -10px;"><sup style="display: inline-block; padding: 10px 10px 0;"><i class="fa fa-question-circle small"></i></sup></a>
				</h4>
				
				<div class="content">
					<p role="alert">
						You will be running into yor mail quota in about a week.  <a href="">Learn more about mail quotas.</a>
					</p>
				</div>
			</li>
			<li class="list-group-item">
				
				<h4>
					Domains
					<a href="#" style="display: inline-block; margin: -10px;"><sup style="display: inline-block; padding: 10px 10px 0;"><i class="fa fa-question-circle small"></i></sup></a>
				</h4>
				
				<p>Buy, connect, and manage domains associated with this site.  <a href="">Learn more about domains.</a></p>
				
				<ul class="nav nav-pills nav-stacked actions">
					<li role="presentation" class="primary"><a href="#"><i class="fa fa-cloud fa-lg fa-fw"></i> Get a Domain</a></li>
					<li role="presentation"><a href="#"><i class="fa fa-external-link-square fa-lg fa-fw"></i> Connect a Third-Party Domain</a></li>
				</ul>
				
				<h5>Third-Party Domains</h5>
				
				<ul class="nav nav-pills nav-stacked">
					<li role="presentation" class="wc-dn wc-dn-ok"><a href="#">
						<label>careers.alstom.com</label>
						<div class="">
							<span class="label label-primary pull-right">Primary</span>
							<span class="expires">Never Expires</span>
						</div>
					</a></li>
				</ul>
				
				<h5>Built-In Domain</h5>
				
				<ul class="nav nav-pills nav-stacked">
					<li role="presentation" class="wc-dn wc-dn-ok"><a href="#">
						<label>illico-test.webcore.io</label>
						<div class="">
							<span class="label label-default pull-right">Development</span>
							<span class="expires">Never Expires</span>
						</div>
					</a></li>
				</ul>
				
			</li>
			
			<li class="list-group-item">
				
				<h4>
					<i class="pull-right fa fa-exclamation-triangle fa-lg text-warning"></i>
					E-Mail
					<a href="#" style="display: inline-block; margin: -10px;"><sup style="display: inline-block; padding: 10px 10px 0;"><i class="fa fa-question-circle small"></i></sup></a>
				</h4>
				
				<p>Connect and manage mail servers.  <a href="">Learn more about mail.</a></p>
				
				<ul class="nav nav-pills nav-stacked actions">
					<li role="presentation"><a href="#"><i class="fa fa-external-link-square fa-lg fa-fw"></i> Connect a Third-Party Service</a></li>
				</ul>
				
				<h5>Built-In Mail Service</h5>
				
				<ul class="nav nav-pills nav-stacked">
					<li role="presentation" class="wc-dn wc-dn-ng"><a href="#">
						<label>illico-test.webcore.io</label>
						<div class="">
							<span class="label label-primary pull-right">Primary</span>
							<span class="expires">Sent <strong>18,368</strong> out of <strong>30,000</strong>.</span>
						</div>
						# :: include(asset.theme + 'widget.progress', current=[(30, 'success'), (20, 'warning')], minimum=0, maximum=100)
					</a></li>
				</ul>
				
			</li>
			
			<li class="list-group-item">
				<h4>
					Import / Export
					<a href="#" style="display: inline-block; margin: -10px;"><sup style="display: inline-block; padding: 10px 10px 0;"><i class="fa fa-question-circle small"></i></sup></a>
				</h4>
				
				<ul class="nav nav-pills nav-justified actions">
					<li role="presentation" class="primary" style="padding-right: 5px;"><a href="#"><i class="fa fa-download fa-lg fa-fw"></i> Import</a></li>
					<li role="presentation" style="padding-left: 5px;"><a href="#"><i class="fa fa-upload fa-lg fa-fw"></i> Export</a></li>
				</ul>
			</li>
			
			<!--
			<li class="list-group-item">
				<a href="javascript:$('#wc-p-notice').removeClass('loading loaded');">Default</a>
				<a href="javascript:$('#wc-p-notice').removeClass('loaded').addClass('loading');">Loading</a>
				<a href="javascript:$('#wc-p-notice').removeClass('loading').addClass('loaded');">Loaded</a>
			</li>
			-->
		</ul>
		
		<div role="tabpanel" class="tab-pane" id="wc-cfg-text">
			
			<div class="">
				<h2>Heading 2</h2>
			</div>
			
		</div>
	</div>
	
</div>
<div class="wc-properties-trigger"><a href="#"><i class="fa fa-pencil fa-flip-horizontal fa-lg fa-fw"></i></a></div>
</article>

: end
