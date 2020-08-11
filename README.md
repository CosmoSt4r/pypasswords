# Pypasswords - work with passwords easily.

Pypasswords provides easy hashing, checking and generating passwords for you.

# Overview

  - Hash passwords using your favourite hashing algorithms
  - Check passwords for strength or validity
  - Generate passwords with your own parameters

## Installation

To install this package you can use Pypi via pip

```
$ pip install pypasswords
```

## Usage

First you need to import all methods from this package

```py
from pypasswords import hash_it, check_it, generate_it
```
... or simply

```py
from pypasswords import *
```

#### Hashing

You can easily hash your password with just one line of code:

```py
hash_it('qwerty')
```

**hash_it** method has the following parameters:
* **password** - (string)
* **hash_type** - (string). *Optional*. Use to specify hashing algorithm. Default: *sha-256*
* **salting** - (bool). *Optional*. Use to specify whether to use salt or not. More [here](https://en.wikipedia.org/wiki/Salt_(cryptography)). Default: *False*. Warning: if you specify salt=*True* then the method will generate random salt and return both the hash and the salt.
* **static_salt** - (string). *Optional*. Use to specify your own salt.
* **salt_length** - (int). *Optional*. Use to specify the length of the salt. Default: *6*
* **local_parameter** - (string). *Optional*. Use to specify local parameter. More [here](https://www.openwall.com/presentations/YaC2012-Password-Hashing-At-Scale/mgp00005.html).

##### Examples:

```py
hash_it('qwerty', hash_type='sha512')
hash_it('qwerty', salting=True, static_salt='some_word')
hash_it('qwerty', salting=True, salt_length=10, local_parameter='word')
```

#### Checking

You can check your password for strength or validity:

```py
check_it('qwerty')
```

**check_it** method has the following parameters:
* **password** - (string)
* **check_type** - (string). *Optional*. There are 2 check types: strength and valid. Default: *strength*
  - *strength* check type will return number 0-100 indicating strength of your password. If strength more than 30 then the password is good.If strength more than 50 then the password is strong.
  - *valid* check type will return True or False whether password has 'stop chars' or not. You have to specify *stop_chars* to use this check type.
* **stop_chars** - (string). *Optional*. Use to specify stop characters to check your password for validity.

##### Examples:

```py
check_it('123some-password321')
check_it('qwerty', check_type='valid', stop_chars='0123456789')
```

#### Generating

You can generate password with your own parameters:

```py
generate_it()
```

**generate_it** method has the following parameters:
* **strength** - (int). *Optional*. Defalut: *2*
  - **1** - *low*. Using letters only.
  - **2** - *medium*. Using letters and numbers.
  - **3** - *high*. Using letters, numbers and symbols.
* **length** - (int). *Optional*. Use to specify password length. Default: *12*

##### Examples:

```py
generate_it(strength=2)
generate_it(strength=3, length=3)
```

License
----

MIT

#
Pypasswords uses one open source package to work properly:

* [zxcvbn](https://github.com/dropbox/zxcvbn) - password strength estimator

And of course **pypasswords** itself is open source with a [public repository](https://github.com/CosmoSt4r/pypasswords)
 on GitHub.