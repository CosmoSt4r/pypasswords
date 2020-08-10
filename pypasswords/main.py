import hashlib
from random import choice
from .config import sault_dictionary
from zxcvbn import zxcvbn
from math import log


def hash_it(password, hash_type='sha256', saulting=False,
            static_sault='', sault_length=6, local_parameter=''):

    def hash_password(word, hashing_type):

        # hashing password
        try:
            hashed_password = hashlib.new(hashing_type)
        except ValueError:
            raise ValueError(f'unsupported hash type {hashing_type}. Try using sha256, sha384, sha512')

        hashed_password.update(word.encode())
        word = hashed_password.hexdigest()
        return word

    def sault_password(word, static, length):

        # adding sault to the password
        if not static:
            # if static_sault isn't specified, generate the sault
            sault = ''
            for _ in range(length):
                sault += choice(sault_dictionary)
            return word + sault
        else:
            # using static_sault
            sault = static
            return word + sault

    def add_local_parameter(word, parameter):

        # adding locale_parameter
        return word + parameter

    # main function to hash the password
    if saulting:
        password = sault_password(password, static_sault, sault_length)

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
        raise ValueError(f'unsupported check type {check_type}. Try using strength, valid.')

    return result
