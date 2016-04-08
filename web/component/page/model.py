# encoding: utf-8

from pkg_resources import iter_entry_points

from bson import ObjectId
from mongoengine import EmbeddedDocument, ObjectIdField, EmbeddedDocumentField, ListField, StringField, ReferenceField, MapField, URLField, ImageField
from mongoengine.base import get_document

from web.contentment.util import D_
from web.contentment.util.model import Properties
from web.component.page.block.base import Block

from ..asset import Asset
from .render import render_page_content


log = __import__('logging').getLogger(__name__)



class Page(Asset):
	__icon__ = 'file-text-o'
	
	content = ListField(EmbeddedDocumentField(Block), db_field='p_c', default=list, simple=False)
	handler = StringField(db_field='a_h', default='web.component.page.controller:PageController')  # TODO: PythonReferenceField
	
	# Visualization
	
	def tree(self, indent=''):
		print(indent, repr(self), sep='')
		
		for child in self.content:
			child.tree(indent + '    ')
		
		for child in self.children:
			child.tree(indent + '    ')
	
	# Useful for rapidly loading assets that would be lazily loaded later anyway.
	# For example, during page rendering, or during page export to a static mirror.
	
	def __references__(self):
		"""Identify the references to all assets required for rendering this page."""
		
		# First, we identify the Block subclasses that might reference another Asset.
		participants = tuple(j for j in (get_document(i) for i in Block._subclasses) if hasattr(j, '__references__'))
		
		content = self.__class__.objects.no_dereference().scalar('content').get(id=self.id)
		
		for chunk in content:
			if not isinstance(chunk, participants):
				continue
			
			for reference in chunk.__references__():
				yield reference
	
	# Data Portability
	
	def __json__(self):
		return dict(super().__json__(), 
				contents = [i.as_json for i in self.content]  # Capture child nodes.
			)
	
	def __html_stream__(self, context):
		return render_page_content(context, self)
	
	def __text__(self):
		return '\n\n'.join(i.as_text for i in self.content)


# Identify and register all blocks.

_blocks = list(i.load() for i in iter_entry_points('web.page.block'))

if __debug__:
	for _block in _blocks:
		print("Found block: " + repr(_block))
