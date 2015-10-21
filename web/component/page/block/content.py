# encoding: utf-8

from mongoengine import StringField, MapField, URLField, ImageField

from web.contentment.util import D_

from .base import Block
from .content_ import render_text_block


class DescriptionBlock(Block):
	__icon__ = 'asterisk'


class TextBlock(Block):
	__icon__ = 'font'
	
	content = MapField(StringField(), db_field='c', default=dict)  # TODO: TranslatedField.
	format = StringField(db_field='f', default='html', choices=['html', 'textile', 'md', 'rest'])  # TODO: Dynamic.
	
	# Data Portability
	
	def __html_stream__(self):
		return render_text_block(self, D_(self.content))
	
	def __json__(self):
		return dict(super(TextBlock, self).as_json,
				target = self._data['target'].id
			)
	
	def __text__(self):
		return ''  # TODO: Content extraction.


class QuoteBlock(Block):
	__icon__ = 'wc-b-quote'
	
	pass


class ButtonBlock(Block):
	__icon__ = 'wc-b-button'
	
	label = MapField(StringField(), db_field='c', default=dict)  # TODO: TranslatedField.
	target = URLField(db_field='t')


class ImageBlock(Block):
	__icon__ = 'wc-b-image'
	
	image = ImageField(db_field='i')
	source = URLField(db_field='s')
	target = URLField(db_field='t')
	caption = MapField(StringField(), db_field='c', default=dict)  # TODO: TranslatedField.
