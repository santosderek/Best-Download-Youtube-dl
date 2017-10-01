from setuptools import setup, find_packages

setup(name='Best Quality Youtube-dl',
      version='0.1',
      description='Use Youtube-dl at best quality.',
      author='Derek Santos',
      license='The MIT License (MIT)',
      packages=['bdl'],
      scripts=['bdl/main.py'],
      entry_points={
          'console_scripts':
              ['bdl = bdl.main:main']  # bdl = best download
      },
      )
