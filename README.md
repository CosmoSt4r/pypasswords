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
from pypasswords import hash_it, check_it, generate_it, match_it
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
* **salting** - (bool). *Optional*. Use to specify whether to use salt or not. More [here](https://en.wikipedia.org/wiki/Salt_(cryptography)). Default: *False*. Warning: if you specify salting=*True* then the method will generate random salt and return both the hash and the salt.
* **static_salt** - (string). *Optional*. Use to specify your own salt.
* **salt_length** - (int). *Optional*. Use to specify the length of the salt. Default: *6*
* **local_parameter** - (string). *Optional*. Use to specify local parameter. More [here](https://www.openwall.com/presentations/YaC2012-Password-Hashing-At-Scale/mgp00005.html).

##### Examples:

```py
hash_it('qwerty', hash_type='sha512')
>>> d8578edf8458ce06fbc5bb76a58c5ca4

hash_it('qwerty', salting=True, static_salt='some_word')
>>> ('c4f5d86792a50717d99fba1807d489a7f59ff7a95a293facd2b8c628a17cb722', 'some_word')

hash_it('qwerty', salting=True, salt_length=10, local_parameter='word')
>>> ('bb5310271a8d927f6cf45ad5d1442e2c0d3c7f3bdb68681022688d0555724ed5', '0<JM]bdTV!')
```

#### Checking

You can check your password for strength or validity:

```py
check_it('qwerty')
```

**check_it** method has the following parameters:
* **password** - (string)
* **check_type** - (string). *Optional*. There are 2 check types: strength and valid. Default: *strength*
  - *strength* check type will return number indicating strength of your password. If strength more than 10 then the password is strong.
  - *valid* check type will return True or False whether password has 'stop chars' or not. You have to specify *stop_chars* to use this check type.
* **stop_chars** - (string). *Optional*. Use to specify stop characters to check your password for validity.

##### Examples:

```py
check_it('123some-password321')
>>> 11  # strong password

check_it('qwerty', check_type='valid', stop_chars='0123456789')
>>> True
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
>>> 3XXCltDo4obb

generate_it(strength=3, length=12)
>>> (W:rbP!253UY
```

#### Matching

You can match password with some password's hash:

```py
match_it('entered_password', 'd8578edf8458ce06fbc5bb76a58c5ca4')
```

**match_it** method has the following parameters:
* **password** - (string). The password you want to match with your hash
* **hash** - (string). The hash you want to match with your passwords
* **hash_type** - (string). *Optional*. Use to specify hashing algorithm. Default: *sha-256*
* **salt** - (string). *Optional*. Use to specify password's salt. More [here](https://en.wikipedia.org/wiki/Salt_(cryptography)).
* **local_parameter** - (string). *Optional*. Use to specify local parameter. More [here](https://www.openwall.com/presentations/YaC2012-Password-Hashing-At-Scale/mgp00005.html).


##### Examples:

```py
match_it('hello', 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824)
>>> True

match_it('hello', '5d41402abc4b2a76b9719d911017c592', hash_type='md5', salt='123', local_parameter='321')
>>> False
```


License
----

MIT

#
Pypasswords uses one open source package to work properly:

* [zxcvbn](https://github.com/dropbox/zxcvbn) - password strength estimator

And of course **pypasswords** itself is open source with a [public repository](https://github.com/CosmoSt4r/pypasswords)
 on GitHub.
