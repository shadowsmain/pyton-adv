import re
import time

name = 'иван'

RE_NAME_VALIDAOR = re.compile(r'^[А-ЯЁ][а-я]+$')

assert not RE_NAME_VALIDAOR.match('иван')
print(RE_NAME_VALIDAOR.match('иван'))
print(RE_NAME_VALIDAOR.match('Иван')), RE_NAME_VALIDAOR.match('Иван').group(0))
print(RE_NAME_VALIDAOR.match('Иван '))
print(RE_NAME_VALIDAOR.fullmatch('Иван '))
