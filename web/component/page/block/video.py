# encoding: utf-8

from mongoengine import StringField, MapField
from web.component.asset.xml.templates import text_block_content
from web.component.asset.xml.importers import text_block_content as text_block_content_importer

from .base import Block
from .video_ import render_video_block


class VideoBlock(Block):
	__icon__ = 'youtube-play'
	
	__xml_exporters__ = {
		'videos': text_block_content,
	}
	
	__xml_importers__ = {
		'videos': text_block_content_importer,
	}
	
	# Data Definition
	
	KINDS = [
			"place",
			"directions",
			"search",
			"view",
			"streetview",
		]
	
	STYLES = [
			"roadmap",
			"satellite",
		]
	
	video = StringField(default=None, read=True, write=True)
	videos = MapField(StringField(), default=dict, simple=False)
	
	# Data Portability
	
	def __json__(self):
		return dict(super(VideoBlock, self).as_json,
				video = self.video,
			)
	
	def __html_stream__(self, context=None):
		return render_video_block(context, self)
	
	def __text__(self):
		return self.target.__text__()
