from distutils.core import setup

fhandler = open('README.rst', 'r')
long_desc = fhandler.read()
fhandler.close()

setup(name='djsonify',
      packages=['djsonify', 'djsonify.templatetags'],
      version='0.3.0',
      description="Django additions for JSON",
      long_description=long_desc,
      author='Marius Grigaitis, Romain Garrigues',
      author_email='m@mar.lt, romain.garrigues.cs@gmail.com',
      license='BSD',
      keywords=['json', 'django', 'jsonify'],
      requires=['django'],
      url='https://github.com/romgar/django-jsonify/',
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Plugins',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'Framework :: Django',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Topic :: Utilities'])
