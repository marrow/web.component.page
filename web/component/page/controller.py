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
	
	def __call__(self, content):
		log.debug("Updating block with new content.", extra=dict(request=id(self._ctx), page=str(self._page.id), block=str(self._reference), length=len(content)))
		
		#__import__('pudb').set_trace()
		update = {'$set': {'content.$.content.' + self._ctx.lang: content}}
		result = Asset._collection.update({'content.id': self._reference}, update)
		__import__('pprint').pprint(dict(self._page._data))
		__import__('pprint').pprint(dict([i._data for i in self._page.content if i.id == self._reference][0]))
		print(repr(result))
		
		return dict(success=True)


class PageController(AssetController):
	def __call__(self):
		return render_page(self._ctx, self._doc)
	
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
