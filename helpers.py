# Definitions of things for me to import in notebooks

# Classes that do things

class Base(object):
    def __init__(self):
        print('Enter Base.__init__')
        self.base_message = 'Hello from base'
        print('Exit Base.__init__')


class SuperBase(object):
    def __init__(self):
        print('Enter SuperBase.__init__')
        self.base_message = 'Hello from superbase'
        print('Exit SuperBase.__init__')


__all__ = [Base, SuperBase]

if __name__ == '__main__':
    print('This script is not meant to be run directly.')
    print('Please import it in a Jupyter notebook.')
    exit(1)