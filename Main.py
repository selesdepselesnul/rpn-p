from builtins import print
from Parser import RpnParser

if __name__ == '__main__':
    parser = RpnParser('(A+B)*C+(A+B)')
    print(parser.parse())
