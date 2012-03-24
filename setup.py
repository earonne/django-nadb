from distutils.core import setup

setup(name='nadb',
      version='0.1.1',
      license='BSD',
      
      description='A Django blog app',
      long_description=open('README.rst').read(),
      
      author='Daniel Aronne',
      author_email='earonne@quxisto.com',
      url='https://github.com/earonne/nadb/',
      
      install_requires = [
          'markdown',
      ],
      
      packages=['nadb'],
      classifiers=['Development Status :: 3 - Alpha',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )