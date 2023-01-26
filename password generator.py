#import library
import random

#define combinations
lowers = 'abcçdefgğhıijklmnoöpqrsştuüvwxyz'
uppers = 'ABCÇDEFGĞHIiJKLMNOÖPQRSŞTUÜVWXYZ'
numbers = '012345678'
symbols = '!@#$%^&*'

combination = lowers + uppers + numbers + symbols

#fix the length of password
length = 14

#generating the password
password = ''.join(random.sample(combination, length))

#here the password you got!
print(password) 
