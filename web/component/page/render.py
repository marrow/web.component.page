# encoding: cinje

: from web.theme.bootstrap.base import page


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

: end


: def render_page asset
: using page title=str(asset)

<style>
html, body { height: 100%; background-color: #fff; cursor: default; }
input, textarea { cursor: beam; }
p:last-child { margin-bottom: 0; }
h1:first-child, h2:first-child, h3:first-child, h4:first-child, h5:first-child, h6:first-child { margin-top: 0; }




.ih-head { padding: 0; margin: 15px auto; max-width: 960px; position: relative; }
.ih-head section { }

.ih-head menu { position: absolute; right: 15px; top: 0; }
.ih-head menu > li {
	margin-top: 10px;
	display: inline-block;
}
.ih-head menu > li + li {
	margin-left: 20px;
}
.ih-head menu > li > a {
	padding-right: 0;
	padding-left: 0;
	font-size: 16px;
	line-height: 1;
	font-weight: bold;
	color: black;
	opacity: 0.5;
	border-bottom: 2px solid transparent;
	transition: opacity .25s ease-in-out;
	-moz-transition: opacity .25s ease-in-out;
	-webkit-transition: opacity .25s ease-in-out;
}
.ih-head menu > li > a:hover,
.ih-head menu > li > a:focus {
	text-decoration: none;
	background-color: transparent;
	border-bottom-color: black;
	opacity: 0.75;
}
.ih-head menu > .active > a,
.ih-head menu > .active > a:hover,
.ih-head menu > .active > a:focus {
	color: #fff;
	border-bottom-color: #fff;
	opacity: 0.9;
}

.ih-head h1 {
	line-height: 1;
	margin-top: 10px;
	margin-bottom: 0;
	display: inline-block;
}

.ih-head h2 {
	font-size: 31px;
	margin-top: 0;
	line-height: 1.4;
}


body #job-hero { border-top: 1px solid #ccc; border-bottom: 2px solid #ccc; background-color: #eee; -webkit-box-shadow: inset 0 0 5px rgba(0,0,0,0.1); padding: 25px 0; }
body #job-hero h2 { margin: 0 auto; max-width: 960px; display: block; font-size: 24px; }

section.row { padding: 20px 0; margin: 0 auto; max-width: 960px; }
body #job-aside { }

article > :last-child section { margin-top: 80px; padding: 20px 0; text-align: center; border-top: 1px solid #ccc; }
article > :last-child section p, article > :last-child section menu, article > :last-child section li, article > :last-child section a { display: inline-block; }
article > :last-child section a { font-weight: bold; margin-left: 20px; }



</style>

: flush

<article class="container">

: use asset.as_stream

</article>

: flush

<style>
	
	section { text-align: left; }

	.wc-properties { position: fixed; right: -100%; width: 100%; top: 0; height: 100%; overflow-x: visible; overflow-y: scroll; z-index: 10000; background-color: rgba(0,0,0,0.8); border: 0; border-left: 2px solid black; border-radius: 0; color: #ddd; -webkit-transition: right .5s ease-in-out, width .5s ease-in-out; box-model: border-box; }
	
	
	body.wc-prop-active .wc-properties { right: 0px; }
	
	article > section, article > footer, .ih-head-content { -webkit-transition: margin-right .5s ease-in-out; }
	@media (min-width: 640px) {
		.wc-properties { right: -320px; width: 320px; }
		body.wc-prop-active article > section, body.wc-prop-active article > footer,
		body.wc-prop-active .ih-head-content { margin-right: 320px; }
	}
	@media (min-width: 1395px) {
		.wc-properties { right: -420px; width: 420px; }
		body.wc-prop-active article > section, body.wc-prop-active article > footer,
		body.wc-prop-active .ih-head-content { margin-right: 420px; }
	}
		
	.wc-properties-trigger { position: fixed; right: 0px; top: 0px; z-index: 10001; }
	.wc-properties-trigger a { display: block; position: absolute; top: 0; right: 0; width: 32px; height: 32px; border: 16px solid white; border-left-color: transparent; border-bottom-color: transparent; }
	.wc-properties-trigger a i { position: absolute; top: -12px; right: -18px; color: black; }
	
	.wc-properties .wc-tabs {
		width: 100%;
		list-style: none;
		margin: 0;
		padding: 0;
	}
	
	.wc-properties .wc-tabs li {
		display: table-cell;
		width: 1%;
		float: none;
		position: relative;
	}
	
	.wc-properties .wc-tabs li a {
		border: 2px solid black;
		border-top-width: 0;
		background-color: rgba(0,0,0,0.5);
		text-align: center;
		line-height: 1.42857143;
		position: relative;
		display: block;
		padding: 10px 15px;
		text-decoration: none;
		color: rgba(255,255,255,0.75);
		text-shadow: 0 1px 0px rgba(0,0,0,.5)
	}
	
	.wc-properties .wc-tabs li a:hover {
		border-bottom-color: rgba(255,255,255,0.25);
		color: white;
	}
	
	.wc-properties .wc-tabs li.active a {
		background-color: transparent;
		border-color: transparent;
		border-bottom-color: rgba(255,255,255,0.9);
		color: white;
	}
	
	.wc-properties { }
	.wc-properties.panel .list-group-item { background-color: transparent; padding: 15px; border: 0; border-bottom: 2px solid black; }
	.wc-properties .list-group-item:last-child { border-bottom-width: 0; }
	
	.list-group-item > dl { margin: 0; }
	.list-group-item > dl > dt { margin: 0; text-transform: uppercase; font-size: 12px; font-weight: bold; margin-top: 15px; }
	.list-group-item > dl > dd { margin: 0; padding: 0; }
	.list-group-item > dl > dd:last-child { padding-bottom: 0; }
	
	.wc-properties h5 { text-transform: uppercase; font-size: 12px; font-weight: bold; margin-top: 20px; }
	
	.wc-dn { border-radius: 0; background-color: rgba(255,255,255,0.5); border: none; border-left: 3px solid red; }
	.wc-dn.wc-dn-ok { border-left-color: green; }
	.wc-dn.wc-dn-ng { border-left-color: #f0ad4e; }
	.wc-dn label { display: block; font-weight: bold; text-transform: uppercase; cursor: inherit; }
	.wc-dn a { color: white; text-shadow: 0 1px 0px rgba(0,0,0,.5); border-radius: 0; }
	.wc-dn a:hover { color: black; text-shadow: none; border-radius: 0; }
	.wc-dn .progress { margin: 5px 0; height: 6px; border-radius: 0; }
	
	.wc-properties .alert { margin-top: 10px; margin-bottom: 0; }
	.wc-properties .alert:first-child { margin-top: 0; }
	
	/*
	.wc-properties .panel-heading menu li a { color: rgba(255,255,255,0.75); background-color: transparent; border: 2px solid transparent; border-top-width: 0; border-bottom-color: black; border-radius: 0; }
	.wc-properties .panel-heading menu li:first-child a { border-left-width: 0; }
	.wc-properties .panel-heading menu li:last-child a { border-right-width: 0; }
	.wc-properties .panel-heading menu li + li a { border-left-color: transparent; } 
	.wc-properties .panel-heading menu li.active + li a { border-left-color: black; } 
	.wc-properties .panel-heading menu li.active a { color: rgba(255,255,255,0.75); border-bottom-color: transparent; }
	.wc-properties .panel-heading menu li a:hover, .wc-properties .panel-heading .nav li a:selected { border-width: 2px; border-top-width: 0; border-top-color: transparent; }
	.wc-properties .panel-heading menu li a:active {  }
	.wc-properties .panel-heading menu {  }
	*/
	
	.nav-pills.actions li a { background-color: rgba(255, 255, 255, 0.25); color: white; font-weight: bold; text-shadow: 0 1px 0px rgba(0,0,0,.5); font-weight: bold; }
	.nav-pills.actions li a:hover { background-color: rgba(255, 255, 255, 0.75); color: black; text-shadow: 0 1px 0px rgba(255,255,255,.5); }
	
	.wc-properties .list-group-item { overflow: hidden; }
	
	.wc-ld { position: absolute; right: 15px; top: 15px; opacity: 0; -webkit-transition: opacity .5s ease-in-out, -webkit-transform .5s ease-in-out; text-shadow: none; -webkit-transform: scale(0); }
	.loading .wc-ld { opacity: 1; right: 15px; -webkit-transform: scale(1); }
	.loaded .wc-ld { -webkit-transform: scale(2); }
	.wc-properties h4 {  }
	.wc-properties h4 > i { float: right; }
	.loading h4 > i { opacity: 0; -webkit-transition: opacity .5s ease-in-out, -webkit-transform .5s ease-in-out; -webkit-transform: scale(0); }
	.loaded h4 > i { opacity: 1; -webkit-transition: .5s opacity .25s ease-in-out, .5s -webkit-transform .25s ease-in-out; -webkit-transform: scale(1); }
	
	.loading .content { position: relative; margin-top: -100%; opacity: 0; -webkit-transition: 1s opacity ease-in-out, 1s margin-top ease-in-out; }
	.loaded .content { position: relative; margin-top: 0; opacity: 1; -webkit-transition: 1s opacity ease-in-out, 1s margin-top ease-in-out; }
	
	.wc-cfg-flist { margin: 0; }
	.wc-cfg-flist menu { margin: 0 0 0 25px; }
	.wc-cfg-flist a { display: block; margin: 0 -15px; border-bottom: 1px solid black; padding: 10px 15px; color: rgba(255,255,255,0.75); }
	.wc-cfg-flist a i { color: rgba(255,255,255,0.5); }
	.wc-cfg-flist a:hover { text-decoration: none; color: white; }
	.wc-cfg-flist a:hover i { text-decoration: none; color: white; }
</style>

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

: end