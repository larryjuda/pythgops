from setuptools import setup, find_packages


setup(
    name='pythgops',
    version='0.1',
    license='MIT',
    author="Larry Juda",
    author_email='larry.juda@thehutgroup.com',
    packages=['pythgops'],
    url='https://github.com/gmyrianthous/example-publish-pypi',
    install_requires=[
          'pandas',
          'datetime',
          'pymssql',
      ],
)