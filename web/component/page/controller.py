# encoding: utf-8

from bson import ObjectId
from cinje import flatten
from web.component.asset import AssetController

from .model import Asset, Page
from .render import render_page


log = __import__('logging').getLogger(__name__)


class BlockController:
	def __init__(self, context, page, reference):
		self._ctx = context
		self._page = page
		self._reference = reference
	
	def __call__(self, content=None, index=None):
		if content is not None:
			return self._update_content(content.strip())
		if index is not None:
			return self._update_index(index)
	
	def _update_content(self, content):
		log.debug("Updating block with new content.", extra=dict(request=id(self._ctx), page=str(self._page.id), block=str(self._reference), length=len(content)))
		
		update = {'$set': {'content.$.content.' + self._ctx.lang: content}}
		Asset._collection.update({'content.id': self._reference}, update)
		
		return dict(ok=True)
	
	def _update_index(self, index):
		self._page.move_block(self._reference, int(index))
		return dict(ok=True)


class PageController(AssetController):
	def __call__(self):
		return flatten(render_page(self._ctx, self._doc))
	
	def __embed__(self, reference=None):
		return self._doc.__html_stream__(self._ctx)
	
	def __getattr__(self, reference):
		try:
			reference = ObjectId(reference)
		except:
			raise AttributeError()
		
		if reference not in (i.id for i in self._doc.content):
			raise AttributeError()
		
		log.debug("Loaded page block.", extra=dict(request=id(self._ctx), page=str(self._doc.id), block=str(reference)))
		
		return BlockController(self._ctx, self._doc, reference)
