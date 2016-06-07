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
	
	content = ListField(EmbeddedDocumentField(Block), default=list, simple=False, read=True, write=True)
	handler = StringField(default='web.component.page.controller:PageController', read=True, write=False)  # TODO: PythonReferenceField
	
	# Content Manipulation
	
	def insert_block(self, content, index=None, create=True):
		"""Add a block to the page, either at the end of the available blocks, or at a specific index."""
		# TODO: Allow for insertion of multiple blocks using iterable ABC.
		
		content = content.to_mongo() if hasattr(content, 'to_mongo') else content
		
		if create:
			content['id'] = ObjectId()  # Ensure we always have a unique ID.
		
		update = {
				'$push': {
						'content': {'$each': [content]}
					}
			}
		
		if index is not None:
			update['$push']['content']['$position'] = index
		
		return self.update(__raw__=update)
	
	def update_block(self, id=None, index=None, raw=None, **kw):
		"""Update a block on a page by ID or index using MongoEngine-alike semantics.
		
		Passing a `raw` value will merge it with the overall Page query, not the block-speicifc one, allowing for
		additional conditional criteria about the surrounding page.
		"""
		if id is None and index is None:
			raise ValueError()
		
		if id is not None and index is not None:
			raise ValueError()
		
		ops = ('set', 'unset', 'inc', 'dec', 'push', 'push_all', 'pop', 'pull', 'pull_all', 'add_to_set')
		update = dict()
		
		for key, value in kw.items():
			parts = key.split('__')
			parts.insert(1 if parts[0] in ops else 0, 'content__$' if id else 'content__' + str(index))
			update['__'.join(parts)] = value
		
		if raw:
			update.update(raw)
		
		return self.__class__.objects(id=self.id, content__id=id).update(**update)
	
	def remove_block(self, id=None, index=None):
		"""Remove a block by id or index."""
		if id is None and index is None:
			raise ValueError()
		
		if id is not None and index is not None:
			raise ValueError()
		
		if index:
			id = self.content[index].id
		
		return self._collection.update_one({'_id': self.id}, {'$pull': {'content': {'id': id}}})
	
	def move_block(self, id, index):
		"""Move a block to a new index.
		
		NOTE: The new index is post-removal, i.e. it does not adjust if the insertion point is after the original index.
		"""
		
		# TODO: Apply this in a single operation.
		coll = self.__class__._get_collection()
		block = coll.find_one({'_id': self.id, 'content.id': id}, {'content.$': 1})['content'][0]
		self.remove_block(id)
		self.insert_block(block, index, create=False)
	
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
