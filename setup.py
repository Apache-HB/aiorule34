from setuptools import setup

setup (
	name = 'aiorule34',
	version = '0.1',
	description = 'an async wrapper for rule34.xxx',
	url = 'soon™',
	author = 'Elliot Haisley',
	author_email = 'apachehb@gmail.com',
	license = 'Apache2.0',
	packages = ['aiorule34'],
	install_requires = [
		'aiohttp',
		'defusedxml'
	],
	keywords = [
		'rule34',
		'async',
		'api',
		'wrapper',
		'porn'
	],
	zip_safe = False
)