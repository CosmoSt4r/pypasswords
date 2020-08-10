from distutils.core import setup
setup(
  name = 'pypasswords', 
  packages = ['pypasswords'],
  version = '0.1', 
  license='MIT', 
  description = 'Working with passwords made simple', 
  author = 'CosmoStar',                   
  author_email = 'JustCosmos@yandex.ru',
  url = 'https://github.com/CosmoSt4r/pypasswords',
  download_url = 'https://github.com/CosmoSt4r/pypasswords/archive/v_01.tar.gz',
  keywords = ['password', 'passwords', 'check', 'hash', 'simple'],
  install_requires=[
          'hashlib',
          'zxcvbn',
      ],
  classifiers=[
      
    'Development Status :: 3 - Alpha',

    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    'License :: OSI Approved :: MIT License',

    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
