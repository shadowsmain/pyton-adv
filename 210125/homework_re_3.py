import re

RE_NUMBER_VALIDATOR = re.compile(r'^(\d){1}[.,]{1}\d+$')


def number_is_valid(number):
    return RE_NUMBER_VALIDATOR.match(number)


assert number_is_valid('1.32')
assert number_is_valid('1,32')
assert not number_is_valid('asdasd1234')
assert not number_is_valid('22,a44')