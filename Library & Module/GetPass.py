# My GitHub:  		GitHub.com/AliRezaJoodi
# Source Link:      https://docs.python.org/3/library/getpass.html
# Source Link:      https://github.com/python/cpython/blob/3.10/Lib/getpass.py

from getpass import *

print(getpass())    # string defaults is 'Password: '
print(getpass("Enter Password: "))
print(getuser())    # Return the “login name” of the user.
