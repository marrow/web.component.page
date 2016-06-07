# encoding: utf-8

import re

from bson import ObjectId
from mongoengine import EmbeddedDocument, ObjectIdField, EmbeddedDocumentField
from markupsafe import Markup
from marrow.package.loader import load

from web.component.asset import Asset
from web.contentment.util.model import Properties
from web.component.asset.xml.templates import block

from .common_ import base_block_list_item

INITIAL_CAPS = re.compile('(.)([A-Z][a-z]+)')
CAMEL_CASE = re.compile('([a-z0-9])([A-Z])')

class Block(EmbeddedDocument):
	meta = dict(allow_inheritance=True)
	
	__icon__ = 'cube'
	_block_list_item = base_block_list_item
	
	# Data Definition
	
	id = ObjectIdField(default=ObjectId, read=True, write=False)
	properties = EmbeddedDocumentField(Properties, default=Properties, simple=False, verbose_name='property', read=True, write=True)
	
	# Visualization
	
	@property
	def name(self):
		"""An unencoded version of the class name.
		
		Converts various forms of camel-case (i.e. `AwesomeThingBlock`) into space-separated segments, with any instances
		of `Block` removed.  (I.e. `Awesome Thing`)
		"""
		name = self.__class__.__name__.replace('Block', '')
		name = INITIAL_CAPS.sub(r'\1 \2', name)
		return CAMEL_CASE.sub(r'\1 \2', name)
	
	def tree(self, indent=''):
		print(indent, repr(self), sep='')
	
	# Assets
	
	def get_scripts(self, context):
		return []
	
	def get_styles(self, context):
		return []
	
	# Python Methods
	
	def __str__(self):
		return "{label}: #{self.id!s}".format(self=self, label=self.__class__.__name__.replace('Block', ''))
	
	def __repr__(self, extra=None):
		return "{0.__class__.__name__}({0.id}{1}{2}, {0.properties!r})".format(self, ', ' if extra else '', extra)
	
	# Data Portability
	
	def __json__(self):
		return {
				'id': self.id,
				'type': self.__class__.__name__
			}
	
	as_json = property(lambda self: self.__json__())
	
	def __html_stream__(self, context=None):
		return []
	
	as_stream = property(lambda self: self.__html_stream__)  # Note: doesn't call!
	
	def __html__(self):
		return "".join(self.__html_stream__())
	
	as_html = property(lambda self: self.__html__())
	
	def __text__(self):
		return ""
	
	as_text = property(lambda self: self.__text__())

	__xml__ = block

	as_xml = property(lambda self: self.__xml__())
