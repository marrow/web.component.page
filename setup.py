#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function

import os
import sys
import codecs


try:
	from setuptools.core import setup, find_packages
except ImportError:
	from setuptools import setup, find_packages

from setuptools.command.test import test as TestCommand


if sys.version_info < (2, 7):
	raise SystemExit("Python 2.7 or later is required.")
elif sys.version_info > (3, 0) and sys.version_info < (3, 3):
	raise SystemExit("Python 3.3 or later is required.")

exec(open(os.path.join("web", "component", "page", "release.py")).read())


class PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		
		self.test_args = []
		self.test_suite = True
	
	def run_tests(self):
		import pytest
		sys.exit(pytest.main(self.test_args))


here = os.path.abspath(os.path.dirname(__file__))

tests_require = [
		'pytest',  # test collector and extensible runner
		'pytest-cov',  # coverage reporting
		'pytest-flakes',  # syntax validation
		'pytest-cagoule',  # intelligent test execution
		'pytest-spec<=0.2.22',  # output formatting
	]


setup(
	name = "web.component.page",
	version = version,
	
	description = description,
	long_description = codecs.open(os.path.join(here, 'README.rst'), 'r', 'utf8').read(),
	url = url,
	download_url = '',
	
	author = author.name,
	author_email = author.email,
	
	license = 'MIT',
	keywords = '',
	classifiers = [
			"Development Status :: 5 - Production/Stable",
			"Environment :: Console",
			"Environment :: Web Environment",
			"Intended Audience :: Developers",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
			"Programming Language :: Python",
			"Programming Language :: Python :: 2",
			"Programming Language :: Python :: 2.7",
			"Programming Language :: Python :: 3",
			"Programming Language :: Python :: 3.3",
			"Programming Language :: Python :: 3.4",
			"Programming Language :: Python :: Implementation :: CPython",
			"Programming Language :: Python :: Implementation :: PyPy",
			"Topic :: Internet :: WWW/HTTP :: WSGI",
			"Topic :: Software Development :: Libraries :: Python Modules",
		],
	
	packages = find_packages(exclude=['bench', 'docs', 'example', 'test']),
	include_package_data = True,
	namespace_packages = [
			'web',  # primary namespace
			'web.component',  # contentment pluggable components
			'web.component.page',  # do not use
			'web.component.page.block',  # embeddable blocks
		],
	
	entry_points = {
			'web.component': [
					'core.page = web.component.page.component:PageComponent',
				],
			
			# Individual blocks within a page layout may have independent controllers.
			'web.page.block': [
					'reference = web.component.page.block.reference:ReferenceBlock',
					'description = web.component.page.block.content:DescriptionBlock',
					'text = web.component.page.block.content:TextBlock',
					'quote = web.component.page.block.content:QuoteBlock',
					'button = web.component.page.block.content:ButtonBlock',
					'image = web.component.page.block.content:ImageBlock',
					
					'map = web.component.page.block.map:MapBlock',
					'video = web.component.page.block.video:VideoBlock',
					#' = web.component.page.block.:Block',
				],
			
			# Content blocks may use one of several different renderers, allowing content authors to copywrite in a
			# format of their own choosing.  Markdown is recommended for general use.
			'web.page.render': [
					# pass-through, or basic HTML clean-up
					'basic = web.component.page.render.basic:BasicRenderer',
					# for untrusted content
					'sanatize = web.component.page.render.sanitize:SanitizingRenderer',
					# for dynamic content
					'template = web.component.page.render.template:TemplateRenderer',
					
					# markup engines
					#'texting = web.component.page.render.texting:TextingRenderer [texting]',
					'textile = web.component.page.render.textile:TextileRenderer [textile]',
					#'markdown = web.component.page.render.markdown:MarkdownRenderer [markdown]',
					'bbcode = web.component.page.render.bbcode:BBCodeRenderer [bbcode]',
					#' = web.component.page.render.:Renderer',
				],
		},
	
	install_requires = [
			#'web.template<3.0.0',  # extensible template engine support
			'marrow.package<2.0',  # dynamic execution and plugin management
			'WebOb',  # HTTP request and response objects, and HTTP status code exceptions
			'mongoengine',  # database layer
			'pytz',  # timzone support
			'blinker',  # signals
			'markupsafe',  # injection protection
			# 'cinje',  # Pending release.  # high-performance streaming template engine
			'babel',  # internationalization and localization
		],
	
	extras_require = dict(
			development = tests_require,
			
			# TBD: Required by various sub-components.
			textile = ['textile'],
			texting = ['marrow.texting'],
			markdown = ['markdown'],
			bbcode = ['bbcode'],
		),
	
	tests_require = tests_require,
	
	zip_safe = True,
	cmdclass = dict(
			test = PyTest,
		)
)
