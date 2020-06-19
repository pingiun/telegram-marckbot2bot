from setuptools import setup

setup(
	name='telegram-marckbot2bot',
	version='0.1',
	py_modules=['assign'],
	scripts=['bot.py'],
	install_requires=['python-telegram-bot', 'jsonpickle']
)
