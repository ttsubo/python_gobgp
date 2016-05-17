import json
import sys
from fabric.api import local


def add_prefix(prefix):
    cmd = 'gobgp -j global rib add {0}'.format(prefix)
    ret = local(cmd, capture=True)
    return ret

def main(argv):
    prefix = argv[1]
    ret = add_prefix(prefix)
    if ret == "":
        print "Success!"
    else:
        print "Error!"

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print "Usage: python add_prefix.py [prefix]"
        sys.exit()
    else:
        main(sys.argv)
