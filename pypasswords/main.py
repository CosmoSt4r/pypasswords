import hashlib
from random import choice
from .config import salt_dictionary, numbers, letters, symbols
from zxcvbn import zxcvbn
from math import log


def hash_it(password, hash_type='sha256', salting=False,
            static_salt='', salt_length=6, local_parameter=''):

    def hash_password(word, hashing_type):

        # hashing password
        try:
            hashed_password = hashlib.new(hashing_type)
        except ValueError:
            raise ValueError(f'unsupported hash type {hashing_type}. Try using sha256, sha384, sha512')

        hashed_password.update(word.encode())
        word = hashed_password.hexdigest()
        return word

    def salt_password(word, static, length):

        # adding salt to the password
        if not static:
            # if static_salt isn't specified, generate the salt
            pass_salt = ''
            for _ in range(length):
                pass_salt += choice(salt_dictionary)
            return word + pass_salt, pass_salt
        else:
            # using static_salt
            pass_salt = static
            return word + pass_salt, pass_salt

    def add_local_parameter(word, parameter):

        # adding locale_parameter
        return word + parameter

    # main function to hash the password
    salt = None

    # add the salt if it's given
    if salting:
        password, salt = salt_password(password, static_salt, salt_length)

    # add the local parameter if it's given
    if local_parameter:
        password = add_local_parameter(password, local_parameter)

    # hash the password
    password = hash_password(password, hash_type)

    if salt:
        return password, salt
    else:
        return password


def check_it(password, check_type='strength', stop_chars=''):

    if check_type == 'strength':
        result = zxcvbn(password)['crack_times_seconds']['online_no_throttling_10_per_second']
        result = int(log(result, 10))

    elif check_type == 'valid':
        for c in password:
            # checking every char in password
            if c in stop_chars:
                # if stop_char in password then it is invalid
                result = False
                break
        else:
            # if there is no stop_chars in password then it is valid
            result = True
    else:
        # unknown check_type
        raise ValueError(f'unsupported check type {check_type}. Try using strength or valid.')

    return result


def generate_it(strength=2, length=12):

    if strength == 1:
        # 1 - Low. Using letters only
        password = ''
        for _ in range(length):
            password += choice(letters)
        return password

    elif strength == 2:
        # 2 - Medium. Using letters and numbers
        password = ''
        for _ in range(length):
            password += choice(letters + numbers)
        return password

    elif strength == 3:
        # 3 - High. Using letters, numbers and symbols
        password = ''
        for _ in range(length):
            password += choice(letters + numbers + symbols)
        return password

    else:
        # Unknown strength
        raise ValueError(f'unsupported strength. Try using 1, 2 or 3.')


def match_it(user_password, hashed_password, hash_type='sha256', salt='', local_parameter=''):

    # adding salt and local parameter to the given password
    password = user_password + salt + local_parameter

    # hashing given password
    password = hash_it(password, hash_type=hash_type)

    # match given password with given hash
    if password == hashed_password:
        return True
    else:
        return False
