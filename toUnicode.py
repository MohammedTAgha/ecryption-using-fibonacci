# Python3 code to demonstrate working of
# Convert String to unicode characters
# using re.sub() + ord() + lambda
import re

# initializing string
test_str = '179'

res = (re.sub('.', lambda x: r'% 4X' % ord(x.group()), test_str))


