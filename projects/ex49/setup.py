try:
    from setuptools import setup
except ImportError:
    from destutils.core import setup

config = {
    'description': 'My first test project',
    'author': 'Dmitry',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'dmitry.alex.sergeev@gmail.com',
    'version': '0.1',
    'packages': ['ex49'],
    'scripts': [],
    'name': 'ex49'
}

setup(**config)