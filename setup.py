from distutils.core import setup
from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
  name = 'pypasswords', 
  packages = ['pypasswords'],
  version = '0.4.0', 
  license='MIT', 
  description = 'Working with passwords made simple',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'CosmoStar',                   
  author_email = 'JustCosmos@yandex.ru',
  url = 'https://github.com/CosmoSt4r/pypasswords',
  download_url = 'https://github.com/CosmoSt4r/pypasswords/archive/v_0.4.tar.gz',
  keywords = ['password', 'passwords', 'check', 'hash', 'simple'],
  install_requires=[
          'zxcvbn',
      ],
  classifiers=[
      
    'Development Status :: 4 - Beta',

    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'Topic :: Security :: Cryptography',

    'License :: OSI Approved :: MIT License',

    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
