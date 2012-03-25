from distutils.core import setup

setup(name='nadb',
      version=__import__('nadb').get_version().replace(' ', '-'),
      license='BSD',
      
      description='Not Another Django Blog app!',
      long_description=open('README.rst').read(),
      
      author='Daniel Aronne',
      author_email='earonne@quxisto.com',
      url='https://github.com/earonne/django-nadb/',
      
      install_requires = [
          'django-markup',
      ],
      
      packages=['django-nadb'],
      classifiers=['Development Status :: 3 - Alpha',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )