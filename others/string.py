import string

#abcd...ABCD
def letters():
    return string.ascii_letters

#abcd
def lowercases():
    return string.ascii_lowercase

#ABCD
def uppercases():
    return string.ascii_uppercase

#0123456789
def digits():
    return string.digits

#0123456789abcdefABCDEF
def hexdigits():
    return string.hexdigits

#01234567
def octdigits():
    return string.octdigits

#print(ord("A")) > 65
