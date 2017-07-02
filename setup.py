import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(name='nltk-frog',
      version='1.0.0',
      description='NLTK interface with Frog NLP package',
      long_description=README,
      author='Paulius Danenas',
      author_email='danpaulius@gmail.com',
      url='https://github.com/paudan/nltk-frog',
      py_modules=['nltk-opennlp'],
      packages=['nltk_frog'],
      install_requires=['nltk'],
      license='GPL Version 3',
    )



