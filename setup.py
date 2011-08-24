from setuptools import setup


fhandler = open('README.rst', 'r')
long_desc = fhandler.read()
fhandler.close()

setup(name='django-jsonify',
      version='0.1',
      description="Django template tag for json encoding",
      long_description=long_desc,
      author='Marius Grigaitis ()',
      author_email='m@mar.lt',
      license='BSD License',
      keywords='json django jsonify',
      packages=['jsonify'],
      classifiers=[])
