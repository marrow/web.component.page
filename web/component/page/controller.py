# encoding: utf-8

from web.component.asset import AssetController

from .model import Page
from .render import render_page


class PageController(AssetController):
	def __call__(self):
		return render_page(self._doc)
	
	def __embed__(self, reference=None):
		return self._doc.as_html
