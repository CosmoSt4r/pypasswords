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
            salt = ''
            for _ in range(length):
                salt += choice(salt_dictionary)
            return word + salt
        else:
            # using static_salt
            salt = static
            return word + salt

    def add_local_parameter(word, parameter):

        # adding locale_parameter
        return word + parameter

    # main function to hash the password
    if salting:
        password = salt_password(password, static_salt, salt_length)

    if local_parameter:
        password = add_local_parameter(password, local_parameter)

    password = hash_password(password, hash_type)
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
