import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

dependencies = ['pyyaml', 'pycurl']

# Add additional compatibility shims
if sys.version_info[0] > 2:
  dependencies.append('future')

setup(name='pyresttest',
      version='1.6.1.dev',
      description='Python RESTful API Testing & Microbenchmarking Tool',
      long_description='Python RESTful API Testing & Microbenchmarking Tool \n Documentation at https://github.com/svanoort/pyresttest',
      maintainer='Sam Van Oort',
      maintainer_email='samvanoort@gmail.com',
      url='https://github.com/svanoort/pyresttest',
      keywords=['rest', 'web', 'http', 'testing'],
      classifiers=[
          'Environment :: Console',
          'License :: OSI Approved :: Apache Software License',
          'Natural Language :: English',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Testing',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Utilities'
      ],
      py_modules=['pyresttest.resttest', 'pyresttest.generators', 'pyresttest.binding',
                  'pyresttest.parsing', 'pyresttest.validators', 'pyresttest.contenthandling',
                  'pyresttest.benchmarks', 'pyresttest.tests', 'pyresttest.ext.validator_jsonschema', 'pyresttest.six'],
      license='Apache License, Version 2.0',
      install_requires=dependencies,
      # Make this executable from command line when installed
      scripts=['util/pyresttest', 'util/resttest.py'],
      provides=['pyresttest']
      )
