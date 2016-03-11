# encoding: utf-8

from bson import ObjectId
from mongoengine import EmbeddedDocument, ObjectIdField, EmbeddedDocumentField

from marrow.package.loader import load

from web.component.asset import Asset
from web.contentment.util.model import Properties
from web.component.asset.xml.templates import block


class Block(EmbeddedDocument):
	meta = dict(allow_inheritance=True)
	
	__icon__ = 'cube'
	
	# Data Definition
	
	id = ObjectIdField(db_field='i', default=ObjectId) #, read=True, write=False)
	properties = EmbeddedDocumentField(Properties, db_field='p', default=Properties, simple=False, verbose_name='property') #, read=True, write=True)
	
	# Visualization
	
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
	
	def __html_stream__(self):
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
