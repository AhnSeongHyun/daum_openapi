from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='daum_openapi',

      version=version,
      description="Python Library of Daum Open Data API",
      long_description=open("README.md").read() + "\n",
      classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python',
      'Topic :: Text Processing :: Markup :: HTML',
      'Topic :: Software Development :: Libraries :: Python Modules',
      ], 
      keywords='daum openapi',
      author='SeongHyun.Ahn',
      author_email='sh84.ahn@gmail.com',
      url='https://github.com/AhnSeongHyun/daum_openapi',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'xmltodict',
          'requests'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      
      )