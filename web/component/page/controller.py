# encoding: utf-8

from bson import ObjectId
from cinje import flatten
from web.component.asset import AssetController

from .model import Asset
from .render import render_page


log = __import__('logging').getLogger(__name__)


class BlockResource:
	__dispatch__ = 'resource'
	
	def __init__(self, context, page, reference):
		self._ctx = context
		self._page = page._doc
		self._reference = reference
	
	def post(self, content=None, index=None):
		if content is not None:
			return self._update_content(content.strip())
		if index is not None:
			return self._update_index(index)
	
	def delete(self):
		result = self._page.remove_block(id=self._reference)
		return {'ok': True, 'deleted': self._page.path + '/' + str(self._reference)}
	
	def _update_content(self, content):
		log.debug("Updating block with new content.", extra=dict(request=id(self._ctx), page=str(self._page.id), block=str(self._reference), length=len(content)))
		
		update = {'$set': {'content.$.content.' + self._ctx.lang: content}}
		Asset._collection.update({'_id': self._page.id, 'content.id': self._reference}, update)
		
		return dict(ok=True)
	
	def _update_index(self, index):
		self._page.move_block(self._reference, int(index))
		return dict(ok=True)


class PageController(AssetController):
	__dispatch__ = 'resource'
	__resource__ = BlockResource
	
	def get(self):  # TODO: Accept matching, this is the text/html non-xhr handler.
		if __debug__:
			return flatten(render_page(self._ctx, self._doc))
		
		return render_page(self._ctx, self._doc)
	
	def __embed__(self, reference=None):
		return self._doc.__html_stream__(self._ctx)
	
	def __getitem__(self, reference):
		if self._ctx.domain != 'illicohodes.com':  # Fair chunk of private code for the moment.  :(
			raise KeyError()
		
		try:
			reference = ObjectId(reference)
		except:
			raise KeyError()
		
		if reference not in (i.id for i in self._doc.content):
			raise KeyError()
		
		log.debug("Loaded page block.", extra=dict(request=id(self._ctx), page=str(self._doc.id), block=str(reference)))
		
		return reference
