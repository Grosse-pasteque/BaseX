""" With this function you can easyly get the result of an encoded string or even decode a string, automatizing action of encoded
    transmisions, received transmissions.
    :type: EnD_f -> Encode and Decode Function

    :param encode_or_decode:
    - if param is == "En" -> Function will be in encrypt mode
    - if param is == "De" -> Function will be in decrypt mode
    :param value: -> string that contain the value that you want to encode or decode it depends on the mode you selected in first param
    :param dict_config:
    This arg is the most important, it's your entire configuration that is in this argument.
    - make sure that your variable is dict()
    - make sure that it respects this format :
        >>> dict_config = {
        >>>     0: [base, loop],
        >>>     1: [base, loop]
        >>> }

        :keyword:   -> With base that is equivalent to the base type that you want to use.
                    -> With loop that is equivalent to the number of loop that you want the encode or decode to do.

                    :key    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            - base can be: 16, 32, 64, 85
                            - loop should be between: 0 - 10
                                (WARN: if you put more than 10 it will take sometimes...)
                            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :return:
    - Create file
    - Write configuration into this file
    - Self execute this file
    - print the result

        :keyword:   Exemple for this function:
                    >>> dict_config = {
                    >>>     0: [64, 2],
                    >>>     1: [32, 3]
                    >>> }

                    :key    "En" -> Encode mode:
                    >>> val = EnD_f("En", "hello", dict_config)
                    >>> print(val)

                            "De" -> Decode mode:
                    >>> print(EnD_f("De", val, dict_config))

                    :returns:
                    "hello" encoded with dict_config gives:
                    >>> b'JJJEIRKXKYZEUS2ZLJKUSURSJNEVUQ2WINLEEU2JKZCFKQ2OKNJEQVJWKQZFASJ5'

                    "last" decoded is equivalent to "hello" encoded with dict_config that will be decoded with dict_config:
                    >>> b'hello'
"""
import base64

class B_EnD:
    def __init__(self, ENCODING: str, CONFIG: dict):
        self.ENCODING = ENCODING
        self.CONFIG = CONFIG

    def encode(self, value: str):
        value = value.encode(self.ENCODING)  # encode value to ascii
        for key in self.CONFIG:  # for number of different encode
            for loop in range(self.CONFIG[key][1]):
                value = eval(f"base64.b{str(self.CONFIG[key][0])}encode({value})\n")
        return value

    def decode(self, value: str):
        count_0 = len(self.CONFIG) - 1  # set decoding counter
        for values in self.CONFIG:  # for number of different encode
            for loop in range(self.CONFIG[count_0][1]):
                value = eval(f"base64.b{str(self.CONFIG[count_0][0])}decode({value})")
            count_0 -= 1
        count_0 = 0
        return value
