# -*- coding: utf-8 -*-
# Любая из следующих форм литеральных строк работает в latin-1.
# Изменение кодировки выше на либо ascii, либо utf-8 приведет к неудаче,
# потому что тогда 0хc4 и 0хе8 в myStrl не будут допустимыми.
myStrl = 'a'#'AABeC'
myStr2 = 'z'#'A\u00c4B\U000000e8C'
myStr3 = 'x'#'A' + chr(0xC4) + 'B' + chr(0xE8) + 'C'
import sys
print('Default encoding:', sys.getdefaultencoding()) # Стандартная кодировка
for aStr in myStrl, myStr2, myStr3:
    print('{0}, strlen={1}, '.format(aStr, len(aStr)), end='')
    bytesl = aStr.encode()  # Согласно стандартной кодировке utf-8:
                            # 2 байта для не ASCII
    bytes2 = aStr.encode('latin-1') # Один байт на символ
                                    # bytes3 = aStr.encode(’ascii') # ASCII потерпит неудачу:
                                    # за пределами диапазона 0..127
    print('byteslenl={0}, bytes1еп2={1}'.format(len(bytesl), len(bytes2)))
