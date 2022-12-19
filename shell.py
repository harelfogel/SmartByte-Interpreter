import basic
import sys

if sys.argv[1]:
    result, error = basic.run('<stdin>', sys.argv[1])

if error:
    print(error.as_string())
elif result:
    if len(result.elements) == 1:
        print(repr(result.elements[0]))
    else:
        print(repr(result))