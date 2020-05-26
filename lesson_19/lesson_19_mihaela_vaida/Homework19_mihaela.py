import contextlib
import sys

class JustSomeExceptions:
    def __enter__(self):
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is IndexError:
            print('Got a KeyError')
        elif exc_type is KeyError:
            print('Got an IndexError')

        return True


@contextlib.contextmanager
def printing_ok():

    original_write = sys.stdout.write

    error_message = ''
    try:
        yield 'I am just a message checker!'

    except KeyError:
        # Raised when a mapping (dictionary) key is not found in the set of existing keys.

        print('Got a KeyError ')
    except IndexError:
        # Raised when a sequence subscript is out of range. (Slice indices are silently truncated to fall in the allowed range; if an index is not an integer,
        print('Got an IndexError')
    finally:

        if error_message:
            print(error_message)


with JustSomeExceptions() :
    print("Let's check if it works!" )
    fruits= {'apple': 2, 'avocado':4}
    print( fruits['mango '])


with JustSomeExceptions() :
    print("Let's check if it works!")
    list = [23, 44, 23, 32]
    print(list[4])

with JustSomeExceptions():
    print("Let's check if it works!")
    a = 1 / 0
    print(a)



with printing_ok() as mirror:

    print(mirror)

print(mirror)



print(mirror)
print('No more mirror')
print('*' * 50)

with printing_ok() as mirror:
    dic = {'name': 'John', 'age': 34}
    print(dic['city'])
    print(mirror)

print('*' * 50)
with printing_ok() as mirror:
    list = [23, 44, 23, 32]
    print(list[5])
print(mirror)

print('*' * 50)
with printing_ok() as mirror:
    a = 1 / 0

    print(mirror)